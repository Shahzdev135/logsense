from dataclasses import dataclass


@dataclass
class LogEvent:
    timestamp: int
    host: str
    source: str
    pid: int | None
    priority: int
    unit: str | None
    message: str

    @property
    def severity(self):
        levels = {
            0: "EMERGENCY",
            1: "ALERT",
            2: "CRITICAL",
            3: "ERROR",
            4: "WARNING",
            5: "NOTICE",
            6: "INFO",
            7: "DEBUG",
        }

        return levels.get(self.priority, "UNKNOWN")

    @classmethod
    def from_journal(cls, entry):
        return cls(
            timestamp=int(
                entry.get(
                    "_SOURCE_REALTIME_TIMESTAMP",
                    entry["__REALTIME_TIMESTAMP"],
                )
            ),
            host=entry.get("_HOSTNAME", "unknown"),
            source=entry.get("SYSLOG_IDENTIFIER", "unknown"),
            pid=int(entry["_PID"]) if entry.get("_PID") else None,
            priority=int(entry.get("PRIORITY", 6)),
            unit=entry.get("_SYSTEMD_UNIT"),
            message=entry.get("MESSAGE", ""),
        )
