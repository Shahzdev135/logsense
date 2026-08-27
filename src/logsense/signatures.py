from dataclasses import dataclass


@dataclass
class Signature:
    name: str
    description: str
    severity: str
    impact: str
    patterns: list[str]


KERNEL_PANIC = Signature(
    name="kernel_panic",
    description="Kernel reported a panic condition",
    severity="EMERGENCY",
    impact="CRITICAL",
    patterns=["kernel panic", "kernel panic - not syncing"],
)

KERNEL_OOM = Signature(
    name="kernel_oom",
    description="Kernel reported an out-of-memory condition",
    severity="CRITICAL",
    impact="HIGH",
    patterns=[
        "out of memory",
        "oom-killer",
        "killed process",
    ],
)

SIGNATURES = [
    KERNEL_PANIC,
    KERNEL_OOM,
]
