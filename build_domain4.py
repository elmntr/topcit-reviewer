# Domain 4 data: Understanding Information Security
d4 = {
    "id": "domain4",
    "title": "Domain 4: Understanding Information Security",
    "icon": "🛡️",
    "description": "CIA Triad, modern threat landscape (APT, Ransomware, Qshing), Symmetric & Asymmetric Cryptography, Hash functions, Digital Signatures, PKI, Authentication (FIDO, MFA), Access Control (Bell-LaPadula, Biba, RBAC), Web Security (OWASP Top 10), Network Defenses (Firewalls, IDS/IPS, DMZ), and ISMS-P/ISO 27001.",
    "sections": [
        {
            "id": "sec-overview",
            "title": "1. CIA Triad & The Modern Threat Landscape",
            "badge": "Day 7 • Session 1",
            "summary": "Core pillars of information security, extended security attributes, malware classifications, APT stages, and modern social engineering attacks.",
            "content": """
<h3>1. The CIA Triad & Extended Security Pillars</h3>
<div class="card-grid">
  <div class="summary-card">
    <h4>Confidentiality (기밀성)</h4>
    <p>Ensures information is accessible only to authorized entities. Prevent unauthorized disclosures.</p>
    <p><em>Enforced by:</em> Encryption (AES, RSA), Access Controls (DAC/MAC/RBAC), data masking.</p>
  </div>
  <div class="summary-card">
    <h4>Integrity (무결성)</h4>
    <p>Guarantees data has not been altered, fabricated, or deleted by unauthorized parties.</p>
    <p><em>Enforced by:</em> Cryptographic Hash Functions (SHA-256), Digital Signatures, HMAC, Checksums.</p>
  </div>
  <div class="summary-card">
    <h4>Availability (가용성)</h4>
    <p>Ensures systems and data are reliably accessible to authorized users when needed.</p>
    <p><em>Enforced by:</em> Redundant servers (HA), RAID, UPS, Disaster Recovery (DR), DDoS mitigation.</p>
  </div>
  <div class="summary-card">
    <h4>Authenticity & Non-Repudiation</h4>
    <p><strong>Authenticity (인증성):</strong> Verifying the genuine identity of communicating entities.</p>
    <p><strong>Non-Repudiation (부인방지):</strong> Proving that an action or message originated from a specific party such that they cannot deny having sent it. (Enforced by <em>Digital Signatures & PKI</em>).</p>
  </div>
</div>

<h3>2. Malware & Modern Cyber Threat Taxonomy</h3>
<table class="data-table">
  <thead>
    <tr><th>Threat Type</th><th>Propagation & Execution Mechanism</th><th>Distinguishing Trait</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Virus (바이러스)</strong></td><td>Attaches malicious code to an existing legitimate executable host file. Requires user execution to run and replicate.</td><td>Parasitic; cannot run independently without host.</td></tr>
    <tr><td><strong>Worm (웜)</strong></td><td>Self-replicating program that propagates autonomously across network vulnerabilities without needing a host program or human action.</td><td>Autonomous network spreading (consumes bandwidth).</td></tr>
    <tr><td><strong>Trojan Horse (트로이 목마)</strong></td><td>Disguises itself as legitimate, desirable software (utility, game) while concealing malicious payload.</td><td>Does not replicate; relies on deceit for installation.</td></tr>
    <tr><td><strong>Ransomware (랜섬웨어)</strong></td><td>Encrypts user documents and system files using asymmetric/symmetric ciphers; demands cryptocurrency ransom for decryption key.</td><td>Financial extortion via cryptographic denial of data.</td></tr>
    <tr><td><strong>Fileless Malware (파일리스 공격)</strong></td><td>Executes malicious code directly in volatile RAM using legitimate native OS administrative tools (PowerShell, WMI). No files written to disk.</td><td>Evades traditional signature-based disk antivirus.</td></tr>
    <tr><td><strong>Cryptojacking (크립토재킹)</strong></td><td>Silently hijacks the victim's CPU/GPU computing resources to mine cryptocurrency without authorization.</td><td>Causes hardware overheating and high electricity usage.</td></tr>
  </tbody>
</table>

<h3>3. Advanced Social Engineering Attacks</h3>
<ul>
  <li><strong>APT (Advanced Persistent Threat):</strong> Long-term, sophisticated, multi-stage cyber campaign targeted against a specific organization by state-sponsored or organized groups.
    <ul>
      <li><em>Stages:</em> Reconnaissance &rarr; Initial Intrusion (Spear Phishing) &rarr; Lateral Movement &rarr; Privilege Escalation &rarr; Persistent Backdoor &rarr; Data Exfiltration.</li>
    </ul>
  </li>
  <li><strong>Pharming (파밍):</strong> Modifies local DNS hosts file or compromises DNS servers to silently redirect users to fraudulent clone websites, even when the user types the exact correct URL.</li>
  <li><strong>Smishing & Vishing:</strong> SMS-based phishing links (Smishing) or phone voice impersonation (Vishing).</li>
  <li><strong>Qshing (큐싱):</strong> QR code phishing. Malicious QR codes placed on physical surfaces (e-scooters, posters) that redirect scanning smartphones to malware download sites or credential harvesters.</li>
</ul>
"""
        },
        {
            "id": "sec-symmetric",
            "title": "2. Symmetric Cryptography & Block Cipher Modes",
            "badge": "Day 7 • Session 2",
            "summary": "Secret-key cryptography mechanisms, key count formula, block vs stream ciphers, DES, AES, Korean national ciphers, and block cipher operational modes.",
            "content": """
<h3>1. Symmetric Key Cryptography (대칭키 암호)</h3>
<p>Uses the <strong>same secret key</strong> for both encryption and decryption.</p>
<ul>
  <li><strong>Pros:</strong> Extremely high computational throughput; ideal for encrypting large volumes of bulk data.</li>
  <li><strong>Cons:</strong> Secret Key Distribution Problem (how to securely share the key across an untrusted network); Scalability issue.</li>
</ul>

<div class="note-box alert-info">
  <strong>Key Count Formula for Symmetric Systems:</strong>
  <p>To enable secure pairwise communication among <em>N</em> users:</p>
  <pre class="code-block">Total Symmetric Keys = N &times; (N - 1) / 2</pre>
  <p><em>Example:</em> For 100 users: <code>100 &times; 99 / 2 = 4,950 keys</code>.</p>
</div>

<h3>2. Major Symmetric Block Ciphers</h3>
<table class="data-table">
  <thead>
    <tr><th>Cipher</th><th>Origin</th><th>Block Size</th><th>Key Lengths</th><th>Structure & Status</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>DES</strong></td><td>IBM / NIST (1977)</td><td>64 bits</td><td>56 bits (effective)</td><td>16-round Feistel network. Broken; vulnerable to brute-force.</td></tr>
    <tr><td><strong>3DES (Triple-DES)</strong></td><td>NIST</td><td>64 bits</td><td>112 or 168 bits</td><td>Applies DES 3 times: Encrypt-Decrypt-Encrypt (EDE). Deprecated due to small 64-bit block size.</td></tr>
    <tr><td><strong>AES (Advanced Encryption Standard)</strong></td><td>Rijndael / NIST (2001)</td><td>128 bits</td><td>128, 192, or 256 bits</td><td>Substitution-Permutation Network (SPN). Global gold standard. Fast and unbreakable.</td></tr>
    <tr><td><strong>SEED</strong></td><td>KISA (South Korea, 1998)</td><td>128 bits</td><td>128 bits</td><td>16-round Feistel. Korean national standard.</td></tr>
    <tr><td><strong>ARIA</strong></td><td>South Korea (2004)</td><td>128 bits</td><td>128, 192, 256 bits</td><td>SPN structure. Lightweight, optimized for smart cards and IoT.</td></tr>
    <tr><td><strong>LEA</strong></td><td>NSRI (South Korea, 2013)</td><td>128 bits</td><td>128, 192, 256 bits</td><td>Lightweight Encryption Algorithm. Extremely fast on 32-bit embedded platforms.</td></tr>
  </tbody>
</table>

<h3>3. Block Cipher Modes of Operation</h3>
<table class="data-table">
  <thead>
    <tr><th>Mode</th><th>Operation Mechanism</th><th>Security & Characteristics</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>ECB (Electronic Codebook)</strong></td><td>Each plaintext block is encrypted independently with the key.</td><td><strong>INSECURE:</strong> Identical plaintext blocks produce identical ciphertext blocks, preserving visual data patterns (e.g., ECB penguin). Never use for bulk data.</td></tr>
    <tr><td><strong>CBC (Cipher Block Chaining)</strong></td><td>Each plaintext block is XORed with the preceding ciphertext block before encryption. First block XORed with an <strong>Initialization Vector (IV)</strong>.</td><td>Secure. Hides patterns. Sequential (cannot parallelize encryption). Transmission error in one block affects two blocks during decryption.</td></tr>
    <tr><td><strong>CTR (Counter Mode)</strong></td><td>Encrypts successive values of a counter to generate a keystream, which is XORed with plaintext.</td><td>Turns block cipher into stream cipher. Highly parallelizable in hardware, supports random access.</td></tr>
  </tbody>
</table>
"""
        },
        {
            "id": "sec-asymmetric",
            "title": "3. Asymmetric Cryptography, Hash Functions & PKI",
            "badge": "Day 7 • Session 3",
            "summary": "Public-key cryptography principles, RSA vs ECC, cryptographic hash functions, digital signature workflows, and X.509 PKI architecture.",
            "content": """
<h3>1. Asymmetric Key Cryptography (비대칭키 / 공개키 암호)</h3>
<p>Uses a mathematically paired key set: a <strong>Public Key (공개키)</strong> (freely shared) and a <strong>Private Key (개인키)</strong> (kept strictly secret).</p>
<ul>
  <li><strong>Key Count:</strong> For <em>N</em> users, only <strong>2N keys</strong> are required.</li>
  <li><strong>Two Primary Operational Modes:</strong>
    <ul>
      <li><strong>Confidentiality (Encryption):</strong> Sender encrypts with <em>Receiver's Public Key</em>. Only the <em>Receiver's Private Key</em> can decrypt.</li>
      <li><strong>Authentication & Non-Repudiation (Digital Signature):</strong> Sender encrypts/signs hash with <em>Sender's Private Key</em>. Anyone can verify using the <em>Sender's Public Key</em>.</li>
    </ul>
  </li>
</ul>

<h4>Major Asymmetric Algorithms:</h4>
<ul>
  <li><strong>RSA (Rivest-Shamir-Adleman):</strong> Security based on the extreme computational difficulty of <strong>factoring large prime numbers</strong>. (Standard key length: 2048 to 4096 bits).</li>
  <li><strong>ECC (Elliptic Curve Cryptography):</strong> Security based on the <strong>Elliptic Curve Discrete Logarithm Problem (ECDLP)</strong>.
    <ul>
      <li><em>Key Advantage:</em> Equivalent security with drastically smaller key sizes (e.g., <strong>256-bit ECC &approx; 3072-bit RSA</strong>). Faster computation, lower power consumption, ideal for mobile devices and smart cards.</li>
    </ul>
  </li>
  <li><strong>Diffie-Hellman (DH):</strong> Key exchange protocol enabling two parties to establish a shared secret key over an insecure channel without transmitting the key itself.</li>
</ul>

<h3>2. Cryptographic Hash Functions & Digital Signatures</h3>
<div class="note-box alert-info">
  <strong>Three Critical Properties of Cryptographic Hash Functions:</strong>
  <ol>
    <li><strong>Pre-image Resistance (One-Way):</strong> Given hash value <code>h</code>, it is computationally infeasible to find input <code>x</code> such that <code>H(x) = h</code>.</li>
    <li><strong>Second Pre-image Resistance (Weak Collision Resistance):</strong> Given input <code>x</code>, it is infeasible to find a different input <code>y &ne; x</code> such that <code>H(x) = H(y)</code>.</li>
    <li><strong>Collision Resistance (Strong Collision Resistance):</strong> Infeasible to find ANY two distinct inputs <code>x</code> and <code>y</code> such that <code>H(x) = H(y)</code>.</li>
  </ol>
</div>

<h4>Digital Signature Workflow:</h4>
<pre class="code-block">
[Sender] Message --(Hash)--> Digest --(Encrypt with Sender Private Key)--> Signature
                                                                               |
[Network Transmission: Message + Signature] -----------------------------------+
                                                                               |
[Receiver]
   1. Message --(Hash)--> Calculated Digest
   2. Signature --(Decrypt with Sender Public Key)--> Decrypted Digest
   3. Compare: Calculated Digest == Decrypted Digest ? 
      --> If MATCH: Guaranteed Integrity, Authenticity, and Non-Repudiation!
</pre>

<h3>3. Public Key Infrastructure (PKI - 공개키 기반 구조)</h3>
<ul>
  <li><strong>CA (Certificate Authority / 인증기관):</strong> Trusted third party that issues, signs, and manages digital certificates bound to entities (e.g., KICA, VeriSign).</li>
  <li><strong>RA (Registration Authority / 등록기관):</strong> Verifies user identity during certificate application before passing request to CA.</li>
  <li><strong>CRL (Certificate Revocation List):</strong> Periodic list published by CA listing compromised or revoked certificates before their expiry.</li>
  <li><strong>OCSP (Online Certificate Status Protocol):</strong> Real-time network protocol for checking certificate revocation status instantaneously.</li>
  <li><strong>X.509 Standard:</strong> Universal format for digital certificates (Issuer, Subject, Public Key, Validity Period, CA Signature).</li>
</ul>
"""
        },
        {
            "id": "sec-access-control",
            "title": "4. Authentication Technologies & Access Control Models",
            "badge": "Day 8 • Session 1",
            "summary": "Multi-factor authentication, FIDO passwordless standards, DAC vs MAC vs RBAC, and Bell-LaPadula vs Biba formal security models.",
            "content": """
<h3>1. Authentication Factors (MFA)</h3>
<p>Authentication verifies claiming identity based on four fundamental categories:</p>
<ul>
  <li><strong>Something you know (지식 기반):</strong> Passwords, PINs, security questions. (Susceptible to guessing, shoulder surfing).</li>
  <li><strong>Something you have (소유 기반):</strong> Smart cards, physical OTP tokens, SMS codes, smartphones. (Can be lost or stolen).</li>
  <li><strong>Something you are (생체 기반):</strong> Fingerprints, iris scans, facial recognition, voice patterns. (Cannot be changed if compromised).</li>
  <li><strong>Somewhere you are (위치 기반):</strong> GPS coordinates, corporate IP subnets.</li>
</ul>
<div class="note-box alert-warning">
  <strong>MFA Definition:</strong> Requiring two or more <em>DIFFERENT categories</em> of factors (e.g., Password + OTP token). Using two passwords is NOT multi-factor authentication.
</div>

<h4>FIDO (Fast ID Online):</h4>
<p>An open standard for passwordless authentication. Private key never leaves the secure enclave (TPM) on the user's local device; user unlocks private key locally via biometrics, and the device signs a cryptographic challenge to authenticate with the server.</p>

<h3>2. Access Control Policies</h3>
<table class="data-table">
  <thead>
    <tr><th>Policy</th><th>Full Name</th><th>Decision Authority</th><th>Implementation</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>DAC</strong></td><td>Discretionary Access Control (임의적 접근 통제)</td><td><strong>Resource Owner</strong> determines permissions at their discretion.</td><td>Access Control Lists (ACLs), Unix file permissions (<code>chmod 755</code>).</td></tr>
    <tr><td><strong>MAC</strong></td><td>Mandatory Access Control (강제적 접근 통제)</td><td><strong>Central System Policy</strong> based on security classifications (Top Secret, Secret, Unclassified) and user clearances.</td><td>Multi-level military systems, SELinux.</td></tr>
    <tr><td><strong>RBAC</strong></td><td>Role-Based Access Control (역할 기반 접근 통제)</td><td>Permissions assigned to <strong>Roles</strong>; users assigned to roles based on organizational responsibilities.</td><td>Enterprise ERP, corporate IT systems (Separation of Duties, Least Privilege).</td></tr>
  </tbody>
</table>

<h3>3. Formal Security Models: Bell-LaPadula vs Biba</h3>
<div class="table-responsive">
  <table class="data-table">
    <thead>
      <tr><th>Model</th><th>Primary Focus</th><th>Simple Security Property (Read)</th><th>*-Property / Star Property (Write)</th><th>Mnemonic</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Bell-LaPadula (BLP)</strong></td><td><strong>Confidentiality (기밀성)</strong><br>(Military / Government)</td><td><strong>No Read Up (NRU):</strong> A subject at a lower clearance cannot read data at a higher classification level.</td><td><strong>No Write Down (NWD):</strong> A subject at a higher clearance cannot write data to a lower classification level (prevents leaking secrets).</td><td><em>"Read Down, Write Up"</em></td></tr>
      <tr><td><strong>Biba Model</strong></td><td><strong>Integrity (무결성)</strong><br>(Commercial / Financial)</td><td><strong>No Read Down (NRD):</strong> A subject cannot read data of lower integrity level (prevents contaminating high-integrity analysis with dirty data).</td><td><strong>No Write Up (NWU):</strong> A subject cannot write or alter data at a higher integrity level.</td><td><em>"Read Up, Write Down"</em></td></tr>
    </tbody>
  </table>
</div>
"""
        },
        {
            "id": "sec-web-network",
            "title": "5. Web Security, OWASP Top 10 & Network Defenses",
            "badge": "Day 8 • Session 2",
            "summary": "Mechanisms and defenses for SQL Injection, XSS, CSRF, Buffer Overflow, Firewalls, IDS/IPS, and security zones (DMZ).",
            "content": """
<h3>1. Web Application Attacks (OWASP Top 10)</h3>

<h4>A) SQL Injection (SQL 삽입)</h4>
<ul>
  <li><strong>Vulnerability:</strong> Unsanitized user input is concatenated directly into SQL command strings, allowing attackers to manipulate query logic (e.g., entering <code>' OR '1'='1</code>).</li>
  <li><strong>Impact:</strong> Unauthorized authentication bypass, data theft, arbitrary database alteration or destruction.</li>
  <li><strong>Defenses:</strong>
    <ol>
      <li><strong>Prepared Statements / Parameterized Queries:</strong> Enforces strict separation between code and data. Database pre-compiles SQL template and treats inputs strictly as parameter literals.</li>
      <li>Use modern Object-Relational Mappers (ORM).</li>
      <li>Strict input validation with allow-lists.</li>
    </ol>
  </li>
</ul>

<h4>B) Cross-Site Scripting (XSS)</h4>
<ul>
  <li><strong>Vulnerability:</strong> Web application reflects un-escaped malicious client-side JavaScript into the victim's browser.</li>
  <li><strong>Types:</strong>
    <ul>
      <li><em>Stored XSS:</em> Malicious script is permanently saved in the database (e.g., comment board) and served to all subsequent visitors.</li>
      <li><em>Reflected XSS:</em> Script payload is carried within URL request parameters and reflected back immediately in search results or error pages.</li>
      <li><em>DOM-based XSS:</em> Client-side script manipulates the DOM tree insecurely without server round-trip.</li>
    </ul>
  </li>
  <li><strong>Defenses:</strong> Context-aware HTML entity encoding (converting <code>&lt;</code> to <code>&amp;lt;</code>), Content Security Policy (CSP), setting <code>HttpOnly</code> flag on sensitive session cookies.</li>
</ul>

<h4>C) Cross-Site Request Forgery (CSRF)</h4>
<ul>
  <li><strong>Vulnerability:</strong> Tricking an authenticated user's browser into transmitting unauthorized HTTP requests to a target site where the user is logged in.</li>
  <li><strong>Defenses:</strong> Unique unpredictable <strong>Anti-CSRF Tokens</strong> validated on the server for state-changing requests; setting cookie <code>SameSite=Strict</code> or <code>SameSite=Lax</code>.</li>
</ul>

<h3>2. Network Security Architecture & Devices</h3>
<table class="data-table">
  <thead>
    <tr><th>Device / Architecture</th><th>OSI Layer</th><th>Operating Mechanism</th><th>Key Characteristics</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Packet Filtering Firewall</strong></td><td>L3 (Network) & L4 (Transport)</td><td>Inspects packet headers against rule base (Source/Dest IP, Port, Protocol).</td><td>Stateless. High speed; cannot inspect payload or track connection states.</td></tr>
    <tr><td><strong>Stateful Inspection Firewall</strong></td><td>L3 to L5</td><td>Tracks TCP handshake and connection state in a dynamic <em>State Table</em>.</td><td>Blocks out-of-sequence packets; superior security over basic packet filtering.</td></tr>
    <tr><td><strong>WAF (Web Application Firewall)</strong></td><td>L7 (Application)</td><td>Deep packet inspection of HTTP/HTTPS payload for application-layer attacks.</td><td>Defends against SQLi, XSS, CSRF, directory traversal.</td></tr>
    <tr><td><strong>IDS vs IPS</strong></td><td>L3 to L7</td><td><strong>IDS:</strong> Passively monitors traffic and alerts on threats.<br><strong>IPS:</strong> In-line active inspection that drops malicious packets automatically.</td><td>Detection modes: <em>Signature-based (Misuse)</em> vs <em>Anomaly-based (Heuristic)</em>.</td></tr>
    <tr><td><strong>DMZ (Demilitarized Zone)</strong></td><td>Perimeter Network</td><td>Isolated buffer subnet positioned between untrusted Internet and trusted internal Intranet.</td><td>Hosts public-facing servers (Web, Mail, DNS, Proxy). If DMZ is breached, internal database network remains protected behind an inner firewall.</td></tr>
    <tr><td><strong>VPN (Virtual Private Network)</strong></td><td>L3 (IPSec) / L4 (SSL/TLS)</td><td>Establishes encrypted tunnel over public internet.</td><td>IPSec Tunnel Mode encrypts both original IP header and payload with a new IP header.</td></tr>
  </tbody>
</table>
"""
        }
    ]
}
