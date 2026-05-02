from collections import Counter

with open("app.log", "r") as file:
    logs = file.readlines()

levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_messages = []

for log in logs:
    for level in levels:
        if log.startswith(level):
            levels[level] += 1
            if level == "ERROR":
                error_messages.append(log.replace("ERROR", "").strip())

print("\nLOG FILE ANALYSIS DASHBOARD\n")
print(f"Total Entries: {len(logs)}")
print(f"INFO Logs: {levels['INFO']}")
print(f"WARNING Logs: {levels['WARNING']}")
print(f"ERROR Logs: {levels['ERROR']}")

if error_messages:
    most_common = Counter(error_messages).most_common(1)[0][0]
    print("\nMost Frequent Error:")
    print(most_common)
