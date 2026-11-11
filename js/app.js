// TOPCIT Mastery Web Application - Interactive Engine

document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

// App State
const state = {
  currentView: 'plan',
  currentDomain: 'domain1',
  currentExamIndex: 0,
  examAnswers: {},
  examFlagged: {},
  examTimerSeconds: 120 * 60, // 120 mins
  examInterval: null,
  examSubmitted: false,
  pomoSeconds: 25 * 60,
  pomoTotal: 25 * 60,
  pomoInterval: null,
  pomoIsRunning: false,
  pomoMode: 'study', // 'study' or 'break'
  currentCardIndex: 0,
  cardFlipped: false,
  currentCardDomain: 'all',
  quizSubmitted: false,
  quizAnswers: {},
  completedSessions: (() => { try { const saved = JSON.parse(localStorage.getItem('topcit_completed_sessions') || '[]'); return Array.isArray(saved) ? saved : []; } catch { return []; } })(),
  accountUser: null,
  theme: localStorage.getItem('topcit_theme_v2') === 'dark' ? 'dark' : 'light'
};

let supabaseClient = null;
let progressSyncTimer = null;
let accountSyncMessage = 'Progress is saved on this device.';
let accountRecoveryMode = false;
const DATA_STRUCTURE_PRACTICE = [
  {
    scenario: 'A print server must process jobs in the same order they arrive. New jobs can be added while the printer is busy.',
    structure: 'Queue', classification: 'Linear',
    explanation: 'A queue is linear and follows FIFO: the first job enqueued is the first job dequeued. That preserves arrival order.'
  },
  {
    scenario: 'A text editor must undo the most recent change first, then the change before that.',
    structure: 'Stack', classification: 'Linear',
    explanation: 'A stack is linear and follows LIFO. The last edit pushed onto the stack is the first one popped for undo.'
  },
  {
    scenario: 'An organization chart connects each manager to several reports. Every employee, except the top leader, has one direct manager.',
    structure: 'Tree', classification: 'Non-linear',
    explanation: 'A tree is non-linear because it branches into parent-child levels. This is a hierarchy, not a sequence.'
  },
  {
    scenario: 'A route planner stores cities and the roads between them. A city can connect to many other cities, and you need to find routes.',
    structure: 'Graph', classification: 'Non-linear',
    explanation: 'A graph is non-linear: cities are vertices and roads are edges. Traversal algorithms such as BFS or Dijkstra can find routes.'
  },
  {
    scenario: 'A sensor records exactly 24 hourly readings each day. The app often retrieves the reading for a known hour number.',
    structure: 'Array', classification: 'Linear',
    explanation: 'An array is linear and stores items in indexed order. A known hour maps directly to an index for fast random access.'
  }
];
let dataStructurePracticeState = { index: 0, checked: false, score: 0, structure: '', classification: '', reason: '', correct: false };

function progressStorageKey(userId = '') {
  return userId ? `topcit_completed_sessions:${userId}` : 'topcit_completed_sessions';
}

function readStoredProgress(key) {
  try {
    const parsed = JSON.parse(localStorage.getItem(key) || '[]');
    return Array.isArray(parsed) ? parsed.filter(id => typeof id === 'string') : [];
  } catch {
    return [];
  }
}

function storeProgressLocally() {
  localStorage.setItem(progressStorageKey(state.accountUser?.id), JSON.stringify(state.completedSessions));
}

function setAccountMessage(message) {
  accountSyncMessage = message;
  const output = document.getElementById('account-message');
  if (output) output.textContent = message;
}

function updateAccountControls() {
  const button = document.getElementById('account-button');
  const signOut = document.getElementById('account-signout');
  const signIn = document.getElementById('account-signin');
  const signUp = document.getElementById('account-signup');
  const reset = document.getElementById('account-reset');
  const updatePassword = document.getElementById('account-update-password');
  const configured = Boolean(supabaseClient);
  if (button) {
    button.textContent = state.accountUser ? 'Synced' : 'Account';
    button.title = state.accountUser ? 'Study progress is synced to your account' : 'Sign in to sync progress across devices';
  }
  if (signOut) signOut.hidden = !state.accountUser;
  if (signIn) signIn.hidden = accountRecoveryMode;
  if (signUp) signUp.hidden = accountRecoveryMode;
  if (reset) reset.hidden = accountRecoveryMode;
  if (updatePassword) updatePassword.hidden = !accountRecoveryMode;
  if (!configured) setAccountMessage('Account sync needs a Supabase project. Your progress still saves on this device.');
  else setAccountMessage(accountSyncMessage);
}

function validCompletedSessions(ids) {
  const validIds = new Set(getStudyPlan().flatMap(day => day.sessions.map(session => session.id)));
  return [...new Set(ids)].filter(id => validIds.has(id));
}

function scheduleCloudProgressSave() {
  if (!supabaseClient || !state.accountUser) return;
  clearTimeout(progressSyncTimer);
  setAccountMessage('Syncing progress…');
  progressSyncTimer = setTimeout(async () => {
    const userId = state.accountUser?.id;
    if (!userId) return;
    const completed = validCompletedSessions(state.completedSessions);
    const { error } = await supabaseClient.from('study_progress').upsert({
      user_id: userId,
      completed_sessions: completed,
      updated_at: new Date().toISOString()
    }, { onConflict: 'user_id' });
    if (state.accountUser?.id !== userId) return;
    setAccountMessage(error ? 'Cloud sync failed. Your progress is still saved on this device.' : 'Progress synced to your account.');
  }, 400);
}

async function applyAccountSession(session) {
  const user = session?.user || null;
  const previousUserId = state.accountUser?.id || null;
  if (user?.id === previousUserId) {
    updateAccountControls();
    return;
  }

  clearTimeout(progressSyncTimer);
  if (!user) {
    state.accountUser = null;
    state.completedSessions = validCompletedSessions(readStoredProgress(progressStorageKey()));
    storeProgressLocally();
    setAccountMessage('Signed out. Progress on this device is saved locally.');
    renderStudyPlan();
    updateAccountControls();
    return;
  }

  const guestProgress = readStoredProgress(progressStorageKey());
  const accountProgress = readStoredProgress(progressStorageKey(user.id));
  state.accountUser = user;
  state.completedSessions = validCompletedSessions([...guestProgress, ...accountProgress]);
  storeProgressLocally();
  renderStudyPlan();
  setAccountMessage('Loading your saved progress…');

  const { data, error } = await supabaseClient
    .from('study_progress')
    .select('completed_sessions')
    .eq('user_id', user.id)
    .maybeSingle();

  if (state.accountUser?.id !== user.id) return;
  if (error) {
    setAccountMessage('Could not load cloud progress. Check the Supabase setup; local progress is safe.');
    updateAccountControls();
    return;
  }

  const cloudProgress = Array.isArray(data?.completed_sessions) ? data.completed_sessions : [];
  state.completedSessions = validCompletedSessions([...guestProgress, ...accountProgress, ...cloudProgress]);
  storeProgressLocally();
  renderStudyPlan();
  if (state.completedSessions.length !== cloudProgress.length) scheduleCloudProgressSave();
  else setAccountMessage('Progress synced to your account.');
  updateAccountControls();
}

function setupAccountSync() {
  const dialog = document.getElementById('account-dialog');
  const config = window.TOPCIT_SUPABASE_CONFIG || {};
  const api = window.supabase;
  const ready = config.url && config.publishableKey && api?.createClient;

  document.getElementById('account-button')?.addEventListener('click', () => dialog?.showModal());
  document.getElementById('account-close')?.addEventListener('click', () => dialog?.close());
  dialog?.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });

  if (ready) {
    supabaseClient = api.createClient(config.url, config.publishableKey, {
      auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true }
    });
  }

  const emailInput = document.getElementById('account-email');
  const passwordInput = document.getElementById('account-password');
  const withCredentials = () => {
    if (!supabaseClient) {
      updateAccountControls();
      return null;
    }
    const email = emailInput?.value.trim();
    const password = passwordInput?.value;
    if (!email || !password) {
      setAccountMessage('Enter your email and password to continue.');
      return null;
    }
    return { email, password };
  };

  document.getElementById('account-signin')?.addEventListener('click', async () => {
    const credentials = withCredentials();
    if (!credentials) return;
    setAccountMessage('Signing in…');
    const { data, error } = await supabaseClient.auth.signInWithPassword(credentials);
    if (error) return setAccountMessage(error.message);
    await applyAccountSession(data.session);
    dialog?.close();
  });

  document.getElementById('account-signup')?.addEventListener('click', async () => {
    const credentials = withCredentials();
    if (!credentials) return;
    if (credentials.password.length < 8) return setAccountMessage('Use a password with at least 8 characters.');
    setAccountMessage('Creating your account…');
    const { data, error } = await supabaseClient.auth.signUp({
      ...credentials,
      options: { emailRedirectTo: `${window.location.origin}${window.location.pathname}` }
    });
    if (error) return setAccountMessage(error.message);
    if (data.session) {
      await applyAccountSession(data.session);
      dialog?.close();
    } else {
      setAccountMessage('Account created. Check your email to confirm it, then sign in here.');
    }
  });

  document.getElementById('account-reset')?.addEventListener('click', async () => {
    if (!supabaseClient) return updateAccountControls();
    const email = emailInput?.value.trim();
    if (!email) return setAccountMessage('Enter your email first, then choose “Forgot password?”.');
    const { error } = await supabaseClient.auth.resetPasswordForEmail(email, {
      redirectTo: `${window.location.origin}${window.location.pathname}`
    });
    setAccountMessage(error ? error.message : 'If an account uses that email, a password reset link is on its way.');
  });

  document.getElementById('account-update-password')?.addEventListener('click', async () => {
    const password = passwordInput?.value || '';
    if (password.length < 8) return setAccountMessage('Use a password with at least 8 characters.');
    const { error } = await supabaseClient.auth.updateUser({ password });
    if (error) return setAccountMessage(error.message);
    accountRecoveryMode = false;
    passwordInput.value = '';
    setAccountMessage('Password updated. Your progress is synced to your account.');
    updateAccountControls();
    dialog?.close();
  });

  document.getElementById('account-signout')?.addEventListener('click', async () => {
    if (!supabaseClient) return;
    const { error } = await supabaseClient.auth.signOut();
    if (error) setAccountMessage(error.message);
    else dialog?.close();
  });

  if (supabaseClient) {
    supabaseClient.auth.onAuthStateChange((event, session) => {
      setTimeout(() => {
        if (event === 'PASSWORD_RECOVERY') {
          accountRecoveryMode = true;
          if (passwordInput) passwordInput.value = '';
          setAccountMessage('Enter a new password for your account.');
          updateAccountControls();
          dialog?.showModal();
          passwordInput?.focus();
        }
        applyAccountSession(session);
      }, 0);
    });
    supabaseClient.auth.getSession().then(({ data, error }) => {
      if (error) setAccountMessage('Could not restore your account session. Sign in again to sync.');
      else applyAccountSession(data.session);
    });
  }
  updateAccountControls();
}

// Safe accessors for data arrays
function getExamQuestions() {
  if (typeof EXAM_QUESTIONS !== 'undefined' && Array.isArray(EXAM_QUESTIONS)) return EXAM_QUESTIONS;
  if (typeof window !== 'undefined' && window.EXAM_QUESTIONS && Array.isArray(window.EXAM_QUESTIONS)) return window.EXAM_QUESTIONS;
  return [];
}

function getFlashcards() {
  if (typeof FLASHCARDS_DATA !== 'undefined' && Array.isArray(FLASHCARDS_DATA)) return FLASHCARDS_DATA;
  if (typeof window !== 'undefined' && window.FLASHCARDS_DATA && Array.isArray(window.FLASHCARDS_DATA)) return window.FLASHCARDS_DATA;
  return [];
}

function getStudyPlan() {
  if (typeof STUDY_PLAN !== 'undefined' && Array.isArray(STUDY_PLAN)) return STUDY_PLAN;
  if (typeof window !== 'undefined' && window.STUDY_PLAN && Array.isArray(window.STUDY_PLAN)) return window.STUDY_PLAN;
  return [];
}

function getModulesData() {
  if (typeof MODULES_DATA !== 'undefined') return MODULES_DATA;
  if (typeof window !== 'undefined' && window.MODULES_DATA) return window.MODULES_DATA;
  return {};
}

function initApp() {
  applyTheme(state.theme);
  setupAccountSync();
  setupNavigation();
  setupPomodoro();
  renderStudyPlan();
  setupFlashcards();
  setupSearch();
  handleHashChange();
  window.addEventListener('hashchange', handleHashChange);
}

// Audio synthesizer for Pomodoro chime (zero external dependency)
function playChime(type = 'start') {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    if (type === 'break') {
      osc.frequency.setValueAtTime(523.25, ctx.currentTime);
      osc.frequency.setValueAtTime(659.25, ctx.currentTime + 0.15);
      gain.gain.setValueAtTime(0.3, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.8);
      osc.start();
      osc.stop(ctx.currentTime + 0.8);
    } else {
      osc.frequency.setValueAtTime(440, ctx.currentTime);
      osc.frequency.setValueAtTime(880, ctx.currentTime + 0.1);
      gain.gain.setValueAtTime(0.25, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.5);
      osc.start();
      osc.stop(ctx.currentTime + 0.5);
    }
  } catch (e) {
    console.log('Audio chime not supported:', e);
  }
}

// Theme Toggle
function applyTheme(t) {
  document.documentElement.setAttribute('data-theme', t);
  localStorage.setItem('topcit_theme_v2', t);
  const btn = document.getElementById('theme-toggle-btn');
  if (btn) btn.textContent = t === 'dark' ? 'Light theme' : 'Dark theme';
}

document.getElementById('theme-toggle-btn')?.addEventListener('click', () => {
  state.theme = state.theme === 'dark' ? 'light' : 'dark';
  applyTheme(state.theme);
});

// Mobile Sidebar Toggle
document.getElementById('mobile-toggle')?.addEventListener('click', () => {
  document.getElementById('sidebar')?.classList.toggle('open');
});
document.getElementById('sidebar-close')?.addEventListener('click', () => {
  document.getElementById('sidebar')?.classList.remove('open');
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') document.getElementById('sidebar')?.classList.remove('open');
});

// Navigation & Router
function setupNavigation() {
  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const view = item.getAttribute('data-view');
      const domain = item.getAttribute('data-domain');
      if (view) {
        window.location.hash = '#' + view;
        handleHashChange();
        document.getElementById('sidebar')?.classList.remove('open');
      } else if (domain) {
        window.location.hash = '#' + domain;
        handleHashChange();
        document.getElementById('sidebar')?.classList.remove('open');
      }
    });
  });
}

function handleHashChange() {
  const hash = window.location.hash.replace('#', '') || 'plan';
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

  if (hash.startsWith('domain')) {
    showView('domain-view');
    renderDomainView(hash);
    const nav = document.querySelector(`.nav-item[data-domain="${hash}"]`);
    if (nav) nav.classList.add('active');
  } else {
    showView(hash.startsWith('quiz-domain') ? 'quizzes' : hash);
    const nav = document.querySelector(`.nav-item[data-view="${hash.startsWith('quiz-domain') ? 'quizzes' : hash}"]`);
    if (nav) nav.classList.add('active');

    if (hash === 'exam') {
      initExam();
    } else if (hash === 'flashcards') {
      renderFlashcard();
    } else if (hash === 'plan') {
      renderStudyPlan();
    } else if (hash === 'cheatsheet') {
      renderCheatSheet();
    } else if (hash === 'quizzes') {
      renderQuizzes();
    } else if (hash.startsWith('quiz-domain')) {
      renderQuizzes(hash);
    }
  }
}

function showView(viewId) {
  document.querySelectorAll('.view-section').forEach(sec => sec.classList.remove('active'));
  const target = document.getElementById(viewId + '-section') || document.getElementById(viewId);
  if (target) {
    target.classList.add('active');
    const scrollContainer = document.querySelector('.content-area');
    if (scrollContainer) scrollContainer.scrollTop = 0;
  }
}

// ----------------------------------------------------
// 14-Day Study Plan Engine
// ----------------------------------------------------
function renderStudyPlan() {
  const container = document.getElementById('study-plan-container');
  const plan = getStudyPlan();
  if (!container || !plan.length) return;

  const totalSessions = plan.reduce((acc, day) => acc + day.sessions.length, 0);
  const validIds = new Set(plan.flatMap(day => day.sessions.map(session => session.id)));
  state.completedSessions = [...new Set(state.completedSessions.filter(id => validIds.has(id)))];
  storeProgressLocally();
  const completedCount = state.completedSessions.length;
  const percent = Math.round((completedCount / totalSessions) * 100);
  const domainProgress = Object.keys(getModulesData()).map(domainId => {
    const sessions = plan.flatMap(day => day.domainId === domainId ? day.sessions : []);
    const done = sessions.filter(session => state.completedSessions.includes(session.id)).length;
    return { domainId, name: plan.find(day => day.domainId === domainId)?.domainName || domainId, done, total: sessions.length, percent: sessions.length ? Math.round(done / sessions.length * 100) : 0 };
  });

  let html = `
    <div class="summary-card" style="margin-bottom: 2rem; border-left: 4px solid var(--primary); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
      <div>
        <h4 style="margin: 0; color: var(--text-main); font-size: 1.25rem;">14-Day Exam Readiness Progress</h4>
        <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 0.25rem;">
          ${completedCount} of ${totalSessions} sessions completed (${percent}%) &bull; 14-day plan
        </p>
      </div>
      <div class="overall-progress" style="display: flex; align-items: center; gap: 1rem;">
        <div style="width: 160px; height: 12px; background: var(--bg-card); border-radius: 9999px; overflow: hidden; border: 1px solid var(--border);">
          <div style="width: ${percent}%; height: 100%; background: var(--success); transition: width 0.3s ease;"></div>
        </div>
        <span style="font-weight: 800; font-size: 1.1rem; color: var(--success);">${percent}%</span>
      </div>
    </div>
    <div class="domain-progress-grid">
      ${domainProgress.map(domain => `<div class="domain-progress-card"><div><strong>${domain.name}</strong><span>${domain.done}/${domain.total} sessions</span></div><progress value="${domain.done}" max="${domain.total}" aria-label="${domain.name} progress"></progress><b>${domain.percent}%</b></div>`).join('')}
    </div>
    <div class="plan-timeline">
  `;

  plan.forEach(day => {
    const dayCompleted = day.sessions.every(s => state.completedSessions.includes(s.id));
    html += `
      <div class="day-card ${dayCompleted ? 'completed' : ''}">
        <div class="day-header">
          <span class="day-badge">Day ${day.day}</span>
          <span class="day-title">${day.title}</span>
          <span style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">~${day.estimatedMinutes} mins</span>
        </div>
        <div class="day-body">
          <p style="font-size: 0.88rem; color: var(--primary); font-weight: 600; margin-bottom: 1rem;">
            <span class="session-target-label">Goal</span> ${day.target}
          </p>
          <div class="session-list">
    `;

    day.sessions.forEach(sess => {
      const isDone = state.completedSessions.includes(sess.id);
      html += `
        <div class="session-item" id="session-item-${sess.id}">
          <input type="checkbox" class="session-checkbox" data-session-id="${sess.id}" ${isDone ? 'checked' : ''}>
          <div class="session-info">
            <h5>
              ${sess.title}
              <span style="font-size: 0.72rem; padding: 0.1rem 0.4rem; background: var(--bg-card); border-radius: 4px; color: var(--warning); font-family: var(--font-mono);">${sess.duration}</span>
            </h5>
            <div class="session-topics">
              ${sess.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}
            </div>
            ${sess.reviewTips ? `<p class="session-tip"><strong>Note</strong> ${sess.reviewTips}</p>` : ''}
          </div>
          <button class="session-action-btn" onclick="goToSessionTopic('${sess.topicId}', '${day.domainId}')">
            Study &rarr;
          </button>
        </div>
      `;
    });

    html += `
          </div>
        </div>
      </div>
    `;
  });

  html += `</div>`;
  container.innerHTML = html;

  // Checkbox listeners
  container.querySelectorAll('.session-checkbox').forEach(cb => {
    cb.addEventListener('change', (e) => {
      const sid = e.target.getAttribute('data-session-id');
      if (e.target.checked) {
        if (!state.completedSessions.includes(sid)) state.completedSessions.push(sid);
      } else {
        state.completedSessions = state.completedSessions.filter(id => id !== sid);
      }
      storeProgressLocally();
      scheduleCloudProgressSave();
      renderStudyPlan();
    });
  });
}

function goToSessionTopic(topicId, domainId) {
  if (topicId.startsWith('quiz')) {
    state.quizAnswers = {};
    state.quizSubmitted = false;
    window.location.hash = '#' + topicId;
  } else if (topicId === 'full-exam') {
    window.location.hash = '#exam';
  } else if (topicId === 'weak-areas') {
    window.location.hash = '#exam';
  } else if (topicId.startsWith('flashcards')) {
    window.location.hash = '#flashcards';
  } else if (topicId.startsWith('cheatsheet')) {
    window.location.hash = '#cheatsheet';
  } else {
    const sectionAliases = { 'sec-pki-auth': 'sec-asymmetric', 'biz-planning': 'biz-strategy' };
    window.location.hash = '#' + domainId;
    setTimeout(() => {
      const el = document.getElementById(sectionAliases[topicId] || topicId);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }, 150);
  }
}

function renderQuizzes(quizId = '') {
  const container = document.getElementById('quiz-container');
  if (!container) return;
  const quizzes = typeof QUIZZES_DATA !== 'undefined' ? QUIZZES_DATA : {};
  const domainNames = { 'quiz-domain1': 'Software Development', 'quiz-domain2': 'Data & Databases', 'quiz-domain3': 'System Architecture', 'quiz-domain4': 'Information Security', 'quiz-domain5': 'IT Business & Ethics', 'quiz-domain6': 'Project Management' };
  const selectedId = quizzes[quizId] ? quizId : Object.keys(quizzes)[0];
  const items = quizzes[selectedId] || [];
  if (!items.length) {
    container.innerHTML = '<div class="summary-card">No quizzes are available yet.</div>';
    return;
  }
  if (!quizId || !quizzes[quizId]) {
    state.quizAnswers = {};
    state.quizSubmitted = false;
  }
  let score = 0;
  const body = items.map((question, index) => {
    const selected = state.quizAnswers[index];
    const correct = selected === question.correct;
    if (correct) score++;
    return `<article class="quiz-question summary-card"><h3>${index + 1}. ${question.question}</h3><div class="q-options">${question.options.map((option, optionIndex) => `<button class="q-option ${selected === optionIndex ? 'selected' : ''} ${state.quizSubmitted && optionIndex === question.correct ? 'quiz-correct' : ''} ${state.quizSubmitted && selected === optionIndex && !correct ? 'quiz-wrong' : ''}" onclick="selectQuizAnswer(${index}, ${optionIndex})" ${state.quizSubmitted ? 'disabled' : ''}><b>${String.fromCharCode(65 + optionIndex)}.</b> ${option}</button>`).join('')}</div>${state.quizSubmitted ? `<p class="quiz-explanation"><strong>${correct ? 'Correct.' : 'Review this one.'}</strong> ${question.explanation}</p>` : ''}</article>`;
  }).join('');
  const options = Object.keys(quizzes).map(id => `<option value="${id}" ${selectedId === id ? 'selected' : ''}>${domainNames[id] || id}</option>`).join('');
  container.innerHTML = `<div class="quiz-toolbar summary-card"><label for="quiz-domain-select">Choose a domain</label><select id="quiz-domain-select">${options}</select><span>${items.length} questions</span></div>${state.quizSubmitted ? `<div class="quiz-score summary-card" role="status">You got <strong>${score} / ${items.length}</strong> correct.</div>` : ''}${body}<div class="quiz-actions">${state.quizSubmitted ? '<button class="btn-secondary" onclick="resetQuiz()">Try again</button>' : '<button class="btn-primary" onclick="submitQuiz()">Check answers</button>'}</div>`;
  document.getElementById('quiz-domain-select')?.addEventListener('change', event => {
    state.quizAnswers = {};
    state.quizSubmitted = false;
    window.location.hash = '#' + event.target.value;
  });
}

window.selectQuizAnswer = (questionIndex, optionIndex) => {
  if (state.quizSubmitted) return;
  state.quizAnswers[questionIndex] = optionIndex;
  renderQuizzes(window.location.hash.slice(1));
};
window.submitQuiz = () => { state.quizSubmitted = true; renderQuizzes(window.location.hash.slice(1)); };
window.resetQuiz = () => { state.quizAnswers = {}; state.quizSubmitted = false; renderQuizzes(window.location.hash.slice(1)); };

// ----------------------------------------------------
// Domain Study View Engine
// ----------------------------------------------------
function renderDomainView(domainId) {
  const container = document.getElementById('domain-content-container');
  const modules = getModulesData();
  if (!container || !modules[domainId]) return;

  const data = modules[domainId];
  let html = `
    <div class="view-header">
      <p class="domain-kicker">${domainId.replace('domain', 'Domain ')}</p>
      <h2>${data.title}</h2>
      <p>${data.description}</p>
    </div>
    <div class="domain-sections-wrapper" style="display: flex; flex-direction: column; gap: 2rem;">
  `;

  data.sections.forEach(sec => {
    html += `
      <section id="${sec.id}" class="domain-section-card summary-card" style="padding: 2rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem;">
          <h3 style="font-size: 1.35rem; color: var(--primary); font-weight: 700;">${sec.title}</h3>
          <span style="font-size: 0.75rem; background: var(--bg-card); color: var(--text-muted); padding: 0.25rem 0.65rem; border-radius: 9999px;">${sec.badge}</span>
        </div>
        ${sec.summary ? `<p class="section-summary">${sec.summary}</p>` : ''}
        ${sec.id === 'sw-ds-algo' ? renderDataStructurePractice() : ''}
        <div class="section-html-content">
          ${sec.content}
        </div>
      </section>
    `;
  });

  html += `</div>`;
  container.innerHTML = html;
  if (domainId === 'domain1') setupDataStructurePractice();
}

function renderDataStructurePractice() {
  const { index, checked, score } = dataStructurePracticeState;
  const total = DATA_STRUCTURE_PRACTICE.length;
  if (index >= total) {
    return `<div class="practical-lab" id="data-structure-practice">
      <div class="practical-lab-heading"><div><p class="domain-kicker">PRACTICAL DRILL</p><h4>Data structure casework</h4></div><span>${total}/${total} cases</span></div>
      <progress value="${total}" max="${total}" aria-label="Practice cases completed"></progress>
      <p class="practical-result">You matched <strong>${score} / ${total}</strong> structures and classifications.</p>
      <button class="btn-secondary" id="ds-practice-restart" type="button">Run the cases again</button>
    </div>`;
  }
  const item = DATA_STRUCTURE_PRACTICE[index];
  const progress = index + (checked ? 1 : 0);
  const feedback = checked
    ? `<strong>${dataStructurePracticeState.correct ? 'Good call.' : `Best fit: ${item.structure} · ${item.classification}.`}</strong> ${item.explanation} Compare that with your reason above.`
    : 'Classify by shape: sequence (linear) or branching/network (non-linear).';
  return `<div class="practical-lab" id="data-structure-practice">
    <div class="practical-lab-heading"><div><p class="domain-kicker">PRACTICAL DRILL</p><h4>Pick the structure for the job</h4></div><span>Case ${index + 1} of ${total}</span></div>
    <progress value="${progress}" max="${total}" aria-label="Practice progress"></progress>
    <p class="practical-scenario">${item.scenario}</p>
    <div class="practical-fields">
      <label>Best structure
        <select id="ds-practice-structure" ${checked ? 'disabled' : ''}>
          <option value="">Choose one…</option>
          ${['Array', 'Linked list', 'Stack', 'Queue', 'Tree', 'Graph'].map(value => `<option value="${value}" ${dataStructurePracticeState.structure === value ? 'selected' : ''}>${value}</option>`).join('')}
        </select>
      </label>
      <label>Classification
        <select id="ds-practice-classification" ${checked ? 'disabled' : ''}>
          <option value="">Choose one…</option><option ${dataStructurePracticeState.classification === 'Linear' ? 'selected' : ''}>Linear</option><option ${dataStructurePracticeState.classification === 'Non-linear' ? 'selected' : ''}>Non-linear</option>
        </select>
      </label>
    </div>
    <label class="practical-reason-label" for="ds-practice-reason">Explain why in one sentence before checking.</label>
    <textarea id="ds-practice-reason" rows="2" placeholder="Think about how the items connect or what order they must follow…" ${checked ? 'disabled' : ''}></textarea>
    <div class="practical-lab-actions">
      <button class="btn-primary" id="ds-practice-check" type="button" ${checked ? 'hidden' : ''}>Check my answer</button>
      <button class="btn-secondary" id="ds-practice-next" type="button" ${checked ? '' : 'hidden'}>${index + 1 === total ? 'See my result' : 'Next case'}</button>
    </div>
    <p class="practical-feedback" id="ds-practice-feedback" role="status" aria-live="polite">${feedback}</p>
  </div>`;
}

function setupDataStructurePractice() {
  const host = document.getElementById('data-structure-practice');
  if (!host) return;
  const update = () => {
    host.innerHTML = renderDataStructurePractice();
    setupDataStructurePractice();
  };
  if (dataStructurePracticeState.index >= DATA_STRUCTURE_PRACTICE.length) {
    host.querySelector('#ds-practice-restart')?.addEventListener('click', () => {
      dataStructurePracticeState = { index: 0, checked: false, score: 0, structure: '', classification: '', reason: '', correct: false };
      update();
    });
    return;
  }
  host.querySelector('#ds-practice-structure').value = dataStructurePracticeState.structure;
  host.querySelector('#ds-practice-classification').value = dataStructurePracticeState.classification;
  host.querySelector('#ds-practice-reason').value = dataStructurePracticeState.reason;
  host.querySelector('#ds-practice-structure').addEventListener('change', event => { dataStructurePracticeState.structure = event.target.value; });
  host.querySelector('#ds-practice-classification').addEventListener('change', event => { dataStructurePracticeState.classification = event.target.value; });
  host.querySelector('#ds-practice-reason').addEventListener('input', event => { dataStructurePracticeState.reason = event.target.value; });
  host.querySelector('#ds-practice-check')?.addEventListener('click', () => {
    const structure = host.querySelector('#ds-practice-structure').value;
    const classification = host.querySelector('#ds-practice-classification').value;
    const reason = host.querySelector('#ds-practice-reason').value.trim();
    const feedback = host.querySelector('#ds-practice-feedback');
    if (!structure || !classification || !reason) {
      feedback.textContent = 'Choose both answers and write a quick reason before checking.';
      return;
    }
    const item = DATA_STRUCTURE_PRACTICE[dataStructurePracticeState.index];
    const correct = structure === item.structure && classification === item.classification;
    if (correct) dataStructurePracticeState.score++;
    dataStructurePracticeState.structure = structure;
    dataStructurePracticeState.classification = classification;
    dataStructurePracticeState.reason = reason;
    dataStructurePracticeState.correct = correct;
    dataStructurePracticeState.checked = true;
    host.querySelector('#ds-practice-structure').disabled = true;
    host.querySelector('#ds-practice-classification').disabled = true;
    host.querySelector('#ds-practice-reason').disabled = true;
    host.querySelector('#ds-practice-check').hidden = true;
    host.querySelector('#ds-practice-next').hidden = false;
    host.querySelector('progress').value = dataStructurePracticeState.index + 1;
    host.querySelector('.practical-lab-heading > span').textContent = `Case ${dataStructurePracticeState.index + 1} of ${DATA_STRUCTURE_PRACTICE.length} · ${dataStructurePracticeState.score} correct`;
    feedback.innerHTML = `<strong>${correct ? 'Good call.' : `Best fit: ${item.structure} · ${item.classification}.`}</strong> ${item.explanation} Compare that with your reason above.`;
  });
  host.querySelector('#ds-practice-next')?.addEventListener('click', () => {
    dataStructurePracticeState.index++;
    dataStructurePracticeState.checked = false;
    dataStructurePracticeState.structure = '';
    dataStructurePracticeState.classification = '';
    dataStructurePracticeState.reason = '';
    update();
  });
}

// ----------------------------------------------------
// Pomodoro Timer Engine
// ----------------------------------------------------
function setupPomodoro() {
  const timeDisplay = document.getElementById('pomo-display');
  const toggleBtn = document.getElementById('pomo-toggle');
  const modeBadge = document.getElementById('pomo-mode');

  function updateDisplay() {
    const mins = Math.floor(state.pomoSeconds / 60);
    const secs = state.pomoSeconds % 60;
    if (timeDisplay) {
      timeDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }
  }

  function toggleTimer() {
    if (state.pomoIsRunning) {
      clearInterval(state.pomoInterval);
      state.pomoIsRunning = false;
      if (toggleBtn) {
        toggleBtn.textContent = '▶';
        toggleBtn.classList.remove('running');
      }
    } else {
      state.pomoIsRunning = true;
      if (toggleBtn) {
        toggleBtn.textContent = '⏸';
        toggleBtn.classList.add('running');
      }
      playChime('start');
      state.pomoInterval = setInterval(() => {
        if (state.pomoSeconds > 0) {
          state.pomoSeconds--;
          updateDisplay();
        } else {
          clearInterval(state.pomoInterval);
          state.pomoIsRunning = false;
          if (state.pomoMode === 'study') {
            playChime('break');
            alert('Session complete. Take a 5-minute break.');
            state.pomoMode = 'break';
            state.pomoSeconds = 5 * 60;
            state.pomoTotal = 5 * 60;
            if (modeBadge) modeBadge.textContent = 'Break';
          } else {
            playChime('start');
            alert('Break finished. Ready for your next 25-minute study session?');
            state.pomoMode = 'study';
            state.pomoSeconds = 25 * 60;
            state.pomoTotal = 25 * 60;
            if (modeBadge) modeBadge.textContent = 'Study';
          }
          if (toggleBtn) {
            toggleBtn.textContent = '▶';
            toggleBtn.classList.remove('running');
          }
          updateDisplay();
        }
      }, 1000);
    }
  }

  toggleBtn?.addEventListener('click', toggleTimer);
  updateDisplay();
}

// ----------------------------------------------------
// Flashcards Interactive Engine
// ----------------------------------------------------
function setupFlashcards() {
  const card = document.getElementById('active-flashcard');
  card?.addEventListener('click', () => {
    state.cardFlipped = !state.cardFlipped;
    card.classList.toggle('flipped', state.cardFlipped);
  });

  document.getElementById('card-prev-btn')?.addEventListener('click', (e) => {
    e.stopPropagation();
    navigateCard(-1);
  });
  document.getElementById('card-next-btn')?.addEventListener('click', (e) => {
    e.stopPropagation();
    navigateCard(1);
  });
  document.getElementById('card-flip-btn')?.addEventListener('click', (e) => {
    e.stopPropagation();
    state.cardFlipped = !state.cardFlipped;
    card?.classList.toggle('flipped', state.cardFlipped);
  });

  document.getElementById('flashcard-domain-filter')?.addEventListener('change', (e) => {
    state.currentCardDomain = e.target.value;
    state.currentCardIndex = 0;
    renderFlashcard();
  });
}

function getFilteredCards() {
  const allCards = getFlashcards();
  if (state.currentCardDomain === 'all') return allCards;
  return allCards.filter(c => c.domain === state.currentCardDomain);
}

function navigateCard(direction) {
  const cards = getFilteredCards();
  if (cards.length === 0) return;
  state.currentCardIndex = (state.currentCardIndex + direction + cards.length) % cards.length;
  state.cardFlipped = false;
  document.getElementById('active-flashcard')?.classList.remove('flipped');
  renderFlashcard();
}

function renderFlashcard() {
  const cards = getFilteredCards();
  const card = document.getElementById('active-flashcard');
  const countDisplay = document.getElementById('card-counter');
  if (!card || cards.length === 0) return;

  const current = cards[state.currentCardIndex];
  document.getElementById('card-front-domain').textContent = current.domainName;
  document.getElementById('card-front-cat').textContent = current.category;
  document.getElementById('card-front-text').textContent = current.front;

  document.getElementById('card-back-cat').textContent = current.category;
  document.getElementById('card-back-text').innerHTML = current.back.replace(/\n/g, '<br>');

  if (countDisplay) {
    countDisplay.textContent = `${state.currentCardIndex + 1} / ${cards.length}`;
  }
}

// ----------------------------------------------------
// CICT / TOPCIT Full Simulation Mock Exam Engine
// ----------------------------------------------------
function initExam() {
  const questions = getExamQuestions();
  if (!questions || questions.length === 0) {
    console.error('No exam questions loaded');
    return;
  }
  if (!state.examInterval && !state.examSubmitted) {
    startExamTimer();
  }
  renderExamQuestionGrid();
  renderCurrentExamQuestion();
}

function startExamTimer() {
  const timerDisplay = document.getElementById('exam-countdown');
  state.examInterval = setInterval(() => {
    if (state.examTimerSeconds > 0) {
      state.examTimerSeconds--;
      const hrs = Math.floor(state.examTimerSeconds / 3600);
      const mins = Math.floor((state.examTimerSeconds % 3600) / 60);
      const secs = state.examTimerSeconds % 60;
      if (timerDisplay) {
        timerDisplay.textContent = `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
      }
    } else {
      clearInterval(state.examInterval);
      submitExam();
    }
  }, 1000);
}

function renderExamQuestionGrid() {
  const grid = document.getElementById('exam-nav-grid');
  const questions = getExamQuestions();
  if (!grid || !questions.length) return;

  grid.innerHTML = questions.map((q, idx) => {
    const isAnswered = state.examAnswers[idx] !== undefined;
    const isCurrent = idx === state.currentExamIndex;
    const isFlagged = state.examFlagged[idx];

    let classes = 'exam-q-btn';
    if (isCurrent) classes += ' current';
    if (isAnswered) classes += ' answered';
    if (isFlagged) classes += ' flagged';

    return `<button class="${classes}" onclick="jumpToExamQuestion(${idx})">${idx + 1}</button>`;
  }).join('');
}

function renderCurrentExamQuestion() {
  const box = document.getElementById('exam-question-box');
  const questions = getExamQuestions();
  if (!box || !questions.length) return;

  const q = questions[state.currentExamIndex];
  const selected = state.examAnswers[state.currentExamIndex];
  const isFlagged = state.examFlagged[state.currentExamIndex];

  let formatBadge = '';
  if (q.format === 'short_answer') {
    formatBadge = '<span class="q-badge">Short Answer (단답형)</span>';
  } else if (q.format === 'calculation') {
    formatBadge = '<span class="q-badge">Calculation (계산형)</span>';
  } else {
    formatBadge = '<span class="q-badge">Multiple Choice (선다형)</span>';
  }

  let answerInputHtml = '';
  if (q.format === 'short_answer' || q.format === 'calculation') {
    answerInputHtml = `
      <div style="margin: 1.5rem 0; padding: 1.25rem; background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius);">
        <label style="display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.6rem; color: var(--text-main);">
          ${q.format === 'calculation' ? 'Enter calculated value:' : 'Enter technical keyword or term:'}
        </label>
        <div style="display: flex; gap: 0.75rem; align-items: center;">
          <input type="text" id="short-answer-field" 
            value="${selected !== undefined ? selected : ''}" 
            placeholder="${q.placeholder || 'Type your answer here...'}"
            style="flex: 1; max-width: 480px; background: var(--bg-card); border: 2px solid ${selected ? 'var(--primary)' : 'var(--border)'}; color: var(--text-main); padding: 0.75rem 1rem; border-radius: var(--radius); font-size: 1rem; font-family: ${q.format === 'calculation' ? 'var(--font-mono)' : 'inherit'}; outline: none;"
            oninput="handleShortAnswerInput(this.value)">
          <button class="btn-primary" style="padding: 0.75rem 1.25rem;" onclick="saveCurrentTextAnswer()">Save Answer</button>
        </div>
        <p style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.6rem;">
          Case-insensitive. Synonyms and standard abbreviations are accepted.
        </p>
      </div>
    `;
  } else {
    answerInputHtml = `
      <div class="q-options">
        ${q.options.map((opt, oIdx) => `
          <div class="q-option ${selected === oIdx ? 'selected' : ''}" onclick="selectExamOption(${oIdx})">
            <span style="font-weight: 700; width: 24px;">${String.fromCharCode(65 + oIdx)}.</span>
            <span>${opt}</span>
          </div>
        `).join('')}
      </div>
    `;
  }

  let html = `
    <div class="q-meta">
      <span class="q-badge domain">${q.domainName}</span>
      ${formatBadge}
      <span class="q-badge">${q.difficulty}</span>
      <span class="q-badge" style="margin-left: auto; color: var(--warning); font-weight: 700;">${q.points} Points</span>
    </div>
    <div class="q-text">
      <strong>Question ${state.currentExamIndex + 1} of ${questions.length}:</strong><br>
      ${q.question}
    </div>
    ${answerInputHtml}
    <div class="q-actions" style="margin-top: 2rem;">
      <button class="btn-secondary" onclick="toggleExamFlag()">
        ${isFlagged ? 'Remove flag' : 'Flag for review'}
      </button>
      <div style="display: flex; gap: 0.75rem;">
        <button class="btn-secondary" onclick="prevExamQuestion()" ${state.currentExamIndex === 0 ? 'disabled' : ''}>&larr; Prev</button>
        <button class="btn-secondary" onclick="nextExamQuestion()" ${state.currentExamIndex === questions.length - 1 ? 'disabled' : ''}>Next &rarr;</button>
      </div>
      <button class="btn-primary" style="background: var(--success);" onclick="confirmSubmitExam()">Submit Exam</button>
    </div>
  `;

  box.innerHTML = html;
  renderExamQuestionGrid();
}

window.handleShortAnswerInput = function(val) {
  if (state.examSubmitted) return;
  const trimmed = val.trim();
  if (trimmed) {
    state.examAnswers[state.currentExamIndex] = trimmed;
  } else {
    delete state.examAnswers[state.currentExamIndex];
  }
  renderExamQuestionGrid();
};

window.saveCurrentTextAnswer = function() {
  const input = document.getElementById('short-answer-field');
  if (input) {
    handleShortAnswerInput(input.value);
    alert('Answer saved! Move to the next question when ready.');
  }
};


window.jumpToExamQuestion = function(idx) {
  state.currentExamIndex = idx;
  renderCurrentExamQuestion();
};

window.selectExamOption = function(optIdx) {
  if (state.examSubmitted) return;
  state.examAnswers[state.currentExamIndex] = optIdx;
  renderCurrentExamQuestion();
};

window.toggleExamFlag = function() {
  state.examFlagged[state.currentExamIndex] = !state.examFlagged[state.currentExamIndex];
  renderCurrentExamQuestion();
};

window.prevExamQuestion = function() {
  if (state.currentExamIndex > 0) {
    state.currentExamIndex--;
    renderCurrentExamQuestion();
  }
};

window.nextExamQuestion = function() {
  const questions = getExamQuestions();
  if (state.currentExamIndex < questions.length - 1) {
    state.currentExamIndex++;
    renderCurrentExamQuestion();
  }
};

window.confirmSubmitExam = function() {
  const questions = getExamQuestions();
  const answeredCount = Object.keys(state.examAnswers).length;
  const total = questions.length;
  if (confirm(`You have answered ${answeredCount} of ${total} questions. Finish and view your practice results?`)) {
    submitExam();
  }
};

function submitExam() {
  clearInterval(state.examInterval);
  state.examSubmitted = true;
  const questions = getExamQuestions();

  let totalScore = 0;
  let domainScores = {
    domain1: { earned: 0, total: 0, name: "Software Development" },
    domain2: { earned: 0, total: 0, name: "Data & DB" },
    domain3: { earned: 0, total: 0, name: "System Architecture" },
    domain4: { earned: 0, total: 0, name: "Information Security" },
    domain5: { earned: 0, total: 0, name: "IT Business & Ethics" },
    domain6: { earned: 0, total: 0, name: "Project Management" }
  };

  const results = [];

  questions.forEach((q, idx) => {
    if (!domainScores[q.domain]) return;
    domainScores[q.domain].total += q.points;
    const userVal = state.examAnswers[idx];
    let isCorrect = false;

    if (q.format === 'mcq') {
      isCorrect = (userVal === q.correct);
    } else {
      const cleanInput = String(userVal || '').trim().toLowerCase();
      if (cleanInput && q.acceptableAnswers) {
        isCorrect = q.acceptableAnswers.some(ans => ans.toLowerCase().trim() === cleanInput);
      }
    }

    if (isCorrect) {
      totalScore += q.points;
      domainScores[q.domain].earned += q.points;
    }

    results.push({
      index: idx,
      question: q,
      userAnswer: userVal,
      isCorrect: isCorrect
    });
  });

  const maxPoints = questions.reduce((sum, question) => sum + question.points, 0);
  const score = maxPoints ? Math.round(totalScore * 1000 / maxPoints) : 0;

  // Map the practice score to the platform's estimated competency bands.
  let level = 1;
  let levelDesc = "Level 1 (Novice Beginner): Fundamental understanding of computing terminology.";
  if (score >= 800) {
    level = 5;
    levelDesc = "Level 5 (Expert / Lead Architect): Capable of enterprise-scale architecture, advanced creative problem solving, and strategic IT leadership.";
  } else if (score >= 600) {
    level = 4;
    levelDesc = "Level 4 (Advanced Professional): Capable of independently executing complex software engineering, database design, and end-to-end project management.";
  } else if (score >= 400) {
    level = 3;
    levelDesc = "Level 3 (Intermediate / University Graduate Standard): Meets hiring standards for entry-level professional IT roles in industry.";
  } else if (score >= 200) {
    level = 2;
    levelDesc = "Level 2 (Basic Novice): Understands fundamental principles; requires guidance in applied industry tasks.";
  }

  renderExamReport(score, level, levelDesc, domainScores, results);
}

function renderExamReport(score, level, desc, domainScores, results) {
  const container = document.getElementById('exam-container-wrapper');
  if (!container) return;

  let html = `
    <div class="report-modal">
      <h3 style="text-align: center; font-size: 1.6rem; margin-bottom: 0.5rem;">Mock exam results</h3>
      <p style="text-align: center; color: var(--text-muted); font-size: 0.9rem;">Practice diagnostic across multiple choice, short answer, and calculation questions</p>
      
      <div class="score-badge-circle">
        <span class="score-num">${score}</span>
        <span class="score-denom">/ 1000 Points</span>
      </div>

      <div style="text-align: center; margin-bottom: 2rem;">
        <span class="level-badge">Estimated TOPCIT Level ${level}</span>
        <p style="font-size: 0.95rem; margin-top: 0.75rem; color: var(--text-main); font-weight: 500;">${desc}</p>
      </div>

      <h4 style="margin-bottom: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">Domain Breakdown</h4>
      <div style="display: flex; flex-direction: column; gap: 1rem; margin-bottom: 2rem;">
  `;

  for (const [key, d] of Object.entries(domainScores)) {
    const pct = d.total > 0 ? Math.round((d.earned / d.total) * 100) : 0;
    html += `
      <div>
        <div style="display: flex; justify-content: space-between; font-size: 0.88rem; margin-bottom: 0.25rem;">
          <span style="font-weight: 600;">${d.name}</span>
          <span style="font-family: var(--font-mono); color: var(--text-muted);">${d.earned} / ${d.total} pts (${pct}%)</span>
        </div>
        <div style="height: 10px; background: var(--bg-card); border-radius: 9999px; overflow: hidden; border: 1px solid var(--border);">
          <div style="width: ${pct}%; height: 100%; background: ${pct >= 70 ? 'var(--success)' : pct >= 40 ? 'var(--warning)' : 'var(--danger)'};"></div>
        </div>
      </div>
    `;
  }

  html += `
      </div>

      <h4 style="margin-bottom: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;">Detailed Question Review (65 Questions)</h4>
      <div style="max-height: 400px; overflow-y: auto; display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 2rem; padding-right: 0.5rem;">
  `;

  results.forEach(r => {
    const q = r.question;
    let expectedText = '';
    let userText = '';

    if (q.format === 'mcq') {
      expectedText = `${String.fromCharCode(65 + q.correct)}. ${q.options[q.correct]}`;
      userText = r.userAnswer !== undefined ? `${String.fromCharCode(65 + r.userAnswer)}. ${q.options[r.userAnswer]}` : 'Unanswered';
    } else {
      expectedText = q.acceptableAnswers.join(' / ');
      userText = r.userAnswer ? r.userAnswer : 'Unanswered';
    }

    html += `
      <div style="padding: 1rem; background: var(--bg-main); border: 1px solid ${r.isCorrect ? 'var(--success)' : 'var(--danger)'}; border-radius: var(--radius);">
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 0.35rem;">
          <span style="font-weight: 700; color: ${r.isCorrect ? 'var(--success)' : 'var(--danger)'};">
            ${r.isCorrect ? '✓ Correct (+ ' + q.points + ' pts)' : '✗ Incorrect (0 pts)'}
          </span>
          <span style="color: var(--text-muted);">${q.domainName} &bull; ${q.format.toUpperCase()}</span>
        </div>
        <p style="font-size: 0.92rem; font-weight: 600; margin-bottom: 0.5rem;">Q${r.index + 1}: ${q.question}</p>
        <p style="font-size: 0.85rem; margin-bottom: 0.25rem;"><strong>Your Answer:</strong> <span style="color: ${r.isCorrect ? 'var(--success)' : 'var(--danger)'};">${userText}</span></p>
        <p style="font-size: 0.85rem; margin-bottom: 0.5rem;"><strong>Correct Answer:</strong> <span style="color: var(--success); font-weight: 600;">${expectedText}</span></p>
        <p style="font-size: 0.82rem; color: var(--text-muted);">${q.explanation}</p>
      </div>
    `;
  });

  html += `
      </div>

      <div style="display: flex; justify-content: center; gap: 1rem;">
        <button class="btn-primary" onclick="window.location.hash='#plan'">Back to 14-Day Plan</button>
        <button class="btn-secondary" onclick="window.location.reload()">Retake Full Exam</button>
      </div>
    </div>
  `;

  container.innerHTML = html;
}

// ----------------------------------------------------
// Global Search Engine
// ----------------------------------------------------
function setupSearch() {
  const searchInput = document.getElementById('global-search-input');
  const resultsBox = document.getElementById('search-results');
  if (!searchInput || !resultsBox) return;

  const search = () => {
    const query = searchInput.value.toLowerCase().trim();
    resultsBox.replaceChildren();
    if (!query) { resultsBox.hidden = true; return; }
    const matches = Object.entries(getModulesData()).flatMap(([domainId, domain]) => domain.sections
      .filter(section => `${section.title} ${section.content}`.toLowerCase().includes(query))
      .map(section => ({ domainId, domain: domain.title, section }))
    ).slice(0, 8);
    if (!matches.length) {
      const empty = document.createElement('p');
      empty.className = 'search-empty';
      empty.textContent = 'No matching topics found';
      resultsBox.append(empty);
    }
    matches.forEach(match => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'search-result';
      button.setAttribute('role', 'option');
      button.innerHTML = `<strong></strong><span></span>`;
      button.querySelector('strong').textContent = match.section.title;
      button.querySelector('span').textContent = match.domain;
      button.addEventListener('click', () => {
        resultsBox.hidden = true;
        window.location.hash = '#' + match.domainId;
        setTimeout(() => document.getElementById(match.section.id)?.scrollIntoView({ behavior: 'smooth' }), 150);
      });
      resultsBox.append(button);
    });
    resultsBox.hidden = false;
  };
  searchInput.addEventListener('input', search);
  searchInput.addEventListener('keydown', event => {
    if (event.key === 'Escape') resultsBox.hidden = true;
    if (event.key === 'Enter') resultsBox.querySelector('.search-result')?.click();
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.search-box')) resultsBox.hidden = true;
  });
}

// ----------------------------------------------------
// High-Yield Cheat Sheet Engine
// ----------------------------------------------------
function renderCheatSheet() {
  const container = document.getElementById('cheatsheet-container');
  if (!container) return;

  container.innerHTML = `
    <div class="summary-card" style="margin-bottom: 2rem;">
      <h3 style="color: var(--primary); margin-bottom: 1rem;">Essential TOPCIT formulas</h3>
      <table class="data-table">
        <thead>
          <tr><th>Topic</th><th>Concept / Name</th><th>Exact Formula</th><th>Key Variables</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>PM & Comms</strong></td><td>Communication Channels</td><td><code>Channels = N &times; (N - 1) / 2</code></td><td>N = number of team members</td></tr>
          <tr><td><strong>PM & Schedule</strong></td><td>PERT Expected Duration</td><td><code>TE = (O + 4M + P) / 6</code></td><td>O = Optimistic, M = Most Likely, P = Pessimistic</td></tr>
          <tr><td><strong>PM & Schedule</strong></td><td>PERT Standard Deviation</td><td><code>&sigma; = (P - O) / 6</code></td><td>Variance &sigma;² = ((P - O) / 6)²</td></tr>
          <tr><td><strong>PM & EVM</strong></td><td>Cost Variance (CV)</td><td><code>CV = EV - AC</code></td><td>Positive = Under budget; Negative = Over budget</td></tr>
          <tr><td><strong>PM & EVM</strong></td><td>Schedule Variance (SV)</td><td><code>SV = EV - PV</code></td><td>Positive = Ahead of schedule; Negative = Behind</td></tr>
          <tr><td><strong>PM & EVM</strong></td><td>Cost Performance Index</td><td><code>CPI = EV / AC</code></td><td>&gt; 1.0 = Favorable (Under budget)</td></tr>
          <tr><td><strong>PM & EVM</strong></td><td>Schedule Performance Index</td><td><code>SPI = EV / PV</code></td><td>&gt; 1.0 = Favorable (Ahead of schedule)</td></tr>
          <tr><td><strong>PM & EVM</strong></td><td>Estimate at Completion (EAC)</td><td><code>EAC = BAC / CPI</code></td><td>BAC = Total Project Baseline Budget</td></tr>
          <tr><td><strong>Software Eng.</strong></td><td>Cyclomatic Complexity</td><td><code>V(G) = E - N + 2</code></td><td>E = Edges, N = Nodes in flow graph</td></tr>
          <tr><td><strong>Networking</strong></td><td>Usable Host Count (CIDR)</td><td><code>Hosts = 2^(32 - prefix) - 2</code></td><td>Subtract Network ID & Broadcast ID</td></tr>
          <tr><td><strong>Security</strong></td><td>Symmetric Key Count</td><td><code>Keys = N &times; (N - 1) / 2</code></td><td>Asymmetric Keys = 2N</td></tr>
          <tr><td><strong>ITSM / SLA</strong></td><td>System Availability %</td><td><code>Availability = [MTBF / (MTBF + MTTR)] &times; 100%</code></td><td>MTBF = Reliability, MTTR = Maintainability</td></tr>
        </tbody>
      </table>
    </div>
  `;
}
