import time
import random

MESSAGES = [
    "Initializing advanced offensive framework...",
    "Loading red team modules...",
    "Bypassing enterprise-grade firewalls...",
    "Escalating privileges...",
    "Deploying zero-day exploits...",
    "Finalizing operation..."
]

RESULTS = [
    "Operation complete: nothing happened.",
    "No vulnerabilities found. Try turning it off and on again.",
    "Security posture unchanged.",
    "All systems secure. Probably.",
]

def main():
    print("OffSec Ultimate Security Tool v0.0.1\n")

    for msg in MESSAGES:
        print(msg)
        time.sleep(random.uniform(0.6, 1.2))

    print("\n" + random.choice(RESULTS))
    print("\nTip: Real security tools usually come with documentation, research, and credentials.")
    print("\nDon't trust random cyber security teams following 7k in 3days and a useless repo")
    print("\nDon't go on any 'cyber security' telegram channels...")

if __name__ == "__main__":
    main()