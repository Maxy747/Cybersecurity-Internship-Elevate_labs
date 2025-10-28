# Elevate Labs - Cybersecurity Internship Portfolio

This repository contains all the completed tasks and projects for the Elevate Labs Cybersecurity Internship. It serves as a portfolio demonstrating practical, hands-on skills in network security, system hardening, vulnerability assessment, and threat analysis.

## 📌 Table of Contents

- [Tasks](#tasks)
  - [Task 1: Network Scanning (Nmap)](#task-1-network-scanning-nmap)
  - [Task 2: Phishing Email Analysis](#task-2-phishing-email-analysis)
  - [Task 3: Vulnerability Assessment (OpenVAS)](#task-3-vulnerability-assessment-openvas)
  - [Task 4: Firewall Configuration](#task-4-firewall-configuration)
  - [Task 5: Network Traffic Analysis (Wireshark)](#task-5-network-traffic-analysis-wireshark)
  - [Task 6: Password Strength Evaluation](#task-6-password-strength-evaluation)
  - [Task 7: Browser Security Audit](#task-7-browser-security-audit)
  - [Task 8: VPN Analysis](#task-8-vpn-analysis)
- [Projects](#projects)
  - [Linux Hardening Audit Tool](#linux-hardening-audit-tool)
- [Core Competencies & Tools](#core-competencies--tools)
- [Repository Structure](#repository-structure)

---

## 📋 Tasks

This section details the 8 foundational tasks completed during the internship, each focusing on a different domain of cybersecurity.

### Task Overview

| # | Task | Tools Used | Key Focus | Deliverable |
|---|------|------------|-----------|-------------|
| 1 | Network Scanning | Nmap | Network reconnaissance, port enumeration, service detection | [scan_results masked.txt](./Task%201/scan_results%20masked.txt) |
| 2 | Phishing Email Analysis | Manual Analysis | Social engineering, email forensics, threat indicators | [Report.md](./Task%202/Report.md) |
| 3 | Vulnerability Assessment | OpenVAS/Greenbone | Vulnerability scanning, CVE analysis, risk assessment | [report.md](./Task%203/report.md) |
| 4 | Firewall Configuration | Windows Defender/UFW | Network access control, security policy implementation | [Report.md](./Task%204/Report.md) |
| 5 | Network Traffic Analysis | Wireshark | Packet capture, protocol analysis, traffic inspection | [readme.md](./Task%205/readme.md) |
| 6 | Password Strength Evaluation | Manual Analysis | Password security, attack vectors, complexity analysis | [Task_6_Password_Report.md](./Task%206/Task_6_Password_Report.md) |
| 7 | Browser Security Audit | Manual Analysis | Extension security, permission analysis, attack surface reduction | [readme.md](./Task%207/readme.md) |
| 8 | VPN Analysis | ProtonVPN | Privacy tools, encryption, secure communications | [readme.md](./Task%208/readme.md) |

---

### Task 1: Network Scanning (Nmap)

**Objective:** Used **Nmap** to perform a SYN scan on a local network to identify live hosts, enumerate open ports, and determine the services running on those ports.

**Key Learnings:**
- Network reconnaissance techniques
- Service version detection
- Port state analysis

**Deliverable:** [`Task 1/scan_results masked.txt`](./Task%201/scan_results%20masked.txt)

---

### Task 2: Phishing Email Analysis

**Objective:** Analyzed a sample phishing email impersonating Netflix. The analysis identified multiple red flags, including sender address spoofing, urgent/threatening language, grammatical errors, and a suspicious link to a fake domain.

**Key Learnings:**
- Email header analysis
- Social engineering tactics identification
- URL inspection and domain verification

**Deliverable:** [`Task 2/Report.md`](./Task%202/Report.md)

---

### Task 3: Vulnerability Assessment (OpenVAS)

**Objective:** Conducted a "Full and fast" vulnerability scan on a host PC using **OpenVAS** (Greenbone Security Manager). The scan identified 82 total results, including medium-severity vulnerabilities like deprecated TLSv1.0/TLSv1.1 protocols and MSRPC service enumeration.

**Key Learnings:**
- Vulnerability scanning methodologies
- CVE identification and analysis
- Risk assessment and prioritization

**Deliverable:** [`Task 3/report.md`](./Task%203/report.md)

---

### Task 4: Firewall Configuration

**Objective:** Implemented and tested basic firewall rules on a host machine. This involved creating a new inbound rule to block all TCP traffic on port 23 (Telnet) to prevent unauthorized access.

**Key Learnings:**
- Firewall rule creation and management
- Network access control
- Security policy implementation

**Deliverable:** [`Task 4/Report.md`](./Task%204/Report.md)

---

### Task 5: Network Traffic Analysis (Wireshark)

**Objective:** Captured and analyzed live network packets using **Wireshark**. The task involved generating traffic (browsing, ping) and then filtering the capture to identify and inspect various protocols, including **DNS**, **TCP**, **ICMP**, **HTTP**, and **ARP**.

**Key Learnings:**
- Packet capture and analysis
- Protocol behavior understanding
- Network troubleshooting techniques

**Deliverable:** [`Task 5/readme.md`](./Task%205/readme.md)

---

### Task 6: Password Strength Evaluation

**Objective:** Researched password security concepts (Brute Force, Dictionary Attacks) and evaluated the strength of different passwords (e.g., `password123`, `P@sswOrd!2025`, and a passphrase). This task highlighted the importance of length, complexity, and passphrases.

**Key Learnings:**
- Password attack vectors
- Entropy and complexity analysis
- Best practices for password policies

**Deliverable:** [`Task 6/Task_6_Password_Report.md`](./Task%206/Task_6_Password_Report.md)

---

### Task 7: Browser Security Audit

**Objective:** Reviewed installed browser extensions to identify and remove suspicious or unnecessary add-ons. The audit focused on the security risks of extensions with highly invasive permissions, such as "Read and change all your data on the websites you visit."

**Key Learnings:**
- Browser extension security risks
- Permission model analysis
- Attack surface reduction

**Deliverable:** [`Task 7/readme.md`](./Task%207/readme.md)

---

### Task 8: VPN Analysis

**Objective:** Explored the role of **VPNs** in privacy and secure communication. This involved installing a VPN client (ProtonVPN), verifying the IP address change, and researching the benefits (encryption, IP masking) and limitations (speed, trust in provider) of VPNs.

**Key Learnings:**
- VPN protocols and encryption
- Privacy vs. security trade-offs
- Threat model considerations

**Deliverable:** [`Task 8/readme.md`](./Task%208/readme.md)

---

## 🚀 Projects

### Linux Hardening Audit Tool

A Python-based script designed to automatically audit the security configuration of a Linux system against common security benchmarks.

**Description:** The tool runs a series of checks by executing shell commands from within Python, capturing the output, and generating a real-time report that marks each check as `PASS` or `FAIL`. For failed checks, it provides clear recommendations for remediation.

**Features:**
- ✅ Checks restrictive file permissions for `/etc/shadow`
- ✅ Audits the SSH configuration file (`/etc/ssh/sshd_config`) for insecure settings like `PermitRootLogin`
- ✅ Verifies that a host-based firewall (UFW) is active
- ✅ Scans for insecure legacy services (e.g., `telnet`)

**Files:**
- **Report:** [`Projects/Linux Hardening Audit Tool/readme.md`](./Projects/Linux%20Hardening%20Audit%20Tool/readme.md)
- **Code:** [`Projects/Linux Hardening Audit Tool/audit_process.py`](./Projects/Linux%20Hardening%20Audit%20Tool/audit_process.py)
- **Sample Output:** [`Projects/Linux Hardening Audit Tool/Output.txt`](./Projects/Linux%20Hardening%20Audit%20Tool/Output.txt)

---

## 🛠️ Core Competencies & Tools

This internship provided practical experience with the following tools and cybersecurity domains:

### Network Security
- **Nmap** - Network scanning and reconnaissance
- **Wireshark** - Packet capture and protocol analysis
- **Firewall Configuration** - UFW (Linux), Windows Defender Firewall

### Vulnerability Management
- **OpenVAS / Greenbone Security Manager (GSM)** - Automated vulnerability scanning
- Risk assessment and prioritization

### Threat Analysis
- Phishing email analysis and indicators of compromise
- Browser extension security auditing
- Social engineering awareness

### System Security
- Linux system hardening and configuration auditing
- Password strength analysis and policy evaluation
- Principle of Least Privilege (PoLP)

### Scripting & Automation
- **Python** - System automation using subprocess module
- Security auditing scripts

### Privacy & Encryption
- **Virtual Private Networks (VPNs)** - Privacy tools and encryption

### Security Concepts
- TCP/IP networking fundamentals
- DNS, HTTP, TLS, SSH protocols
- Attack vectors: Brute Force, Dictionary Attacks
- Defense in depth strategies

---

## 📁 Repository Structure

```
.
├── Task 1/
│   └── scan_results masked.txt
├── Task 2/
│   └── Report.md
├── Task 3/
│   └── report.md
├── Task 4/
│   └── Report.md
├── Task 5/
│   └── readme.md
├── Task 6/
│   └── Task_6_Password_Report.md
├── Task 7/
│   └── readme.md
├── Task 8/
│   └── readme.md
└── Projects/
    └── Linux Hardening Audit Tool/
        ├── readme.md
        ├── audit_process.py
        └── Output.txt
```

---

## 📝 License

This repository is maintained as a portfolio project for educational purposes.

---

## 📧 Contact

For questions or collaboration opportunities, feel free to reach out through GitHub.

---

**Note:** All sensitive information, including IP addresses and system-specific details, has been masked or redacted in the deliverables to maintain security and privacy.
