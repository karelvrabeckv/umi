# Module builder

import constants as c
import math as m

railway = []

"""
Check the most important constraints
and build up the railway.
"""
def build(tracks):
  # The minimum of curved tracks must be eight
  if tracks[c.CURVED_TRACK] < 8:
    return False

  # The amount of convergent tracks must be equal to divergent
  if tracks[c.DIVERGENT_TRACK] != tracks[c.CONVERGENT_TRACK]:
    return False

  if not railroad(
    c.START_X, # Initial X coordinate
    c.START_Y, # Initial Y coordinate
    c.START_ANGLE, # Initial angle
    tracks[c.STRAIGHT_TRACK], # Number of straight tracks
    tracks[c.CURVED_TRACK], # Number of curved tracks
    tracks[c.DIVERGENT_TRACK], # Number of divergent tracks
    tracks[c.CONVERGENT_TRACK], # Number of convergent tracks
    [], # Sequence of tracks
    [], # Start points for tracks
    [(c.START_X, c.START_Y, c.START_ANGLE)], # End points for tracks
    c.CURVED_TRACK # The type of the track we want to add
  ):
    return False
  return railway

"""
Check if point Q lies on segment P–R.
"""
def on_segment(P, Q, R):
  if ((min(P[0], R[0]) <= Q[0] <= max(P[0], R[0])) and
      (min(P[1], R[1]) <= Q[1] <= max(P[1], R[1]))):
    return True
  return False

"""
Get the orientation of points P, Q and R.
"""
def get_orientation(P, Q, R):
  value = (Q[1] - P[1]) * (R[0] - Q[0]) - (Q[0] - P[0]) * (R[1] - Q[1])
  if value > 0:
    return 1 # Clockwise
  elif value < 0:
    return 2 # Counterclockwise
  else:
    return 0 # Collinear

"""
Build the railway with BRUTE FORCE.
"""
def railroad(x, y, angle, str_num, cur_num, div_num, con_num, path, starts, ends, track_to_add):
  for i, end in enumerate(ends):
    # We reached the end point
    if x == end[0] and y == end[1] and angle == end[2] and len(path):
      r_ends = [*ends]
      r_ends.pop(i)

      # Build the remaining parts of the track
      for start in starts:
        r_starts = [*starts]
        r_starts.pop(0)

        # Try adding different tracks
        return (
          railroad(start[0], start[1], start[2], str_num, cur_num, div_num, con_num, path, r_starts, r_ends, c.STRAIGHT_TRACK) or
          railroad(start[0], start[1], start[2], str_num, cur_num, div_num, con_num, path, r_starts, r_ends, c.CURVED_TRACK) or
          railroad(start[0], start[1], start[2], str_num, cur_num, div_num, con_num, path, r_starts, r_ends, c.DIVERGENT_TRACK) or
          railroad(start[0], start[1], start[2], str_num, cur_num, div_num, con_num, path, r_starts, r_ends, c.CONVERGENT_TRACK)
        )

      # We did not used all of the tracks
      if str_num or cur_num or div_num or con_num:
        return False

      global railway
      railway = [*path]
      return True

  # We are out of the tracks
  if ((track_to_add == c.STRAIGHT_TRACK and not str_num) or
      (track_to_add == c.CURVED_TRACK and not cur_num) or
      (track_to_add == c.DIVERGENT_TRACK and not div_num) or
      (track_to_add == c.CONVERGENT_TRACK and not con_num)):
    return False

  # Initialize new values
  n_x, n_y, n_angle = x, y, angle
  n_str_num, n_cur_num, n_div_num, n_con_num = str_num, cur_num, div_num, con_num
  n_path = [*path]
  n_starts = [*starts]
  n_ends = [*ends]

  # Calculate a new position and angle
  if track_to_add in {c.STRAIGHT_TRACK, c.DIVERGENT_TRACK, c.CONVERGENT_TRACK}:
    # The angle is leaved as is
    n_x += round(m.cos(angle)) * c.SIZE_OF_STRAIGHT_TRACK
    n_y += round(m.sin(angle)) * c.SIZE_OF_STRAIGHT_TRACK
  elif track_to_add == c.CURVED_TRACK:
    # The angle is reduced by 45 degrees
    n_x += (round(m.cos(angle)) or round(m.cos(angle - m.pi / 4))) * c.SIZE_OF_CURVED_TRACK
    n_y += (round(m.sin(angle)) or round(m.sin(angle - m.pi / 4))) * c.SIZE_OF_CURVED_TRACK
    n_angle = (angle - m.pi / 4) % (2 * m.pi)

  # Check the overlaps
  for track in path:
    P, Q, R, S = (x, y), (n_x, n_y), track[0], track[1]

    # Get all the necessary orientations
    O1 = get_orientation(P, Q, R)
    O2 = get_orientation(P, Q, S)
    O3 = get_orientation(R, S, P)
    O4 = get_orientation(R, S, Q)

    # Check the cases of intersection
    if (((O1 != O2) and (O3 != O4)) or
        (not O1 and on_segment(P, R, Q)) or
        (not O2 and on_segment(P, S, Q)) or
        (not O3 and on_segment(R, P, S)) or
        (not O4 and on_segment(R, Q, S))):
      # Avoid the connection of tracks
      if ((P[0] == S[0] and P[1] == S[1]) or
          (Q[0] == R[0] and Q[1] == R[1])):
        continue
      return False

  # Modify the amount of tracks and the path
  if track_to_add == c.STRAIGHT_TRACK:
    n_str_num -= 1
    n_path.append(((x, y, m.degrees(angle)), (n_x, n_y, m.degrees(n_angle)), c.STRAIGHT_TRACK))
  elif track_to_add == c.CURVED_TRACK:
    n_cur_num -= 1
    n_path.append(((x, y, m.degrees(angle)), (n_x, n_y, m.degrees(n_angle)), c.CURVED_TRACK))
  elif track_to_add == c.DIVERGENT_TRACK:
    n_div_num -= 1
    n_path.append(((x, y, m.degrees(angle)), (n_x, n_y, m.degrees(n_angle)), c.DIVERGENT_TRACK))
  elif track_to_add == c.CONVERGENT_TRACK:
    n_con_num -= 1
    n_path.append(((x, y, m.degrees(angle)), (n_x, n_y, m.degrees(n_angle)), c.CONVERGENT_TRACK))

  # Add a new start or end point
  if track_to_add == c.DIVERGENT_TRACK:
    # The second track diverges to 45 degrees
    s_x = x + (round(m.cos(angle)) or round(m.cos(angle - m.pi / 4))) * c.SIZE_OF_CURVED_TRACK
    s_y = y + (round(m.sin(angle)) or round(m.sin(angle - m.pi / 4))) * c.SIZE_OF_CURVED_TRACK
    s_angle = (angle - m.pi / 4) % (2 * m.pi)
    n_starts.append((s_x, s_y, s_angle))
  elif track_to_add == c.CONVERGENT_TRACK:
    # The second track converges from 45 degrees
    e_x = n_x + (round(m.cos(angle - m.pi)) or round(m.cos(angle - m.pi + m.pi / 4))) * c.SIZE_OF_CURVED_TRACK
    e_y = n_y + (round(m.sin(angle - m.pi)) or round(m.sin(angle - m.pi + m.pi / 4))) * c.SIZE_OF_CURVED_TRACK
    e_angle = (angle + m.pi / 4) % (2 * m.pi)
    n_ends.append((e_x, e_y, e_angle))

  # Try adding different tracks
  return (
    railroad(n_x, n_y, n_angle, n_str_num, n_cur_num, n_div_num, n_con_num, n_path, n_starts, n_ends, c.STRAIGHT_TRACK) or
    railroad(n_x, n_y, n_angle, n_str_num, n_cur_num, n_div_num, n_con_num, n_path, n_starts, n_ends, c.CURVED_TRACK) or
    railroad(n_x, n_y, n_angle, n_str_num, n_cur_num, n_div_num, n_con_num, n_path, n_starts, n_ends, c.DIVERGENT_TRACK) or
    railroad(n_x, n_y, n_angle, n_str_num, n_cur_num, n_div_num, n_con_num, n_path, n_starts, n_ends, c.CONVERGENT_TRACK)
  )
