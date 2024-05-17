from fnmatch import fnmatchcase


BAD_LINE_PATTERNS = [
    "*Montana State University - Office of Admissions*",
    "*Page * of *",
    "Prospect Tally- By High School*",
    "*High School * Count*",
    "*202570 and later*",
    "*Total:*",
    ' ' * 108 + "*"
]


def is_bad_line(text: str) -> bool:
    """
    Check if a line is bad based on a list of patterns
    :param text: line of text to check
    :return: true if the line is bad, false otherwise
    """
    for pattern in BAD_LINE_PATTERNS:
        if fnmatchcase(text, pattern):
            return True
    return False


def parse_fixedwidth(text: str, start_ind: int = None,
                     end_ind: int = None) -> str:
    """
    Parse a fixed-width field from a line
    :param text: line of text
    :param start_ind: start index of the field
    :param end_ind: end index of the field
    :return: parsed field
    """
    if not start_ind:
        start_ind = 0
    if not end_ind:
        end_ind = len(text)
    return text[start_ind:end_ind].strip()


def merge_dicts(primary: dict, merge: dict) -> dict:
    """
    Merge two dictionaries
    :param primary: first dictionary
    :param merge: second dictionary
    :return: merged dictionary
    """
    if not merge:
        return primary
    for key, value in merge.items():
        if not value:
            continue
        sep = ' ' if key != "ceeb code" else ''
        primary[key] = f"{primary[key]}{sep}{value}"
    return primary


def sanitize_lines(data: list[str]) -> tuple[list[str], list[str]]:
    """
    Remove empty and bad lines from a list of strings
    :param data: list of strings
    :return: list of strings with empty and bad lines removed
    """
    stripped = [l.rstrip() for l in data if l.strip()]
    print(f"Removed {len(data) - len(stripped)} empty lines.")

    good_lines = []
    bad_lines = []
    for row in stripped:
        if is_bad_line(row):
            bad_lines.append(row)
            continue
        good_lines.append(row)
    print(f"Removed {len(bad_lines)} bad lines.")
    return good_lines, bad_lines
