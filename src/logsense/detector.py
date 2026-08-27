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
