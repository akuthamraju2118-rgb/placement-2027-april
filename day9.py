print("--- Day 9: Dynamic Array Engine & List Manipulation ---")

servers = ["Dubai-Main", "AbuDhabi-Secondary", "Sharjah-Edge"]
print("Initial Server Array Layout:", servers)

servers.append("Ajman-Backup")
servers.sort()
print("Optimized Global Infrastructure Map:", servers)
