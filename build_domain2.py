# Domain 2 data: Understanding and Using Data
d2 = {
    "id": "domain2",
    "title": "Domain 2: Understanding and Using Data",
    "icon": "🗄️",
    "description": "Data architecture, ANSI-SPARC 3-Schema, Relational Model, Keys, Integrity Constraints, ERD modeling, Normalization (1NF-BCNF), SQL mastery, ACID transactions, Concurrency Control, Recovery, Indexing, and Big Data/NoSQL.",
    "sections": [
        {
            "id": "db-arch",
            "title": "1. Data Concepts, File Systems vs DBMS & ANSI-SPARC Architecture",
            "badge": "Day 3 • Session 1",
            "summary": "DIKW hierarchy, limitations of file systems, ANSI-SPARC 3-level database architecture, logical/physical data independence, and DBA vs DA roles.",
            "content": """
<h3>1. Data, Information, Knowledge, and Wisdom (DIKW Hierarchy)</h3>
<div class="card-grid">
  <div class="summary-card">
    <h4>Data (데이터)</h4>
    <p>Raw, unorganized facts, signals, or symbols without context (e.g., "38.5").</p>
  </div>
  <div class="summary-card">
    <h4>Information (정보)</h4>
    <p>Data processed, structured, and contextualized to become meaningful (e.g., "Patient temperature is 38.5&deg;C - High fever").</p>
  </div>
  <div class="summary-card">
    <h4>Knowledge (지식)</h4>
    <p>Information integrated with human experience, rules, and context to enable actionable decision-making (e.g., "Administer antipyretic medication if temperature exceeds 38.0&deg;C").</p>
  </div>
  <div class="summary-card">
    <h4>Wisdom (지혜)</h4>
    <p>Evaluated understanding and ethical insight into why decisions work (e.g., "Understanding patient history to diagnose underlying recurrent viral infection").</p>
  </div>
</div>

<h3>2. File Processing System vs DBMS</h3>
<table class="data-table">
  <thead>
    <tr><th>Issue</th><th>File Processing System (파일 시스템)</th><th>DBMS (데이터베이스 관리 시스템)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Data Redundancy</strong></td><td>High. The same data is stored repeatedly across different application files.</td><td>Controlled / Minimized. Centralized storage with unified schema.</td></tr>
    <tr><td><strong>Data Inconsistency</strong></td><td>High risk. Updating data in one file leaves outdated copies elsewhere.</td><td>Guaranteed consistency via transactions and integrity constraints.</td></tr>
    <tr><td><strong>Data Independence</strong></td><td>None. Application programs are tightly coupled to physical file structures.</td><td>High. Logical and physical data independence via 3-schema architecture.</td></tr>
    <tr><td><strong>Concurrency & Security</strong></td><td>Difficult to enforce atomic updates and multi-user access controls.</td><td>Robust ACID transactions, row-level locks, role-based security.</td></tr>
  </tbody>
</table>

<h3>3. ANSI-SPARC 3-Level Database Architecture</h3>
<p>Proposed to achieve <strong>Data Independence</strong> (separating application programs from underlying physical storage).</p>

<table class="data-table">
  <thead>
    <tr><th>Level / Schema</th><th>Target Audience</th><th>Description & Characteristics</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>External Schema (외부 스키마)</strong></td><td>End Users / Application Programmers</td><td>Individual user views. Each user or application sees only the subset of data relevant to their specific business task (User Views). Multiple external schemas can exist.</td></tr>
    <tr><td><strong>Conceptual Schema (개념 스키마)</strong></td><td>Organization / DBA / Data Architect</td><td>Global logical structure of the entire database. Defines all entities, relationships, constraints, and business rules without regard to physical storage. Exactly ONE conceptual schema exists.</td></tr>
    <tr><td><strong>Internal Schema (내부 스키마)</strong></td><td>System Developers / Storage Engineers</td><td>Physical storage structure. Describes how data is physically stored on disk, record layouts, indices, clustering, hashing, and encryption.</td></tr>
  </tbody>
</table>

<h4>Two Types of Data Independence</h4>
<div class="note-box alert-info">
  <strong>Key TOPCIT Concept - Data Independence:</strong>
  <ul>
    <li><strong>Logical Data Independence (논리적 데이터 독립성):</strong> The ability to modify the <em>Conceptual Schema</em> (e.g., adding an entity or attribute) without requiring changes to existing <em>External Schemas</em> or application programs. Mapped between <strong>External &harr; Conceptual</strong>.</li>
    <li><strong>Physical Data Independence (물리적 데이터 독립성):</strong> The ability to alter the <em>Internal Schema</em> (e.g., adding B+Tree indices, partitioning tables, moving data to SSD) without requiring changes to the <em>Conceptual Schema</em> or applications. Mapped between <strong>Conceptual &harr; Internal</strong>.</li>
  </ul>
</div>

<h3>4. Database Roles: DBA vs DA vs Modeler</h3>
<ul>
  <li><strong>Database Administrator (DBA):</strong> Focuses on operational management, DBMS installation, performance tuning, indexing, backup & recovery, user privilege grants, and 24/7 system availability.</li>
  <li><strong>Data Architect (DA):</strong> Focuses on enterprise-wide data governance, standard terminology, domain definitions, conceptual and logical data models, data quality standards, and integration architecture.</li>
  <li><strong>Data Modeler:</strong> Works closely with business users to translate domain requirements into conceptual ERDs and normalized logical relational schemas.</li>
</ul>
"""
        },
        {
            "id": "db-relational",
            "title": "2. Relational Data Model, Keys & Integrity Constraints",
            "badge": "Day 3 • Session 2",
            "summary": "Formal definitions of relation, tuple, attribute, degree, cardinality, relational keys, and foundational integrity rules.",
            "content": """
<h3>1. Relational Data Model Terminology</h3>
<table class="data-table">
  <thead>
    <tr><th>Formal Term</th><th>Common SQL Term</th><th>Definition</th><th>Example / Property</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Relation (릴레이션)</strong></td><td>Table</td><td>A two-dimensional structure composed of rows and columns containing homogenous data.</td><td>Customer table</td></tr>
    <tr><td><strong>Tuple (튜플)</strong></td><td>Row / Record</td><td>A single row representing one instance of an entity. Tuples are unordered and unique.</td><td>(101, 'Alice', 'Seoul')</td></tr>
    <tr><td><strong>Attribute (속성)</strong></td><td>Column / Field</td><td>A named characteristic or property of an entity. Attributes are unordered.</td><td>CustomerID, Name, City</td></tr>
    <tr><td><strong>Domain (도메인)</strong></td><td>Data Type / Valid Range</td><td>The set of atomic values allowed for a given attribute.</td><td>Age domain: integers 0..120</td></tr>
    <tr><td><strong>Degree (차수)</strong></td><td>Number of Columns</td><td>The total count of attributes in a relation. Usually static over time.</td><td>Table with 5 columns &rarr; Degree = 5</td></tr>
    <tr><td><strong>Cardinality (기수 / 카디널리티)</strong></td><td>Number of Rows</td><td>The total count of tuples in a relation. Highly dynamic over time.</td><td>Table with 100 rows &rarr; Cardinality = 100</td></tr>
  </tbody>
</table>

<h3>2. Classification of Relational Keys</h3>
<div class="card-grid">
  <div class="summary-card">
    <h4>Super Key (슈퍼키)</h4>
    <p>A set of one or more attributes that uniquely identifies a tuple within a relation. Satisfies <strong>Uniqueness (유일성)</strong>, but does <em>not</em> need to satisfy Minimality (최소성).</p>
    <p><em>Example:</em> <code>{StudentID}</code>, <code>{StudentID, Name}</code>, <code>{StudentID, Email, Phone}</code> are all valid super keys.</p>
  </div>
  <div class="summary-card">
    <h4>Candidate Key (후보키)</h4>
    <p>A minimal super key. Must satisfy both <strong>Uniqueness (유일성)</strong> AND <strong>Minimality (최소성)</strong> (no attribute can be removed without losing uniqueness).</p>
    <p><em>Example:</em> If both <code>StudentID</code> and <code>ResidentID</code> uniquely identify a student alone, both are Candidate Keys.</p>
  </div>
  <div class="summary-card">
    <h4>Primary Key (기본키 - PK)</h4>
    <p>The specific Candidate Key chosen by the database designer to uniquely identify tuples in the table. Must never contain <code>NULL</code> values and must never change frequently.</p>
  </div>
  <div class="summary-card">
    <h4>Alternate Key (대체키 / 보조키)</h4>
    <p>Any Candidate Key that was NOT selected as the Primary Key (e.g., <code>ResidentID</code> when <code>StudentID</code> is PK).</p>
  </div>
  <div class="summary-card">
    <h4>Foreign Key (외래키 - FK)</h4>
    <p>An attribute in one relation (referencing relation) whose values must match the Primary Key of another relation (referenced relation), or be <code>NULL</code>. Establishes relationships.</p>
  </div>
</div>

<h3>3. Relational Integrity Constraints</h3>
<table class="data-table">
  <thead>
    <tr><th>Integrity Constraint</th><th>Core Rule</th><th>Violation Example</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Entity Integrity (개체 무결성)</strong></td><td>Primary Key attributes can <strong>never be NULL</strong> and must be strictly unique within the relation.</td><td>Inserting a customer record with <code>CustomerID = NULL</code> or duplicate <code>CustomerID = 101</code>.</td></tr>
    <tr><td><strong>Referential Integrity (참조 무결성)</strong></td><td>A Foreign Key value in the referencing table must either <strong>match an existing Primary Key value</strong> in the referenced table, or be <code>NULL</code>.</td><td>An Order record referencing <code>CustomerID = 999</code> when customer 999 does not exist in Customers table.</td></tr>
    <tr><td><strong>Domain Integrity (도메인 무결성)</strong></td><td>All attribute values must belong to the defined domain type, format, length, and valid range.</td><td>Inserting text 'ABC' into a numerical <code>Salary</code> column.</td></tr>
    <tr><td><strong>User-Defined Integrity (사용자 정의 무결성)</strong></td><td>Specific business rules and logic enforced via CHECK constraints, triggers, or assertions.</td><td>CHECK constraint ensuring <code>DiscountRate &le; 0.30</code>.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "db-erd",
            "title": "3. Conceptual Data Modeling & ER Diagramming",
            "badge": "Day 3 • Session 3",
            "summary": "Entity-Relationship modeling components, cardinalities, participation constraints, and step-by-step conversion of ER diagrams to relational tables.",
            "content": """
<h3>1. ER Model Components (Peter Chen Notation)</h3>
<ul>
  <li><strong>Entity (개체):</strong> A real-world object, concept, or event distinguishable from others. Represented as a <strong>Rectangle</strong>.
    <ul>
      <li><em>Strong Entity (정규 개체):</em> Exists independently in the real world with its own primary key.</li>
      <li><em>Weak Entity (약한 개체):</em> Depends on the existence of an identifying owner entity; cannot be identified by its own attributes alone. Represented by a <strong>Double Rectangle</strong>. Has a partial key (discriminator) underlined with a dashed line.</li>
    </ul>
  </li>
  <li><strong>Attribute (속성):</strong> A property describing an entity. Represented as an <strong>Oval / Ellipse</strong>.
    <ul>
      <li><em>Simple vs Composite:</em> Composite attributes can be divided into smaller sub-parts (e.g., <code>Address</code> &rarr; <code>State</code>, <code>City</code>, <code>ZipCode</code>).</li>
      <li><em>Single-valued vs Multi-valued:</em> Multi-valued attributes can hold multiple values for one instance (e.g., <code>PhoneNumber</code>, <code>Hobby</code>). Represented by a <strong>Double Oval</strong>.</li>
      <li><em>Derived Attribute:</em> Calculated dynamically from other stored attributes (e.g., <code>Age</code> calculated from <code>DateOfBirth</code>). Represented by a <strong>Dashed Oval</strong>.</li>
    </ul>
  </li>
  <li><strong>Relationship (관계):</strong> An association among two or more entities. Represented as a <strong>Diamond</strong>.</li>
</ul>

<h3>2. Cardinality & Participation Constraints</h3>
<ul>
  <li><strong>Cardinality Ratios:</strong> 1:1 (One-to-One), 1:N (One-to-Many), N:M (Many-to-Many).</li>
  <li><strong>Participation Constraints:</strong>
    <ul>
      <li><em>Total Participation (전체 참여 - Mandatory):</em> Every entity instance MUST participate in the relationship. Represented by a <strong>Double Line</strong> connecting entity to diamond. (e.g., Every <code>Employee</code> must belong to a <code>Department</code>).</li>
      <li><em>Partial Participation (부분 참여 - Optional):</em> Only some entity instances participate. Represented by a <strong>Single Line</strong>. (e.g., Only some <code>Employees</code> manage a <code>Department</code>).</li>
    </ul>
  </li>
</ul>

<h3>3. Converting ER Diagrams to Relational Schemas</h3>
<div class="note-box alert-warning">
  <strong>Critical Transformation Rules:</strong>
  <ol>
    <li><strong>1:1 Relationship:</strong> Place the primary key of either table into the other as a foreign key. Prefer putting the foreign key into the table with <em>total participation</em> to avoid NULLs.</li>
    <li><strong>1:N Relationship:</strong> Take the primary key from the '1' side and add it as a <strong>Foreign Key</strong> into the 'N' (Many) side table. Never reverse this!</li>
    <li><strong>N:M (Many-to-Many) Relationship:</strong> CANNOT be represented with simple foreign keys without severe anomalies. Must create a <strong>Bridge / Associative Table (교차 테이블)</strong> whose primary key is a composite of the primary keys of both participating entities.</li>
    <li><strong>Multi-Valued Attribute:</strong> Create a new independent table containing the parent entity's primary key (as FK) and the attribute value. The composite of both columns becomes the primary key.</li>
  </ol>
</div>
"""
        },
        {
            "id": "db-normalization",
            "title": "4. Database Normalization & Denormalization",
            "badge": "Day 4 • Session 1",
            "summary": "Root causes of data anomalies, step-by-step normal forms (1NF through BCNF), and strategic denormalization trade-offs.",
            "content": """
<h3>1. Data Anomalies (데이터 이상 현상)</h3>
<p>Poor relational design leads to three destructive data anomalies due to un-normalized redundant data:</p>
<div class="card-grid">
  <div class="summary-card">
    <h4>Insertion Anomaly (삽입 이상)</h4>
    <p>Cannot insert a fact about one entity without unnaturally inventing artificial, unrelated facts for another entity (or leaving PK fields NULL, violating entity integrity).</p>
  </div>
  <div class="summary-card">
    <h4>Deletion Anomaly (삭제 이상)</h4>
    <p>Deleting a record about one entity unintentionally destroys unintended, valuable facts about a completely different entity.</p>
  </div>
  <div class="summary-card">
    <h4>Update Anomaly (수정 이상)</h4>
    <p>Updating a value requires modifying multiple duplicate rows. Missing even one row results in data inconsistency where contradictory facts exist simultaneously.</p>
  </div>
</div>

<h3>2. Step-by-Step Normalization Process (1NF to BCNF)</h3>
<table class="data-table">
  <thead>
    <tr><th>Normal Form</th><th>Requirement / Rule</th><th>Resolution Technique</th><th>Exam Keyphrase</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>1NF (제1정규형)</strong></td><td>All attribute domains contain only <strong>Atomic Values</strong> (no multi-valued attributes or repeating groups).</td><td>Split repeating rows or multi-column groups into separate atomic tuples.</td><td>"원자값 (Atomic value)"</td></tr>
    <tr><td><strong>2NF (제2정규형)</strong></td><td>Must be in 1NF AND have <strong>No Partial Functional Dependencies</strong>. Every non-key attribute must be <em>fully functionally dependent</em> on the entire primary key (applies when PK is composite).</td><td>Decompose table so attributes dependent on only part of the composite PK move to a separate table.</td><td>"부분 함수 종속성 제거 (Full functional dependency)"</td></tr>
    <tr><td><strong>3NF (제3정규형)</strong></td><td>Must be in 2NF AND have <strong>No Transitive Functional Dependencies</strong> (<code>X &rarr; Y &rarr; Z</code> where X is candidate key, but non-key Z depends on non-key Y).</td><td>Decompose table so <code>Y &rarr; Z</code> forms its own table, keeping Y as foreign key in original table.</td><td>"이행적 함수 종속성 제거 (Transitive dependency)"</td></tr>
    <tr><td><strong>BCNF (Boyce-Codd)</strong></td><td>Must be in 3NF AND <strong>Every Determinant must be a Candidate Key</strong> (applies when multiple overlapping composite candidate keys exist).</td><td>Decompose so every functional dependency <code>X &rarr; Y</code> has X as a candidate key.</td><td>"모든 결정자가 후보키 (Determinant is Candidate Key)"</td></tr>
    <tr><td><strong>4NF (제4정규형)</strong></td><td>Must be in BCNF AND contain <strong>No Multi-Valued Dependencies (MVD)</strong> (<code>X &twoheadrightarrow; Y</code>).</td><td>Decompose independent multi-valued facts into separate tables.</td><td>"다치 종속성 제거"</td></tr>
    <tr><td><strong>5NF (제5정규형)</strong></td><td>Must be in 4NF AND contain <strong>No Join Dependencies</strong> (Project-Join Normal Form PJNF).</td><td>Ensure table cannot be decomposed into smaller tables without loss of lossless-join.</td><td>"조인 종속성 제거"</td></tr>
  </tbody>
</table>

<h3>3. Strategic Denormalization (반정규화 / 역정규화)</h3>
<p>While normalization minimizes redundancy and eliminates anomalies, excessive normalization increases the number of joins required to answer business queries, severely degrading read performance.</p>

<h4>Reasons and Methods for Denormalization:</h4>
<ul>
  <li><strong>Duplicate Columns:</strong> Copy frequently accessed columns into child tables to avoid expensive joins.</li>
  <li><strong>Derived / Summary Columns:</strong> Store pre-calculated totals (e.g., <code>TotalOrderAmount</code>, <code>ItemCount</code>) to avoid slow <code>COUNT()</code> and <code>SUM()</code> table scans.</li>
  <li><strong>Table Merging:</strong> Merging 1:1 tables or merging lookup tables when queries always fetch both together.</li>
  <li><strong>Table Partitioning:</strong>
    <ul>
      <li><em>Horizontal Partitioning (Range, List, Hash):</em> Splitting rows across tables (e.g., Partition orders by year).</li>
      <li><em>Vertical Partitioning:</em> Splitting columns based on frequency of access (e.g., separating huge binary <code>ProfileImage</code> or <code>TextBody</code> from fast metadata).</li>
    </ul>
  </li>
</ul>
"""
        },
        {
            "id": "db-sql",
            "title": "5. SQL Mastery & Query Optimization",
            "badge": "Day 4 • Session 2",
            "summary": "DDL, DML, DCL commands, complex SQL joins, grouping mechanics, subqueries, and window analytical functions.",
            "content": """
<h3>1. SQL Command Classifications</h3>
<ul>
  <li><strong>DDL (Data Definition Language):</strong> Defines database schemas and objects. Auto-commits in most RDBMS.
    <ul>
      <li><code>CREATE TABLE</code>, <code>ALTER TABLE</code>, <code>DROP TABLE</code>, <code>TRUNCATE TABLE</code> (fast table purge, resets high water mark, cannot rollback).</li>
    </ul>
  </li>
  <li><strong>DML (Data Manipulation Language):</strong> Manages data within objects. Can be committed or rolled back.
    <ul>
      <li><code>SELECT</code>, <code>INSERT INTO</code>, <code>UPDATE ... SET</code>, <code>DELETE FROM</code> (row-by-row deletion, logs in redo log, can rollback).</li>
    </ul>
  </li>
  <li><strong>DCL (Data Control Language):</strong> Manages security privileges and transaction boundaries.
    <ul>
      <li><code>GRANT SELECT ON Orders TO user1;</code></li>
      <li><code>REVOKE INSERT ON Orders FROM user1;</code></li>
      <li><code>COMMIT;</code>, <code>ROLLBACK;</code>, <code>SAVEPOINT sp1;</code></li>
    </ul>
  </li>
</ul>

<h3>2. SQL Joins Illustrated</h3>
<table class="data-table">
  <thead>
    <tr><th>Join Type</th><th>Behavior</th><th>SQL Syntax Example</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>INNER JOIN</strong></td><td>Returns only rows with matching values in both tables.</td><td><code>SELECT * FROM A INNER JOIN B ON A.id = B.a_id;</code></td></tr>
    <tr><td><strong>LEFT OUTER JOIN</strong></td><td>Returns all rows from left table (A), plus matching rows from right (B). Unmatched B fields return <code>NULL</code>.</td><td><code>SELECT * FROM A LEFT JOIN B ON A.id = B.a_id;</code></td></tr>
    <tr><td><strong>RIGHT OUTER JOIN</strong></td><td>Returns all rows from right table (B), plus matching rows from left (A). Unmatched A fields return <code>NULL</code>.</td><td><code>SELECT * FROM A RIGHT JOIN B ON A.id = B.a_id;</code></td></tr>
    <tr><td><strong>FULL OUTER JOIN</strong></td><td>Returns all rows when there is a match in either left or right table. Unmatched sides return <code>NULL</code>.</td><td><code>SELECT * FROM A FULL OUTER JOIN B ON A.id = B.a_id;</code></td></tr>
    <tr><td><strong>CROSS JOIN</strong></td><td>Cartesian Product. Every row of A combined with every row of B. (Rows = RowsA &times; RowsB).</td><td><code>SELECT * FROM A CROSS JOIN B;</code></td></tr>
  </tbody>
</table>

<h3>3. Aggregation & Window Functions</h3>
<pre class="code-block">
-- Window ranking functions comparison:
SELECT 
    DepartmentID, EmployeeName, Salary,
    ROW_NUMBER() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) as row_num,
    RANK()       OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) as rnk,
    DENSE_RANK() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) as dense_rnk
FROM Employees;
</pre>
<div class="note-box alert-info">
  <strong>Window Functions Difference:</strong>
  <ul>
    <li><code>ROW_NUMBER()</code>: Assigns sequential unique integers (1, 2, 3, 4) regardless of ties.</li>
    <li><code>RANK()</code>: Ties get same rank; leaves gaps after ties (e.g., 1, 2, 2, <strong>4</strong>).</li>
    <li><code>DENSE_RANK()</code>: Ties get same rank; NO gaps after ties (e.g., 1, 2, 2, <strong>3</strong>).</li>
  </ul>
</div>
"""
        },
        {
            "id": "db-transactions",
            "title": "6. Transactions, Concurrency, Recovery & Big Data",
            "badge": "Day 4 • Session 3",
            "summary": "ACID properties, concurrency anomalies, 2PL and isolation levels, Write-Ahead Logging, B+Tree indexing, CAP theorem, and Big Data technologies.",
            "content": """
<h3>1. Transaction ACID Properties</h3>
<p>A transaction is a logical unit of work that must satisfy the four <strong>ACID</strong> guarantees:</p>
<table class="data-table">
  <thead>
    <tr><th>Property</th><th>Full Name</th><th>Definition & Meaning</th><th>Enforcing Subsystem</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>A</strong></td><td><strong>Atomicity (원자성)</strong></td><td>"All or Nothing". All operations in the transaction execute successfully, or the entire transaction is rolled back with zero side effects.</td><td>Recovery Manager (Undo Log / Rollback)</td></tr>
    <tr><td><strong>C</strong></td><td><strong>Consistency (일관성)</strong></td><td>A transaction transforms the database from one valid state satisfying all integrity constraints (PK, FK, CHECK) to another valid state.</td><td>Integrity Enforcement Subsystem</td></tr>
    <tr><td><strong>I</strong></td><td><strong>Isolation (고립성 / 격리성)</strong></td><td>Concurrently executing transactions cannot see or interfere with each other's intermediate uncommitted states.</td><td>Concurrency Control Subsystem (Locking / MVCC)</td></tr>
    <tr><td><strong>D</strong></td><td><strong>Durability (지속성 / 영속성)</strong></td><td>Once a transaction commits, its updates survive permanently in persistent storage, even in the event of an immediate system crash or power outage.</td><td>Recovery Manager (Redo Log / Write-Ahead Logging)</td></tr>
  </tbody>
</table>

<h3>2. Concurrency Anomalies & SQL Isolation Levels</h3>
<div class="table-responsive">
  <table class="data-table">
    <thead>
      <tr><th>Isolation Level</th><th>Dirty Read (오독)</th><th>Non-Repeatable Read (반복불가 읽기)</th><th>Phantom Read (유령 읽기)</th><th>Mechanism</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Read Uncommitted</strong></td><td>Allowed (Occurs)</td><td>Allowed</td><td>Allowed</td><td>Reads without locking. Dirty reads possible.</td></tr>
      <tr><td><strong>Read Committed</strong> (Default in Oracle/Postgres)</td><td>Prevented</td><td>Allowed</td><td>Allowed</td><td>Holds read lock only during query; releases immediately after read.</td></tr>
      <tr><td><strong>Repeatable Read</strong> (Default in MySQL InnoDB)</td><td>Prevented</td><td>Prevented</td><td>Allowed</td><td>Holds shared locks on read data until transaction ends.</td></tr>
      <tr><td><strong>Serializable</strong></td><td>Prevented</td><td>Prevented</td><td>Prevented</td><td>Full range locking or snapshot serializability. Highest isolation, lowest throughput.</td></tr>
    </tbody>
  </table>
</div>

<h3>3. Concurrency Control Mechanisms</h3>
<ul>
  <li><strong>Locking Types:</strong>
    <ul>
      <li><em>Shared Lock (S-Lock / Read Lock):</em> Multiple transactions can acquire S-locks concurrently to read data. Blocks X-locks.</li>
      <li><em>Exclusive Lock (X-Lock / Write Lock):</em> Only one transaction can hold an X-lock to modify data. Blocks all other S-locks and X-locks.</li>
    </ul>
  </li>
  <li><strong>Two-Phase Locking Protocol (2PL - 2단계 로킹):</strong>
    <ul>
      <li><em>Growing Phase:</em> Transaction may acquire locks, but cannot release any lock.</li>
      <li><em>Shrinking Phase:</em> Transaction may release locks, but cannot acquire any new lock.</li>
      <li>Guarantees <strong>Serializability</strong>, but does NOT prevent Deadlocks.</li>
      <li><em>Strict 2PL:</em> All exclusive locks held until commit/abort. Prevents cascading aborts.</li>
    </ul>
  </li>
  <li><strong>MVCC (Multi-Version Concurrency Control):</strong> Readers do not block writers, and writers do not block readers. Reads fetch a consistent historical snapshot (undo segment) of data matching transaction start time.</li>
</ul>

<h3>4. Distributed Databases, CAP Theorem & NoSQL</h3>
<div class="note-box alert-warning">
  <strong>CAP Theorem (Brewer's Theorem):</strong> In any distributed asynchronous network, a system can simultaneously guarantee at most <strong>two out of three</strong> properties:
  <ul>
    <li><strong>C (Consistency):</strong> Every read receives the most recent write or an error.</li>
    <li><strong>A (Availability):</strong> Every non-failing node returns a non-error response for every request.</li>
    <li><strong>P (Partition Tolerance):</strong> System continues operating despite network packet loss or split-brain network partitions. (Partition tolerance is mandatory in real distributed systems).</li>
  </ul>
  <em>Trade-offs:</em> <strong>CP Systems</strong> (HBase, MongoDB) sacrifice availability for strict consistency. <strong>AP Systems</strong> (Cassandra, DynamoDB) sacrifice immediate consistency for high availability using <strong>BASE</strong> (Basically Available, Soft state, Eventual consistency).
</div>

<h4>Four NoSQL Database Categories:</h4>
<ul>
  <li><strong>Key-Value Store:</strong> Fast in-memory hash map lookup (Redis, Memcached, DynamoDB).</li>
  <li><strong>Document Store:</strong> Stores hierarchical JSON/BSON documents with rich nested indexing (MongoDB, CouchDB).</li>
  <li><strong>Column-Family Store:</strong> Wide column storage optimized for massive write throughput and sparse matrices (Apache Cassandra, HBase).</li>
  <li><strong>Graph Database:</strong> Nodes, edges, and properties optimized for deep multi-hop relationship traversals (Neo4j, Amazon Neptune).</li>
</ul>
"""
        }
    ]
}
