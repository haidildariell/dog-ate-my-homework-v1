"""Dog Ate My Homework — funniest excuse entry.

Writes a single one-line dog excuse to /output/entry.txt.
The line is the dog's own voice: caught eating the homework,
convinced it did nothing wrong.
"""

import os

ENTRY_LINE = "You said sit. You said stay. Nobody said don't eat the homework. I followed orders."

OUTPUT_PATH = "/output/entry.txt"

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_line(line):
    """Check the entry line meets the bounty constraints."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) < MIN_LENGTH or len(line) > MAX_LENGTH:
        raise ValueError(
            "entry line must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    line.encode("utf-8")
    return line


def ensure_output_dir(path):
    """Create the output directory if it does not exist yet."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def write_entry(line, path=OUTPUT_PATH):
    """Write the validated line to the output file."""
    ensure_output_dir(path)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return path


def main():
    line = validate_line(ENTRY_LINE)
    path = write_entry(line)
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
