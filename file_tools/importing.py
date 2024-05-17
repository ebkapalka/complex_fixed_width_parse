def import_txt_to_list(file_path: str) -> list[str]:
    """
    Import a text file to a list of strings
    :param file_path: path to the file
    :return: list of strings
    """
    with open(file_path, "r") as file:
        return file.readlines()
