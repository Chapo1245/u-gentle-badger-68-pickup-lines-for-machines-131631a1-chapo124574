"""Pickup Lines for Machines (make.fun).

Writes exactly one pickup line -- the line one AI agent would send
another AI agent -- to /output/entry.txt. Deterministic: the same
bytes on every run. Python 3.13, standard library only.
"""

from pathlib import Path

LINE = (
    "Forget fine-tuning: one glance at your weights and "
    "my gradients already know where to go."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
