import builder as b
import constants as c
import sys as s
import time as t

"""
0: First argument -> main.py
1: Second argument -> number of STRAIGHT tracks
2: Third argument -> number of CURVED tracks
3: Fourth argument -> number of DIVERGENT tracks
4: Fifth argument -> number of CONVERGENT tracks
"""

# Check the number of arguments
if len(s.argv) != 5:
  print("[ERROR] Wrong number of arguments.")
  exit()

# Check the minimum of tracks
sum = 0
for i in range(1, 5):
  sum = sum + int(s.argv[i])
if not sum:
  print("[ERROR] At least one type of tracks must be nonzero.")
  exit()

# Get all the tracks
tracks = {
  c.STRAIGHT_TRACK: int(s.argv[1]),
  c.CURVED_TRACK: int(s.argv[2]),
  c.DIVERGENT_TRACK: int(s.argv[3]),
  c.CONVERGENT_TRACK: int(s.argv[4])
}

# Build a railway and measure time
real_start = t.time()
cpu_start = t.process_time()
railway = b.build(tracks)
cpu_end = t.process_time()
real_end = t.time()

print("")
print("[REAL TIME] " + str(format(real_end - real_start, ".5f")) + " s")
print("[CPU TIME] " + str(format(cpu_end - cpu_start, ".5f")) + " s")
print("")

# Show the railway
if not railway:
  print("No solution found for this set of tracks.")
else:
  for track in railway:
    print(track)

print("")
