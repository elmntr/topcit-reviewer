# Domain 5 data: Understanding the IT Business and Ethics
d5 = {
    "id": "domain5",
    "title": "Domain 5: Understanding the IT Business and Ethics",
    "icon": "💼",
    "description": "Business-IT alignment, Gartner Hype Cycle, Porter's Value Chain, Strategic Frameworks (SWOT, 3C, 5-Forces, BCG, PEST), IT Governance (COBIT), Enterprise Architecture (TOGAF, Zachman), ISP, S/W Acquisition (ISO 12207), BPR, Six Sigma, ERP/SCM/CRM, ITIL/SLA, and IP Law & Ethics.",
    "sections": [
        {
            "id": "biz-concept",
            "title": "1. IT Business Concept, Alignment & Gartner Hype Cycle",
            "badge": "Day 9 • Session 1",
            "summary": "Strategic alignment of IT with business goals, the IT productivity paradox, digital transformation, and the 5 stages of the Gartner Hype Cycle.",
            "content": """
<h3>1. IT Business Concept & Strategic Alignment</h3>
<p>Modern enterprises no longer view IT merely as a back-office cost center for automation; IT is a <strong>strategic core competency</strong> that enables innovative business models, operational disruption, and competitive advantage.</p>

<div class="note-box alert-warning">
  <strong>The IT Productivity Paradox (IT 생산성 패러독스 - Robert Solow):</strong>
  <p>"We see computers everywhere except in the productivity statistics." Massive investments in IT systems do not automatically translate into improved corporate profitability if:</p>
  <ul>
    <li>IT investments are misaligned with business strategy.</li>
    <li>Business processes remain outdated (digitizing a broken process yields a faster broken process).</li>
    <li>Employees lack adequate training, change management, and cultural adoption.</li>
  </ul>
</div>

<h3>2. The Gartner Hype Cycle (가트너 하이프 사이클)</h3>
<p>A graphical representation of the maturity, adoption, and social application of emerging technologies through five distinct phases:</p>

<table class="data-table">
  <thead>
    <tr><th>Phase</th><th>Name</th><th>Characteristics & Market Sentiment</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Phase 1</strong></td><td><strong>Innovation Trigger (기술 촉발)</strong></td><td>A breakthrough technology announcement or proof-of-concept sparks public interest. Commercially viable products do not yet exist.</td></tr>
    <tr><td><strong>Phase 2</strong></td><td><strong>Peak of Inflated Expectations (정점 / 버블기)</strong></td><td>Media frenzy creates unrealistic expectations and irrational exuberance. A few success stories accompanied by many unpublicized failures.</td></tr>
    <tr><td><strong>Phase 3</strong></td><td><strong>Trough of Disillusionment (환멸 단계)</strong></td><td>Experiments and implementations fail to deliver on excessive hype. Public interest wanes, media turns skeptical, and poorly capitalized startups collapse.</td></tr>
    <tr><td><strong>Phase 4</strong></td><td><strong>Slope of Enlightenment (계몽 단계)</strong></td><td>True real-world use cases, benefits, and architectural best practices emerge. Second-generation refined products are launched with solid enterprise value.</td></tr>
    <tr><td><strong>Phase 5</strong></td><td><strong>Plateau of Productivity (생산성 안정기)</strong></td><td>Mainstream commercial adoption takes off. Clear ROI criteria established; technology becomes a standard operational component.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "biz-strategy",
            "title": "2. Porter's Value Chain & Strategic Analysis Frameworks",
            "badge": "Day 9 • Session 2",
            "summary": "Michael Porter's Value Chain Model, SWOT matrix cross-strategies, 3C analysis, Porter's Five Forces, and the BCG growth-share matrix.",
            "content": """
<h3>1. Michael Porter's Value Chain Model (가치사슬 모형)</h3>
<p>Categorizes a firm's organizational activities into <strong>Primary Activities</strong> and <strong>Support Activities</strong> that collectively create margin/value for customers:</p>

<table class="data-table">
  <thead>
    <tr><th>Category</th><th>Activity Name</th><th>Operational Function & Role</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="5"><strong>Primary Activities (본원적 활동)</strong><br>Directly involved in the physical creation, sale, and support of the product.</td><td><strong>Inbound Logistics (물류 투입)</strong></td><td>Receiving, storing, and disseminating raw material inputs (e.g., warehouse warehousing).</td></tr>
    <tr><td><strong>Operations (운영 / 생산)</strong></td><td>Transforming inputs into final products/services (e.g., machining, assembly, testing).</td></tr>
    <tr><td><strong>Outbound Logistics (물류 산출)</strong></td><td>Collecting, storing, and physically distributing products to buyers (e.g., shipping, fulfillment).</td></tr>
    <tr><td><strong>Marketing & Sales (마케팅 및 영업)</strong></td><td>Inducing buyers to purchase the product (e.g., advertising, pricing, sales force).</td></tr>
    <tr><td><strong>Service (서비스)</strong></td><td>Maintaining and enhancing product value after sale (e.g., installation, repair, warranty).</td></tr>
    <tr><td rowspan="4"><strong>Support Activities (지원 활동)</strong><br>Provide infrastructure and foundational inputs across all primary activities.</td><td><strong>Firm Infrastructure (기업 구조 / 인프라)</strong></td><td>General management, legal, finance, accounting, quality management.</td></tr>
    <tr><td><strong>Human Resource Management (HRM)</strong></td><td>Recruiting, hiring, training, development, and compensation.</td></tr>
    <tr><td><strong>Technology Development (기술 개발)</strong></td><td>R&amp;D, IT systems, process engineering, software architecture.</td></tr>
    <tr><td><strong>Procurement (조달 활동)</strong></td><td>Purchasing raw materials, services, and assets used across the enterprise.</td></tr>
  </tbody>
</table>

<h3>2. Strategic Analysis Frameworks</h3>

<h4>A) SWOT Analysis & Cross-Strategies</h4>
<table class="data-table">
  <thead>
    <tr><th>SWOT Matrix</th><th>Strengths (강점 - S)</th><th>Weaknesses (약점 - W)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Opportunities (기회 - O)</strong></td><td><strong>SO Strategy (Aggressive / 공격적):</strong> Use internal strengths to aggressively capitalize on external market opportunities.</td><td><strong>WO Strategy (Turnaround / 보완):</strong> Overcome internal weaknesses by exploiting external opportunities.</td></tr>
    <tr><td><strong>Threats (위협 - T)</strong></td><td><strong>ST Strategy (Diversification / 우회):</strong> Use internal strengths to avoid or neutralize external threats.</td><td><strong>WT Strategy (Defensive / 철수):</strong> Minimize internal weaknesses and avoid external threats (retrenchment/liquidation).</td></tr>
  </tbody>
</table>

<h4>B) Porter's Five Forces Model (5대 경쟁 요인)</h4>
<ol>
  <li><strong>Threat of New Entrants (신규 진입자의 위협):</strong> Height of entry barriers (capital requirements, patents, switching costs).</li>
  <li><strong>Bargaining Power of Buyers (구매자의 교섭력):</strong> High when buyers purchase in large volumes or have low switching costs.</li>
  <li><strong>Bargaining Power of Suppliers (공급자의 교섭력):</strong> High when inputs are specialized and few suppliers exist.</li>
  <li><strong>Threat of Substitute Products (대체재의 위협):</strong> Readily available alternative products offering better price-performance.</li>
  <li><strong>Rivalry Among Existing Competitors (기존 경쟁자 간의 경쟁):</strong> Intensity of price competition, advertising wars, market growth rate.</li>
</ol>

<h4>C) BCG Growth-Share Matrix</h4>
<div class="card-grid">
  <div class="summary-card">
    <h4>Stars (별)</h4>
    <p>High Market Growth + High Relative Market Share. Fast growth, generates cash but requires heavy investment to defend leadership.</p>
  </div>
  <div class="summary-card">
    <h4>Cash Cows (현금 젖소)</h4>
    <p>Low Market Growth + High Relative Market Share. Generates massive, steady profits with minimal required reinvestment; funds other ventures.</p>
  </div>
  <div class="summary-card">
    <h4>Question Marks (물음표)</h4>
    <p>High Market Growth + Low Relative Market Share. High cash consumer with uncertain future; requires substantial investment to become a Star.</p>
  </div>
  <div class="summary-card">
    <h4>Dogs (개)</h4>
    <p>Low Market Growth + Low Relative Market Share. Weak competitive position in stagnant market; prime candidates for divestiture/liquidation.</p>
  </div>
</div>
"""
        },
        {
            "id": "biz-ea-isp",
            "title": "3. IT Governance, Enterprise Architecture & ISP",
            "badge": "Day 10 • Session 1",
            "summary": "COBIT governance framework, 4 EA architecture views, Zachman and TOGAF frameworks, and the 3 phases of Information Strategy Planning.",
            "content": """
<h3>1. IT Governance & COBIT</h3>
<p><strong>IT Governance</strong> is the responsibility of corporate executives and board of directors, consisting of leadership, organizational structures, and processes that ensure enterprise IT sustains and extends business strategies.</p>
<ul>
  <li><strong>COBIT (Control Objectives for Information and Related Technologies):</strong> Globally accepted IT governance framework by ISACA. Separates <em>Governance</em> (Evaluate, Direct, Monitor - EDM) from <em>Management</em> (Plan, Build, Run, Monitor - APO, BAI, DSS, MEA).</li>
</ul>

<h3>2. Enterprise Architecture (EA - 전사 아키텍처)</h3>
<p>EA is a comprehensive blueprint that aligns organizational strategy, business processes, and IT assets to guide enterprise evolution and eliminate the IT productivity paradox.</p>

<h4>The 4 Core Views of EA (B-A-D-T):</h4>
<table class="data-table">
  <thead>
    <tr><th>Architecture View</th><th>Acronym</th><th>Scope & Deliverables</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Business Architecture</strong></td><td><strong>BA</strong></td><td>Defines enterprise business strategies, organizational hierarchy, business processes, and functions.</td></tr>
    <tr><td><strong>Application Architecture</strong></td><td><strong>AA</strong></td><td>Defines application systems required to support business functions, component relationships, and interfaces.</td></tr>
    <tr><td><strong>Data Architecture</strong></td><td><strong>DA</strong></td><td>Defines enterprise logical data models, data governance, master data management, and standard domains.</td></tr>
    <tr><td><strong>Technical Architecture</strong></td><td><strong>TA</strong></td><td>Defines underlying hardware infrastructure, network topology, OS, middleware, and security solutions.</td></tr>
  </tbody>
</table>

<h4>Major EA Frameworks:</h4>
<ul>
  <li><strong>Zachman Framework:</strong> A two-dimensional 6&times;6 classification matrix mapping communication interrogatives (What, How, Where, Who, When, Why) against stakeholder perspectives (Planner, Owner, Designer, Builder, Subcontractor, Functioning System).</li>
  <li><strong>TOGAF (The Open Group Architecture Framework):</strong> Built around the <strong>ADM (Architecture Development Method)</strong> iterative cycle from Preliminary phase through Architecture Vision, Business/IS/Tech Architecture, Opportunities, Migration Planning, and Change Management.</li>
</ul>

<h3>3. Information Strategy Planning (ISP - 정보전략계획)</h3>
<p>A systematic top-down methodology for establishing a medium-to-long-term corporate information vision and actionable IT execution roadmap.</p>
<ol>
  <li><strong>Phase 1: Environment Analysis (As-Is):</strong> Business environment scan, corporate strategy review, current IT systems assessment, stakeholder interview, benchmarking.</li>
  <li><strong>Phase 2: Target Architecture Design (To-Be):</strong> Defining future business processes, future target EA architectures (BA, AA, DA, TA).</li>
  <li><strong>Phase 3: Implementation Strategy & Roadmap:</strong> Gap analysis (To-Be minus As-Is), project candidate derivation, prioritization (ROI, urgency, technical feasibility), cost estimation (TCO), and multi-year master rollout schedule.</li>
</ol>
"""
        },
        {
            "id": "biz-acquisition",
            "title": "4. S/W Acquisition, Outsourcing & Process Improvement",
            "badge": "Day 10 • Session 2",
            "summary": "ISO/IEC 12207 life cycle processes, procurement documents (RFI, RFP), BPR vs Process Innovation, Six Sigma DMAIC, and TRIZ.",
            "content": """
<h3>1. ISO/IEC 12207 Software Life Cycle Processes</h3>
<p>International standard defining the architecture for software life cycle processes:</p>
<ul>
  <li><strong>Primary Processes (기본 공정):</strong> Acquisition (획득), Supply (공급), Development (개발), Operation (운영), Maintenance (유지보수).</li>
  <li><strong>Supporting Processes (지원 공정):</strong> Documentation, Configuration Management, Quality Assurance (QA), Verification, Validation, Joint Review, Audit, Problem Resolution.</li>
  <li><strong>Organizational Processes (조직 공정):</strong> Management, Infrastructure, Improvement, Training.</li>
</ul>

<h3>2. Business Process Improvement Techniques</h3>
<table class="data-table">
  <thead>
    <tr><th>Methodology</th><th>Improvement Pace</th><th>Target & Philosophy</th><th>Key Metrics / Steps</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>BPR (Business Process Reengineering)</strong></td><td><strong>Radical / Breakthrough (혁신적)</strong></td><td>Fundamental rethinking and radical redesign of core business processes to achieve dramatic improvements in cost, quality, and speed (Hammer &amp; Champy).</td><td>Starting from a clean sheet; discarding legacy assumptions completely.</td></tr>
    <tr><td><strong>PI (Process Innovation)</strong></td><td>Continuous / Systematic</td><td>Incremental and ongoing process enhancements aligned with IT systems implementation.</td><td>Cross-functional team optimization.</td></tr>
    <tr><td><strong>Six Sigma (6&sigma;)</strong></td><td>Data-driven / Statistical</td><td>Defect reduction to near perfection: <strong>3.4 Defects Per Million Opportunities (DPMO)</strong>.</td><td><strong>DMAIC:</strong> Define &rarr; Measure &rarr; Analyze &rarr; Improve &rarr; Control.<br><em>DMADV:</em> For designing brand new defect-free processes.</td></tr>
    <tr><td><strong>TRIZ (트리즈)</strong></td><td>Algorithmic Inventive</td><td>Theory of Inventive Problem Solving (Genrich Altshuller). Analyzed patents to identify <strong>40 inventive principles</strong> for resolving engineering and business contradictions without compromise.</td><td>Contradiction Matrix, 40 Inventive Principles.</td></tr>
  </tbody>
</table>

<h3>3. Enterprise Software Systems</h3>
<ul>
  <li><strong>ERP (Enterprise Resource Planning):</strong> Enterprise-wide integrated suite sharing a <strong>single central database</strong> across Finance, HR, Logistics, Procurement, and Manufacturing to eliminate data silos.</li>
  <li><strong>SCM (Supply Chain Management):</strong> Optimizes end-to-end material, information, and financial flows from raw material suppliers to end consumers. Crucial for mitigating the <strong>Bullwhip Effect (채찍 효과)</strong> (where small swings in consumer demand trigger exponentially magnified demand distortions upstream).</li>
  <li><strong>CRM (Customer Relationship Management):</strong> Maximizes Customer Lifetime Value (CLV) via Operational, Analytical, and Collaborative customer touchpoints.</li>
</ul>
"""
        },
        {
            "id": "biz-solutions-ethics",
            "title": "5. ITSM, ITIL, Intellectual Property & Legal Ethics",
            "badge": "Day 10 • Session 3",
            "summary": "ITIL service lifecycle, SLA metrics, copyright vs patent distinctions, Personal Information Protection Act, and digital ethics.",
            "content": """
<h3>1. IT Service Management (ITSM) & ITIL</h3>
<p><strong>ITIL (Information Technology Infrastructure Library):</strong> Best practice framework for delivering high-quality IT services aligned with business needs.</p>

<table class="data-table">
  <thead>
    <tr><th>ITIL Process</th><th>Core Objective</th><th>Key Characteristic</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Incident Management (장애 관리)</strong></td><td>Restore normal service operation as quickly as possible with minimal business disruption.</td><td>Focuses on speed and workarounds (e.g., rebooting a frozen server).</td></tr>
    <tr><td><strong>Problem Management (문제 관리)</strong></td><td>Identify and eliminate the underlying <strong>root cause</strong> of recurring incidents to prevent future recurrence.</td><td>Root cause analysis (RCA), permanent fixes, Known Error Database (KEDB).</td></tr>
    <tr><td><strong>Change Management (변경 관리)</strong></td><td>Ensure standardized methods and procedures are used for efficient and prompt handling of all changes to minimize IT risk.</td><td>Change Advisory Board (CAB) reviews and approves RFCs.</td></tr>
  </tbody>
</table>

<h4>SLA (Service Level Agreement) & Key Metrics:</h4>
<ul>
  <li><strong>SLA:</strong> Formal negotiated agreement between service provider and customer detailing service scope, performance metrics, and penalties for underperformance.</li>
  <li><strong>MTBF (Mean Time Between Failures):</strong> Average operational time between service breakdowns (Measure of <em>Reliability</em>).</li>
  <li><strong>MTTR (Mean Time To Repair / Recover):</strong> Average time required to repair and restore failed service (Measure of <em>Maintainability</em>).</li>
  <li><strong>Availability Formula:</strong> <code>Availability (%) = MTBF / (MTBF + MTTR) &times; 100%</code>.</li>
</ul>

<h3>2. Intellectual Property Rights (IPR) & Software Law</h3>
<table class="data-table">
  <thead>
    <tr><th>IP Right</th><th>Target of Protection</th><th>Protection Requirement</th><th>Protection Term</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Copyright (저작권)</strong></td><td><strong>Expression (표현)</strong> of ideas (Source code, binary, user manual). Does NOT protect abstract algorithms, mathematical principles, or business concepts.</td><td>Arises <strong>automatically upon creation</strong> (no registration mandatory).</td><td>Author's lifetime + <strong>70 years</strong> post-mortem.</td></tr>
    <tr><td><strong>Patent (특허권)</strong></td><td><strong>Invention / Technology (기술적 사상)</strong> (Novel technical methods, algorithms with industrial applicability).</td><td>Requires formal government examination (Novelty, Inventiveness, Industrial Applicability).</td><td><strong>20 years</strong> from patent filing date.</td></tr>
    <tr><td><strong>Trade Secret (영업비밀)</strong></td><td>Non-public proprietary commercial formulas, customer lists, internal algorithms.</td><td>Must maintain active secrecy efforts and independent economic value.</td><td>Perpetual as long as secrecy is preserved.</td></tr>
  </tbody>
</table>

<h3>3. Personal Information Protection Principles</h3>
<ul>
  <li><strong>Minimal Collection:</strong> Only collect the minimum personal data strictly necessary for the stated purpose.</li>
  <li><strong>Purpose Limitation:</strong> Personal data cannot be used or disclosed for purposes beyond the original informed consent.</li>
  <li><strong>Informed Consent:</strong> Clear, explicit user consent required prior to collection (separate opt-in for sensitive and marketing data).</li>
  <li><strong>Destruction of Expired Data:</strong> Data must be permanently destroyed immediately once the retention period ends or collection purpose is achieved.</li>
  <li><strong>Mandatory Breach Notification:</strong> Report security breach to authorities and notify affected data subjects within designated statutory timeframes (e.g., 72 hours under GDPR / Korean law).</li>
</ul>
"""
        }
    ]
}
