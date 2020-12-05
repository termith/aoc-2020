"""
Instead of zones or groups, this airline uses binary space partitioning to seat people.
A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127).
The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

Every seat also has a unique seat ID: multiply the row by 8, then add the column

P1. What is the highest seat ID on a boarding pass?

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

P2. What is the ID of your seat?
"""

max_id = 0
ids = []

with open('input') as f:
    for board_pass in f:
        board_pass = board_pass.strip()
        row = int(board_pass[:7].replace('F', '0').replace('B', '1'), base=2)
        seat = int(board_pass[7:].replace('L', '0').replace('R', '1'), base=2)
        seat_id = row * 8 + seat
        ids.append(seat_id)
        max_id = max(seat_id, max_id)

print(f'Max seat id is {max_id}')

ids.sort()

i = 0
j = 1
while j != len(ids):
    if ids[i] + 1 != ids[j]:
        print(f'Your seat is {ids[i] + 1}')
        break
    else:
        i += 1
        j += 1
