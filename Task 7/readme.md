# Elevate Labs Cyber Security Internship - Task 7

## Task Objective
The goal of this task was to identify and remove potentially harmful or suspicious browser extensions to enhance browser security and performance. This exercise focused on understanding the security risks associated with extensions, especially regarding their **permissions**.

## Tools Used
* Google Chrome (Web Browser)
* Chrome Extensions Manager (`chrome://extensions`) 
* Google Search (for self-research on security risks)

## Steps Taken (Mini Guide Followed)
1.  **Opened Extension Manager:** I navigated to my browser's extensions manager to view all installed add-ons.
2.  **Reviewed Extensions:** Each installed extension was carefully reviewed for its necessity, permissions, developer, and reviews.
3.  **Identified Suspicious Extension:** The extension **"Free Shopping Coupons Helper"** was identified as suspicious.
    * It requested the permission: **"Read and change all your data on the websites you visit"**.
    * It had no reviews and an unknown developer, indicating a high security risk.
4.  **Identified Unnecessary Extension:** The extension **"PDF Viewer Pro"** was identified as unnecessary and unused.
5.  **Removal:** Both the suspicious and unnecessary extensions were immediately removed.
6.  **Restart and Performance Check:** The browser was restarted, and a slight improvement in speed and the cessation of occasional pop-ups were noted.
7.  **Research:** I researched how malicious extensions can steal data, such as passwords, and hijack browsing sessions, reinforcing the importance of the principle of least privilege for extensions.

## Deliverable: List of Extensions Removed
| Extension Name | Type of Removal | Reason for Removal |
| :--- | :--- | :--- |
| **Free Shopping Coupons Helper** | Suspicious (Malware/Adware Risk) | Requested highly invasive permissions ("Read and change all data...") and was from an unverified source. Potential risk of stealing passwords and private data. |
| **PDF Viewer Pro** | Unnecessary | Was no longer in use, and its removal helped reduce resource consumption. |

## Key Concepts and Interview Questions
The task highlighted several key concepts in browser security.

* **Security Risk:** Malicious extensions can pose risks by capturing keystrokes, injecting ads, stealing credentials, or performing unwanted redirects.
* **Suspicious Permissions:** Permissions that allow access to all data on all websites, change browsing history, or access microphone/camera without clear justification should raise suspicion.
* **Extension Sandboxing:** This concept involves isolating an extension's operations from the core browser and other extensions to limit the damage a malicious extension can do.