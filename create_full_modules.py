import json, sys

modules = {}

# DOMAIN 1: Software Development
modules["domain1"] = {
    "id": "domain1",
    "title": "Domain 1: Software Development",
    "icon": "💻",
    "description": "Software Engineering principles, SDLC models, Agile/Scrum, Data Structures, Algorithms, Software Architecture, GoF Design Patterns, UI/UX, Testing, Refactoring, SCM, and Open Source Software Licenses.",
    "sections": [
        {
            "id": "sw-sdlc",
            "title": "1. Software Engineering Overview & SDLC Lifecycle Models",
            "badge": "Day 1 • Session 1",
            "summary": "Core definitions of software engineering, causes of software crisis, 4 key elements, and deep comparison of traditional SDLC models.",
            "content": """
<h3>1. Background and Purpose of Software Engineering</h3>
<p><strong>Software Engineering (SE)</strong> is the systematic, disciplined, and quantifiable approach to the development, operation, and maintenance of software. It emerged in the late 1960s to address the <em>Software Crisis</em>.</p>

<div class="note-box alert-warning">
  <strong>The Software Crisis:</strong> Characterized by projects exceeding budget, missing deadlines, failing customer requirements, poor software quality, and exponentially increasing maintenance costs. As hardware costs plummeted and software complexity exploded, systematic engineering methodologies became mandatory.
</div>

<h4>Four Key Elements of Software Engineering</h4>
<table class="data-table">
  <thead>
    <tr><th>Element</th><th>Description</th><th>Examples</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Methods (방법)</strong></td><td>Provide the 'how-to' technical questions for building software. Includes requirements analysis, design modeling, program construction, testing, and maintenance.</td><td>Object-oriented analysis, Structured design, Agile practices</td></tr>
    <tr><td><strong>Tools (도구)</strong></td><td>Automated or semi-automated support for methods. When tools are integrated so that information created by one tool can be used by another, a system called CASE is established.</td><td>IDE, Git, Jira, SonarQube, CASE tools</td></tr>
    <tr><td><strong>Procedures (절차)</strong></td><td>The glue that holds the methods and tools together. Defines the sequence in which methods are applied, deliverables required, controls, and milestones.</td><td>SDLC process, QA audit checklists, release approvals</td></tr>
    <tr><td><strong>People (인력)</strong></td><td>The most critical element. Software is an intellectual product developed by humans. Team organization, communication, and competence dictate success.</td><td>Product Owner, Architects, Developers, Testers</td></tr>
  </tbody>
</table>

<h3>2. Software Development Lifecycle (SDLC) Models</h3>
<p>An SDLC model defines the phases and sequence through which software progresses from inception to retirement.</p>

<h4>A) Waterfall Model (폭포수 모델)</h4>
<ul>
  <li><strong>Concept:</strong> Classic sequential model where each phase must be fully completed and approved (with signed-off documentation) before the next phase begins. No overlapping phases.</li>
  <li><strong>Phases:</strong> Feasibility Study &rarr; Requirements Analysis &rarr; System & S/W Design &rarr; Implementation (Coding) &rarr; Testing &rarr; Deployment & Maintenance.</li>
  <li><strong>Strengths:</strong> Highly structured, easy to manage, clear milestones and documentation at every stage.</li>
  <li><strong>Weaknesses:</strong> Inflexible to requirement changes, working software only appears late in the lifecycle, high risk if requirements were misunderstood early on.</li>
  <li><strong>Best Applied To:</strong> Projects with clear, stable, well-understood requirements and mature technology.</li>
</ul>

<h4>B) Prototyping Model (프로토타이핑 모델)</h4>
<ul>
  <li><strong>Concept:</strong> Quickly builds an operational mock-up or prototype to clarify ambiguous requirements with the client, iterate based on user feedback, and then construct the real system.</li>
  <li><strong>Types:</strong>
    <ul>
      <li><em>Throwaway Prototyping:</em> Prototype is used only to understand requirements and then discarded; production system is built cleanly from scratch.</li>
      <li><em>Evolutionary Prototyping:</em> The prototype is iteratively refined and scaled until it becomes the final production system.</li>
    </ul>
  </li>
  <li><strong>Strengths:</strong> Minimizes requirement misunderstanding, enhances client satisfaction, early user feedback.</li>
  <li><strong>Weaknesses:</strong> Tendency for clients to confuse a prototype with a finished system, risk of poor architectural foundation if evolutionary prototyping is poorly controlled.</li>
</ul>

<h4>C) Spiral Model (나선형 모델 - Boehm)</h4>
<ul>
  <li><strong>Concept:</strong> Combines the iterative nature of prototyping with the controlled, systematic aspects of the Waterfall model, with a core emphasis on <strong>Risk Analysis</strong> at every cycle.</li>
  <li><strong>Four Repeating Quadrants:</strong>
    <ol>
      <li><strong>Objective Setting & Planning:</strong> Determine goals, alternatives, constraints.</li>
      <li><strong>Risk Analysis & Resolution:</strong> Identify risks, evaluate alternatives, resolve risks (often using prototypes or simulations).</li>
      <li><strong>Development & Validation:</strong> Develop the next-level product and verify.</li>
      <li><strong>Review & Next Phase Planning:</strong> Client evaluates results and plans the next cycle.</li>
    </ol>
  </li>
  <li><strong>Best Applied To:</strong> Large-scale, mission-critical, high-cost, high-risk systems.</li>
</ul>

<h4>D) V-Model (V-모델)</h4>
<p>An extension of the Waterfall model that explicitly couples each development phase on the left descending arm with its corresponding testing/verification phase on the right ascending arm.</p>

<pre class="code-block">
   Requirements Analysis ------------------------> Acceptance Testing
          \                                              /
       System Design -----------------------------> System Testing
             \                                          /
         Architecture Design -----------------> Integration Testing
                \                                    /
             Detailed Design -------------> Unit Testing
                    \                             /
                     \-----> Coding / Implementation
</pre>

<div class="note-box alert-info">
  <strong>TOPCIT Exam Tip:</strong> Memorize the V-Model test mapping pairs:
  <ul>
    <li><strong>Unit Testing (단위 테스트):</strong> Verifies Detailed Design (Module/Class logic).</li>
    <li><strong>Integration Testing (통합 테스트):</strong> Verifies Architecture Design & Interfaces between modules.</li>
    <li><strong>System Testing (시스템 테스트):</strong> Verifies System Design & Non-functional requirements (Performance, Security, Load).</li>
    <li><strong>Acceptance Testing (인수 테스트):</strong> Verifies User Requirements Analysis from the client's perspective (Alpha & Beta testing).</li>
  </ul>
</div>

<h4>E) Incremental vs Evolutionary Models</h4>
<table class="data-table">
  <thead>
    <tr><th>Feature</th><th>Incremental Model (증분 모델)</th><th>Evolutionary Model (진화 모델)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Development Strategy</strong></td><td>Breaks system into functional chunks; builds core features first, then adds new distinct modules sequentially.</td><td>Builds a complete skeleton system covering all functions at basic fidelity, then iteratively refines and deepens all functions.</td></tr>
    <tr><td><strong>Release Nature</strong></td><td>Each release adds new features.</td><td>Each release improves and refines existing features based on user usage.</td></tr>
    <tr><td><strong>Requirement Certainty</strong></td><td>Overall requirements known upfront, delivery staged.</td><td>Requirements evolve and clarify over time.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sw-agile",
            "title": "2. Agile Methodologies & Scrum Framework",
            "badge": "Day 1 • Session 2",
            "summary": "Agile Manifesto values and principles, detailed breakdown of Scrum roles, artifacts, and ceremonies, XP practices, and Kanban.",
            "content": """
<h3>1. The Agile Philosophy</h3>
<p>Agile was created as a reaction against heavy, document-driven, rigid waterfall processes. It values adaptive planning, evolutionary development, early delivery, and continual improvement.</p>

<div class="card-grid">
  <div class="summary-card">
    <h4>Agile Manifesto: 4 Core Values</h4>
    <ol>
      <li><strong>Individuals and interactions</strong> over processes and tools</li>
      <li><strong>Working software</strong> over comprehensive documentation</li>
      <li><strong>Customer collaboration</strong> over contract negotiation</li>
      <li><strong>Responding to change</strong> over following a plan</li>
    </ol>
  </div>
</div>

<h3>2. The Scrum Framework</h3>
<p>Scrum is an iterative and incremental framework for managing complex work. It organizes work into fixed-length iterations called <strong>Sprints</strong> (typically 1 to 4 weeks).</p>

<h4>A) Three Scrum Roles</h4>
<ul>
  <li><strong>Product Owner (PO):</strong> Owns the product vision. Responsible for maximizing product value. Exclusively manages and prioritizes the <em>Product Backlog</em>. Serves as the primary bridge to stakeholders and customers.</li>
  <li><strong>Scrum Master (SM):</strong> Servant-leader and agile coach. Ensures Scrum rules and values are adhered to. Removes impediments (roadblocks) for the development team. Does <em>not</em> manage or assign tasks to developers.</li>
  <li><strong>Development Team:</strong> Self-organizing, cross-functional group of professionals (typically 3 to 9 members) who execute the work and deliver a potentially releasable Increment of software at the end of each Sprint.</li>
</ul>

<h4>B) Three Scrum Artifacts</h4>
<ul>
  <li><strong>Product Backlog:</strong> An ordered, dynamic list of everything that might be needed in the product (user stories, feature requests, bug fixes, technical requirements). Prioritized by business value.</li>
  <li><strong>Sprint Backlog:</strong> The set of Product Backlog items selected for the current Sprint, plus the tactical plan and task breakdown for delivering the Sprint Goal. Owned entirely by the Development Team.</li>
  <li><strong>Increment & Definition of Done (DoD):</strong> The inspectable, usable sum of all Product Backlog items completed during a Sprint, meeting the agreed quality checklist ("Definition of Done").</li>
  <li><strong>Burndown Chart:</strong> A graphical representation of work left to do versus time.
    <ul>
      <li>X-axis = Sprint days / time</li>
      <li>Y-axis = Remaining story points or estimated hours</li>
      <li>A line trending above the ideal diagonal indicates the team is behind schedule; below means ahead of schedule.</li>
    </ul>
  </li>
</ul>

<h4>C) Five Scrum Ceremonies (Events)</h4>
<table class="data-table">
  <thead>
    <tr><th>Ceremony</th><th>Timing & Timebox</th><th>Purpose & Output</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Sprint Planning</strong></td><td>Start of Sprint (max 8h for 1-month sprint)</td><td>PO presents prioritized backlog; Team determines Sprint Goal and creates Sprint Backlog.</td></tr>
    <tr><td><strong>Daily Scrum (Stand-up)</strong></td><td>Daily, same time/place (strict 15 minutes)</td><td>Team inspects progress toward Sprint Goal. Each member answers: What did I do yesterday? What will I do today? What blockers do I face?</td></tr>
    <tr><td><strong>Sprint Review</strong></td><td>End of Sprint (max 4h)</td><td>Team demonstrates completed working Increment to stakeholders and collects feedback. Product Backlog is adapted.</td></tr>
    <tr><td><strong>Sprint Retrospective</strong></td><td>After Review, before next Planning (max 3h)</td><td>Internal team reflection on people, relationships, process, and tools. Identifies actionable process improvements for next Sprint.</td></tr>
    <tr><td><strong>Backlog Refinement (Grooming)</strong></td><td>Ongoing throughout Sprint (~10% capacity)</td><td>Adding detail, estimates, and order to items in the Product Backlog.</td></tr>
  </tbody>
</table>

<h3>3. Extreme Programming (XP)</h3>
<p>XP is an agile methodology that focuses heavily on engineering excellence and developer practices.</p>
<ul>
  <li><strong>5 Core Values:</strong> Communication, Simplicity, Feedback, Courage, Respect.</li>
  <li><strong>Core Practices:</strong>
    <ul>
      <li><strong>Pair Programming:</strong> Two programmers work together at one workstation (Driver writes code; Navigator reviews, thinks strategically). Increases code quality and knowledge sharing.</li>
      <li><strong>Test-Driven Development (TDD):</strong> Write automated tests before writing functional code (Red &rarr; Green &rarr; Refactor).</li>
      <li><strong>Continuous Integration (CI):</strong> Integrate and verify code into a shared repository multiple times daily via automated builds and tests.</li>
      <li><strong>Small Releases:</strong> Frequent deployment of small, fully tested increments.</li>
      <li><strong>Refactoring:</strong> Continually restructuring code to improve internal design without changing external behavior.</li>
      <li><strong>Collective Code Ownership:</strong> Anyone on the team can change any piece of code at any time.</li>
      <li><strong>Metaphor:</strong> A shared story or naming system explaining how the system works.</li>
    </ul>
  </li>
</ul>
"""
        },
        {
            "id": "sw-reuse",
            "title": "3. Software Reuse & Reverse Engineering",
            "badge": "Day 1 • Session 3",
            "summary": "Mechanisms and targets of software reuse, obstacles, reverse engineering, restructuring, and reengineering.",
            "content": """
<h3>1. Software Reuse (소프트웨어 재사용)</h3>
<p>Software reuse is the process of creating new software systems from existing software assets rather than building them from scratch.</p>

<h4>A) Targets of Software Reuse</h4>
<ul>
  <li><strong>Source Code / Components:</strong> Modules, functions, libraries, packages (e.g., UI libraries, cryptographic packages).</li>
  <li><strong>Design / Architecture:</strong> Design patterns (GoF), reference architectures, domain models.</li>
  <li><strong>Requirements & Specifications:</strong> Use cases, functional specs for standard domain workflows (e.g., standard e-commerce checkout).</li>
  <li><strong>Test Assets:</strong> Test suites, test cases, automated test scripts, mock datasets.</li>
  <li><strong>Documentation:</strong> User manuals, API documentation, operational runbooks.</li>
</ul>

<h4>B) White-Box vs Black-Box Reuse</h4>
<table class="data-table">
  <thead>
    <tr><th>Category</th><th>Mechanism</th><th>Pros & Cons</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>White-Box Reuse</strong></td><td>The internal source code is visible and can be modified/customized to fit new requirements.</td><td>Highly flexible; however, requires deep understanding of source code and increases maintenance complexity if modified divergent branches exist.</td></tr>
    <tr><td><strong>Black-Box Reuse</strong></td><td>The component is reused strictly through its well-defined external interface (API) without modifying internal code.</td><td>Predictable, easier to maintain and upgrade; however, inflexible if the component doesn't exactly match requirements.</td></tr>
  </tbody>
</table>

<h3>2. Reverse Engineering vs Reengineering</h3>
<p>Software evolves over time and legacy code must frequently be modernized.</p>

<div class="card-grid">
  <div class="summary-card">
    <h4>Reverse Engineering (역공학)</h4>
    <p>Analyzing an existing operational system (often only compiled binary or legacy code without documentation) to identify its components, interrelationships, and recover high-level abstractions and design representations.</p>
    <ul>
      <li><em>Code &rarr; Design Specification &rarr; Conceptual Requirements</em></li>
      <li>Goal: Understanding, documentation recovery, legacy migration assessment. Does <strong>not</strong> change the system functionality.</li>
    </ul>
  </div>
  <div class="summary-card">
    <h4>Reengineering (재공학)</h4>
    <p>Examining, restructuring, and altering an existing software system to reconstitute it in a new form, improving quality, maintainability, or performance.</p>
    <ul>
      <li>Process: <em>Reverse Engineering &rarr; Restructuring / Refactoring &rarr; Forward Engineering</em></li>
      <li>Preserves business logic while modernizing architecture (e.g., converting legacy COBOL mainframe to cloud-native microservices).</li>
    </ul>
  </div>
</div>
"""
        },
        {
            "id": "sw-ds-algo",
            "title": "4. Data Structures, Algorithms & Design Principles",
            "badge": "Day 2 • Session 1",
            "summary": "Core linear and non-linear data structures, Big-O analysis, sorting/searching algorithms, and foundational design principles.",
            "content": """
<h3>1. Data Structures Classification</h3>
<div class="table-responsive">
  <table class="data-table">
    <thead>
      <tr><th>Category</th><th>Structure</th><th>Key Characteristics & Access Pattern</th><th>Use Cases</th></tr>
    </thead>
    <tbody>
      <tr><td rowspan="4"><strong>Linear (선형)</strong></td><td><strong>Array</strong></td><td>Contiguous memory allocation; O(1) random access by index; O(n) insertion/deletion.</td><td>Lookup tables, fixed-size buffers</td></tr>
      <tr><td><strong>Linked List</strong></td><td>Nodes connected by pointers; O(n) traversal; O(1) insertion/deletion once pointer is located.</td><td>Dynamic collections, memory allocation pools</td></tr>
      <tr><td><strong>Stack</strong></td><td><strong>LIFO (Last In, First Out)</strong>. Push and Pop operations at the top only. O(1) operations.</td><td>Function call stack, recursion, undo operations, parenthesis matching, syntax parsing</td></tr>
      <tr><td><strong>Queue</strong></td><td><strong>FIFO (First In, First Out)</strong>. Enqueue at rear, Dequeue at front. O(1) operations.</td><td>CPU scheduling, print spooling, asynchronous message queues, BFS traversal</td></tr>
      <tr><td rowspan="4"><strong>Non-Linear (비선형)</strong></td><td><strong>Binary Tree</strong></td><td>Hierarchical structure where each node has at most 2 children (Left, Right).</td><td>Expression trees, decision trees</td></tr>
      <tr><td><strong>Binary Search Tree (BST)</strong></td><td>Left subtree values &lt; Node value &lt; Right subtree values. Average search O(log n); Worst case O(n) if unbalanced (skewed).</td><td>Dynamic sorted search</td></tr>
      <tr><td><strong>Heap</strong></td><td>Complete binary tree. Max-Heap (parent &ge; children) or Min-Heap (parent &le; children). Root is always max or min. Insert/Delete O(log n).</td><td>Priority queues, Heap Sort, Dijkstra algorithm</td></tr>
      <tr><td><strong>Graph</strong></td><td>Vertices (Nodes) and Edges (Directed/Undirected, Weighted). Represented via Adjacency Matrix (dense) or Adjacency List (sparse).</td><td>Networks, routing, social graphs, dependency resolution</td></tr>
    </tbody>
  </table>
</div>

<h3>2. Algorithm Complexity & Big-O Notation</h3>
<p>Big-O notation describes the upper bound (worst-case) asymptotic complexity as input size <em>n</em> grows.</p>
<pre class="code-block">
O(1) &lt; O(log n) &lt; O(n) &lt; O(n log n) &lt; O(n²) &lt; O(2ⁿ) &lt; O(n!)
[Fastest / Most Efficient] ----------------------> [Slowest / Intractable]
</pre>

<h4>Sorting Algorithms Comparison</h4>
<table class="data-table">
  <thead>
    <tr><th>Algorithm</th><th>Best Time</th><th>Average Time</th><th>Worst Time</th><th>Space</th><th>Stability</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Bubble Sort</strong></td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Stable</td></tr>
    <tr><td><strong>Selection Sort</strong></td><td>O(n²)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Unstable</td></tr>
    <tr><td><strong>Insertion Sort</strong></td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>Stable</td></tr>
    <tr><td><strong>Quick Sort</strong></td><td>O(n log n)</td><td>O(n log n)</td><td>O(n²) (bad pivot)</td><td>O(log n)</td><td>Unstable</td></tr>
    <tr><td><strong>Merge Sort</strong></td><td>O(n log n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n)</td><td>Stable</td></tr>
    <tr><td><strong>Heap Sort</strong></td><td>O(n log n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(1)</td><td>Unstable</td></tr>
  </tbody>
</table>

<h3>3. Graph Search & Minimum Spanning Tree (MST)</h3>
<ul>
  <li><strong>DFS (Depth-First Search):</strong> Explores as deep as possible along each branch before backtracking. Implemented via <em>Recursion or Stack</em>. O(V + E).</li>
  <li><strong>BFS (Breadth-First Search):</strong> Explores all neighbor nodes at current depth before moving to next level. Implemented via <em>Queue</em>. Finds shortest unweighted path. O(V + E).</li>
  <li><strong>Kruskal's Algorithm (MST):</strong> Greedy algorithm. Sorts all edges by weight, adds the lowest weight edge that does not form a cycle (using Union-Find / Disjoint Set). O(E log E).</li>
  <li><strong>Prim's Algorithm (MST):</strong> Greedy algorithm. Starts from a root node and continuously adds the minimum weight edge connecting the growing tree to a new vertex. O(E + V log V) with Fibonacci heap.</li>
  <li><strong>Dijkstra's Algorithm:</strong> Computes single-source shortest paths in a weighted graph with <em>non-negative edge weights</em>. Uses Min-Priority Queue.</li>
</ul>

<h3>4. Principles of Software Design: Cohesion & Coupling</h3>
<p>The gold standard of software design is: <strong>High Cohesion (높은 응집도) and Low Coupling (낮은 결합도)</strong>.</p>

<h4>A) Cohesion Levels (from Strongest/Best to Weakest/Worst)</h4>
<ol>
  <li><strong>Functional Cohesion (기능적):</strong> [BEST] All elements of the module contribute to a single, well-defined task (e.g., <code>calculateSquareRoot()</code>).</li>
  <li><strong>Sequential Cohesion (순차적):</strong> Output from one activity is the direct input to the next activity within the module.</li>
  <li><strong>Communicational Cohesion (교환적):</strong> All elements operate on the same input data or produce the same output dataset.</li>
  <li><strong>Procedural Cohesion (절차적):</strong> Activities are executed in a specified sequence, but operate on different data.</li>
  <li><strong>Temporal Cohesion (시간적):</strong> Elements are bundled together because they must execute at the same time (e.g., <code>systemStartupInit()</code>).</li>
  <li><strong>Logical Cohesion (논리적):</strong> Elements perform logically similar tasks, but the specific operation is selected by a control flag (e.g., a function that prints reports A, B, or C based on a mode integer).</li>
  <li><strong>Coincidental Cohesion (우연적):</strong> [WORST] Elements have no meaningful relationship; grouped purely by accident or arbitrary placement.</li>
</ol>

<h4>B) Coupling Levels (from Loosest/Best to Tightest/Worst)</h4>
<ol>
  <li><strong>Data Coupling (자료 결합도):</strong> [BEST] Modules communicate entirely by passing simple primitive data arguments (e.g., integers, strings).</li>
  <li><strong>Stamp Coupling (스탬프 결합도):</strong> Modules share a composite data structure (e.g., passing an entire Employee record when only Employee.id is needed).</li>
  <li><strong>Control Coupling (제어 결합도):</strong> One module passes control flags or switches that dictate the internal logic flow of another module.</li>
  <li><strong>External Coupling (외부 결합도):</strong> Modules share an externally imposed data format, communication protocol, or device interface.</li>
  <li><strong>Common Coupling (공통 결합도):</strong> Multiple modules read and write to global variables or a shared memory region.</li>
  <li><strong>Content Coupling (내용 결합도):</strong> [WORST] One module directly accesses, modifies, or branches into the internal code or private data of another module.</li>
</ol>
"""
        },
        {
            "id": "sw-patterns",
            "title": "5. Object-Oriented Design & GoF Design Patterns",
            "badge": "Day 2 • Session 2",
            "summary": "SOLID principles, UML diagrams, and the 23 Gang of Four (GoF) design patterns categorized by Creational, Structural, and Behavioral.",
            "content": """
<h3>1. SOLID Object-Oriented Principles</h3>
<table class="data-table">
  <thead>
    <tr><th>Principle</th><th>Full Name</th><th>Core Meaning & Implementation</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>S</strong></td><td><strong>Single Responsibility Principle (단일 책임 원칙)</strong></td><td>A class should have one, and only one, reason to change. Each class should encapsulate a single responsibility.</td></tr>
    <tr><td><strong>O</strong></td><td><strong>Open/Closed Principle (개방 폐쇄 원칙)</strong></td><td>Software entities should be <strong>open for extension</strong>, but <strong>closed for modification</strong>. Achieved through interfaces and abstraction.</td></tr>
    <tr><td><strong>L</strong></td><td><strong>Liskov Substitution Principle (리스코프 치환 원칙)</strong></td><td>Subtypes must be substitutable for their base types without altering program correctness (child classes must fulfill parent contracts).</td></tr>
    <tr><td><strong>I</strong></td><td><strong>Interface Segregation Principle (인터페이스 분리 원칙)</strong></td><td>Clients should not be forced to depend on methods they do not use. Prefer many small, specific interfaces over one bloated interface.</td></tr>
    <tr><td><strong>D</strong></td><td><strong>Dependency Inversion Principle (의존 역전 원칙)</strong></td><td>High-level modules should not depend on low-level modules; both should depend on abstractions (interfaces). Abstractions should not depend on details.</td></tr>
  </tbody>
</table>

<h3>2. GoF (Gang of Four) 23 Design Patterns</h3>

<h4>A) Creational Patterns (생성 패턴 - 5 Patterns)</h4>
<p>Deal with object creation mechanisms, creating objects in a manner suitable to the situation.</p>
<ul>
  <li><strong>Singleton:</strong> Ensures a class has only one instance and provides a global point of access to it.</li>
  <li><strong>Factory Method:</strong> Defines an interface for creating an object, but lets subclasses decide which class to instantiate.</li>
  <li><strong>Abstract Factory:</strong> Provides an interface for creating families of related or dependent objects without specifying their concrete classes.</li>
  <li><strong>Builder:</strong> Separates the construction of a complex object from its representation so that the same construction process can create different representations.</li>
  <li><strong>Prototype:</strong> Creates new objects by cloning an existing instance (prototype).</li>
</ul>

<h4>B) Structural Patterns (구조 패턴 - 7 Patterns)</h4>
<p>Deal with object composition and class structure, easing design by identifying simple ways to realize relationships.</p>
<ul>
  <li><strong>Adapter:</strong> Converts the interface of a class into another interface clients expect. Lets incompatible interfaces work together.</li>
  <li><strong>Bridge:</strong> Decouples an abstraction from its implementation so that the two can vary independently.</li>
  <li><strong>Composite:</strong> Composes objects into tree structures to represent part-whole hierarchies. Clients treat individual objects and compositions uniformly.</li>
  <li><strong>Decorator:</strong> Attaches additional responsibilities to an object dynamically (alternative to subclassing for extending functionality).</li>
  <li><strong>Facade:</strong> Provides a unified, simplified high-level interface to a complex subsystem.</li>
  <li><strong>Flyweight:</strong> Shares fine-grained objects efficiently to support large numbers of small objects without high memory consumption.</li>
  <li><strong>Proxy:</strong> Provides a surrogate or placeholder for another object to control access to it (Virtual Proxy, Protection Proxy, Remote Proxy).</li>
</ul>

<h4>C) Behavioral Patterns (행위 패턴 - 11 Patterns)</h4>
<p>Deal with communication, responsibility assignment, and algorithms between objects.</p>
<ul>
  <li><strong>Observer:</strong> Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically (Publish-Subscribe).</li>
  <li><strong>Strategy:</strong> Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.</li>
  <li><strong>Template Method:</strong> Defines the skeleton of an algorithm in a base class, deferring some steps to subclasses without changing the algorithm's structure.</li>
  <li><strong>Command:</strong> Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.</li>
  <li><strong>Iterator:</strong> Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.</li>
  <li><strong>State:</strong> Allows an object to alter its behavior when its internal state changes (object appears to change its class).</li>
  <li><strong>Mediator:</strong> Defines an object that encapsulates how a set of objects interact, preventing loose objects from referring to each other explicitly.</li>
  <li><strong>Memento:</strong> Captures and externalizes an object's internal state without violating encapsulation, allowing the object to be restored later.</li>
  <li><strong>Visitor:</strong> Represents an operation to be performed on elements of an object structure. Lets you define a new operation without changing the classes of the elements on which it operates.</li>
  <li><strong>Chain of Responsibility:</strong> Passes a request along a chain of handlers until one handles it.</li>
  <li><strong>Interpreter:</strong> Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences.</li>
</ul>
"""
        },
        {
            "id": "sw-testing",
            "title": "6. Software Testing, Refactoring & Open Source Licenses",
            "badge": "Day 2 • Session 3",
            "summary": "White-box vs Black-box test design techniques, testing levels, refactoring code smells, and legal obligations of open-source licenses.",
            "content": """
<h3>1. Software Testing Methodologies</h3>

<h4>A) White-Box Testing (구조적 / 백박스 테스트)</h4>
<p>Tests internal logic, code paths, and data flow of the software. Requires source code access.</p>
<ul>
  <li><strong>Statement Coverage (문장 커버리지):</strong> Every executable statement is executed at least once.</li>
  <li><strong>Branch / Decision Coverage (분기 커버리지):</strong> Every decision outcome (True and False) is exercised at least once.</li>
  <li><strong>Condition Coverage (조건 커버리지):</strong> Every individual Boolean condition in a decision is evaluated as both True and False at least once.</li>
  <li><strong>Condition/Decision Coverage:</strong> Both decision outcomes and individual condition outcomes are tested.</li>
  <li><strong>Multiple Condition Coverage (다중 조건 커버리지):</strong> Tests all possible combinations of condition outcomes within each decision (most rigorous).</li>
  <li><strong>Basis Path Testing (기본 경로 테스트):</strong> Uses Cyclomatic Complexity <code>V(G) = E - N + 2</code> (where E = edges, N = nodes) to determine the number of linearly independent paths.</li>
</ul>

<h4>B) Black-Box Testing (기능적 / 블랙박스 테스트)</h4>
<p>Tests system functionality without knowledge of internal code or implementation details.</p>
<ul>
  <li><strong>Equivalence Partitioning (동등 분할):</strong> Divides input data into valid and invalid partitions; tests one representative value from each partition.</li>
  <li><strong>Boundary Value Analysis (경계값 분석):</strong> Errors frequently occur at boundaries. Tests values directly on, just below, and just above partition boundaries (e.g., for range 1..100, test 0, 1, 2, 99, 100, 101).</li>
  <li><strong>Cause-Effect Graphing:</strong> Systematically maps logical combinations of inputs (causes) to outputs (effects) using Boolean logic graphs, which are then converted to Decision Tables.</li>
  <li><strong>Decision Table Testing:</strong> Tabular representation of complex business rules with condition combinations and resulting actions.</li>
  <li><strong>State Transition Testing:</strong> Tests state changes and event triggers in systems behaving as finite-state machines.</li>
  <li><strong>Error Guessing:</strong> Experience-based testing targeting known human error patterns and edge cases.</li>
</ul>

<h3>2. Testing Levels</h3>
<ol>
  <li><strong>Unit Testing:</strong> Verifies individual functions/classes (stubs and mock objects).</li>
  <li><strong>Integration Testing:</strong> Verifies interfaces between components.
    <ul>
      <li><em>Top-Down:</em> Begins at main module; sub-modules replaced by <strong>Stubs</strong> (dummy called modules).</li>
      <li><em>Bottom-Up:</em> Begins at terminal leaf modules; higher-level modules replaced by <strong>Drivers</strong> (dummy caller programs).</li>
      <li><em>Sandwich (Hybrid):</em> Combines top-down for top layers and bottom-up for bottom layers.</li>
    </ul>
  </li>
  <li><strong>System Testing:</strong> Verifies entire integrated system against system specifications (Performance, Stress, Security, Recovery, Volume).</li>
  <li><strong>Acceptance Testing:</strong> Validates system against customer business requirements.
    <ul>
      <li><em>Alpha Testing:</em> Controlled testing by real users at the developer's site.</li>
      <li><em>Beta Testing:</em> Live operational testing by end users in their own real-world environment.</li>
    </ul>
  </li>
</ol>

<h3>3. Open Source Software (OSS) Licenses</h3>
<table class="data-table">
  <thead>
    <tr><th>License</th><th>Type</th><th>Source Code Disclosure</th><th>Patent Protection</th><th>Examples</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>GPL (v2/v3)</strong></td><td>Strong Copyleft</td><td><strong>Mandatory:</strong> Any derivative work or linked application MUST be open-sourced under GPL.</td><td>v3 includes explicit patent grant.</td><td>Linux Kernel, Git</td></tr>
    <tr><td><strong>LGPL</strong></td><td>Weak Copyleft</td><td>Dynamic linking does NOT require open-sourcing the parent program. Only modifications to the library itself must be disclosed.</td><td>Moderate</td><td>FFmpeg, standard libraries</td></tr>
    <tr><td><strong>MPL (Mozilla)</strong></td><td>File-based Copyleft</td><td>Only modified MPL-licensed files must be disclosed; other files in project can remain proprietary.</td><td>Yes</td><td>Firefox components</td></tr>
    <tr><td><strong>Apache 2.0</strong></td><td>Permissive</td><td>No disclosure required for derivative work. Must retain notices. <strong>Includes explicit grant of patent rights</strong> from contributors.</td><td>Explicit patent grant & retaliation clause</td><td>Android, Spark, Hadoop</td></tr>
    <tr><td><strong>BSD / MIT</strong></td><td>Permissive</td><td>No disclosure required. Can be used in closed commercial software with minimal copyright notice attribution.</td><td>No explicit patent terms</td><td>React, Node.js, Python</td></tr>
  </tbody>
</table>
"""
        }
    ]
}

print("Domain 1 built successfully.")
