#! /usr/bin/env python

import os

TEAMS_DIR = "."

alls = [x.strip() for x in open(os.path.join(TEAMS_DIR, "students.txt")).readlines()]
allocd = set()
for tl in os.listdir(TEAMS_DIR):
    if not tl.startswith("team_"):
        continue
    mems = [x.strip() for x in open(os.path.join(TEAMS_DIR, tl, "members.txt")).readlines()]
    for m in mems:
        if m in allocd:
            print("Warning: %s appears in multiple teams" % m)
        if m not in alls:
            print("Warning: %s not in student records" % m)
        allocd.add(m)

print("\nUnallocated students:")
for m in alls:
    if m not in allocd:
        print(m)
