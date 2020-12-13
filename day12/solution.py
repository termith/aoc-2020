with open('input') as f:
    instructions = f.readlines()

DIRECTIONS = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, 1),
    'S': (0, -1)
}

ROTATIONS = ['E', 'S', 'W', 'N']


def part_1():
    current_position = [0, 0]
    current_direction = 0
    for line in instructions:
        instruction = line[0]
        value = int(line[1:])
        if instruction in ROTATIONS:
            d = DIRECTIONS[instruction]
            current_position[0] += d[0] * value
            current_position[1] += d[1] * value
        elif instruction == 'F':
            d = DIRECTIONS[ROTATIONS[current_direction]]
            current_position[0] += d[0] * value
            current_position[1] += d[1] * value
        else:
            rotation_value = value // 90
            rotation_value = rotation_value * -1 if instruction == 'L' else rotation_value
            current_direction = (current_direction + rotation_value) % len(ROTATIONS)

    print(current_position)


part_1()


def part_2():
    ship_position = [0, 0]
    waypoint_position = [10, 1]
    for line in instructions:
        instruction = line[0]
        value = int(line[1:])
        if instruction in ROTATIONS:
            d = DIRECTIONS[instruction]
            waypoint_position[0] += d[0] * value
            waypoint_position[1] += d[1] * value
        elif instruction == 'F':
            ship_position[0] += value * waypoint_position[0]
            ship_position[1] += value * waypoint_position[1]
        else:
            rotation_value = value // 90
            for _ in range(rotation_value):
                if instruction == 'L':
                    tmp = waypoint_position[0]
                    waypoint_position[0] = -1 * waypoint_position[1]
                    waypoint_position[1] = tmp
                else:
                    tmp = waypoint_position[0]
                    waypoint_position[0] = waypoint_position[1]
                    waypoint_position[1] = -1 * tmp
    print(ship_position)
    print(abs(ship_position[0]) + abs(ship_position[1]))


part_2()
