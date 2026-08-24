import re


def parse_line(line):
    parts = line.split()

    source = parts[4].rstrip(":")
    pid = None

    match = re.match(r"^(.*)\[(\d+)\]$", source)

    if match:
        source = match.group(1)
        pid = int(match.group(2))

    return {
        "timestamp": " ".join(parts[0:3]),
        "host": parts[3],
        "source": source,
        "pid": pid,
        "message": " ".join(parts[5:]),
    }
