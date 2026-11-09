// 14-Day Study Plan Data
// Designed for burnout prevention: 3-4 bite-sized sessions (25 min each) per day

var STUDY_PLAN = [
  {
    day: 1,
    title: "Domain 1 (Part 1): Software Engineering & Development Lifecycle",
    domainId: "domain1",
    domainName: "Software Development",
    target: "Master SDLC Models, Agile/Scrum, Software Reuse & Reverse Engineering",
    estimatedMinutes: 80,
    sessions: [
      {
        id: "d1-s1",
        title: "Session 1: Software Engineering Basics & Traditional SDLC",
        duration: "25 min",
        topicId: "sw-sdlc",
        topics: [
          "Characteristics & Crisis of Software",
          "4 Key Elements: Methods, Tools, Procedures, People",
          "Waterfall Model vs Prototyping Model",
          "Spiral Model (Risk Analysis) & V-Model (V&V)"
        ],
        reviewTips: "Focus on comparing Waterfall vs Agile and understanding which phase in V-Model verifies which development stage."
      },
      {
        id: "d1-s2",
        title: "Session 2: Agile Methodologies & Scrum Framework",
        duration: "25 min",
        topicId: "sw-agile",
        topics: [
          "Agile Manifesto: 4 Values and 12 Principles",
          "Scrum Roles: Product Owner, Scrum Master, Development Team",
          "Scrum Artifacts: Product Backlog, Sprint Backlog, Burndown Chart",
          "Scrum Ceremonies: Sprint Planning, Daily Scrum, Review, Retrospective",
          "Extreme Programming (XP) Core Practices: Pair Programming, TDD, CI"
        ],
        reviewTips: "TOPCIT frequently tests Scrum roles and Burndown chart interpretation."
      },
      {
        id: "d1-s3",
        title: "Session 3: Software Reuse & Reverse Engineering",
        duration: "25 min",
        topicId: "sw-reuse",
        topics: [
          "Software Reuse: Component vs Design Pattern vs Architecture Reuse",
          "Obstacles and Countermeasures for Code Reuse",
          "Reverse Engineering: Code to Design Recovery",
          "Reengineering vs Restructuring vs Forward Engineering"
        ],
        reviewTips: "Know the difference between Reverse Engineering and Reengineering."
      }
    ]
  },
  {
    day: 2,
    title: "Domain 1 (Part 2): Architecture, Design, Testing & OSS Licenses",
    domainId: "domain1",
    domainName: "Software Development",
    target: "Master Data Structures, GoF Patterns, Cohesion/Coupling, Testing & Open Source",
    estimatedMinutes: 100,
    sessions: [
      {
        id: "d2-s1",
        title: "Session 1: Data Structures, Algorithms & Design Principles",
        duration: "25 min",
        topicId: "sw-ds-algo",
        topics: [
          "Linear vs Non-linear Data Structures (Stack, Queue, Tree, Graph)",
          "Algorithm Complexity (Big-O: O(1) to O(n²))",
          "Sorting & Searching (Quick, Merge, Heap, Binary Search)",
          "Software Design Principles: Abstraction, Information Hiding, Modularity",
          "Cohesion Levels (Coincidental to Functional) & Coupling Levels (Data to Content)"
        ],
        reviewTips: "Memorize: High Cohesion + Low Coupling = Good Design! Know all 7 cohesion types."
      },
      {
        id: "d2-s2",
        title: "Session 2: OOP, UML & GoF Design Patterns",
        duration: "25 min",
        topicId: "sw-patterns",
        topics: [
          "SOLID Principles (SRP, OCP, LSP, ISP, DIP)",
          "UML Diagrams: Class, Sequence, State, Use Case",
          "Creational Patterns: Singleton, Factory Method, Abstract Factory, Builder",
          "Structural Patterns: Adapter, Facade, Composite, Decorator, Proxy",
          "Behavioral Patterns: Observer, Strategy, Template Method, State"
        ],
        reviewTips: "Match scenario requirements to the correct GoF Design Pattern."
      },
      {
        id: "d2-s3",
        title: "Session 3: Testing, Refactoring & Open Source Licenses",
        duration: "25 min",
        topicId: "sw-testing",
        topics: [
          "White-Box Testing: Statement, Branch, Condition, Multiple Condition Coverage",
          "Black-Box Testing: Equivalence Partitioning, Boundary Value Analysis",
          "Testing Levels: Unit, Integration (Stubs & Drivers), System, Acceptance",
          "Refactoring Techniques & Code Smells",
          "OSS Licenses: GPL (Copyleft), LGPL, Apache 2.0 (Patents), MIT, BSD"
        ],
        reviewTips: "Remember: GPL requires derivative works to be open-source; MIT/BSD are permissive."
      },
      {
        id: "d2-s4",
        title: "Session 4: Domain 1 Knowledge Check Quiz",
        duration: "20 min",
        topicId: "quiz-domain1",
        topics: [
          "3-question practice quiz for Domain 1",
          "Check your answers and review each explanation"
        ],
        reviewTips: "Aim for at least 80% before moving to Domain 2."
      }
    ]
  },
  {
    day: 3,
    title: "Domain 2 (Part 1): Data Fundamentals, Architecture & ER Modeling",
    domainId: "domain2",
    domainName: "Understanding and Using Data",
    target: "Master Data vs Information, ANSI-SPARC 3-Schema, Relational Model & ERDs",
    estimatedMinutes: 80,
    sessions: [
      {
        id: "d3-s1",
        title: "Session 1: Data, Information & Database Architecture",
        duration: "25 min",
        topicId: "db-arch",
        topics: [
          "DIKW Pyramid: Data, Information, Knowledge, Wisdom",
          "File Processing System vs DBMS (Redundancy, Inconsistency, Sharing)",
          "ANSI-SPARC 3-Level Architecture: External, Conceptual, Internal Schemas",
          "Logical vs Physical Data Independence",
          "Key Roles: DBA (Operational Management) vs DA (Data Modeling & Architecture)"
        ],
        reviewTips: "Know which mapping provides Logical Data Independence (External-Conceptual)."
      },
      {
        id: "d3-s2",
        title: "Session 2: Relational Data Model & Integrity Constraints",
        duration: "25 min",
        topicId: "db-relational",
        topics: [
          "Relation, Tuple (Row), Attribute (Column), Degree, Cardinality",
          "Relational Keys: Super Key, Candidate Key, Primary Key, Alternate Key, Foreign Key",
          "Entity Integrity (PK not null & unique)",
          "Referential Integrity (FK must match valid PK or be null)",
          "Domain Integrity & User-Defined Integrity"
        ],
        reviewTips: "Understand Cardinality vs Degree calculation and the exact definition of Super vs Candidate key."
      },
      {
        id: "d3-s3",
        title: "Session 3: Conceptual Data Modeling & ER Diagramming",
        duration: "25 min",
        topicId: "db-erd",
        topics: [
          "Entity Types (Strong vs Weak) and Identifying Relationships",
          "Attribute Classifications: Simple/Composite, Single/Multi-valued, Derived",
          "Cardinality Ratios: 1:1, 1:N, N:M",
          "Participation Constraints: Total vs Partial Participation",
          "Converting ER Diagrams to Relational Schemas (Handling N:M relationships)"
        ],
        reviewTips: "N:M relationships always require a separate bridge/associative table with composite primary key."
      }
    ]
  },
  {
    day: 4,
    title: "Domain 2 (Part 2): Normalization, SQL, Transactions & Big Data",
    domainId: "domain2",
    domainName: "Understanding and Using Data",
    target: "Master Normalization (1NF-BCNF), SQL Joins, ACID, Concurrency & NoSQL",
    estimatedMinutes: 100,
    sessions: [
      {
        id: "d4-s1",
        title: "Session 1: Database Normalization & Denormalization",
        duration: "25 min",
        topicId: "db-normalization",
        topics: [
          "Data Anomalies: Insertion, Deletion, Update Anomalies",
          "1NF: Atomic values only (eliminate repeating groups)",
          "2NF: 1NF + Eliminate partial functional dependencies",
          "3NF: 2NF + Eliminate transitive functional dependencies (A -> B -> C)",
          "BCNF: 3NF + Every determinant is a candidate key",
          "Denormalization: Trade-offs, reasons (performance, joins), and methods"
        ],
        reviewTips: "Be ready to identify which normal form a table violates from a given schema and dependency set."
      },
      {
        id: "d4-s2",
        title: "Session 2: SQL Mastery & Query Optimization",
        duration: "25 min",
        topicId: "db-sql",
        topics: [
          "DDL (CREATE, ALTER, DROP, TRUNCATE) vs DML (SELECT, INSERT, UPDATE, DELETE)",
          "DCL (GRANT, REVOKE, COMMIT, ROLLBACK)",
          "INNER JOIN, LEFT/RIGHT/FULL OUTER JOIN, CROSS JOIN, NATURAL JOIN",
          "GROUP BY, HAVING vs WHERE clauses, Subqueries (Scalar, Correlated)",
          "Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK()"
        ],
        reviewTips: "Remember: WHERE filters before grouping; HAVING filters aggregated groups."
      },
      {
        id: "d4-s3",
        title: "Session 3: Transactions, Concurrency, Recovery & Big Data",
        duration: "25 min",
        topicId: "db-transactions",
        topics: [
          "ACID Properties: Atomicity, Consistency, Isolation, Durability",
          "Concurrency Problems: Lost Update, Dirty Read, Non-Repeatable Read, Phantom Read",
          "Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable",
          "Concurrency Control: Two-Phase Locking (2PL), MVCC",
          "Indexing (B+Tree properties) & Recovery (WAL - Write Ahead Logging)",
          "CAP Theorem (Consistency, Availability, Partition Tolerance), NoSQL types (Key-Value, Document, Column, Graph), Hadoop & Spark"
        ],
        reviewTips: "B+Trees store all records in leaf nodes connected as a linked list for range queries."
      },
      {
        id: "d4-s4",
        title: "Session 4: Domain 2 Knowledge Check Quiz",
        duration: "20 min",
        topicId: "quiz-domain2",
        topics: [
          "2-question practice quiz for Domain 2",
          "Review query execution, normalization, and transaction isolation"
        ],
        reviewTips: "Review SQL joins and ACID failure scenarios."
      }
    ]
  },
  {
    day: 5,
    title: "Domain 3 (Part 1): System Architecture & Computer Hardware",
    domainId: "domain3",
    domainName: "Overview of System Architecture",
    target: "Master System Architecture Styles, Computer Hardware, CPU Cycle & Memory Hierarchy",
    estimatedMinutes: 80,
    sessions: [
      {
        id: "d5-s1",
        title: "Session 1: System Architecture Concepts & Multi-Tier Layouts",
        duration: "25 min",
        topicId: "sys-arch-layout",
        topics: [
          "Information System Components: H/W, S/W, Network, Database, People",
          "Client-Server Models: 2-Tier vs 3-Tier (Web - WAS - DB)",
          "Web Server (Static content: Apache/Nginx) vs WAS (Dynamic logic: Tomcat/WebLogic)",
          "Microservices Architecture (MSA) vs Monolithic Architecture",
          "Load Balancing & High Availability (Active-Active, Active-Standby)"
        ],
        reviewTips: "Know the distinct roles of Web Server vs Web Application Server (WAS)."
      },
      {
        id: "d5-s2",
        title: "Session 2: Computer Architecture & CPU Execution",
        duration: "25 min",
        topicId: "sys-cpu",
        topics: [
          "Von Neumann Architecture (Stored Program) vs Harvard Architecture",
          "CPU Core Components: ALU, Control Unit (CU), Registers (PC, IR, MAR, MBR, AC)",
          "System Bus: Address Bus, Data Bus, Control Bus",
          "Instruction Cycle: Fetch, Decode, Execute, Store, Interrupt",
          "CISC (Variable length, complex) vs RISC (Fixed length, simple, pipelined)"
        ],
        reviewTips: "Program Counter (PC) stores the address of the NEXT instruction to be executed."
      },
      {
        id: "d5-s3",
        title: "Session 3: Memory Hierarchy, Cache & Storage Architecture",
        duration: "25 min",
        topicId: "sys-memory-io",
        topics: [
          "Memory Hierarchy: Registers -> L1/L2/L3 Cache -> RAM -> SSD/HDD",
          "Cache Memory & Locality: Temporal Locality vs Spatial Locality",
          "Cache Write Policies: Write-Through vs Write-Back",
          "I/O Control: Programmed I/O, Interrupt-Driven I/O, Direct Memory Access (DMA)",
          "RAID Architectures: RAID 0 (Striping), RAID 1 (Mirroring), RAID 5 (Parity), RAID 6, RAID 10"
        ],
        reviewTips: "DMA transfers data directly between I/O device and main memory without continuous CPU intervention."
      }
    ]
  },
  {
    day: 6,
    title: "Domain 3 (Part 2): Operating Systems & Computer Networking",
    domainId: "domain3",
    domainName: "Overview of System Architecture",
    target: "Master Process/Thread, Scheduling, Deadlocks, Paging, OSI 7-Layer & TCP/IP",
    estimatedMinutes: 100,
    sessions: [
      {
        id: "d6-s1",
        title: "Session 1: OS Process Management, Scheduling & Deadlocks",
        duration: "25 min",
        topicId: "sys-os-process",
        topics: [
          "Process vs Thread (Shared memory space: Code/Data/Heap vs private Stack)",
          "Process States & Transitions: New, Ready, Running, Waiting, Terminated",
          "CPU Scheduling: FCFS, SJF, SRTF, Round Robin (Quantum size impact), Priority",
          "Critical Section & Synchronization: Mutual Exclusion, Progress, Bounded Waiting",
          "4 Deadlock Conditions: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait",
          "Banker's Algorithm (Deadlock Avoidance) & Safe State"
        ],
        reviewTips: "Memorize the 4 Coffman Deadlock conditions; breaking any one prevents deadlock."
      },
      {
        id: "d6-s2",
        title: "Session 2: Memory Management, Virtual Memory & File Systems",
        duration: "25 min",
        topicId: "sys-os-memory",
        topics: [
          "Paging (Fixed size, eliminates external fragmentation) vs Segmentation (Logical units)",
          "Virtual Memory & Demand Paging (Page Fault Mechanism)",
          "Page Replacement Algorithms: FIFO (Belady's Anomaly), LRU, LFU, Optimal",
          "Thrashing: Working Set Model & Page Fault Frequency (PFF)",
          "Unix File System & Inode: Direct blocks, Single/Double/Triple indirect blocks"
        ],
        reviewTips: "LRU replaces the page that has not been used for the longest period of time."
      },
      {
        id: "d6-s3",
        title: "Session 3: Computer Networking (OSI 7 Layers & TCP/IP)",
        duration: "25 min",
        topicId: "sys-network",
        topics: [
          "OSI 7-Layer Model: Physical, Data Link, Network, Transport, Session, Presentation, Application",
          "TCP vs UDP: 3-Way Handshake (SYN, SYN-ACK, ACK), 4-Way Handshake (FIN)",
          "IPv4 Addressing, Subnet Masks & CIDR Calculations (Network ID, Broadcast ID, Host range)",
          "Routing Protocols: RIP (Distance Vector, Hop count), OSPF (Link State, Dijkstra), BGP (Path Vector)",
          "Key Protocols: DNS, DHCP, ARP/RARP, HTTP/HTTPS, ICMP"
        ],
        reviewTips: "Practice calculating usable IP host count: 2^(32-prefix) - 2."
      },
      {
        id: "d6-s4",
        title: "Session 4: Domain 3 Knowledge Check Quiz",
        duration: "20 min",
        topicId: "quiz-domain3",
        topics: [
          "2-question practice quiz for Domain 3",
          "Review subnetting, CPU scheduling, and deadlock scenarios"
        ],
        reviewTips: "Check your subnetting and scheduling calculation speed."
      }
    ]
  },
  {
    day: 7,
    title: "Domain 4 (Part 1): Security Concepts, Threats & Cryptography",
    domainId: "domain4",
    domainName: "Understanding Information Security",
    target: "Master CIA Triad, Malware, Threat Types, Symmetric & Asymmetric Cryptography",
    estimatedMinutes: 80,
    sessions: [
      {
        id: "d7-s1",
        title: "Session 1: Information Security Overview & Threat Landscape",
        duration: "25 min",
        topicId: "sec-overview",
        topics: [
          "CIA Triad: Confidentiality, Integrity, Availability (+ Non-repudiation, Authenticity)",
          "Malware Types: Viruses (host file needed), Worms (self-replicating), Trojans (disguised), Ransomware",
          "Advanced Threats: APT (Advanced Persistent Threat), Drive-by Download, Fileless Attacks, Cryptojacking",
          "Social Engineering: Phishing, Spear Phishing, Smishing (SMS), Vishing (Voice), Pharming (DNS redirection), Qshing (QR codes)"
        ],
        reviewTips: "TOPCIT loves new threat terms like Qshing, Fileless Malware, and APT lifecycle stages."
      },
      {
        id: "d7-s2",
        title: "Session 2: Symmetric Cryptography & Block Cipher Modes",
        duration: "25 min",
        topicId: "sec-symmetric",
        topics: [
          "Symmetric (Secret Key) Encryption: High speed, Key distribution challenge",
          "Number of Keys for N users: N(N-1)/2",
          "Block Ciphers: DES (64-bit block, 56-bit key), 3DES, AES (128-bit block, 128/192/256-bit key)",
          "Korean Standard Ciphers: SEED (128-bit), ARIA, HIGHT, LEA",
          "Block Cipher Modes: ECB (Pattern leakage), CBC (Uses IV, chained), CTR (Parallel counter)"
        ],
        reviewTips: "Never use ECB mode for images or structured data because patterns remain visible."
      },
      {
        id: "d7-s3",
        title: "Session 3: Asymmetric Cryptography & Hash Functions",
        duration: "25 min",
        topicId: "sec-asymmetric",
        topics: [
          "Asymmetric (Public Key) Encryption: Public Key encrypts, Private Key decrypts (Key count: 2N)",
          "Algorithms: RSA (Integer factorization), ECC (Elliptic curve - shorter key, high security), Diffie-Hellman",
          "One-Way Hash Functions: Pre-image resistance, Second pre-image resistance, Collision resistance",
          "Hash Algorithms: MD5 (Broken), SHA-1 (Deprecated), SHA-2 (SHA-256, SHA-512), SHA-3",
          "Message Authentication Code (HMAC): Integrates secret key with hash for integrity + authenticity"
        ],
        reviewTips: "256-bit ECC provides equivalent security to 3072-bit RSA with much faster computation."
      }
    ]
  },
  {
    day: 8,
    title: "Domain 4 (Part 2): PKI, Access Control, Web Attacks & Standards",
    domainId: "domain4",
    domainName: "Understanding Information Security",
    target: "Master Digital Signatures, PKI, MAC/DAC/RBAC, OWASP Top 10, Firewalls & ISMS-P",
    estimatedMinutes: 100,
    sessions: [
      {
        id: "d8-s1",
        title: "Session 1: Digital Signatures, PKI & Authentication Technologies",
        duration: "25 min",
        topicId: "sec-pki-auth",
        topics: [
          "Digital Signature Workflow: Hash created -> Encrypted with Sender's Private Key -> Verified with Public Key",
          "Guarantees: Integrity, Authentication, Non-repudiation",
          "PKI Components: CA (Certificate Authority), RA (Registration Authority), CRL & OCSP, X.509",
          "Authentication Factors: Something you know, have, are, or where you are",
          "MFA, FIDO (Fast Identity Online - Passwordless public key authentication), SSO & Kerberos"
        ],
        reviewTips: "Digital signatures encrypt the hash with the SENDER'S PRIVATE KEY."
      },
      {
        id: "d8-s2",
        title: "Session 2: Access Control Policies & Security Models",
        duration: "25 min",
        topicId: "sec-access-control",
        topics: [
          "DAC (Discretionary Access Control): Object owner grants permissions (ACLs)",
          "MAC (Mandatory Access Control): System security labels and clearances",
          "RBAC (Role-Based Access Control): Permissions mapped to roles, users assigned to roles",
          "Bell-LaPadula Model (Confidentiality): No Read Up (Simple), No Write Down (*-property)",
          "Biba Model (Integrity): No Read Down (Simple), No Write Up (*-property)"
        ],
        reviewTips: "Bell-LaPadula = Confidentiality (NRU, NWD). Biba = Integrity (NRD, NWU)."
      },
      {
        id: "d8-s3",
        title: "Session 3: Web Security, OWASP Top 10, Network Defenses & ISMS-P",
        duration: "25 min",
        topicId: "sec-web-network",
        topics: [
          "SQL Injection & Defense: Parameterized queries / Prepared Statements",
          "Cross-Site Scripting (XSS: Stored, Reflected, DOM) & Cross-Site Request Forgery (CSRF: Anti-CSRF Token, SameSite)",
          "Buffer Overflow Defenses: ASLR, DEP/NX, Stack Canary",
          "Firewalls: Packet Filter (L3/L4) vs Stateful Inspection vs Application Proxy (L7) vs WAF",
          "IDS vs IPS: Signature-based (Misuse) vs Anomaly-based",
          "Security Standards: ISO/IEC 27001, ISMS-P, GDPR (Privacy by Design, 72h breach reporting)"
        ],
        reviewTips: "Prepared statements are the primary defense against SQL Injection."
      },
      {
        id: "d8-s4",
        title: "Session 4: Domain 4 Knowledge Check Quiz",
        duration: "20 min",
        topicId: "quiz-domain4",
        topics: [
          "2-question practice quiz for Domain 4",
          "Review attack scenarios, cryptography choices, and security models"
        ],
        reviewTips: "Make sure you can spot SQLi, XSS, and CSRF vulnerabilities in sample code."
      }
    ]
  },
  {
    day: 9,
    title: "Domain 5 (Part 1): IT Business Strategy & Environmental Analysis",
    domainId: "domain5",
    domainName: "Understanding the IT Business and Ethics",
    target: "Master Business-IT Alignment, Hype Cycle, Porter's Value Chain & Strategic Frameworks",
    estimatedMinutes: 80,
    sessions: [
      {
        id: "d9-s1",
        title: "Session 1: IT Business Concept & Industry Ecosystem",
        duration: "25 min",
        topicId: "biz-concept",
        topics: [
          "Business-IT Alignment: IT as a strategic enabler, not just cost center",
          "Gartner Hype Cycle: Innovation Trigger -> Peak of Inflated Expectations -> Trough of Disillusionment -> Slope of Enlightenment -> Plateau of Productivity",
          "Digital Transformation (DX) & Platform Business Models",
          "IT Productivity Paradox: Why IT spending doesn't automatically create profit without organizational alignment"
        ],
        reviewTips: "Memorize the 5 stages of the Gartner Hype Cycle in order."
      },
      {
        id: "d9-s2",
        title: "Session 2: Porter's Value Chain & Strategic Analysis Frameworks",
        duration: "25 min",
        topicId: "biz-strategy",
        topics: [
          "Porter's Value Chain: Primary Activities (Inbound, Operations, Outbound, Sales/Marketing, Service) vs Support Activities (Infrastructure, HR, Tech Dev, Procurement)",
          "SWOT Matrix & Cross-Strategies: SO (Aggressive), ST (Diversification), WO (Turnaround), WT (Defensive)",
          "3C Analysis: Customer, Competitor, Company",
          "Porter's 5 Forces: New Entrants, Buyer Power, Supplier Power, Substitutes, Industry Rivalry",
          "PEST Analysis (Political, Economic, Social, Technological) & McKinsey 7S"
        ],
        reviewTips: "Know which activities in Porter's Value Chain are Primary vs Support."
      },
      {
        id: "d9-s3",
        title: "Session 3: BCG Matrix, KPI & Strategic Goal Setting",
        duration: "25 min",
        topicId: "biz-planning",
        topics: [
          "BCG Growth-Share Matrix: Stars, Question Marks (Problem Children), Cash Cows, Dogs",
          "Balanced Scorecard (BSC): Financial, Customer, Internal Business Process, Learning & Growth",
          "Key Performance Indicators (KPI) and Critical Success Factors (CSF)"
        ],
        reviewTips: "Cash Cows have high market share in a low-growth market, generating steady cash flow."
      }
    ]
  },
  {
    day: 10,
    title: "Domain 5 (Part 2): EA, ISP, Enterprise Systems, ITSM & IT Ethics",
    domainId: "domain5",
    domainName: "Understanding the IT Business and Ethics",
    target: "Master EA (TOGAF/Zachman), ISP, ERP/SCM/CRM, ITIL, SLA & Intellectual Property",
    estimatedMinutes: 100,
    sessions: [
      {
        id: "d10-s1",
        title: "Session 1: IT Governance, Enterprise Architecture & ISP",
        duration: "25 min",
        topicId: "biz-ea-isp",
        topics: [
          "IT Governance: COBIT 5/2019 Principles and Alignment",
          "Enterprise Architecture (EA): 4 Views - Business (BA), Application (AA), Data (DA), Technical (TA)",
          "EA Frameworks: Zachman (6x6 matrix), TOGAF (ADM Architecture Development Method)",
          "Information Strategy Planning (ISP): As-Is Analysis -> To-Be Design -> Transition Plan & Roadmap"
        ],
        reviewTips: "Remember the 4 core architectures of EA: BA, AA, DA, TA."
      },
      {
        id: "d10-s2",
        title: "Session 2: S/W Acquisition, Outsourcing & Process Improvement",
        duration: "25 min",
        topicId: "biz-acquisition",
        topics: [
          "ISO/IEC 12207 Software Life Cycle: Primary, Supporting, Organizational Processes",
          "Procurement Documents: RFI, RFP, Proposal, Evaluation & Contract",
          "Outsourcing Types (Total, Selective, Offshoring) & Governance",
          "Process Improvement: BPR (Radical redesign) vs PI (Continuous improvement)",
          "Six Sigma: DMAIC (Existing processes) vs DMADV (New processes) - 3.4 DPMO",
          "TRIZ (Theory of Inventive Problem Solving) & SERVQUAL"
        ],
        reviewTips: "BPR is radical breakthrough redesign; Six Sigma DMAIC is data-driven statistical defect reduction."
      },
      {
        id: "d10-s3",
        title: "Session 3: Enterprise Solutions (ERP/SCM/CRM), ITSM/ITIL & IT Ethics",
        duration: "25 min",
        topicId: "biz-solutions-ethics",
        topics: [
          "Enterprise Solutions: ERP (Single DB), SCM (Bullwhip effect reduction), CRM, PLM",
          "Decision Support: EDW, Business Intelligence (BI), OLAP",
          "ITSM & ITIL Framework: Incident, Problem, Change, Release Management",
          "SLA (Service Level Agreement) & SLM (Service Level Management)",
          "Intellectual Property Rights: Copyright (Expression, 70 yrs post-mortem), Patent (Novel invention, 20 yrs from filing), Trade Secret",
          "Personal Information Protection Act & AI Ethics"
        ],
        reviewTips: "Copyright protects the expression of code, while Patents protect novel technical inventions/algorithms."
      },
      {
        id: "d10-s4",
        title: "Session 4: Domain 5 Knowledge Check Quiz",
        duration: "20 min",
        topicId: "quiz-domain5",
        topics: [
          "2-question practice quiz for Domain 5",
          "Review business frameworks, SLA terms, and ethics cases"
        ],
        reviewTips: "Focus on distinguishing Incident vs Problem management and SLA metrics."
      }
    ]
  },
  {
    day: 11,
    title: "Domain 6 (Part 1): Business Communication & Technical Documentation",
    domainId: "domain6",
    domainName: "Project Management & Technical Communication",
    target: "Master Communication Channels, MECE, Logic Trees, RFP, SRS & Technical Writing",
    estimatedMinutes: 80,
    sessions: [
      {
        id: "d11-s1",
        title: "Session 1: Business Communication Concepts & Channel Formula",
        duration: "25 min",
        topicId: "pm-comm",
        topics: [
          "Communication Process: Sender -> Encoding -> Channel (Noise) -> Receiver -> Decoding -> Feedback",
          "Communication Directions: Top-Down, Bottom-Up, Horizontal/Lateral",
          "Communication Channels Formula: N(N - 1) / 2 (Essential TOPCIT calculation!)",
          "Example: If team increases from 5 to 8 members, channels increase from 10 to 28 (+18)",
          "Active Listening, Emotional Intelligence & Persuasion Techniques"
        ],
        reviewTips: "Always be ready to calculate communication channel growth when team size changes."
      },
      {
        id: "d11-s2",
        title: "Session 2: Logical Thinking & Problem Solving Techniques",
        duration: "25 min",
        topicId: "pm-problem-solving",
        topics: [
          "MECE (Mutually Exclusive, Collectively Exhaustive) Principle",
          "Logic Tree: Issue Tree (What), Why Tree (Root Cause), How Tree (Solution)",
          "5 Whys Analysis for Root Cause Identification",
          "Fishbone / Ishikawa Diagram (Cause and Effect: 4M/6M categories)",
          "Delphi Technique (Anonymous iterative expert consensus) & Pareto 80/20 Rule"
        ],
        reviewTips: "MECE ensures no overlaps and no gaps in problem breakdown."
      },
      {
        id: "d11-s3",
        title: "Session 3: Business & Technical Document Writing",
        duration: "25 min",
        topicId: "pm-documentation",
        topics: [
          "Business Documents: Official Letters, Meeting Minutes (Action items with owner/deadline), Email Etiquette",
          "Technical Documents: RFI, RFP (Scope, requirements, evaluation), Proposal",
          "Software Requirements Specification (SRS: IEEE 830)",
          "Requirements Traceability Matrix (RTM: Links requirements to test cases)",
          "Design Specifications, Test Plans, User Manuals & Project Completion Reports"
        ],
        reviewTips: "Meeting minutes must always specify attendee signatures, decisions made, and action items with owners and deadlines."
      }
    ]
  },
  {
    day: 12,
    title: "Domain 6 (Part 2): Project Management (CPM, PERT, EVM & Risk)",
    domainId: "domain6",
    domainName: "Project Management & Technical Communication",
    target: "Master PMBOK, Organizational Structures, Critical Path Method, PERT, EVM & Risk Matrix",
    estimatedMinutes: 100,
    sessions: [
      {
        id: "d12-s1",
        title: "Session 1: Project Organization & Life Cycle (PMBOK)",
        duration: "25 min",
        topicId: "pm-organization",
        topics: [
          "Project Definition: Temporary, Unique Deliverable, Progressive Elaboration vs Operations (Ongoing)",
          "Triple Constraint: Scope, Time, Cost (+ Quality)",
          "Organizational Structures: Functional (PM has little authority) vs Matrix (Weak, Balanced, Strong) vs Projectized (PM has full authority)",
          "PMO (Project Management Office): Supportive, Controlling, Directive",
          "5 PM Process Groups: Initiating (Project Charter), Planning, Executing, Monitoring/Controlling, Closing"
        ],
        reviewTips: "Know which organizational structure gives the Project Manager the highest authority (Projectized)."
      },
      {
        id: "d12-s2",
        title: "Session 2: Scope & Schedule Management (CPM & PERT)",
        duration: "25 min",
        topicId: "pm-schedule",
        topics: [
          "WBS (Work Breakdown Structure): Deliverable-oriented decomposition, Work Packages",
          "Scope Creep vs Gold Plating",
          "Precedence Diagramming Method (PDM): FS, SS, FF, SF relationships",
          "Critical Path Method (CPM): Longest duration path, Float/Slack = 0",
          "Forward Pass (ES, EF = ES + Duration) & Backward Pass (LF, LS = LF - Duration)",
          "PERT 3-Point Estimate: TE = (O + 4M + P) / 6; Standard Deviation = (P - O) / 6",
          "Schedule Compression: Crashing (Add resources, cost up) vs Fast Tracking (Parallel tasks, risk up)"
        ],
        reviewTips: "Practice PERT calculation: If Optimistic=4, Most Likely=7, Pessimistic=16, TE = (4 + 28 + 16)/6 = 8 days."
      },
      {
        id: "d12-s3",
        title: "Session 3: Earned Value Management (EVM) & Risk Management",
        duration: "25 min",
        topicId: "pm-evm-risk",
        topics: [
          "EVM Core Metrics: Planned Value (PV), Earned Value (EV), Actual Cost (AC), BAC",
          "Variances: CV = EV - AC (Positive=Under budget), SV = EV - PV (Positive=Ahead of schedule)",
          "Indices: CPI = EV / AC (>1 Under budget), SPI = EV / PV (>1 Ahead of schedule)",
          "Forecasting: Estimate at Completion EAC = BAC / CPI",
          "Risk Management: Qualitative (P x I Matrix) vs Quantitative (EMV = Probability x Impact)",
          "Risk Response Strategies: Threat (Avoid, Mitigate, Transfer, Accept) vs Opportunity (Exploit, Enhance, Share, Accept)"
        ],
        reviewTips: "EVM questions are guaranteed on TOPCIT! Memorize CV, SV, CPI, and SPI formulas."
      },
      {
        id: "d12-s4",
        title: "Session 4: Domain 6 Knowledge Check Quiz",
        duration: "20 min",
        topicId: "quiz-domain6",
        topics: [
          "2-question practice quiz for Domain 6",
          "Review EVM calculations, Critical Path finding, and communication channel formulas"
        ],
        reviewTips: "Make sure you can solve EVM and PERT word problems in under 60 seconds."
      }
    ]
  },
  {
    day: 13,
    title: "High-Yield Consolidation & Cheat Sheet Mastery",
    domainId: "review",
    domainName: "Comprehensive Review",
    target: "Cram High-Frequency Formulas, Acronyms, Flashcards & Weak Points across all 6 Domains",
    estimatedMinutes: 90,
    sessions: [
      {
        id: "d13-s1",
        title: "Session 1: All-Formula Drill & High-Frequency Calculations",
        duration: "25 min",
        topicId: "cheatsheet-formulas",
        topics: [
          "EVM: CV, SV, CPI, SPI, EAC",
          "PERT: Expected Duration TE = (O + 4M + P)/6 and Sigma = (P - O)/6",
          "Communication Channels: N(N - 1) / 2",
          "Networking: CIDR, Usable Hosts = 2^(32-prefix) - 2",
          "Cryptography: Symmetric Keys = N(N - 1) / 2, Asymmetric Keys = 2N"
        ],
        reviewTips: "Write down each formula on paper from memory without looking."
      },
      {
        id: "d13-s2",
        title: "Session 2: Flashcard Review Blitz (45 Cards)",
        duration: "25 min",
        topicId: "flashcards-all",
        topics: [
          "Review the 45 cards across all six domains",
          "Filter by domain and flip each card to check your recall"
        ],
        reviewTips: "Flip fast: aim for 10-15 seconds per card."
      },
      {
        id: "d13-s3",
        title: "Session 3: Cross-Domain Trap Topics & Weak Area Review",
        duration: "25 min",
        topicId: "weak-areas",
        topics: [
          "Cohesion types vs Coupling types (frequently confused)",
          "Normalization: 2NF (partial dep) vs 3NF (transitive dep) vs BCNF",
          "Bell-LaPadula (Confidentiality) vs Biba (Integrity)",
          "BPR vs Six Sigma DMAIC vs PI",
          "Crashing vs Fast Tracking"
        ],
        reviewTips: "Re-read the comparison tables for pairs of concepts you commonly mix up."
      }
    ]
  },
  {
    day: 14,
    title: "CICT / TOPCIT Mock Exam Day",
    domainId: "exam",
    domainName: "Mock Exam Simulation",
    target: "Simulate Real Exam: 65 Questions, 120 Mins, 1000-Point Scale with Diagnostic Report",
    estimatedMinutes: 130,
    sessions: [
      {
        id: "d14-s1",
        title: "Session 1: Exam Environment Setup & Mindset Check",
        duration: "10 min",
        topicId: "exam-prep",
        topics: [
          "Prepare a quiet desk with scrap paper and a water bottle",
          "Close distracting browser tabs",
          "Review exam strategy: 65 questions, 120 minutes = ~1.8 min per question",
          "Strategy: First pass easy questions, flag calculation/scenario problems for second pass"
        ],
        reviewTips: "Never leave any question blank in TOPCIT — no negative marking!"
      },
      {
        id: "d14-s2",
        title: "Session 2: Full CICT/TOPCIT Mock Exam (65 Questions)",
        duration: "100 min",
        topicId: "full-exam",
        topics: [
          "Take the full 65-question assessment under strict timed conditions",
          "Questions cover all 6 domains proportionally",
          "Submit and review your practice score (0-1000) and estimated level (1-5)"
        ],
        reviewTips: "Keep an eye on the countdown timer. Pace yourself steadily."
      },
      {
        id: "d14-s3",
        title: "Session 3: In-Depth Diagnostic Review & Final Polish",
        duration: "20 min",
        topicId: "exam-review",
        topics: [
          "Analyze domain breakdown report: identify lowest scoring domain",
          "Read full answer explanations for all missed questions",
          "Final boost of confidence: you are now prepared!"
        ],
        reviewTips: "A Level 3 (400+) is standard graduation level; Level 4 (600+) is honors/advanced professional!"
      }
    ]
  }
];

if (typeof window !== "undefined") { window.STUDY_PLAN = STUDY_PLAN; }
