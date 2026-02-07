import pandas as pd
import math

MIN_X, MAX_X = 0, 10000
MIN_Y, MAX_Y = 0, 10000


def extract_coordinates(line):
    coords_text = line.strip()
    coords_text = coords_text.replace("LINESTRING", "").strip()
    coords_text = coords_text.lstrip("(").rstrip(")")

    coords = []
    for pair in coords_text.split(","):
        pair = pair.strip()
        if not pair:
            continue

        parts = pair.split()
        if len(parts) != 2:
            continue

        x, y = map(float, parts)
        coords.append((x, y))

    return coords


def road_length(coords):
    """Compute total road length"""
    length = 0.0
    for i in range(1, len(coords)):
        x1, y1 = coords[i - 1]
        x2, y2 = coords[i]
        length += math.dist((x1, y1), (x2, y2))
    return length


def check_invalid_road(coords):
    if len(coords) < 2:
        return True, "Invalid geometry (less than 2 points)"

    first_point = coords[0]
    zero_length = True

    for x, y in coords:
        if not (MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y):
            return True, "Coordinate out of range"

        if (x, y) != first_point:
            zero_length = False

    if zero_length:
        return True, "Zero-length line"

    return False, None


def main():
    records = []

    with open("streets_xgen.wkt", "r") as file:
        for index, line in enumerate(file, start=1):
            if not line.startswith("LINESTRING"):
                continue

            coords = extract_coordinates(line)
            is_invalid, reason = check_invalid_road(coords)

            length = road_length(coords) if len(coords) >= 2 else 0.0

            records.append({
                "road_id": index,
                "num_points": len(coords),
                "length": length,
                "is_valid": not is_invalid,
                "error_type": reason
            })

            if is_invalid:
                print("Invalid road geometry detected")
                print(f"Road index: {index}")
                print(f"Reason: {reason}")
                print("-" * 40)

    # ---- Data Science Part ----
    df = pd.DataFrame(records)

    print("\n===== DATA QUALITY SUMMARY =====")
    print("Total roads:", len(df))
    print("Valid roads:", df["is_valid"].sum())
    print("Invalid roads:", (~df["is_valid"]).sum())
    print("\nError distribution:")
    print(df["error_type"].value_counts(dropna=True))

    # Optional export
    df.to_csv("road_validation_report.csv", index=False)


if __name__ == "__main__":
    main()
