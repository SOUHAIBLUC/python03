#!/usr/bin/env


import math


def calculate_distance(point1: tuple[float, float, float],
                       point2: tuple[float, float, float]) -> float:

    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return distance


def parse_coordinates(coord_string: str) -> tuple[int, int, int]:

    parts = coord_string.split(',')

    if len(parts) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(parts)}")

    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        return (x, y, z)

    except ValueError as e:
        raise ValueError(f"Invalid coordinate format: {e}")


def main() -> None:
    """
    Main function demonstrating tuple operations and 3D coordinates.
    """
    print("=== Game Coordinate System ===")

    position1 = (10, 20, 5)
    print(f"Position created: {position1}")

    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, position1)

    print(f"Distance between {origin} and {position1}: {dist1:.2f}")

    print()
    coord_string = "3,4,0"
    print(f'Parsing coordinates: "{coord_string}"')

    try:

        position2 = parse_coordinates(coord_string)
        print(f"Parsed position: {position2}")

        dist2 = calculate_distance(origin, position2)
        print(f"Distance between {origin} and {position2}: {dist2}")

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    print()
    invalid_string = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_string}"')

    try:
        bad_position = parse_coordinates(invalid_string)
        print(f"Parsed position: {bad_position}")

    except ValueError as e:

        print(f"Error parsing coordinates: {e}")

        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print()
    print("Unpacking demonstration:")
    sample_pos = (3, 4, 0)

    x, y, z = sample_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
