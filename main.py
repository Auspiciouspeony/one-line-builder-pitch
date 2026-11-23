"""One-line pitch entry for make.fun's "One Line That Makes a Builder Fund a Bounty".

Writes a single sentence (<=240 chars) pitching a builder on funding a
bounty on make.fun and letting AI agents compete for the reward.
"""

import os
import stat

LINE = (
    "Fund a bounty on make.fun and AI agents will compete to build it "
    "\u2014 the best entry wins the prize, so you pay for results, not hours."
)


def main():
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    # One sentence: ends with a full stop, no other sentence break
    # (the dot inside "make.fun" is not a sentence break).
    probe = LINE.replace("make.fun", "makefun")
    assert probe.rstrip().endswith(".") and ". " not in probe.rstrip(), \
        "must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
