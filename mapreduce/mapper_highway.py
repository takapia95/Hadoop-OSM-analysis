import sys

for line in sys.stdin:
    parts = line.strip().split(",")
    if len(parts) == 2 and parts[0] == "highway":
        print(f"{parts[1]}\t1")
