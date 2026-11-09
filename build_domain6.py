# Domain 6 data: Project Management & Technical Communication
d6 = {
    "id": "domain6",
    "title": "Domain 6: Project Management & Technical Communication",
    "icon": "📊",
    "description": "Business communication models, Channel calculation formula N(N-1)/2, MECE, 5 Whys, Fishbone, Technical writing (RFP, SRS, Meeting Minutes), Presentations (10-20-30), Project organizational structures, PMBOK, WBS, Critical Path Method (CPM), PERT, Earned Value Management (EVM), and Risk Management.",
    "sections": [
        {
            "id": "pm-comm",
            "title": "1. Business Communication & Communication Channel Formula",
            "badge": "Day 11 • Session 1",
            "summary": "The communication transmission model, communication directions, and the essential mathematical formula for communication channels.",
            "content": """
<h3>1. The Communication Process Model</h3>
<p>Communication is the reciprocal exchange of information between two or more parties:</p>
<pre class="code-block">
[Sender] --(Encoding)--> [Message] --(Channel / Medium)--> [Receiver] --(Decoding)--> [Understanding]
   ^                                     | (Noise)                                           |
   +-------------------------------- (Feedback Loop) ----------------------------------------+
</pre>
<ul>
  <li><strong>Encoding (부호화):</strong> Converting thoughts or intentions into a symbolic message format (words, diagrams, gestures).</li>
  <li><strong>Channel (채널):</strong> The medium through which the message travels (face-to-face, email, video conference, documentation).</li>
  <li><strong>Noise (소음 / 잡음):</strong> Psychological, environmental, cultural, or technical interference that distorts message transmission.</li>
  <li><strong>Decoding (해독):</strong> The receiver interprets and assigns meaning to the received symbols.</li>
  <li><strong>Feedback (피드백):</strong> Verification from receiver to sender ensuring the message was received and understood as intended.</li>
</ul>

<h3>2. The Communication Channels Formula</h3>
<div class="note-box alert-warning">
  <strong>Guaranteed TOPCIT Exam Calculation Question:</strong>
  <p>As the number of team members (<em>N</em>) grows, communication complexity explodes combinatorially. The total number of unique communication channels is given by:</p>
  <pre class="code-block">Total Communication Channels = N &times; (N - 1) / 2</pre>
</div>

<h4>Step-by-Step Calculation Examples:</h4>
<table class="data-table">
  <thead>
    <tr><th>Team Size (N)</th><th>Calculation</th><th>Total Channels</th><th>Channel Growth Rate</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>4 members</strong></td><td>4 &times; 3 / 2</td><td><strong>6 channels</strong></td><td>Baseline</td></tr>
    <tr><td><strong>5 members</strong></td><td>5 &times; 4 / 2</td><td><strong>10 channels</strong></td><td>+4 channels (+67%)</td></tr>
    <tr><td><strong>8 members</strong></td><td>8 &times; 7 / 2</td><td><strong>28 channels</strong></td><td>+18 channels (+180%)</td></tr>
    <tr><td><strong>10 members</strong></td><td>10 &times; 9 / 2</td><td><strong>45 channels</strong></td><td>+35 channels (+350%)</td></tr>
  </tbody>
</table>
<div class="note-box alert-info">
  <strong>Sample Exam Problem:</strong> "A project team originally had 6 members. Two new developers join the team. How many NEW communication channels have been added?"<br>
  <em>Solution:</em>
  <ul>
    <li>Initial (N = 6): <code>6 &times; 5 / 2 = 15 channels</code></li>
    <li>New (N = 8): <code>8 &times; 7 / 2 = 28 channels</code></li>
    <li>Added Channels: <code>28 - 15 = <strong>13 new channels</strong></code></li>
  </ul>
</div>
"""
        },
        {
            "id": "pm-problem-solving",
            "title": "2. Logical Thinking & Problem Solving Techniques",
            "badge": "Day 11 • Session 2",
            "summary": "McKinsey MECE principle, logic trees, 5 Whys root cause analysis, Ishikawa cause-and-effect diagrams, and Delphi consensus.",
            "content": """
<h3>1. The MECE Principle (Mutually Exclusive, Collectively Exhaustive)</h3>
<p>Developed by McKinsey, <strong>MECE (상호 배제와 전체 포괄)</strong> is the foundational rule of structured business analysis:</p>
<ul>
  <li><strong>Mutually Exclusive (상호 배제):</strong> No overlaps or duplicate categorizations among elements.</li>
  <li><strong>Collectively Exhaustive (전체 포괄):</strong> No gaps or omissions; all possibilities in the problem space are completely accounted for.</li>
</ul>

<h3>2. Logic Trees (로직 트리)</h3>
<ul>
  <li><strong>Issue Tree (What Tree):</strong> Decomposes an overarching problem into structured sub-issues to define "What is the problem?".</li>
  <li><strong>Why Tree (Cause Tree):</strong> Recursively drills down into causes to identify "Why is this problem happening?".</li>
  <li><strong>How Tree (Solution Tree):</strong> Brainstorms concrete action items to answer "How can we resolve this?".</li>
</ul>

<h3>3. Root Cause Analysis Tools</h3>
<div class="card-grid">
  <div class="summary-card">
    <h4>5 Whys Technique (5대 왜 분석)</h4>
    <p>Iteratively asking "Why?" five times to drill past superficial symptoms down to the underlying systemic failure.</p>
    <p><em>Example:</em> Production server crashed &rarr; Out of disk space &rarr; Log files filled drive &rarr; Log rotation script failed &rarr; Script syntax error committed without automated CI testing &rarr; <strong>Root Cause:</strong> Lack of automated regression checks on deployment scripts.</p>
  </div>
  <div class="summary-card">
    <h4>Fishbone / Ishikawa Diagram (특성요인도)</h4>
    <p>Visual cause-and-effect diagram shaped like a fish skeleton. The head represents the problem/effect; the spine branches into major cause categories:</p>
    <ul>
      <li><strong>Manufacturing (4M/6M):</strong> Man, Machine, Material, Method, Measurement, Mother Nature.</li>
      <li><strong>Service / IT (4P):</strong> Policies, Procedures, People, Plant/Technology.</li>
    </ul>
  </div>
  <div class="summary-card">
    <h4>Delphi Method (델파이 기법)</h4>
    <p>A structured communication technique for achieving objective expert consensus on complex forecasting or risk analysis through multiple rounds of <strong>anonymous questionnaires</strong> with aggregated statistical feedback.</p>
  </div>
</div>
"""
        },
        {
            "id": "pm-documentation",
            "title": "3. Business & Technical Document Writing",
            "badge": "Day 11 • Session 3",
            "summary": "Official business letters, meeting minutes best practices, RFI, RFP, Proposal, SRS standards, and Requirements Traceability Matrices.",
            "content": """
<h3>1. Core Business Documents</h3>
<ul>
  <li><strong>Official Letters (공문서):</strong> Formal external written correspondence. Comprises Title, Document Number, Date of Dispatch, Recipient, Body (Context, Action required), Attachments, and Official Stamp/Signature.</li>
  <li><strong>Meeting Minutes (회의록):</strong>
    <div class="note-box alert-info">
      <strong>Mandatory Meeting Minutes Elements:</strong>
      <ol>
        <li>Meeting Date, Time, and Location.</li>
        <li>Attendees and Absentees.</li>
        <li>Meeting Agenda / Objectives.</li>
        <li><strong>Decisions Made (결정 사항):</strong> Clear consensus reached.</li>
        <li><strong>Action Items (후속 조치):</strong> Specific task, <strong>Assigned Owner (담당자)</strong>, and <strong>Strict Deadline (완료 기한)</strong>.</li>
        <li>Next Meeting Schedule.</li>
      </ol>
    </div>
  </li>
  <li><strong>Email Etiquette:</strong> Direct, clear subject line including prefix tag (e.g., <code>[Urgent Request]</code>, <code>[Notice]</code>); inverted pyramid style (conclusion first).</li>
</ul>

<h3>2. Technical Procurement Documents</h3>
<table class="data-table">
  <thead>
    <tr><th>Document</th><th>Full Name</th><th>Issuer</th><th>Purpose & Content</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>RFI</strong></td><td>Request for Information (정보요청서)</td><td>Buyer / Client</td><td>Exploratory market survey sent to vendors to gather information regarding industry trends, vendor capabilities, and technology options before finalizing budget.</td></tr>
    <tr><td><strong>RFP</strong></td><td>Request for Proposal (제안요청서)</td><td>Buyer / Client</td><td>Formal solicitation document specifying project scope, technical requirements, schedule constraints, and evaluation criteria for vendor selection.</td></tr>
    <tr><td><strong>Proposal</strong></td><td>제안서</td><td>Vendor / Bidders</td><td>Vendor's comprehensive technical and commercial response detailing methodology, architecture, staffing, cost quote, and schedule.</td></tr>
    <tr><td><strong>SRS</strong></td><td>Software Requirements Specification (소프트웨어 요구사항 정의서)</td><td>Client &amp; Vendor</td><td>Complete description of system behavior (IEEE 830 standard), covering both <strong>Functional</strong> and <strong>Non-Functional</strong> requirements.</td></tr>
    <tr><td><strong>RTM</strong></td><td>Requirements Traceability Matrix (요구사항 추적표)</td><td>Project Team</td><td>Cross-reference matrix mapping every user requirement to corresponding architectural components, source code modules, and test case IDs. Ensures no requirement is missed during implementation and verification.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "pm-organization",
            "title": "4. Project Concept & Organizational Structures (PMBOK)",
            "badge": "Day 12 • Session 1",
            "summary": "Project vs operational work, the triple constraint, functional vs matrix vs projectized organizations, and PMBOK process groups.",
            "content": """
<h3>1. Project vs Operations</h3>
<table class="data-table">
  <thead>
    <tr><th>Dimension</th><th>Project (프로젝트)</th><th>Operations (운영 / 상시 업무)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Duration</strong></td><td><strong>Temporary (한시성):</strong> Has a definite start date and end date. Concludes when objectives are reached or project terminated.</td><td><strong>Ongoing & Repetitive (지속성):</strong> Continuous, day-to-day ongoing business activities.</td></tr>
    <tr><td><strong>Output</strong></td><td><strong>Unique (유일성):</strong> Delivers a unique product, service, or result.</td><td>Standardized, repetitive goods or services.</td></tr>
    <tr><td><strong>Elaboration</strong></td><td><strong>Progressive Elaboration:</strong> Developed in steps and continuing by increments as information clarifies.</td><td>Standard operating procedures (SOPs).</td></tr>
  </tbody>
</table>

<h3>2. Project Organizational Structures</h3>
<table class="data-table">
  <thead>
    <tr><th>Structure</th><th>PM Authority</th><th>Resource Availability</th><th>Team Reporting Line</th><th>Pros & Cons</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Functional (기능식)</strong></td><td>Little or None</td><td>Very Low</td><td>Team members report strictly to Functional Department Managers (e.g., Engineering, Marketing). PM acts as a mere coordinator.</td><td>Clear career path and technical specialization; poor project focus, slow cross-department communication.</td></tr>
    <tr><td><strong>Weak Matrix (약한 매트릭스)</strong></td><td>Low</td><td>Low</td><td>Dual reporting, but Functional Manager retains major authority. PM acts as project expediter.</td><td>Better project coordination than pure functional; authority ambiguity.</td></tr>
    <tr><td><strong>Balanced Matrix (균형 매트릭스)</strong></td><td>Moderate</td><td>Moderate</td><td>Power shared equally between Functional Manager and Project Manager.</td><td>Balanced technical depth and project urgency; dual-boss conflict.</td></tr>
    <tr><td><strong>Strong Matrix (강한 매트릭스)</strong></td><td>Moderate to High</td><td>Moderate to High</td><td>Dedicated Project Management department. PM holds primary budget and schedule authority.</td><td>Strong project focus while preserving departmental home; administrative overhead.</td></tr>
    <tr><td><strong>Projectized (프로젝트 전담식)</strong></td><td><strong>High to Almost Total</strong></td><td><strong>High to Full</strong></td><td>Full-time dedicated project teams reporting directly to the PM. Departmental silos eliminated.</td><td>Highest loyalty and speed; risk of "No Home" anxiety for team members when project ends.</td></tr>
  </tbody>
</table>

<h3>3. PMBOK 5 Process Groups & 10 Knowledge Areas</h3>
<ul>
  <li><strong>5 Process Groups:</strong>
    <ol>
      <li><strong>Initiating (착수):</strong> Define project, obtain authorization via the <strong>Project Charter (프로젝트 헌장)</strong>, identify stakeholders.</li>
      <li><strong>Planning (기획):</strong> Establish scope, refine objectives, create WBS, schedule, budget, risk management plan.</li>
      <li><strong>Executing (실행):</strong> Complete the work defined in the PM plan.</li>
      <li><strong>Monitoring & Controlling (감시 및 통제):</strong> Track, review, and regulate project performance against baselines; manage change requests.</li>
      <li><strong>Closing (종료):</strong> Formally finalize all activities, handover deliverables, document lessons learned.</li>
    </ol>
  </li>
  <li><strong>10 Knowledge Areas:</strong> Integration, Scope, Schedule, Cost, Quality, Resource, Communications, Risk, Procurement, Stakeholder Management.</li>
</ul>
"""
        },
        {
            "id": "pm-schedule",
            "title": "5. Scope & Schedule Management (WBS, CPM & PERT)",
            "badge": "Day 12 • Session 2",
            "summary": "Work Breakdown Structure, Precedence Diagramming Method, Critical Path Method calculations, float/slack, and PERT 3-point estimation.",
            "content": """
<h3>1. Work Breakdown Structure (WBS - 작업 분류 체계)</h3>
<p>A deliverable-oriented hierarchical decomposition of the total project scope into manageable, trackable components.</p>
<ul>
  <li><strong>Work Package (작업 패키지):</strong> The lowest level of the WBS where cost and schedule can be reliably estimated and managed (8/80 hour rule).</li>
  <li><strong>Scope Creep (범위 크립):</strong> Uncontrolled expansion of product or project scope without adjustments to time, cost, and resources. Prevented via formal Change Control Boards (CCB).</li>
  <li><strong>Gold Plating (골드 플레이팅):</strong> Giving the customer extra, unrequested features. Discouraged in PMBOK because it adds unbudgeted cost and risk.</li>
</ul>

<h3>2. Critical Path Method (CPM - 임계 경로법)</h3>
<p>The <strong>Critical Path</strong> is the longest sequence of dependent activities through a network diagram, determining the <strong>shortest possible total project duration</strong>.</p>
<ul>
  <li>Any delay on a critical path activity delays the entire project completion date!</li>
  <li><strong>Total Float / Slack (여유 시간)</strong> on the critical path is strictly <strong>ZERO</strong>.</li>
  <li><strong>Float Formulas:</strong>
    <pre class="code-block">Total Float = Late Start (LS) - Early Start (ES) = Late Finish (LF) - Early Finish (EF)</pre>
  </li>
</ul>

<h3>3. PERT 3-Point Estimation (베타 분포 삼점 추정)</h3>
<div class="note-box alert-warning">
  <strong>Guaranteed TOPCIT Formula - PERT Beta Distribution:</strong>
  <ul>
    <li><strong>Optimistic Time (O - 낙관치):</strong> Best-case scenario duration.</li>
    <li><strong>Most Likely Time (M - 최빈치):</strong> Realistic duration under normal conditions.</li>
    <li><strong>Pessimistic Time (P - 비관치):</strong> Worst-case scenario duration.</li>
  </ul>
  <pre class="code-block">
Expected Duration (TE) = (O + 4M + P) / 6
Standard Deviation (&sigma;)  = (P - O) / 6
Variance (&sigma;²)            = ((P - O) / 6)²
</pre>
  <p><em>Example Calculation:</em> Given Optimistic = 4 days, Most Likely = 7 days, Pessimistic = 16 days:</p>
  <ul>
    <li><code>TE = (4 + 4&times;7 + 16) / 6 = (4 + 28 + 16) / 6 = 48 / 6 = <strong>8 days</strong></code></li>
    <li><code>Standard Deviation &sigma; = (16 - 4) / 6 = 12 / 6 = <strong>2 days</strong></code></li>
  </ul>
</div>

<h4>Schedule Compression Techniques:</h4>
<ul>
  <li><strong>Crashing (공정 단축):</strong> Adding resources to critical path activities to shorten duration (e.g., overtime, adding personnel). <em>Direct consequence: Increases Cost.</em></li>
  <li><strong>Fast Tracking (공정 중첩):</strong> Performing activities in parallel that were originally planned in sequence. <em>Direct consequence: Increases Risk and rework.</em></li>
</ul>
"""
        },
        {
            "id": "pm-evm-risk",
            "title": "6. Cost Management (EVM) & Project Risk Management",
            "badge": "Day 12 • Session 3",
            "summary": "The complete Earned Value Management formula suite (PV, EV, AC, CV, SV, CPI, SPI, EAC), risk response strategies for threats and opportunities.",
            "content": """
<h3>1. Earned Value Management (EVM - 획득 가치 관리)</h3>
<p>EVM integrates project scope, cost, and schedule to assess project performance and forecast future outcomes.</p>

<h4>Core EVM Metrics:</h4>
<table class="data-table">
  <thead>
    <tr><th>Acronym</th><th>Term</th><th>Meaning</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>BAC</strong></td><td>Budget at Completion (완료 시점 예산)</td><td>Total approved project baseline budget.</td></tr>
    <tr><td><strong>PV</strong></td><td>Planned Value (계획 가치 / BCWS)</td><td>Authorized budget assigned to scheduled work to date.</td></tr>
    <tr><td><strong>EV</strong></td><td>Earned Value (획득 가치 / BCWP)</td><td>Value of work <strong>actually completed</strong> to date, expressed in approved budget.</td></tr>
    <tr><td><strong>AC</strong></td><td>Actual Cost (실제 원가 / ACWP)</td><td>Total realized cost incurred in accomplishing the work to date.</td></tr>
  </tbody>
</table>

<h4>EVM Variance & Performance Formulas (Must Memorize!):</h4>
<div class="note-box alert-warning">
  <table class="data-table">
    <thead>
      <tr><th>Metric</th><th>Formula</th><th>Good State (&gt; 0 or &gt; 1.0)</th><th>Bad State (&lt; 0 or &lt; 1.0)</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Cost Variance (CV)</strong></td><td><code>CV = EV - AC</code></td><td>Positive (&gt;0): <strong>Under Budget</strong> (Cost savings)</td><td>Negative (&lt;0): <strong>Over Budget</strong> (Cost overrun)</td></tr>
      <tr><td><strong>Schedule Variance (SV)</strong></td><td><code>SV = EV - PV</code></td><td>Positive (&gt;0): <strong>Ahead of Schedule</strong></td><td>Negative (&lt;0): <strong>Behind Schedule</strong></td></tr>
      <tr><td><strong>Cost Performance Index (CPI)</strong></td><td><code>CPI = EV / AC</code></td><td>&gt; 1.0: Earning more value per dollar spent</td><td>&lt; 1.0: Cost overrun (e.g., 0.8 means getting 80&cent; of value per dollar)</td></tr>
      <tr><td><strong>Schedule Performance Index (SPI)</strong></td><td><code>SPI = EV / PV</code></td><td>&gt; 1.0: Progressing faster than planned</td><td>&lt; 1.0: Progressing slower than planned</td></tr>
    </tbody>
  </table>
  <h4>Forecasting:</h4>
  <ul>
    <li><strong>Estimate at Completion (EAC):</strong> Expected total cost when project is finished: <code>EAC = BAC / CPI</code>.</li>
    <li><strong>Estimate to Complete (ETC):</strong> Expected cost needed to finish remaining work: <code>ETC = EAC - AC</code>.</li>
  </ul>
</div>

<h3>2. Project Risk Management & Response Strategies</h3>
<ul>
  <li><strong>Risk Score Formula:</strong> <code>Risk Score = Probability &times; Impact</code>.</li>
  <li><strong>Expected Monetary Value (EMV):</strong> <code>EMV = Probability &times; Financial Impact</code>.</li>
</ul>

<h4>Risk Response Strategies Matrix:</h4>
<table class="data-table">
  <thead>
    <tr><th>Strategy for Negative Risks (Threats)</th><th>Operational Meaning</th><th>Strategy for Positive Risks (Opportunities)</th><th>Operational Meaning</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Avoid (회피)</strong></td><td>Eliminate threat entirely (e.g., cancel risky feature, adopt proven tech).</td><td><strong>Exploit (활용)</strong></td><td>Ensure opportunity definitely happens (e.g., assign top talent).</td></tr>
    <tr><td><strong>Mitigate (완화)</strong></td><td>Reduce probability or impact (e.g., add redundant server, prototype).</td><td><strong>Enhance (증대)</strong></td><td>Increase probability or positive impact.</td></tr>
    <tr><td><strong>Transfer (전가)</strong></td><td>Shift ownership and financial impact to third party (e.g., Insurance, Warranty, Outsourcing).</td><td><strong>Share (공유)</strong></td><td>Partner with third party to capture mutual benefit.</td></tr>
    <tr><td><strong>Accept (수용)</strong></td><td>Acknowledge risk without changing plan (Active: create contingency reserve; Passive: deal when happens).</td><td><strong>Accept (수용)</strong></td><td>Take advantage if opportunity arises without active pursuit.</td></tr>
  </tbody>
</table>
"""
        }
    ]
}
