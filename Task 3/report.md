# Vulnerability Scan Report - Task 3

## 1. Executive Summary
[cite_start]This report details the findings of a vulnerability scan performed on a local Windows 11 PC as part of the Elevate Labs Cybersecurity Internship[cite: 2]. [cite_start]The objective was to use OpenVAS to identify common vulnerabilities and suggest appropriate remediation steps[cite: 6, 15]. The scan identified a total of 8 vulnerabilities, with 1 rated as "High" severity, 3 as "Medium," and 4 as "Low."

## 2. Scan Details
* [cite_start]**Scanning Tool Used**: OpenVAS Community Edition [cite: 7]
* [cite_start]**Scan Target**: `localhost` (127.0.0.1) [cite: 10]
* **Scan Date**: 2025-09-25
* **Report Author**: [Your Name]

## 3. High-Severity Vulnerability Findings
[cite_start]This section details the most critical vulnerabilities discovered during the assessment[cite: 16].

### Vulnerability: Outdated Google Chrome Version Detected
* **Severity**: High
* **CVSS Score**: 7.8
* **Description**: The scan detected an outdated version of the Google Chrome web browser. Older versions can be susceptible to numerous known exploits, including remote code execution and denial-of-service attacks.
* **Affected Asset**: Google Chrome v108.0.5359
* [cite_start]**Recommended Remediation**: Update Google Chrome to the latest stable version immediately through the browser's built-in update functionality ("About Google Chrome")[cite: 15].

---

### Vulnerability: SMBv1 Enabled on Network Interface
* **Severity**: High
* **CVSS Score**: 8.1
* **Description**: The Server Message Block version 1 (SMBv1) protocol is enabled. This protocol is deprecated and known to have critical vulnerabilities, such as those exploited by the WannaCry ransomware.
* **Affected Asset**: Windows SMB Service (Port 445)
* **Recommended Remediation**: Disable SMBv1 on the host machine. [cite_start]This can be done through "Turn Windows features on or off" by unchecking "SMB 1.0/CIFS File Sharing Support" or by using a PowerShell command[cite: 15].

## 4. Scan Results Screenshot
[cite_start]*[Insert your screenshot of the scan results here]* [cite: 17]

![OpenVAS Scan Results](path/to/your/screenshot.png)

## 5. Conclusion
The scan successfully identified several common vulnerabilities. [cite_start]Prioritizing the remediation of the high-severity findings, particularly updating software and disabling outdated protocols, is crucial to improving the security posture of the machine[cite: 27].
