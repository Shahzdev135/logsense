import json
import subprocess

from .models import LogEvent


def read_raw_journal(limit=10):
    result = subprocess.run(
        ["journalctl", "--no-pager", "-n", str(limit), "-o", "json"],
        capture_output=True,
        text=True,
        check=True,
    )

    return [json.loads(line) for line in result.stdout.splitlines()]


def read_journal(limit=10):
    return [
        LogEvent.from_journal(entry)
        for entry in read_raw_journal(limit)
    ]
