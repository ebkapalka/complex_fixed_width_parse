from file_tools.exporting import dict_list_to_csv, string_list_to_csv
from file_tools.importing import import_txt_to_list
from processing import sanitize_lines, parse_fixedwidth, merge_dicts


def parse_data(data: list[str]) -> list[dict]:
    """
    Translate the fixed-width data into a list of dictionaries
    :param data: list of strings that are fixed-width lines
    :return: list of dictionaries with the parsed data
    """
    parsed_data: list[dict] = []
    for line in data:
        prev_line = parsed_data[-1] if parsed_data else {}
        current_line = {
            "ceeb code": parse_fixedwidth(line, 0, 16),
            "school name": parse_fixedwidth(line, 16, 56),
            "city": parse_fixedwidth(line, 56, 91),
            "state": parse_fixedwidth(line, 91, 107),
            "count": parse_fixedwidth(line, 107)
        }
        if len(current_line["ceeb code"]) < 2:
            merged_dict = merge_dicts(prev_line, current_line)
            prev_line.update(merged_dict)
            continue
        parsed_data.append(current_line)
    return parsed_data


if __name__ == '__main__':
    file_name = "input/R-T_PR_HighSchool_GEcurr.txt"
    lines = import_txt_to_list(file_name)
    good_lines, bad_lines = sanitize_lines(lines)
    output_data = parse_data(good_lines)

    # Export the data
    string_list_to_csv(bad_lines)
    dict_list_to_csv(output_data)
