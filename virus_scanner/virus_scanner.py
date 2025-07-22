import os

# 🧬 Sample virus signatures (You can add more)
virus_signatures = [
    "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!",
    "<script>evil_script()</script>",
    "malicious_code",
    "trojan_attack()",
    "virus_detected"
]

def scan_file(file_path):
    try:
        with open(file_path, 'r', errors="ignore") as file:
            content = file.read()
            for signature in virus_signatures:
                if signature in content:
                    return True, signature
    except:
        return False, "Unreadable file"
    return False, ""

def scan_directory(directory):
    infected_files = []
    for root, _, files in os.walk(directory):
        for fname in files:
            full_path = os.path.join(root, fname)
            infected, signature = scan_file(full_path)
            if infected:
                infected_files.append((full_path, signature))
    return infected_files

# ---------- MAIN ----------
if __name__ == "__main__":
    folder = input("Enter directory path to scan: ")
    results = scan_directory(folder)

    if results:
        print("⚠️ Infected files found:")
        for path, sig in results:
            print(f" - {path} [Signature: {sig}]")
    else:
        print("✅ No infected files found.")
