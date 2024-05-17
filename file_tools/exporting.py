from datetime import datetime
import csv
import os


def dict_list_to_csv(data: list[dict], folder: str="output") -> None:
    """
    Save a list of dictionaries to a CSV file
    :param folder: folder to save the file
    :param data: list of dictionaries
    :return: None
    """
    if not data:
        print("No data to export.")
        return

    headers = data[0].keys()
    folder = os.path.abspath(folder)
    file_name = f"export_good_{timestamp()}.csv"
    file_path = os.path.join(folder, file_name)
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Data saved to {file_path}")


def string_list_to_csv(data: list[str], folder: str = "output") -> None:
    """
    Save a list of strings to a CSV file
    :param folder: folder to save the file
    :param data: list of strings
    :return: None
    """
    if not data:
        print("No data to export.")
        return

    folder = os.path.abspath(folder)
    file_name = f"export_bad_{timestamp()}.csv"
    file_path = os.path.join(folder, file_name)
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow([row])
    print(f"Data saved to {file_path}")


def timestamp(dt_obj: datetime = None, fmt="%Y%m%d_%H%M%S") -> str:
    """
    Generate a timestamp
    :param dt_obj: datetime object
    :param fmt: format of the timestamp
    :return: timestamp in the specified format
    """
    if not dt_obj:
        dt_obj = datetime.now()
    return dt_obj.strftime(fmt)
