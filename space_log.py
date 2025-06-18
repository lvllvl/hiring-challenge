#!/usr/bin/env python3

def clean_field(field):
    return field.strip()  # remove leading/trailing spaces

def parse_line(line):
    return [clean_field(field) for field in line.split('|')]

max_duration = -1
best_code = None

with open("space_missions.log", "r") as file:
    for line in file:
        line = line.strip()

        # Skip comments or blank lines
        if not line or line.startswith("#"):
            continue

        fields = parse_line(line)

        if len(fields) < 8:
            continue  # Skip incomplete/invalid lines

        destination = fields[2]
        status = fields[3]
        try:
            duration = int(fields[5])  # may throw error if not a number
        except ValueError:
            continue

        if destination == "Mars" and status == "Completed":
            if duration > max_duration:
                max_duration = duration
                best_code = fields[7]

# Print final result
if best_code:
    print(best_code)
