import subprocess
import sys

# We will keep a simple score
score = 0
total_checks = 0

print("--- 🛡️  Starting Linux Security Audit ---")

def run_command(command):
    """
    Runs a shell command, captures its output, and returns it.
    """
    try:
        # Runs the command. `capture_output=True` saves the result.
        # `text=True` makes it a readable string. `shell=True` lets us pass a simple string.
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=5)
        
        # Return the output (stdout) and any error (stderr)
        return result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return None, str(e)

print("\n--- [Check 1: /etc/shadow Permissions] ---")
total_checks += 1
# 'ls -l' shows permissions. 'grep' filters for the file.
command = "ls -l /etc/shadow"
stdout, stderr = run_command(command)

if stdout:
    print(f"Result: {stdout}")
    # Check if the permissions string starts with '-r--------' or '-rw-------'
    if stdout.startswith("-r--------") or stdout.startswith("-rw-------"):
        print("Status: ✅ PASS")
        print("Recommendation: None. Permissions are secure.")
        score += 1
    else:
        print("Status: ❌ FAIL")
        print("Recommendation: Set permissions to '400' or '600' (sudo chmod 400 /etc/shadow)")
else:
    print(f"Status: ❌ ERROR running check: {stderr}")

print("\n--- [Check 2: SSH Root Login] ---")
total_checks += 1
command = "grep '^PermitRootLogin' /etc/ssh/sshd_config"
stdout, stderr = run_command(command)

if stdout:
    print(f"Result: {stdout}")
    if stdout == "PermitRootLogin no":
        print("Status: ✅ PASS")
        print("Recommendation: None. Root login is correctly disabled.")
        score += 1
    else:
        print("Status: ❌ FAIL")
        print("Recommendation: Set 'PermitRootLogin no' in /etc/ssh/sshd_config and restart SSH.")
else:
    # If the command returns nothing, it's either not set or commented out (which is bad)
    print("Result: 'PermitRootLogin' is not explicitly set to 'no'.")
    print("Status: ❌ FAIL")
    print("Recommendation: Add 'PermitRootLogin no' to /etc/ssh/sshd_config.")
print("\n--- [Check 3: Firewall Status] ---")
total_checks += 1
command = "sudo ufw status" # This command needs sudo
stdout, stderr = run_command(command)

if "command not found" in stderr or "sudo: " in stderr:
    print("Status: ⚠️ SKIPPED (UFW not found or sudo error. Run script with 'sudo'.)")
elif stdout and "Status: active" in stdout:
    print(f"Result: {stdout.splitlines()[0]}") # Show only the first line
    print("Status: ✅ PASS")
    print("Recommendation: None. Firewall is active.")
    score += 1
else:
    print(f"Result: Status is inactive or unknown.")
    print("Status: ❌ FAIL")
    print("Recommendation: Enable the firewall (e.g., 'sudo ufw enable').")

print("\n--- [Check 4: Insecure Services (telnet)] ---")
total_checks += 1
command = "systemctl is-active telnet.socket"
stdout, stderr = run_command(command)

if stdout == "active":
    print("Result: telnet service is ACTIVE.")
    print("Status: ❌ FAIL")
    print("Recommendation: Disable and uninstall telnet (sudo systemctl stop telnet.socket).")
else:
    # It will say 'inactive' or 'unknown'
    print("Result: telnet service is not running.")
    print("Status: ✅ PASS")
    print("Recommendation: None.")
    score += 1

print("\n--- 🏁 Audit Complete ---")
print(f"Final Score: {score} / {total_checks} checks passed.")
print("--- End of Report ---")


