# Domain 3 data: Overview of System Architecture
d3 = {
    "id": "domain3",
    "title": "Domain 3: Overview of System Architecture",
    "icon": "🏗️",
    "description": "System architecture layouts, 3-Tier Web-WAS-DB, Computer hardware, CPU cycle, CISC vs RISC, Memory hierarchy, Cache locality, RAID, Operating Systems (Process, Threads, CPU scheduling, Deadlocks, Paging/Virtual memory, Inodes), and Networking (OSI 7-layer, TCP/IP, Subnetting).",
    "sections": [
        {
            "id": "sys-arch-layout",
            "title": "1. System Architecture Layouts & Multi-Tier Models",
            "badge": "Day 5 • Session 1",
            "summary": "Evolution of enterprise architectures, client-server models, Web Server vs WAS distinction, and high-availability server clustering.",
            "content": """
<h3>1. Evolution of System Architectures</h3>
<ul>
  <li><strong>Mainframe Architecture:</strong> Centralized computing where dumb terminals connect directly to a massive central mainframe. Single point of failure, proprietary.</li>
  <li><strong>Client-Server (2-Tier):</strong> Fat client (rich client application) contains presentation and business logic, connecting directly to a database server via ODBC/JDBC. Hard to update client software across thousands of workstations.</li>
  <li><strong>3-Tier Architecture (Web &ndash; WAS &ndash; DB):</strong> Modern enterprise standard separating presentation, business logic, and data storage.
    <ul>
      <li><strong>Tier 1: Presentation Layer (Web Server):</strong> Handles HTTP/HTTPS requests, SSL termination, static content delivery (HTML, CSS, JS, images), reverse proxying, and load balancing (Apache HTTPD, Nginx).</li>
      <li><strong>Tier 2: Application / Business Logic Layer (Web Application Server - WAS):</strong> Executes dynamic business logic, transaction management, connection pooling, enterprise JavaBeans, servlet containers (Tomcat, WebLogic, Jeus).</li>
      <li><strong>Tier 3: Data Layer (DBMS):</strong> Stores persistent data, enforces relational integrity, executes queries, manages ACID transactions (Oracle, MySQL, PostgreSQL).</li>
    </ul>
  </li>
  <li><strong>Microservices Architecture (MSA):</strong> Decomposes complex applications into small, independently deployable, loosely coupled services communicating via lightweight protocols (REST API, gRPC, Event-driven message brokers like Kafka).</li>
</ul>

<h3>2. Server High Availability (HA) Clustering</h3>
<table class="data-table">
  <thead>
    <tr><th>Clustering Mode</th><th>Active Nodes</th><th>Standby Nodes</th><th>Resource Utilization</th><th>Failover Characteristics</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Active-Active (능동-능동)</strong></td><td>All servers concurrently process incoming traffic.</td><td>None (both active).</td><td>High (100% capacity used for load sharing).</td><td>Instant. If one server fails, remaining node absorbs traffic (requires capacity headroom).</td></tr>
    <tr><td><strong>Active-Standby (능동-대기)</strong></td><td>Primary node processes all requests.</td><td>Secondary node waits idle, replicating state.</td><td>Lower (standby server sits idle during normal operations).</td><td>Failover time required for standby node to detect heartbeat loss and assume virtual IP.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sys-cpu",
            "title": "2. Computer Architecture & CPU Execution",
            "badge": "Day 5 • Session 2",
            "summary": "Von Neumann vs Harvard architectures, CPU internal components, registers, the instruction execution cycle, and CISC vs RISC comparison.",
            "content": """
<h3>1. Von Neumann vs Harvard Architecture</h3>
<div class="card-grid">
  <div class="summary-card">
    <h4>Von Neumann Architecture (폰 노이만 구조)</h4>
    <p>Stored-program computer where <strong>program instructions and data share the same physical memory and common bus</strong>.</p>
    <ul>
      <li><em>Von Neumann Bottleneck:</em> CPU throughput is strictly limited because instruction fetch and data read/write cannot occur simultaneously over the shared bus.</li>
    </ul>
  </div>
  <div class="summary-card">
    <h4>Harvard Architecture (하버드 구조)</h4>
    <p>Uses <strong>physically separate memories and separate buses</strong> for instructions (program memory) and data (data memory).</p>
    <ul>
      <li>Allows simultaneous instruction fetch and data operand read/write. Widely used in modern DSPs and CPU internal L1 caches (split L1 I-cache and L1 D-cache).</li>
    </ul>
  </div>
</div>

<h3>2. CPU Internal Components & Key Registers</h3>
<ul>
  <li><strong>ALU (Arithmetic Logic Unit):</strong> Performs arithmetic operations (+, -, *, /) and bitwise logical operations (AND, OR, NOT, XOR, shifts).</li>
  <li><strong>Control Unit (CU):</strong> Directs operations of the processor, generates timing and control signals, orchestrates instruction fetch, decoding, and execution.</li>
  <li><strong>Key Registers:</strong>
    <ul>
      <li><strong>Program Counter (PC):</strong> Holds the memory address of the <em>NEXT</em> instruction to be fetched and executed. Automatically incremented.</li>
      <li><strong>Instruction Register (IR):</strong> Holds the instruction currently being executed/decoded.</li>
      <li><strong>Memory Address Register (MAR):</strong> Holds the physical memory address from which data will be fetched or to which data will be written.</li>
      <li><strong>Memory Buffer / Data Register (MBR / MDR):</strong> Holds the actual data read from or written to memory.</li>
      <li><strong>Accumulator (AC):</strong> Temporarily holds intermediate arithmetic and logical results from the ALU.</li>
      <li><strong>Program Status Word (PSW / Flags):</strong> Holds status condition codes (Zero flag, Carry flag, Sign flag, Overflow flag, Interrupt enable).</li>
    </ul>
  </li>
</ul>

<h3>3. The Instruction Execution Cycle</h3>
<ol>
  <li><strong>Fetch Cycle:</strong> Fetch instruction from memory addressed by PC into IR; increment PC.</li>
  <li><strong>Indirect Cycle:</strong> If instruction uses indirect addressing, fetch effective address from memory.</li>
  <li><strong>Execute Cycle:</strong> Decode opcode and perform specified operation (ALU computation, register transfer).</li>
  <li><strong>Interrupt Cycle:</strong> Check for pending hardware/software interrupts. If present, save current state to stack and jump to Interrupt Service Routine (ISR).</li>
</ol>

<h3>4. CISC vs RISC Architecture</h3>
<table class="data-table">
  <thead>
    <tr><th>Feature</th><th>CISC (Complex Instruction Set Computer)</th><th>RISC (Reduced Instruction Set Computer)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Instruction Set</strong></td><td>Large, complex instruction set (hundreds of multi-cycle instructions).</td><td>Small, highly optimized, simple instruction set.</td></tr>
    <tr><td><strong>Instruction Length</strong></td><td>Variable length (1 to 15+ bytes). Difficult to pipeline.</td><td>Fixed length (typically 32-bit). Ideal for pipelining.</td></tr>
    <tr><td><strong>Execution Time</strong></td><td>Multi-cycle per instruction.</td><td>1 instruction per clock cycle (CPI &approx; 1.0) via pipelining.</td></tr>
    <tr><td><strong>Memory Access</strong></td><td>Instructions can directly access memory operands (Memory-to-Memory).</td><td><strong>Load/Store Architecture only</strong> (Only LOAD and STORE access memory; all computations happen in registers).</td></tr>
    <tr><td><strong>Registers</strong></td><td>Fewer general-purpose registers.</td><td>Large general-purpose register file (32+ registers).</td></tr>
    <tr><td><strong>Representative CPUs</strong></td><td>Intel x86 / AMD x86-64</td><td>ARM, MIPS, RISC-V, Apple Silicon (M-series)</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sys-memory-io",
            "title": "3. Memory Hierarchy, Cache Locality, RAID & DMA",
            "badge": "Day 5 • Session 3",
            "summary": "Memory hierarchy levels, principle of locality, cache write policies, DMA controllers, and detailed breakdown of RAID levels.",
            "content": """
<h3>1. Memory Hierarchy (메모리 계층 구조)</h3>
<pre class="code-block">
[Registers]          &lt;-- Fastest speed, highest cost/bit, smallest capacity
     |
[L1 / L2 / L3 Cache]
     |
[Main Memory (DRAM)]
     |
[Solid-State Drive (SSD) / Hard Disk Drive (HDD)]
     |
[Optical / Tape Backup]  &lt;-- Slowest speed, lowest cost/bit, massive capacity
</pre>

<h4>The Principle of Locality (지역성의 원리)</h4>
<p>Programs do not access memory uniformly; they exhibit two fundamental patterns:</p>
<ul>
  <li><strong>Temporal Locality (시간적 지역성):</strong> If a memory location is referenced once, it will likely be referenced again in the near future (e.g., loop counters, frequently called functions).</li>
  <li><strong>Spatial Locality (공간적 지역성):</strong> If a memory location is referenced, nearby memory locations will likely be referenced soon (e.g., sequential array traversal, instruction stream execution).</li>
</ul>

<h4>Cache Write Policies:</h4>
<ul>
  <li><strong>Write-Through (즉시 쓰기):</strong> Every write to cache is immediately written simultaneously to main memory. Simple, guarantees memory consistency, but slower due to bus traffic.</li>
  <li><strong>Write-Back (지연 쓰기):</strong> Updates are written only to the cache; the modified block is marked with a <strong>Dirty Bit</strong> and written to main memory only when evicted from cache. Faster, but transient risk of inconsistency during crashes.</li>
</ul>

<h3>2. Direct Memory Access (DMA)</h3>
<p>In traditional programmed I/O, the CPU must read every byte from the peripheral device into a register and write it to RAM, causing massive CPU waste.</p>
<div class="note-box alert-info">
  <strong>DMA (직접 메모리 접근):</strong> A dedicated hardware DMA Controller transfers blocks of data directly between high-speed I/O devices (disk, NIC) and main memory over the system bus <strong>without continuous CPU intervention</strong>. The CPU is notified via a single interrupt only when the entire data block transfer is complete.
</div>

<h3>3. RAID (Redundant Array of Independent Disks)</h3>
<table class="data-table">
  <thead>
    <tr><th>RAID Level</th><th>Architecture</th><th>Min Disks</th><th>Capacity Efficiency</th><th>Fault Tolerance</th><th>Pros & Cons</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>RAID 0</strong></td><td>Data Striping (데이터 스트라이핑)</td><td>2</td><td>100% (N disks)</td><td><strong>Zero</strong> (Failure of 1 disk loses all data).</td><td>Fastest read/write throughput; no redundancy.</td></tr>
    <tr><td><strong>RAID 1</strong></td><td>Disk Mirroring (미러링)</td><td>2</td><td>50% (N / 2)</td><td>Tolerates failure of 1 disk per mirrored pair.</td><td>High data safety, fast reads; high storage cost overhead.</td></tr>
    <tr><td><strong>RAID 5</strong></td><td>Block Striping with <strong>Distributed Parity</strong></td><td>3</td><td>(N - 1) / N</td><td>Tolerates failure of <strong>1 single disk</strong>.</td><td>Balanced cost and performance. Rebuild requires parity calculation.</td></tr>
    <tr><td><strong>RAID 6</strong></td><td>Block Striping with <strong>Dual Distributed Parity</strong></td><td>4</td><td>(N - 2) / N</td><td>Tolerates failure of <strong>up to 2 simultaneous disks</strong>.</td><td>High reliability for enterprise arrays; slower write speed due to dual parity computation.</td></tr>
    <tr><td><strong>RAID 10 (1+0)</strong></td><td>Stripe of Mirrors (Striping across mirrored pairs)</td><td>4</td><td>50% (N / 2)</td><td>Tolerates 1 disk failure per mirror pair.</td><td>High performance + high redundancy; expensive.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sys-os-process",
            "title": "4. OS Process Management, CPU Scheduling & Deadlocks",
            "badge": "Day 6 • Session 1",
            "summary": "Process vs Thread distinctions, process control blocks, CPU scheduling algorithms, critical sections, and the 4 Coffman deadlock conditions.",
            "content": """
<h3>1. Process vs Thread</h3>
<table class="data-table">
  <thead>
    <tr><th>Dimension</th><th>Process (프로세스)</th><th>Thread (스레드)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Definition</strong></td><td>An executing program instance with its own private virtual memory space.</td><td>The smallest unit of CPU dispatching/execution within a process (Lightweight Process).</td></tr>
    <tr><td><strong>Memory Sharing</strong></td><td>Isolated address spaces. Communication requires IPC (Inter-Process Communication: Pipes, Sockets, Shared Memory).</td><td>Threads within the same process <strong>share Code, Data, and Heap segments</strong>; each thread retains its own private <strong>Stack and Program Counter (PC)</strong>.</td></tr>
    <tr><td><strong>Context Switch Overhead</strong></td><td>High. Requires flushing TLB, switching page tables and MMU state.</td><td>Low. Only register set and stack pointer must be swapped.</td></tr>
    <tr><td><strong>Fault Isolation</strong></td><td>High. Crash in one process does not affect others.</td><td>Low. Unhandled exception in one thread crashes the entire process.</td></tr>
  </tbody>
</table>

<h3>2. CPU Scheduling Algorithms</h3>
<ul>
  <li><strong>Preemptive (선점형):</strong> The OS can forcibly interrupt a currently running process to assign the CPU to a higher-priority process (e.g., Round Robin, SRTF, Priority Preemptive).
    <ul>
      <li><em>Round Robin (RR):</em> Each process receives a fixed time slice (quantum). If quantum is too large &rarr; degenerates into FCFS; if too small &rarr; context switch overhead dominates.</li>
      <li><em>Shortest Remaining Time First (SRTF):</em> Preemptive version of SJF. Dispatches process with shortest remaining burst time.</li>
    </ul>
  </li>
  <li><strong>Non-Preemptive (비선점형):</strong> Once the CPU is allocated to a process, it holds the CPU until it terminates or voluntarily blocks for I/O (e.g., FCFS, SJF, HRRN).
    <ul>
      <li><em>First-Come, First-Served (FCFS):</em> Susceptible to the <strong>Convoy Effect</strong> (short processes stuck behind a huge CPU-bound process).</li>
      <li><em>Shortest Job First (SJF):</em> Optimal average waiting time, but risks starvation for long processes.</li>
      <li><em>Highest Response Ratio Next (HRRN):</em> Prevents starvation by dynamically factoring aging into priority:
        <code>Priority = (Waiting Time + Service Time) / Service Time</code>.</li>
    </ul>
  </li>
</ul>

<h3>3. Deadlocks (교착 상태) & The 4 Coffman Conditions</h3>
<p>A deadlock is a situation where two or more processes are permanently blocked because each holds a resource that the other requires.</p>

<div class="note-box alert-warning">
  <strong>The 4 Necessary & Sufficient Conditions for Deadlock:</strong>
  <ol>
    <li><strong>Mutual Exclusion (상호 배제):</strong> At least one resource must be held in a non-shareable mode (only one process at a time).</li>
    <li><strong>Hold and Wait (점유와 대기):</strong> A process must currently hold at least one resource while waiting to acquire additional resources held by other processes.</li>
    <li><strong>No Preemption (비선점):</strong> Resources cannot be forcibly seized; a resource can be released only voluntarily by the process holding it after task completion.</li>
    <li><strong>Circular Wait (환형 대기):</strong> A closed circular chain of processes exists, where each process holds resources requested by the next process in the cycle (P0 &rarr; P1 &rarr; ... &rarr; Pn &rarr; P0).</li>
  </ol>
</div>

<h4>Deadlock Handling Strategies:</h4>
<ul>
  <li><strong>Prevention (예방):</strong> Constrain resource requests by eliminating at least ONE of the 4 Coffman conditions (e.g., enforce total resource ordering to eliminate circular wait). Low resource utilization.</li>
  <li><strong>Avoidance (회피 - Dijkstra's Banker's Algorithm):</strong> The OS dynamically tests whether granting a resource request keeps the system in a <strong>Safe State</strong> (a sequence exists where all processes can finish). If unsafe, request is delayed.</li>
  <li><strong>Detection & Recovery (탐지 및 복구):</strong> Periodically runs resource allocation graphs (Wait-For Graph) to find cycles. Resolves by killing processes or preempting resources.</li>
  <li><strong>Ignorance (무시 - Ostrich Algorithm):</strong> Assume deadlocks occur rarely and ignore them (used by modern general-purpose OS like Linux and Windows).</li>
</ul>
"""
        },
        {
            "id": "sys-os-memory",
            "title": "5. Memory Management, Virtual Memory & File Systems",
            "badge": "Day 6 • Session 2",
            "summary": "Paging vs Segmentation, page fault handling, page replacement algorithms, thrashing, and Unix Inode disk block structures.",
            "content": """
<h3>1. Paging vs Segmentation</h3>
<table class="data-table">
  <thead>
    <tr><th>Feature</th><th>Paging (페이징)</th><th>Segmentation (세그먼테이션)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Division Unit</strong></td><td>Fixed-size physical blocks (Pages in virtual memory, Frames in physical memory).</td><td>Variable-size logical blocks based on program semantic units (Main, Subroutine, Stack, Data).</td></tr>
    <tr><td><strong>Fragmentation</strong></td><td><strong>No External Fragmentation</strong>; causes small <strong>Internal Fragmentation</strong> in the last page.</td><td><strong>No Internal Fragmentation</strong>; causes serious <strong>External Fragmentation</strong> over time.</td></tr>
    <tr><td><strong>Mapping Mechanism</strong></td><td>Page Table: Page Number &rarr; Frame Base Address + Offset.</td><td>Segment Table: Segment Number &rarr; Base Address + Limit (checked against length).</td></tr>
  </tbody>
</table>

<h3>2. Virtual Memory Page Replacement Algorithms</h3>
<ul>
  <li><strong>Optimal Page Replacement (OPT / MIN):</strong> Replaces the page that will not be used for the longest period of time in the future. Theoretical benchmark; impossible to implement in practice because future reference strings cannot be known.</li>
  <li><strong>FIFO (First-In, First-Out):</strong> Replaces the oldest page loaded. Exhibits <strong>Belady's Anomaly</strong> (increasing the number of page frames can paradoxically increase the number of page faults!).</li>
  <li><strong>LRU (Least Recently Used):</strong> Replaces the page that has not been referenced for the longest period of time. Approximates OPT effectively using hardware timestamps or stack.</li>
  <li><strong>LFU (Least Frequently Used):</strong> Replaces the page with the smallest reference count.</li>
</ul>

<h4>Thrashing (스레싱) & The Working Set Model:</h4>
<div class="note-box alert-warning">
  <strong>Thrashing:</strong> A catastrophic performance collapse where the system spends more time swapping pages in and out of disk than executing CPU instructions. Occurs when the sum of working sets of all active processes exceeds available physical memory frames.
  <ul>
    <li><strong>Working Set (워킹셋):</strong> The set of pages actively referenced by a process during a sliding time window &Delta;. The OS must allocate enough frames to hold each process's entire working set to prevent thrashing.</li>
  </ul>
</div>

<h3>3. Unix File System & Inode Architecture</h3>
<p>In Unix/Linux, an <strong>Inode (Index Node)</strong> stores all file metadata (file type, permissions, owner, file size, timestamps, block pointers). <strong>The file name is NOT stored in the inode</strong>; it is stored in directory entries mapping name to inode number.</p>
<ul>
  <li><strong>Direct Blocks (직접 블록):</strong> Pointers (typically 12) directly referencing disk data blocks containing file content. Ideal for fast access to small files.</li>
  <li><strong>Single Indirect Block (단일 간접):</strong> Points to a disk block filled with pointers to data blocks.</li>
  <li><strong>Double Indirect Block (이중 간접):</strong> Points to a block of indirect pointer blocks.</li>
  <li><strong>Triple Indirect Block (삼중 간접):</strong> Allows Unix file systems to support massive terabyte-scale files efficiently.</li>
</ul>
"""
        },
        {
            "id": "sys-network",
            "title": "6. Computer Networking, OSI 7 Layers & TCP/IP",
            "badge": "Day 6 • Session 3",
            "summary": "OSI 7-layer vs TCP/IP models, TCP 3-way handshake mechanics, IP addressing, CIDR subnetting calculations, and routing protocols.",
            "content": """
<h3>1. The OSI 7-Layer Reference Model</h3>
<div class="table-responsive">
  <table class="data-table">
    <thead>
      <tr><th>Layer</th><th>Protocol Data Unit (PDU)</th><th>Primary Function</th><th>Protocols & Hardware Devices</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>7. Application</strong></td><td>Data</td><td>Network services directly to user applications (UI, APIs).</td><td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP</td></tr>
      <tr><td><strong>6. Presentation</strong></td><td>Data</td><td>Data format translation, syntax representation, compression, encryption.</td><td>SSL/TLS, JPEG, ASCII, MPEG</td></tr>
      <tr><td><strong>5. Session</strong></td><td>Data</td><td>Establishes, maintains, and synchronizes dialog connections.</td><td>NetBIOS, RPC, Sockets</td></tr>
      <tr><td><strong>4. Transport</strong></td><td>Segment (TCP) / Datagram (UDP)</td><td>End-to-end reliable transmission, port multiplexing, flow/congestion control.</td><td>TCP, UDP; L4 Switch</td></tr>
      <tr><td><strong>3. Network</strong></td><td>Packet</td><td>Logical IP addressing, routing across internetworks.</td><td>IPv4, IPv6, ICMP, ARP, OSPF, BGP; Router, L3 Switch</td></tr>
      <tr><td><strong>2. Data Link</strong></td><td>Frame</td><td>Physical MAC addressing, node-to-node framing, error detection (CRC).</td><td>Ethernet, IEEE 802.11, PPP; Switch, Bridge</td></tr>
      <tr><td><strong>1. Physical</strong></td><td>Bit</td><td>Transmission of raw unstructured bit streams over physical medium.</td><td>RJ45, Fiber, Coaxial; Hub, Repeater</td></tr>
    </tbody>
  </table>
</div>

<h3>2. TCP vs UDP Protocols</h3>
<table class="data-table">
  <thead>
    <tr><th>Characteristic</th><th>TCP (Transmission Control Protocol)</th><th>UDP (User Datagram Protocol)</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Connection Mode</strong></td><td>Connection-oriented (Requires 3-Way Handshake before data transfer).</td><td>Connectionless (Immediate transmission without setup).</td></tr>
    <tr><td><strong>Reliability</strong></td><td>Guaranteed (Sequence numbers, ACKs, retransmissions on loss).</td><td>Best-effort (Unreliable; packets can be lost, duplicated, out of order).</td></tr>
    <tr><td><strong>Flow & Congestion Control</strong></td><td>Yes (Sliding Window, Slow Start, Fast Retransmit).</td><td>None (Application must handle congestion).</td></tr>
    <tr><td><strong>Header Overhead</strong></td><td>20 to 60 bytes.</td><td>8 bytes fixed.</td></tr>
    <tr><td><strong>Use Cases</strong></td><td>Web (HTTP/S), Email (SMTP), File transfer (FTP), SSH.</td><td>Live video streaming, VoIP, DNS queries, Online gaming.</td></tr>
  </tbody>
</table>

<h4>TCP Connection Management:</h4>
<ul>
  <li><strong>3-Way Handshake (Connection Establishment):</strong>
    <ol>
      <li>Client &rarr; Server: <code>SYN</code> (seq = x)</li>
      <li>Server &rarr; Client: <code>SYN-ACK</code> (seq = y, ack = x + 1)</li>
      <li>Client &rarr; Server: <code>ACK</code> (ack = y + 1)</li>
    </ol>
  </li>
  <li><strong>4-Way Handshake (Connection Termination):</strong>
    <ol>
      <li>Client &rarr; Server: <code>FIN</code></li>
      <li>Server &rarr; Client: <code>ACK</code> (Server enters CLOSE_WAIT)</li>
      <li>Server &rarr; Client: <code>FIN</code> (Server finished sending data)</li>
      <li>Client &rarr; Server: <code>ACK</code> (Client enters TIME_WAIT to ensure ACK arrival)</li>
    </ol>
  </li>
</ul>

<h3>3. IP Addressing & CIDR Subnetting Calculations</h3>
<div class="note-box alert-info">
  <strong>CIDR Subnetting Formulas for TOPCIT:</strong>
  <ul>
    <li>Total IP Addresses in a <code>/prefix</code> block = <code>2^(32 - prefix)</code></li>
    <li><strong>Usable Host Addresses</strong> = <code>2^(32 - prefix) - 2</code> (Subtract 2 because the first IP is the <em>Network ID</em> and the last IP is the <em>Broadcast Address</em>).</li>
  </ul>
  <p><em>Example Calculation:</em> Given subnet mask <code>255.255.255.224</code> (/27):</p>
  <ul>
    <li>Prefix = 27 &rarr; Host bits = 32 - 27 = 5</li>
    <li>Total addresses = 2⁵ = 32</li>
    <li>Usable hosts = 32 - 2 = <strong>30 hosts</strong></li>
  </ul>
</div>
"""
        }
    ]
}
