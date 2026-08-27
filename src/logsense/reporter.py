from collections import Counter
from datetime import datetime, timezone


def summarize_findings(findings):
    return Counter(f.impact for f in findings)


def format_timestamp(timestamp):
    return datetime.fromtimestamp(
        timestamp / 1_000_000,
        tz=timezone.utc,
    ).astimezone().strftime("%Y-%m-%d %H:%M:%S")

def assess_health(findings):
    if any(f.impact == "CRITICAL" for f in findings):
        return "UNHEALTHY"

    if any(f.impact == "HIGH" for f in findings):
        return "DEGRADED"

    return "HEALTHY"

def generate_report(events, findings):
    health = assess_health(findings)
    lines = [
        "LogSense Health Report",
        "======================",
	f"Health: {health}",
        f"Events analyzed: {len(events)}",
        f"Findings: {len(findings)}",
        "",
    ]

    summary = summarize_findings(findings)

    if summary:
        lines.append("Impact Summary:")
        for impact, count in summary.items():
            lines.append(f"  {impact}: {count}")
        lines.append("")

    if findings:
        lines.append("Findings:")
        for finding in findings:
            timestamp = format_timestamp(finding.timestamp)

            lines.append(
                f"  [{timestamp}] "
                f"{finding.impact} "
                f"{finding.signature} "
                f"({finding.source})"
            )
            lines.append(f"    {finding.message}")
    else:
        lines.append("No findings detected.")

    return "\n".join(lines)
