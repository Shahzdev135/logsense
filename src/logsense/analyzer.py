from collections import Counter


def count_severities(events):
    return Counter(event.severity for event in events)


def count_by_source(events):
    return Counter(event.source for event in events)


def count_by_source_and_severity(events):
    return Counter(
        (event.source, event.severity)
        for event in events
    )


def print_source_severity_report(events):
    counts = count_by_source_and_severity(events)

    for (source, severity), count in counts.most_common():
        print(f"{source:20} {severity:10} {count}")

def find_problematic_events(events):
    return [
        event
        for event in events
        if event.priority <= 4
    ]

def count_messages(events):
    return Counter(event.message for event in events)
