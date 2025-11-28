#!/usr/bin/python3
"""
Log parsing and statistics accumulation
"""

import sys


def print_stats(total_size, status_code_counts):
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))


def main():
    """Parses log lines from standard input and accumulates statistics."""
    total_size = 0
    status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            try:
                status_code = int(parts[8])
                file_size = int(parts[9])
            except (ValueError, IndexError):
                continue

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            total_size += file_size

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_code_counts)


if __name__ == "__main__":
    main()
