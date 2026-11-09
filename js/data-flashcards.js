// High-Yield CICT / TOPCIT Flashcard Deck

var FLASHCARDS_DATA = [
  {
    "id": "fc1",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "SDLC",
    "front": "What are the 4 Key Elements of Software Engineering?",
    "back": "Methods, Tools, Procedures, and People."
  },
  {
    "id": "fc2",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Agile",
    "front": "What are the 3 distinct roles in the Scrum framework?",
    "back": "1. Product Owner (PO): Manages backlog, prioritizes value, bridges to stakeholders.\n2. Scrum Master (SM): Servant leader, coaches team, removes impediments.\n3. Development Team: Cross-functional self-organizing creators of the increment."
  },
  {
    "id": "fc3",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Architecture",
    "front": "List the 7 levels of Cohesion from Best (Strongest) to Worst (Weakest).",
    "back": "1. Functional\n2. Sequential\n3. Communicational\n4. Procedural\n5. Temporal\n6. Logical\n7. Coincidental"
  },
  {
    "id": "fc4",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Architecture",
    "front": "List the 6 levels of Coupling from Best (Loosest) to Worst (Tightest).",
    "back": "1. Data Coupling\n2. Stamp Coupling\n3. Control Coupling\n4. External Coupling\n5. Common Coupling\n6. Content Coupling"
  },
  {
    "id": "fc5",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "OOP",
    "front": "What does each letter in the SOLID principles stand for?",
    "back": "S: Single Responsibility\nO: Open/Closed\nL: Liskov Substitution\nI: Interface Segregation\nD: Dependency Inversion"
  },
  {
    "id": "fc6",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Testing",
    "front": "What are the 4 test levels and their corresponding V-Model verification targets?",
    "back": "Unit Test &harr; Detailed Design\nIntegration Test &harr; Architecture Design\nSystem Test &harr; System Design\nAcceptance Test &harr; Requirements Analysis"
  },
  {
    "id": "fc7",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Open Source",
    "front": "What is the key legal obligation of the GNU GPL license?",
    "back": "Strong Copyleft: Any derivative work or statically/dynamically linked software distributed must also have its complete source code released under the GPL."
  },
  {
    "id": "fc8",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Design Patterns",
    "front": "What GoF pattern provides a surrogate or placeholder to control access to an object?",
    "back": "Proxy Pattern (Virtual Proxy, Remote Proxy, Protection Proxy)."
  },
  {
    "id": "fc9",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Design Patterns",
    "front": "Which GoF pattern converts the interface of a class into another interface that clients expect?",
    "back": "Adapter Pattern (Wrapper)."
  },
  {
    "id": "fc10",
    "domain": "domain1",
    "domainName": "Software Development",
    "category": "Algorithms",
    "front": "What is the Cyclomatic Complexity formula for a flow graph?",
    "back": "V(G) = E - N + 2\n(E = number of edges, N = number of nodes)"
  },
  {
    "id": "fc11",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Architecture",
    "front": "What are the 3 schema levels in the ANSI-SPARC architecture?",
    "back": "1. External Schema (User views)\n2. Conceptual Schema (Global logical structure)\n3. Internal Schema (Physical disk storage & indices)"
  },
  {
    "id": "fc12",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Relational",
    "front": "What is the difference between Super Key and Candidate Key?",
    "back": "Super Key satisfies Uniqueness only (may include extra attributes).\nCandidate Key is a MINIMAL super key that satisfies both Uniqueness AND Minimality."
  },
  {
    "id": "fc13",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Integrity",
    "front": "State Entity Integrity and Referential Integrity.",
    "back": "Entity Integrity: Primary key cannot be NULL and must be unique.\nReferential Integrity: Foreign key must match an existing primary key in the referenced table, or be NULL."
  },
  {
    "id": "fc14",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Normalization",
    "front": "Define 1NF, 2NF, 3NF, and BCNF requirements succinctly.",
    "back": "1NF: Atomic values only (no repeating groups).\n2NF: 1NF + No partial functional dependencies (full key dependency).\n3NF: 2NF + No transitive functional dependencies (X &rarr; Y &rarr; Z).\nBCNF: 3NF + Every determinant is a candidate key."
  },
  {
    "id": "fc15",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Transactions",
    "front": "What are the 4 ACID properties of database transactions?",
    "back": "Atomicity (All or nothing)\nConsistency (Preserves schema integrity constraints)\nIsolation (Concurrent transactions don't interfere)\nDurability (Committed changes survive system crashes)"
  },
  {
    "id": "fc16",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Concurrency",
    "front": "Explain Dirty Read, Non-Repeatable Read, and Phantom Read.",
    "back": "Dirty Read: Reading uncommitted updates made by another transaction.\nNon-Repeatable Read: Re-reading the same row returns modified values due to an intermediate committed update.\nPhantom Read: Re-executing a range query returns newly inserted/deleted rows."
  },
  {
    "id": "fc17",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "Distributed",
    "front": "State the CAP Theorem trade-off.",
    "back": "A distributed system can guarantee at most TWO of: Consistency (C), Availability (A), and Partition Tolerance (P). Under network partition, systems choose either CP or AP."
  },
  {
    "id": "fc18",
    "domain": "domain2",
    "domainName": "Understanding and Using Data",
    "category": "SQL",
    "front": "Compare RANK() vs DENSE_RANK() vs ROW_NUMBER().",
    "back": "ROW_NUMBER(): Sequential integers without ties (1, 2, 3, 4).\nRANK(): Ties get same rank; leaves gaps (1, 2, 2, 4).\nDENSE_RANK(): Ties get same rank; NO gaps (1, 2, 2, 3)."
  },
  {
    "id": "fc19",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "Hardware",
    "front": "What is the difference between Von Neumann and Harvard architecture?",
    "back": "Von Neumann: Instructions and data share common memory and bus (Von Neumann bottleneck).\nHarvard: Physically separate memories and buses for instructions and data."
  },
  {
    "id": "fc20",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "Hardware",
    "front": "CISC vs RISC: Name 3 fundamental differences.",
    "back": "CISC: Variable length, memory-to-memory operations, complex instruction set.\nRISC: Fixed length (32-bit), Load/Store architecture only (registers for math), single-cycle pipelining."
  },
  {
    "id": "fc21",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "OS",
    "front": "Name the 4 Coffman conditions required for Deadlock.",
    "back": "1. Mutual Exclusion\n2. Hold and Wait\n3. No Preemption\n4. Circular Wait"
  },
  {
    "id": "fc22",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "OS",
    "front": "What is Thrashing in virtual memory?",
    "back": "A state where the system spends almost all its time swapping pages in/out of disk rather than executing application instructions, caused by insufficient physical frames for the total working sets."
  },
  {
    "id": "fc23",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "Storage",
    "front": "Compare RAID 0, RAID 1, and RAID 5.",
    "back": "RAID 0: Striping (100% capacity, fast, NO fault tolerance).\nRAID 1: Mirroring (50% capacity, tolerates 1 disk failure per pair).\nRAID 5: Block striping with distributed parity ((N-1)/N capacity, tolerates 1 disk failure)."
  },
  {
    "id": "fc24",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "Networking",
    "front": "Formula for usable host IP addresses in CIDR subnetting.",
    "back": "Usable Hosts = 2^(32 - prefix) - 2\n(Subtract 2 for Network ID and Broadcast Address)."
  },
  {
    "id": "fc25",
    "domain": "domain3",
    "domainName": "Overview of System Architecture",
    "category": "Networking",
    "front": "List the packets exchanged in a TCP 3-Way Handshake.",
    "back": "1. Client &rarr; Server: SYN\n2. Server &rarr; Client: SYN-ACK\n3. Client &rarr; Server: ACK"
  },
  {
    "id": "fc26",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "category": "Principles",
    "front": "What are the 3 pillars of the CIA Triad?",
    "back": "Confidentiality: Prevention of unauthorized disclosure.\nIntegrity: Prevention of unauthorized modification.\nAvailability: Assurance of timely access for authorized users."
  },
  {
    "id": "fc27",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "category": "Crypto",
    "front": "Formula for total symmetric keys needed for N communicating users.",
    "back": "Total Keys = N &times; (N - 1) / 2"
  },
  {
    "id": "fc28",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "category": "Crypto",
    "front": "Why is 256-bit ECC preferred over 3072-bit RSA in modern mobile and IoT devices?",
    "back": "Elliptic Curve Cryptography (ECC) achieves equivalent cryptographic strength with drastically smaller key sizes, consuming less memory, bandwidth, and CPU battery power."
  },
  {
    "id": "fc29",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "category": "Access Control",
    "front": "Compare Bell-LaPadula vs Biba security models.",
    "back": "Bell-LaPadula (Confidentiality): No Read Up (NRU), No Write Down (NWD).\nBiba (Integrity): No Read Down (NRD), No Write Up (NWU)."
  },
  {
    "id": "fc30",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "category": "Web Security",
    "front": "What is the primary technical defense against SQL Injection?",
    "back": "Prepared Statements (Parameterized Queries), which pre-compile SQL queries and treat inputs strictly as literal data rather than executable code."
  },
  {
    "id": "fc31",
    "domain": "domain4",
    "domainName": "Understanding Information Security",
    "category": "Network",
    "front": "What is the function of a DMZ (Demilitarized Zone)?",
    "back": "An isolated buffer network perimeter hosting public-facing servers (Web, Mail, DNS) between untrusted Internet and internal trusted corporate intranet."
  },
  {
    "id": "fc32",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "category": "Strategy",
    "front": "What are the 5 phases of the Gartner Hype Cycle?",
    "back": "1. Innovation Trigger\n2. Peak of Inflated Expectations\n3. Trough of Disillusionment\n4. Slope of Enlightenment\n5. Plateau of Productivity"
  },
  {
    "id": "fc33",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "category": "Strategy",
    "front": "List the 5 Primary Activities in Michael Porter's Value Chain.",
    "back": "1. Inbound Logistics\n2. Operations\n3. Outbound Logistics\n4. Marketing & Sales\n5. Service"
  },
  {
    "id": "fc34",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "category": "EA",
    "front": "What are the 4 core architecture views of Enterprise Architecture (EA)?",
    "back": "B: Business Architecture (BA)\nA: Application Architecture (AA)\nD: Data Architecture (DA)\nT: Technical Architecture (TA)"
  },
  {
    "id": "fc35",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "category": "Improvement",
    "front": "Distinguish between BPR and Process Innovation (PI).",
    "back": "BPR: Radical, clean-sheet breakthrough redesign for dramatic gains.\nPI: Continuous, incremental, and systematic operational improvement."
  },
  {
    "id": "fc36",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "category": "Law",
    "front": "Software Copyright vs Software Patent: Protection duration?",
    "back": "Copyright: Protects expression automatically; Author's lifetime + 70 years.\nPatent: Protects novel technical inventions; 20 years from filing date."
  },
  {
    "id": "fc37",
    "domain": "domain5",
    "domainName": "Understanding the IT Business and Ethics",
    "category": "ITSM",
    "front": "Formula for System Availability % using MTBF and MTTR.",
    "back": "Availability (%) = [MTBF / (MTBF + MTTR)] &times; 100%"
  },
  {
    "id": "fc38",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "Communication",
    "front": "Formula for Total Communication Channels among N team members.",
    "back": "Channels = N &times; (N - 1) / 2"
  },
  {
    "id": "fc39",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "Schedule",
    "front": "PERT Expected Duration (TE) and Standard Deviation (&sigma;) formulas.",
    "back": "TE = (O + 4M + P) / 6\n&sigma; = (P - O) / 6\n(O = Optimistic, M = Most Likely, P = Pessimistic)"
  },
  {
    "id": "fc40",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "Schedule",
    "front": "What is the Float (Slack) on activities lying on the Critical Path?",
    "back": "Total Float is strictly ZERO (0). Any delay on a critical path activity delays the entire project completion date."
  },
  {
    "id": "fc41",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "Schedule",
    "front": "Crashing vs Fast Tracking: Key trade-offs?",
    "back": "Crashing: Adds resources/overtime to critical path &rarr; Increases Cost.\nFast Tracking: Performs sequential activities in parallel &rarr; Increases Risk of rework."
  },
  {
    "id": "fc42",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "EVM",
    "front": "State the Cost Variance (CV) and Schedule Variance (SV) formulas.",
    "back": "CV = EV - AC (Positive = Under budget, Negative = Over budget)\nSV = EV - PV (Positive = Ahead of schedule, Negative = Behind schedule)"
  },
  {
    "id": "fc43",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "EVM",
    "front": "State the CPI and SPI formulas and interpretation.",
    "back": "CPI = EV / AC (&gt; 1.0 = Under budget, &lt; 1.0 = Cost overrun)\nSPI = EV / PV (&gt; 1.0 = Ahead of schedule, &lt; 1.0 = Behind schedule)"
  },
  {
    "id": "fc44",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "Risk",
    "front": "What are the 4 standard response strategies for Negative Risks (Threats)?",
    "back": "1. Avoid: Eliminate root cause.\n2. Mitigate: Reduce probability or impact.\n3. Transfer: Shift burden via insurance or outsourcing.\n4. Accept: Establish contingency reserve or handle as-is."
  },
  {
    "id": "fc45",
    "domain": "domain6",
    "domainName": "Project Management & Technical Communication",
    "category": "Problem Solving",
    "front": "What does MECE stand for and what does it prevent?",
    "back": "Mutually Exclusive, Collectively Exhaustive.\nIt prevents duplicate overlaps and eliminates missing gaps in problem structuring."
  }
];

if (typeof window !== "undefined") { window.FLASHCARDS_DATA = FLASHCARDS_DATA; }
