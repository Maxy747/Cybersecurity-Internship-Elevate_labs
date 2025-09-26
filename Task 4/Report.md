# Cybersecurity Task 4: Firewall Configuration

## Task Overview
This task involved setting up and testing basic firewall rules on a Windows/Linux operating system as part of the Elevate Labs Cybersecurity Internship. The objective was to block a specific port, test the rule, and understand the fundamentals of network traffic filtering.

## Steps Taken
1.  **Accessed the Firewall:** I used [mention Windows Defender Firewall or UFW on Linux].
2.  **Listed Existing Rules:** I checked the initial state of the firewall.
3.  **Blocked Port 23:** I created a new inbound rule to block TCP traffic on port 23 (Telnet). 
![SharedScreenshot](https://github.com/user-attachments/assets/7b4b6292-4332-4057-b7a2-7227c46e1f28)
4.  **Allowed Port 22 (Linux Only):** I added a rule to allow SSH traffic to ensure remote access was not lost. 
5.  **Verified the Rule:** I listed the active rules to confirm my new rule was in place. A screenshot of this is included in the repository.
![SharedScreenshot1](https://github.com/user-attachments/assets/af76308d-475d-4f34-af09-d0009ae7b011)
6.  **Cleaned Up:** After documenting, I removed the test rule to restore the firewall to its original state. 

## How a Firewall Filters Traffic
A firewall acts as a security guard for a computer network. It inspects all incoming and outgoing data packets and decides whether to allow them to pass or block them based on a set of pre-defined security rules. It can filter traffic based on:
* **IP Addresses:** Allowing or blocking connections from specific devices.
* **Port Numbers:** Blocking access to specific services (like Telnet on port 23 or SSH on port 22).
* **Protocols:** Filtering based on the type of traffic, like TCP, UDP, or ICMP.

This process effectively creates a barrier between a trusted internal network and an untrusted external network (like the internet), preventing unauthorized access and cyberattacks.
