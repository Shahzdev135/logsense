from src.logsense.models import Finding
from src.logsense.signatures import SIGNATURES


def matches_signature(event, signature):
    message = event.message.lower()

    return any(
        pattern.lower() in message
        for pattern in signature.patterns
    )


def detect_signatures(event):
    matches = []

    for signature in SIGNATURES:
        if matches_signature(event, signature):
            matches.append(signature)

    return matches


def analyze_events(events):
    findings = []

    for event in events:
        matches = detect_signatures(event)

        for signature in matches:
            findings.append(
                Finding(
                    signature=signature.name,
                    severity=signature.severity,
                    impact=signature.impact,
                    timestamp=event.timestamp,
                    source=event.source,
                    pid=event.pid,
                    unit=event.unit,
                    message=event.message,
                )
            )

    return findings
