#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry (u-golden-heron-44-fortune-in-a-pot-ded981e9)"""
import os

ENTRY_LINE = "You will grow toward the light, the light will move, and you will call that a journey. The pot holds."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
