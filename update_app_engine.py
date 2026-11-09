with open('/home/justin/Desktop/review/review/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace renderCurrentExamQuestion and submitExam
new_render_q = """function renderCurrentExamQuestion() {
  const box = document.getElementById('exam-question-box');
  const questions = getExamQuestions();
  if (!box || !questions.length) return;

  const q = questions[state.currentExamIndex];
  const selected = state.examAnswers[state.currentExamIndex];
  const isFlagged = state.examFlagged[state.currentExamIndex];

  let formatBadge = '';
  if (q.format === 'short_answer') {
    formatBadge = '<span class="q-badge" style="background: rgba(16, 185, 129, 0.2); color: var(--success); font-weight: 700;">✍️ Short Answer (단답형)</span>';
  } else if (q.format === 'calculation') {
    formatBadge = '<span class="q-badge" style="background: rgba(245, 158, 11, 0.2); color: var(--warning); font-weight: 700;">🔢 Calculation (계산형)</span>';
  } else {
    formatBadge = '<span class="q-badge" style="background: rgba(59, 130, 246, 0.2); color: var(--primary);">📋 Multiple Choice (선다형)</span>';
  }

  let answerInputHtml = '';
  if (q.format === 'short_answer' || q.format === 'calculation') {
    answerInputHtml = `
      <div style="margin: 1.5rem 0; padding: 1.25rem; background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius);">
        <label style="display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.6rem; color: var(--text-main);">
          ${q.format === 'calculation' ? '🧮 Enter Calculated Value:' : '✍️ Enter Technical Keyword / Term:'}
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
          💡 Case-insensitive. Synonyms and standard abbreviations accepted.
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
        ${isFlagged ? '🚩 Unflag' : '🏳️ Flag for Review'}
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
"""

# Now write updated app.js
import re
text = re.sub(r'function renderCurrentExamQuestion\(\) \{[\s\S]*?renderExamQuestionGrid\(\);\s*\}', new_render_q, text)

# Update submitExam logic for mixed grading
new_submit = """function submitExam() {
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

  // Calculate official TOPCIT Competency Level (0 - 1000 scale)
  let level = 1;
  let levelDesc = "Level 1 (Novice Beginner): Fundamental understanding of computing terminology.";
  if (totalScore >= 800) {
    level = 5;
    levelDesc = "Level 5 (Expert / Lead Architect): Capable of enterprise-scale architecture, advanced creative problem solving, and strategic IT leadership.";
  } else if (totalScore >= 600) {
    level = 4;
    levelDesc = "Level 4 (Advanced Professional): Capable of independently executing complex software engineering, database design, and end-to-end project management.";
  } else if (totalScore >= 400) {
    level = 3;
    levelDesc = "Level 3 (Intermediate / University Graduate Standard): Meets hiring standards for entry-level professional IT roles in industry.";
  } else if (totalScore >= 200) {
    level = 2;
    levelDesc = "Level 2 (Basic Novice): Understands fundamental principles; requires guidance in applied industry tasks.";
  }

  renderExamReport(totalScore, level, levelDesc, domainScores, results);
}

function renderExamReport(score, level, desc, domainScores, results) {
  const container = document.getElementById('exam-container-wrapper');
  if (!container) return;

  let html = `
    <div class="report-modal">
      <h3 style="text-align: center; font-size: 1.6rem; margin-bottom: 0.5rem;">🎓 Official CICT / TOPCIT Assessment Report</h3>
      <p style="text-align: center; color: var(--text-muted); font-size: 0.9rem;">Diagnostic Evaluation & Competency Rating (Mixed MCQ + Short Answer + Calculations)</p>
      
      <div class="score-badge-circle">
        <span class="score-num">${score}</span>
        <span class="score-denom">/ 1000 Points</span>
      </div>

      <div style="text-align: center; margin-bottom: 2rem;">
        <span class="level-badge">TOPCIT Competency Level ${level}</span>
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
        <p style="font-size: 0.82rem; color: var(--text-muted); font-style: italic;">💡 ${q.explanation}</p>
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
}"""

text = re.sub(r'function submitExam\(\) \{[\s\S]*?container\.innerHTML = html;\s*\}', new_submit, text)

with open('/home/justin/Desktop/review/review/js/app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated app.js with mixed question UI and grading!")
