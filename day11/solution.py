with open('input') as f:
    seats = list(map(lambda s: s.strip(), f.readlines()))


def calculate_changes_p1(seats):
    changed = list()
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == '.':
                continue
            elif seats[i][j] == 'L':
                if i - 1 >= 0:
                    if '#' in seats[i - 1][max(j - 1, 0):min(j + 1, len(seats[i]) - 1) + 1]:
                        continue
                if '#' in seats[i][max(j - 1, 0):min(j + 1, len(seats[i]) - 1) + 1]:
                    continue
                if i + 1 != len(seats):
                    if '#' in seats[i + 1][max(j - 1, 0):min(j + 1, len(seats[i]) - 1) + 1]:
                        continue
                changed.append((i, j))
            else:
                occupied_seats = 0
                if i - 1 >= 0:
                    occupied_seats += seats[i - 1][max(j - 1, 0):min(j + 1, len(seats[i]) - 1) + 1].count('#')
                occupied_seats += seats[i][max(j - 1, 0):min(j + 1, len(seats[i]) - 1) + 1].count('#') - 1
                if i + 1 != len(seats[i]):
                    occupied_seats += seats[i + 1][max(j - 1, 0):min(j + 1, len(seats[i]) - 1) + 1].count('#')
                if occupied_seats >= 4:
                    changed.append((i, j))
    return changed


def calculate_changes_p2(seats):
    DIRECTIONS = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1)]
    changed = list()
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == '.':
                continue
            elif seats[i][j] == 'L':
                found_x = False
                for d in DIRECTIONS:
                    current_index = [i + d[0], j + d[1]]
                    while (0 <= current_index[0] < len(seats) and 0 <= current_index[1] < len(
                            seats[i])) and not found_x:
                        current_value = seats[current_index[0]][current_index[1]]
                        if current_value == '#':
                            found_x = True
                            break
                        elif current_value == 'L':
                            break
                        else:
                            current_index[0] += d[0]
                            current_index[1] += d[1]
                    if found_x:
                        break
                else:
                    changed.append((i, j))
            else:
                count = 0
                for d in DIRECTIONS:
                    found = False
                    current_index = [i + d[0], j + d[1]]
                    while (0 <= current_index[0] < len(seats) and 0 <= current_index[1] < len(seats[i])) and not found:
                        current_value = seats[current_index[0]][current_index[1]]
                        if current_value == '#':
                            count += 1
                            found = True
                        elif current_value == 'L':
                            found = True
                        else:
                            current_index[0] += d[0]
                            current_index[1] += d[1]
                    if count >= 5:
                        changed.append((i, j))
                        break
    return changed


def change(seats, changes):
    for ij in changes:
        l = list(seats[ij[0]])
        l[ij[1]] = 'L' if l[ij[1]] == '#' else '#'
        seats[ij[0]] = ''.join(l)
    return seats


def solution(seats, calculate_changes):
    while True:
        changes = calculate_changes(seats)
        if not changes:
            cnt = 0
            for i in seats:
                cnt += i.count('#')
            return cnt
        else:
            seats = change(seats, changes)


# print(solution(seats, calculate_changes_p1))


print(solution(seats, calculate_changes_p2))
