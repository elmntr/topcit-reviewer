import json

questions = []

# --- DOMAIN 1: Software Development (14 Questions) ---
questions.append({
    "id": "q1",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In the software engineering V-Model, which testing activity is directly responsible for verifying and validating the system against the 'Detailed Design' specifications?",
    "options": [
        "Unit Testing (단위 테스트)",
        "Integration Testing (통합 테스트)",
        "System Testing (시스템 테스트)",
        "Acceptance Testing (인수 테스트)"
    ],
    "correct": 0,
    "points": 15,
    "explanation": "In the V-Model: Unit Testing corresponds to Detailed Design (internal class/function logic); Integration Testing corresponds to Architecture/System Interface Design; System Testing corresponds to System Design & non-functional requirements; Acceptance Testing corresponds to Requirements Analysis."
})

questions.append({
    "id": "q2",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "A development team is implementing a Scrum project. During the Daily Scrum meeting, a developer reports that they cannot proceed because the staging database server is unresponsive. Whose primary role is it to remove this impediment so the team can continue working?",
    "options": [
        "The Product Owner",
        "The Scrum Master",
        "The Functional Manager",
        "The Project Sponsor"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The Scrum Master is a servant-leader whose core responsibility is coaching the team and removing external impediments and roadblocks that hinder the development team's progress."
})

questions.append({
    "id": "q3",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "A module contains a function with multiple unrelated tasks bundled together simply because they all execute during the system startup phase (e.g., initializing graphics drivers, loading sound effects, and checking disk quota). What type of cohesion does this module exhibit?",
    "options": [
        "Procedural Cohesion (절차적 응집도)",
        "Temporal Cohesion (시간적 응집도)",
        "Logical Cohesion (논리적 응집도)",
        "Communicational Cohesion (교환적 응집도)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Temporal Cohesion occurs when elements are grouped together solely because they are executed at the same point in time (e.g., startup initialization or shutdown routines), despite having no direct functional relationship."
})

questions.append({
    "id": "q4",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which of the following describes the worst (tightest) level of coupling, where one module directly modifies or accesses the internal implementation code and local variables of another module?",
    "options": [
        "Common Coupling (공통 결합도)",
        "Content Coupling (내용 결합도)",
        "Control Coupling (제어 결합도)",
        "Stamp Coupling (스탬프 결합도)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Content Coupling (내용 결합도) is the highest and most detrimental form of coupling, occurring when one module directly accesses, alters, or branches into the internal code or private memory space of another module."
})

questions.append({
    "id": "q5",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "An e-commerce platform needs to dynamically switch between different payment calculation algorithms (Credit Card with 2% fee, PayPal with flat fee, Cryptocurrency with gas fee) at runtime based on user selection without modifying existing checkout classes. Which GoF design pattern should be applied?",
    "options": [
        "Observer Pattern",
        "Strategy Pattern",
        "Decorator Pattern",
        "Factory Method Pattern"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "The Strategy Pattern defines a family of algorithms, encapsulates each one inside a separate class, and makes them interchangeable at runtime. This adheres directly to the Open/Closed Principle."
})

questions.append({
    "id": "q6",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which SOLID object-oriented design principle states that 'Software entities (classes, modules, functions) should be open for extension, but closed for modification'?",
    "options": [
        "Single Responsibility Principle (SRP)",
        "Open/Closed Principle (OCP)",
        "Liskov Substitution Principle (LSP)",
        "Interface Segregation Principle (ISP)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The Open/Closed Principle (OCP) states that systems should be designed to allow new functionality to be added via extension (polymorphism, subclassing, interfaces) without altering existing, tested source code."
})

questions.append({
    "id": "q7",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "In a software module's control flow graph, there are 14 edges (E) and 10 nodes (N). What is the Cyclomatic Complexity V(G) of this module according to McCabe's formula?",
    "options": [
        "4",
        "6",
        "8",
        "12"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "McCabe's Cyclomatic Complexity formula is V(G) = E - N + 2. Substituting E = 14 and N = 10 yields V(G) = 14 - 10 + 2 = 6. This represents the number of linearly independent paths required for complete basis path coverage."
})

questions.append({
    "id": "q8",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "During integration testing, a team decides to use the Top-Down integration approach. What temporary programming constructs must be created to simulate missing sub-modules that have not yet been developed?",
    "options": [
        "Drivers (드라이버)",
        "Stubs (스텁)",
        "Mocks (목)",
        "Spies (스파이)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "In Top-Down integration testing, development starts from the main control module; lower-level sub-modules are replaced by temporary dummy modules called Stubs. Drivers are used in Bottom-Up integration testing to simulate caller routines."
})

questions.append({
    "id": "q9",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Easy",
    "type": "Conceptual",
    "question": "Which data structure operates strictly on the LIFO (Last In, First Out) principle and is commonly utilized by compilers to manage function call frames, handle recursion, and evaluate nested parenthetical expressions?",
    "options": [
        "Queue (큐)",
        "Stack (스택)",
        "Deque (덱)",
        "Priority Queue (우선순위 큐)"
    ],
    "correct": 1,
    "points": 14,
    "explanation": "A Stack operates on LIFO (Last In, First Out), where elements are pushed and popped at the top. It is the fundamental mechanism for call stacks, recursion tracking, undo operations, and expression evaluation."
})

questions.append({
    "id": "q10",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "Which open-source software license is considered a 'Strong Copyleft' license that strictly mandates any derivative work or proprietary application statically or dynamically linked with it to also be open-sourced under the same license terms?",
    "options": [
        "Apache License 2.0",
        "MIT License",
        "GNU General Public License (GPL)",
        "BSD 3-Clause License"
    ],
    "correct": 2,
    "points": 16,
    "explanation": "The GNU GPL is a Strong Copyleft license. Its 'viral' clause mandates that any software modifying, deriving from, or linking to GPL code must distribute its complete source code under the GPL license when distributed."
})

questions.append({
    "id": "q11",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which black-box test design technique is based on the empirical observation that software errors cluster overwhelmingly at the boundary edges of valid and invalid input partitions?",
    "options": [
        "Equivalence Partitioning (동등 분할)",
        "Boundary Value Analysis (경계값 분석)",
        "Cause-Effect Graphing (원인-결과 그래프)",
        "State Transition Testing (상태 전이 테스트)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Boundary Value Analysis (BVA) specifically targets the extreme edges of input equivalence partitions (testing minimum, just below minimum, just above minimum, maximum, etc.) where off-by-one and boundary logic defects cluster."
})

questions.append({
    "id": "q12",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In the Spiral Model proposed by Barry Boehm, what distinctive activity is explicitly carried out during every single radial cycle to mitigate uncertainty before committing substantial development resources?",
    "options": [
        "Formal Contract Renegotiation",
        "Risk Analysis and Assessment (위험 분석)",
        "Acceptance User Testing",
        "Code Refactoring"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The distinguishing hallmark of Barry Boehm's Spiral Model is systematic Risk Analysis conducted at every iterative cycle to identify, evaluate, and mitigate risks before proceeding with engineering."
})

questions.append({
    "id": "q13",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Hard",
    "type": "Scenario",
    "question": "An enterprise has a massive, legacy monolithic C++ codebase with zero documentation. The engineering team uses automated decompilers and static analysis tools to extract high-level class diagrams, component dependencies, and requirements specifications. What process is this?",
    "options": [
        "Software Restructuring (재구조화)",
        "Reverse Engineering (역공학)",
        "Forward Engineering (순공학)",
        "Migration Tuning (이관 튜닝)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Reverse Engineering is the process of analyzing an existing operational system (source or binary) to extract high-level architectural designs, data models, and specifications without altering system functionality."
})

questions.append({
    "id": "q14",
    "domain": "domain1",
    "domainName": "Software Development",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which GoF behavioral pattern establishes a one-to-many relationship between objects such that when the subject object changes its internal state, all dependent observer objects are automatically notified and refreshed?",
    "options": [
        "Mediator Pattern",
        "Observer Pattern",
        "Memento Pattern",
        "Command Pattern"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The Observer Pattern defines a one-to-many dependency where a subject maintains a list of dependents (observers) and automatically broadcasts state changes to them (classic Publish-Subscribe)."
})

print(f"Domain 1: {len(questions)} questions.")


# --- DOMAIN 2: Understanding and Using Data (13 Questions) ---
questions.append({
    "id": "q15",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In the ANSI-SPARC 3-level database architecture, which form of data independence ensures that adding a new column or splitting tables at the Conceptual Schema level will NOT break existing user views or application programs?",
    "options": [
        "Physical Data Independence (물리적 데이터 독립성)",
        "Logical Data Independence (논리적 데이터 독립성)",
        "Conceptual Data Independence (개념적 데이터 독립성)",
        "External Data Independence (외부 데이터 독립성)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Logical Data Independence is achieved via the External-Conceptual Schema mapping, ensuring that modifications to the global conceptual schema do not affect external schemas or application programs."
})

questions.append({
    "id": "q16",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Easy",
    "type": "Conceptual",
    "question": "A relational table contains 8 columns and 1,200 rows. What are the 'Degree (차수)' and 'Cardinality (기수)' of this relation respectively?",
    "options": [
        "Degree = 1,200, Cardinality = 8",
        "Degree = 8, Cardinality = 1,200",
        "Degree = 8, Cardinality = 9,600",
        "Degree = 4, Cardinality = 600"
    ],
    "correct": 1,
    "points": 14,
    "explanation": "In relational algebra: Degree (차수) represents the number of attributes/columns (8). Cardinality (기수) represents the number of tuples/rows (1,200)."
})

questions.append({
    "id": "q17",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which relational integrity constraint strictly mandates that no primary key attribute in a base relation can have a NULL value, ensuring that every tuple can be uniquely distinguished?",
    "options": [
        "Referential Integrity (참조 무결성)",
        "Entity Integrity (개체 무결성)",
        "Domain Integrity (도메인 무결성)",
        "User-Defined Integrity (사용자 정의 무결성)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Entity Integrity dictates that the primary key of a relation cannot be NULL and must be unique, preventing duplicate or unidentifiable tuples."
})

questions.append({
    "id": "q18",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Hard",
    "type": "Scenario",
    "question": "In a university database, a Student table has composite primary key {StudentID, CourseID}. The attribute 'ProfessorOffice' depends only on CourseID (a proper subset of the composite primary key). This violates which normal form?",
    "options": [
        "1NF (제1정규형)",
        "2NF (제2정규형)",
        "3NF (제3정규형)",
        "BCNF (보이스-코드 정규형)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Second Normal Form (2NF) requires that the table is in 1NF and contains NO partial functional dependencies. Here, ProfessorOffice depends only on part of the composite key (CourseID), violating 2NF."
})

questions.append({
    "id": "q19",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "A table is in 2NF. It has primary key 'EmployeeID'. It also contains attributes 'DepartmentID' and 'DepartmentLocation', where EmployeeID -> DepartmentID and DepartmentID -> DepartmentLocation (transitive dependency). Transforming this into 3NF requires which action?",
    "options": [
        "Eliminating repeating atomic groups",
        "Decomposing the relation into two tables: {EmployeeID, DepartmentID} and {DepartmentID, DepartmentLocation}",
        "Adding an index on DepartmentLocation",
        "Converting DepartmentLocation to a surrogate key"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Third Normal Form (3NF) requires eliminating transitive functional dependencies (X -> Y -> Z). Decomposing the relation into (EmployeeID, DepartmentID) and (DepartmentID, DepartmentLocation) resolves the anomaly."
})

questions.append({
    "id": "q20",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Code",
    "question": "Consider the following SQL query. Which rows will be included in the final result set?\nSELECT A.id, B.val FROM TableA A LEFT OUTER JOIN TableB B ON A.id = B.a_id;",
    "options": [
        "Only rows where A.id equals B.a_id",
        "All rows from TableA, with NULL for B.val if no matching row exists in TableB",
        "All rows from TableB, with NULL for A.id if no matching row exists in TableA",
        "A full Cartesian product of all rows from TableA and TableB"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "A LEFT OUTER JOIN preserves all rows from the left table (TableA). If a row in TableA has no matching key in TableB, the columns from TableB return NULL."
})

questions.append({
    "id": "q21",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Hard",
    "type": "Code",
    "question": "In standard SQL, which window ranking function assigns ranks such that tied rows receive the same rank number, and NO rank numbers are skipped (e.g., outputs 1, 2, 2, 3)?",
    "options": [
        "ROW_NUMBER()",
        "RANK()",
        "DENSE_RANK()",
        "NTILE()"
    ],
    "correct": 2,
    "points": 16,
    "explanation": "DENSE_RANK() assigns identical ranks to ties and continues with the immediate next sequential integer (1, 2, 2, 3). Standard RANK() leaves gaps (1, 2, 2, 4), while ROW_NUMBER() assigns strictly unique integers (1, 2, 3, 4)."
})

questions.append({
    "id": "q22",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which ACID transaction property guarantees that once a transaction has successfully executed COMMIT, its data modifications will permanently persist in storage even if an immediate hardware crash or power loss occurs?",
    "options": [
        "Atomicity (원자성)",
        "Consistency (일관성)",
        "Isolation (고립성)",
        "Durability (지속성 / 영속성)"
    ],
    "correct": 3,
    "points": 15,
    "explanation": "Durability (영속성/지속성) guarantees that committed transaction updates remain permanent and survivable against catastrophic power failures or operating system crashes, enforced via Write-Ahead Logging (Redo log)."
})

questions.append({
    "id": "q23",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "Transaction T1 reads a row. Before T1 commits, Transaction T2 updates the same row and commits. When T1 reads the same row again within the same transaction, it observes different attribute values. What concurrency anomaly is this?",
    "options": [
        "Dirty Read (오독)",
        "Non-Repeatable Read (반복 불가능한 읽기)",
        "Phantom Read (유령 읽기)",
        "Lost Update (갱신 손실)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Non-Repeatable Read occurs when a transaction reads the same row twice and finds different data because another transaction committed an update between the two reads. (Phantom read involves new rows matching a range query)."
})

questions.append({
    "id": "q24",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Under the Two-Phase Locking (2PL) protocol, what rule defines the 'Shrinking Phase'?",
    "options": [
        "A transaction may acquire new locks, but cannot release any lock.",
        "A transaction may release locks, but cannot acquire any new locks.",
        "All shared locks must be converted to exclusive locks.",
        "All transactions must execute concurrently without locking."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "In 2PL, the Shrinking Phase begins as soon as the first lock is released. Once in the shrinking phase, a transaction can only release existing locks and is forbidden from acquiring any new locks."
})

questions.append({
    "id": "q25",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "According to Brewer's CAP Theorem, which two properties do distributed NoSQL systems like Apache Cassandra and Amazon DynamoDB choose to prioritize during a network partition, while adopting eventual consistency (BASE)?",
    "options": [
        "Consistency and Partition Tolerance (CP)",
        "Availability and Partition Tolerance (AP)",
        "Consistency and Availability (CA)",
        "Durability and Atomicity (DA)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Under network partition (P), AP systems (like Cassandra and DynamoDB) choose Availability over strict Consistency, guaranteeing that every node remains accessible to serve reads and writes using eventual consistency."
})

questions.append({
    "id": "q26",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Why are B+Trees preferred over standard binary search trees and standard B-Trees as the index storage engine in relational database systems?",
    "options": [
        "Leaf nodes contain pointers to parent nodes only.",
        "All data pointers reside strictly in leaf nodes, and leaf nodes are linked sequentially as a linked list, enabling rapid range scans.",
        "B+Trees consume zero disk space.",
        "B+Trees do not require balanced tree rotations."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "In a B+Tree, internal non-leaf nodes contain only router keys, while all actual data pointers reside in leaf nodes. Crucially, all leaf nodes are connected via a doubly linked list, making sequential range scans (e.g. BETWEEN 10 AND 50) extraordinarily fast."
})

questions.append({
    "id": "q27",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "An online retail analytics team needs to store millions of customer product reviews. Each review contains dynamic, semi-structured nested metadata (tags, author, verified status, nested comments) whose schema changes frequently. Which NoSQL database type is best suited?",
    "options": [
        "Key-Value Store (키-값 데이터베이스)",
        "Document Store (문서 지향 데이터베이스 - e.g., MongoDB)",
        "Relational RDBMS with 5NF Normalization",
        "Hierarchical IMS Database"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Document databases (such as MongoDB) store semi-structured JSON/BSON documents with flexible, dynamic schemas and support deep indexing on nested attributes, making them ideal for polymorphic reviews and catalog data."
})

print(f"Domain 2 added. Total questions: {len(questions)}")


# --- DOMAIN 3: Overview of System Architecture (13 Questions) ---
questions.append({
    "id": "q28",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In a modern 3-Tier enterprise architecture, what is the core functional distinction between a Web Server (e.g., Apache/Nginx) and a Web Application Server (WAS, e.g., Tomcat/Jeus)?",
    "options": [
        "Web Server manages database SQL queries; WAS manages HTTP network routing.",
        "Web Server delivers static web assets (HTML/CSS/Images); WAS executes dynamic business logic, transaction management, and servlet containers.",
        "Web Server runs the operating system kernel; WAS runs in user space.",
        "There is no architectural difference between Web Server and WAS."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Web Servers excel at serving static content and reverse-proxying HTTP traffic. WAS handles dynamic application logic, JVM bytecode execution, servlet lifecycles, and database connection pooling."
})

questions.append({
    "id": "q29",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What is the primary architectural cause of the 'Von Neumann Bottleneck' in classical computer architecture?",
    "options": [
        "The CPU ALU operates at a lower clock speed than system RAM.",
        "Program instructions and data share the same physical memory space and common system bus, preventing simultaneous instruction fetching and data reading.",
        "Secondary storage uses mechanical magnetic platters instead of flash memory.",
        "Microcode cannot execute branch instructions."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The Von Neumann bottleneck arises because both instructions and data must travel across a single shared bus from common memory, creating a throughput limit compared to Harvard architecture which uses separate buses."
})

questions.append({
    "id": "q30",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Easy",
    "type": "Conceptual",
    "question": "Which CPU register holds the memory address of the NEXT instruction to be fetched and executed in the instruction cycle?",
    "options": [
        "Instruction Register (IR)",
        "Program Counter (PC)",
        "Memory Address Register (MAR)",
        "Accumulator (AC)"
    ],
    "correct": 1,
    "points": 14,
    "explanation": "The Program Counter (PC) stores the memory address of the next sequential instruction to be fetched. The Instruction Register (IR) holds the instruction currently being executed."
})

questions.append({
    "id": "q31",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "Which of the following is a defining architectural characteristic of RISC (Reduced Instruction Set Computer) processors compared to CISC processors?",
    "options": [
        "Variable instruction lengths ranging from 1 to 15 bytes",
        "A pure Load/Store architecture where only explicit LOAD and STORE instructions access main memory, while all arithmetic operations occur strictly in registers",
        "Direct memory-to-memory arithmetic operations",
        "Microprogrammed control units executing complex multi-cycle instructions"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "RISC architectures utilize fixed-length instructions and a strict Load/Store model: arithmetic/logic operations only execute on register operands, never directly on main memory addresses."
})

questions.append({
    "id": "q32",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "A loop sequentially reads every element of a large contiguous one-dimensional array. This program behavior strongly demonstrates which principle of cache locality?",
    "options": [
        "Temporal Locality (시간적 지역성)",
        "Spatial Locality (공간적 지역성)",
        "Branch Locality (분기 지역성)",
        "Associative Locality (연관 지역성)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Spatial Locality states that if a memory location is accessed, memory locations physically adjacent to it (such as consecutive array elements) will likely be accessed soon. Temporal locality refers to re-accessing the exact same memory address (like loop counters)."
})

questions.append({
    "id": "q33",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "An enterprise storage array configures four 2TB hard drives using RAID 5. What is the total usable storage capacity, and how many simultaneous disk failures can the array tolerate without data loss?",
    "options": [
        "Usable: 8TB, Tolerates: 0 disk failures",
        "Usable: 6TB, Tolerates: 1 disk failure",
        "Usable: 4TB, Tolerates: 2 disk failures",
        "Usable: 2TB, Tolerates: 3 disk failures"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "RAID 5 uses distributed parity across N disks. Usable capacity = (N - 1) * DiskSize = (4 - 1) * 2TB = 6TB. It can tolerate exactly 1 disk failure. (RAID 6 tolerates 2)."
})

questions.append({
    "id": "q34",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What is the primary operational advantage of Direct Memory Access (DMA) over interrupt-driven I/O during high-volume disk block transfers?",
    "options": [
        "DMA converts analog signals to digital without a modem.",
        "The DMA controller transfers large blocks of data directly between the I/O peripheral and main memory over the system bus without continuous CPU instruction execution.",
        "DMA eliminates the need for RAM cache.",
        "DMA runs inside the CPU registers."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "DMA offloads bulk data transfers from the CPU. The CPU sets up transfer parameters (address, length) and is freed for other tasks; the DMA controller handles data movement directly to RAM and issues a single interrupt when finished."
})

questions.append({
    "id": "q35",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which resource is NOT shared among threads belonging to the same process?",
    "options": [
        "The Code (Text) segment",
        "The Global Data segment",
        "The Heap memory space",
        "The Program Counter (PC) and Stack space"
    ],
    "correct": 3,
    "points": 15,
    "explanation": "Threads within a process share the Code, Data, Heap, and open file descriptors. However, each thread maintains its own private Stack (local variables, function frames) and Program Counter (execution state)."
})

questions.append({
    "id": "q36",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "Which of the following is NOT one of the four Coffman conditions necessary for a system deadlock to occur?",
    "options": [
        "Mutual Exclusion (상호 배제)",
        "Hold and Wait (점유와 대기)",
        "Preemptive Resource Scheduling (선점형 자원 스케줄링)",
        "Circular Wait (환형 대기)"
    ],
    "correct": 2,
    "points": 16,
    "explanation": "The 4 Coffman conditions are Mutual Exclusion, Hold & Wait, NO Preemption (비선점), and Circular Wait. If resources can be preempted (선점), deadlocks cannot occur."
})

questions.append({
    "id": "q37",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "In virtual memory management, what phenomenon occurs when a FIFO page replacement algorithm experiences MORE page faults when the allocated number of physical page frames is increased?",
    "options": [
        "Convoy Effect",
        "Belady's Anomaly (벨레이디의 모순)",
        "Thrashing (스레싱)",
        "Priority Inversion"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Belady's Anomaly is a counter-intuitive flaw in the FIFO page replacement algorithm where increasing the number of memory page frames results in an increase in the number of page faults for certain reference strings."
})

questions.append({
    "id": "q38",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What is 'Thrashing' in an operating system virtual memory environment?",
    "options": [
        "A virus overwriting CPU cache lines.",
        "A severe performance collapse where the system spends more time swapping pages between disk and RAM than executing application code.",
        "Hard drive heads physically colliding with platter surfaces.",
        "Deadlock occurring in the network socket layer."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Thrashing occurs when the total working sets of active processes exceed available physical memory. Page faults occur continually, causing the OS to spend all CPU time swapping pages to and from disk."
})

questions.append({
    "id": "q39",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "A network engineer needs to allocate a subnet for a department that requires 28 usable host computers. Which CIDR subnet mask provides the minimum number of host addresses required without wasting address space?",
    "options": [
        "/26 (255.255.255.192)",
        "/27 (255.255.255.224)",
        "/28 (255.255.255.240)",
        "/29 (255.255.255.248)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Usable hosts formula = 2^(32 - prefix) - 2. For /28: 2^(4) - 2 = 14 hosts (too small). For /27: 2^(5) - 2 = 30 usable hosts, which perfectly fits 28 hosts with minimal waste. /26 provides 62 hosts."
})

questions.append({
    "id": "q40",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In TCP connection establishment (3-Way Handshake), what flag combination does the server transmit in response to the initial client SYN packet?",
    "options": [
        "ACK only",
        "SYN-ACK",
        "FIN-ACK",
        "RST"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "In the TCP 3-Way Handshake: Step 1: Client sends SYN. Step 2: Server responds with SYN-ACK (synchronize sequence numbers and acknowledge client's SYN). Step 3: Client responds with ACK."
})

print(f"Domain 3 added. Total questions: {len(questions)}")


# --- DOMAIN 4: Understanding Information Security (10 Questions) ---
questions.append({
    "id": "q41",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Easy",
    "type": "Conceptual",
    "question": "Which pillar of the CIA Triad is compromised when an attacker executes an unauthorized SQL UPDATE query that alters a customer's bank account balance from $100 to $1,000,000?",
    "options": [
        "Confidentiality (기밀성)",
        "Integrity (무결성)",
        "Availability (가용성)",
        "Accountability (책임성)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Integrity guarantees that data has not been modified, tampered with, or fabricated by unauthorized parties. Unauthorized alteration of account balances directly violates data integrity."
})

questions.append({
    "id": "q42",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "An organization with 200 employees decides to implement pairwise secure symmetric key encryption so that any two employees can communicate confidentially. How many distinct symmetric secret keys must be generated and managed?",
    "options": [
        "200 keys",
        "400 keys",
        "19,900 keys",
        "39,800 keys"
    ],
    "correct": 2,
    "points": 16,
    "explanation": "The symmetric key distribution formula is N * (N - 1) / 2. For N = 200: 200 * 199 / 2 = 19,900 secret keys. (In asymmetric public key cryptography, only 2N = 400 keys would be required)."
})

questions.append({
    "id": "q43",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which of the following is a Korean national symmetric block cipher standard developed by KISA in 1998, utilizing a 128-bit block size and a 16-round Feistel structure?",
    "options": [
        "AES",
        "SEED",
        "DES",
        "RSA"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "SEED is the Korean national standard symmetric block cipher developed by KISA and ETRI in 1998, featuring a 128-bit block size and 128-bit key length using a 16-round Feistel network."
})

questions.append({
    "id": "q44",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "Why is Electronic Codebook (ECB) mode strictly discouraged for encrypting large structured files or bitmap images in commercial production?",
    "options": [
        "It cannot run on 64-bit operating systems.",
        "Identical plaintext blocks are encrypted into identical ciphertext blocks using the same key, revealing underlying data patterns and structure.",
        "It requires a 1024-bit initialization vector.",
        "It does not support decryption."
    ],
    "correct": 1,
    "points": 16,
    "explanation": "In ECB mode, each plaintext block is encrypted independently without feedback or IV. Consequently, identical input blocks produce identical output blocks, preserving structural patterns (illustrated by the famous ECB Penguin leak)."
})

questions.append({
    "id": "q45",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In a standard Digital Signature scheme, what key does the SENDER use to encrypt the message digest to create the digital signature?",
    "options": [
        "The Sender's Public Key",
        "The Sender's Private Key",
        "The Receiver's Public Key",
        "The Receiver's Private Key"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "To create a Digital Signature, the sender hashes the document and encrypts the hash with the SENDER'S PRIVATE KEY. The receiver decrypts it using the SENDER'S PUBLIC KEY to verify authenticity and non-repudiation."
})

questions.append({
    "id": "q46",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "In formal mandatory access control, what is the core rule of the *-Property (Star Property) in the Bell-LaPadula confidentiality model?",
    "options": [
        "No Read Up (NRU): A subject cannot read an object of higher security level.",
        "No Write Down (NWD): A subject at a higher security level cannot write data down to an object of lower security level.",
        "No Write Up (NWU): A subject cannot write to a higher integrity level.",
        "No Read Down (NRD): A subject cannot read lower integrity data."
    ],
    "correct": 1,
    "points": 16,
    "explanation": "The Bell-LaPadula model enforces Confidentiality. The *-Property states 'No Write Down' (NWD): a user with high security clearance cannot write information to a lower classification level, preventing accidental or deliberate leaking of secret data."
})

questions.append({
    "id": "q47",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "A web application takes user input from a form and concatenates it directly into a dynamic SQL query string without escaping or validation. An attacker inputs `' OR '1'='1` to bypass login authentication. What is the most effective primary defense?",
    "options": [
        "Increasing the database password length to 32 characters",
        "Using Prepared Statements (Parameterized Queries)",
        "Installing an SSL/TLS certificate",
        "Running the database server on a non-standard port"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Prepared Statements (Parameterized Queries) pre-compile the SQL template and treat all user input strictly as literal parameter values, completely neutralizing SQL Injection attacks."
})

questions.append({
    "id": "q48",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What is the primary operational difference between an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS)?",
    "options": [
        "IDS runs on routers; IPS runs on DNS servers.",
        "IDS passively monitors traffic and sends alerts upon detecting suspicious signatures; IPS is deployed in-line and actively drops or blocks malicious packets in real time.",
        "IDS detects hardware faults; IPS detects software bugs.",
        "IDS uses symmetric encryption; IPS uses asymmetric encryption."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "IDS is a passive monitoring tool (out-of-band/tap) that logs and alerts administrators when an attack matches known signatures. IPS is an active in-line device that intercepts network packets and immediately drops or blocks malicious traffic."
})

questions.append({
    "id": "q49",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "An attacker creates a malicious QR code on a parking meter that redirects users' smartphones to a counterfeit payment gateway that captures credit card credentials. What emerging cyber threat term describes this?",
    "options": [
        "Smishing",
        "Qshing (큐싱)",
        "Pharming",
        "Vishing"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Qshing (QR code phishing) is a social engineering attack that replaces legitimate QR codes with malicious QR codes to redirect victims to fraudulent phishing sites or trigger malware downloads."
})

questions.append({
    "id": "q50",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In corporate network security design, why are public-facing services such as Web servers, Mail servers, and DNS servers placed in a Demilitarized Zone (DMZ)?",
    "options": [
        "To increase internet download speed for employees.",
        "To provide a buffer network zone isolated between the external untrusted Internet and the internal trusted corporate network, ensuring an attacker breaching the public server cannot directly access internal database servers.",
        "To avoid paying ISP bandwidth fees.",
        "To eliminate the need for server passwords."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "A DMZ isolates public-facing servers on a dedicated perimeter subnet protected by firewalls. If an external attacker compromises a Web server in the DMZ, the internal network and core databases remain shielded behind an inner firewall."
})

# --- DOMAIN 5: Understanding the IT Business and Ethics (8 Questions) ---
questions.append({
    "id": "q51",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In the Gartner Hype Cycle, what phase immediately follows the 'Peak of Inflated Expectations' when experiments fail to meet excessive public hype and media coverage turns skeptical?",
    "options": [
        "Innovation Trigger (기술 촉발)",
        "Trough of Disillusionment (환멸 단계)",
        "Slope of Enlightenment (계몽 단계)",
        "Plateau of Productivity (생산성 안정기)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The 5 stages of the Gartner Hype Cycle are: 1. Innovation Trigger -> 2. Peak of Inflated Expectations -> 3. Trough of Disillusionment -> 4. Slope of Enlightenment -> 5. Plateau of Productivity."
})

questions.append({
    "id": "q52",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "According to Michael Porter's Value Chain Model, which of the following is categorized as a 'Support Activity (지원 활동)' rather than a 'Primary Activity'?",
    "options": [
        "Inbound Logistics (물류 투입)",
        "Operations (운영 / 생산)",
        "Technology Development (기술 개발 / R&D)",
        "Marketing and Sales (마케팅 및 영업)"
    ],
    "correct": 2,
    "points": 15,
    "explanation": "Primary Activities are Inbound Logistics, Operations, Outbound Logistics, Marketing & Sales, and Service. Support Activities are Firm Infrastructure, Human Resource Management, Technology Development, and Procurement."
})

questions.append({
    "id": "q53",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "In a corporate SWOT analysis, a tech startup possesses proprietary patented AI algorithms (Strength), but faces an aggressive price war from large tech conglomerates entering the market (Threat). What type of cross-strategy should the firm formulate?",
    "options": [
        "SO Strategy (공격적 전략)",
        "ST Strategy (우회 / 다각화 전략)",
        "WO Strategy (보완 전략)",
        "WT Strategy (철수 / 방어 전략)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "An ST Strategy (Strength-Threat) utilizes internal corporate strengths (patented AI tech) to avoid, mitigate, or neutralize external threats (price wars from conglomerates)."
})

questions.append({
    "id": "q54",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "What are the four architectural views that constitute an Enterprise Architecture (EA) blueprint under standard frameworks like TOGAF?",
    "options": [
        "Financial, Customer, Internal Process, Learning Architecture",
        "Business Architecture (BA), Application Architecture (AA), Data Architecture (DA), Technical Architecture (TA)",
        "Hardware, Software, Firmware, Middleware Architecture",
        "Planning, Designing, Building, Operating Architecture"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "The foundational four views of Enterprise Architecture (often abbreviated BADT) are: Business Architecture (BA), Application Architecture (AA), Data Architecture (DA), and Technical Architecture (TA)."
})

questions.append({
    "id": "q55",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Which business process improvement philosophy advocates a radical, fundamental rethinking and clean-sheet redesign of core end-to-end workflows to achieve dramatic quantum-leap improvements in cost, quality, and cycle time?",
    "options": [
        "Process Innovation (PI)",
        "Business Process Reengineering (BPR)",
        "Total Quality Management (TQM)",
        "Statistical Process Control (SPC)"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Business Process Reengineering (BPR), championed by Michael Hammer, is characterized by radical, breakthrough redesign starting from scratch, whereas PI and TQM focus on continuous, incremental improvements."
})

questions.append({
    "id": "q56",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Hard",
    "type": "Conceptual",
    "question": "In ITIL service management, what is the core operational distinction between 'Incident Management' and 'Problem Management'?",
    "options": [
        "Incident Management handles hardware; Problem Management handles software.",
        "Incident Management focuses on rapid restoration of normal service operation (often using temporary workarounds); Problem Management investigates and resolves the underlying root cause to prevent recurrence.",
        "Incident Management is performed by executives; Problem Management by developers.",
        "There is no difference."
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Incident Management focuses on speed: restoring disrupted IT service to users as quickly as possible (e.g., restarting a service). Problem Management focuses on root-cause analysis (RCA) to permanently eliminate underlying flaws."
})

questions.append({
    "id": "q57",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "Under intellectual property law, what is the fundamental difference between Copyright protection and Patent protection for software?",
    "options": [
        "Copyright protects the novel technical invention and algorithms; Patent protects the written code.",
        "Copyright protects the creative 'expression' of software (source code text) automatically upon creation for 70 years post-mortem; Patent protects the novel 'technical invention/idea' with industrial applicability for 20 years after formal examination.",
        "Copyright lasts 20 years; Patent lasts 100 years.",
        "Software cannot be copyrighted or patented."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Copyright protects the literal expression of source code automatically without registration (70 years after author's death). Patents protect novel, non-obvious technological inventions and business methods (20 years from filing date)."
})

questions.append({
    "id": "q58",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What phenomenon occurs in Supply Chain Management (SCM) when minor fluctuations in consumer point-of-sale demand trigger exponentially magnified demand distortions as orders propagate upstream to wholesalers and manufacturers?",
    "options": [
        "The Hawthorne Effect",
        "The Bullwhip Effect (채찍 효과)",
        "The Pareto Effect",
        "The Network Effect"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "The Bullwhip Effect refers to the increasing variability of demand orders moving up the supply chain from consumer to retailer, distributor, manufacturer, and supplier due to delayed information and safety-stock batching."
})

# --- DOMAIN 6: Project Management & Technical Communication (7 Questions) ---
questions.append({
    "id": "q59",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "A software project team initially consists of 5 developers. As the project scope expands, 3 additional developers are assigned to the team. How many NEW potential communication channels have been introduced by adding these 3 members?",
    "options": [
        "10 channels",
        "18 channels",
        "28 channels",
        "38 channels"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "Channels formula = N * (N - 1) / 2. Initial (N = 5): 5 * 4 / 2 = 10 channels. New team size (N = 8): 8 * 7 / 2 = 28 channels. New channels added = 28 - 10 = 18 channels."
})

questions.append({
    "id": "q60",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What does the McKinsey MECE principle stand for in structured problem solving and business communication?",
    "options": [
        "Most Effective Corporate Execution",
        "Mutually Exclusive, Collectively Exhaustive (상호 배제와 전체 포괄)",
        "Mission Enabled Customer Engagement",
        "Methodical Evaluation of Core Elements"
    ],
    "correct": 1,
    "points": 15,
    "explanation": "MECE stands for Mutually Exclusive, Collectively Exhaustive. It requires that information, issues, or categorizations be grouped without any overlapping elements and without omitting any possibilities."
})

questions.append({
    "id": "q61",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "In which project organizational structure does the Project Manager (PM) have full-time dedicated staff, maximum authority over budget and resource allocation, and project teams are freed from departmental silos?",
    "options": [
        "Functional Organization (기능식 조직)",
        "Weak Matrix Organization (약한 매트릭스 조직)",
        "Balanced Matrix Organization (균형 매트릭스 조직)",
        "Projectized Organization (프로젝트 전담식 조직)"
    ],
    "correct": 3,
    "points": 15,
    "explanation": "In a Projectized (Project-oriented) organization, dedicated project team members report directly to the PM, who holds total authority over budget, staffing, and execution."
})

questions.append({
    "id": "q62",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "In PERT schedule estimating for a software task, the team estimates: Optimistic duration (O) = 3 days, Most Likely duration (M) = 6 days, and Pessimistic duration (P) = 15 days. What is the PERT Expected Duration (TE) based on the beta distribution?",
    "options": [
        "6.0 days",
        "7.0 days",
        "8.0 days",
        "9.5 days"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "The PERT formula is TE = (O + 4M + P) / 6. Substituting values: TE = (3 + 4 * 6 + 15) / 6 = (3 + 24 + 15) / 6 = 42 / 6 = 7.0 days."
})

questions.append({
    "id": "q63",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Hard",
    "type": "Calculation",
    "question": "A project milestone has a Planned Value (PV) of $100,000. At the status date, the Earned Value (EV) of work completed is $80,000, and the Actual Cost (AC) spent is $100,000. What are the Cost Variance (CV) and Schedule Variance (SV), and what is the project status?",
    "options": [
        "CV = +$20,000, SV = +$20,000 (Under budget, ahead of schedule)",
        "CV = -$20,000, SV = -$20,000 (Over budget, behind schedule)",
        "CV = -$20,000, SV = +$20,000 (Over budget, ahead of schedule)",
        "CV = +$20,000, SV = -$20,000 (Under budget, behind schedule)"
    ],
    "correct": 1,
    "points": 16,
    "explanation": "CV = EV - AC = $80,000 - $100,000 = -$20,000 (Negative = Over budget). SV = EV - PV = $80,000 - $100,000 = -$20,000 (Negative = Behind schedule). Both indices are below 1.0 (CPI = 0.8, SPI = 0.8)."
})

questions.append({
    "id": "q64",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Medium",
    "type": "Conceptual",
    "question": "What is the primary operational trade-off of using the 'Crashing' schedule compression technique versus 'Fast Tracking'?",
    "options": [
        "Crashing performs tasks in parallel and increases risk; Fast Tracking adds budget.",
        "Crashing adds resources or overtime to critical path activities, which directly INCREASES COST; Fast Tracking performs sequential activities in parallel, which directly INCREASES RISK of rework.",
        "Crashing eliminates the project charter.",
        "Crashing reduces scope without customer consent."
    ],
    "correct": 1,
    "points": 15,
    "explanation": "Crashing compresses the critical path by adding resources or paying overtime, which invariably increases project costs. Fast Tracking overlaps dependent activities, which introduces the risk of rework."
})

questions.append({
    "id": "q65",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "difficulty": "Medium",
    "type": "Scenario",
    "question": "A project manager identifies a high-impact risk: catastrophic data center flooding could destroy on-premise servers. The company purchases comprehensive business disruption insurance and enters into a multi-region disaster recovery SLA with a third-party cloud provider. What risk response strategy is this?",
    "options": [
        "Risk Avoidance (회피)",
        "Risk Mitigation (완화)",
        "Risk Transference (전가)",
        "Risk Acceptance (수용)"
    ],
    "correct": 2,
    "points": 15,
    "explanation": "Risk Transference involves shifting the financial impact and operational consequences of a risk to a third party through insurance policies, contractual guarantees, or outsourcing agreements."
})

print(f"Total questions compiled: {len(questions)}")

out_exam = '/home/justin/Desktop/review/review/js/data-exam.js'
with open(out_exam, 'w', encoding='utf-8') as f:
    f.write('// Official CICT / TOPCIT Full Simulation Mock Exam (65 Questions, 1000 Points)\n\n')
    f.write('const EXAM_QUESTIONS = ' + json.dumps(questions, indent=2, ensure_ascii=False) + ';\n')

print("Successfully written js/data-exam.js!")
