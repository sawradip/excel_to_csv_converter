import os
import fnmatch
import subprocess
from tqdm import tqdm


def find_excel_files(directory):
    """
    Function to find all Excel files in a given directory.
    
    Args:
    directory (str): The directory in which to search for Excel files.

    Returns:
    list: A list of file paths for Excel files found in the directory.
    """
    excel_files = []
    # Walk the directory structure
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # If file is an Excel file, add to list
            if fnmatch.fnmatch(filename, '*.xlsx') or fnmatch.fnmatch(filename, '*.xlsb'):
                excel_files.append(os.path.join(root, filename))
    return excel_files


def convert_excel_to_csv(excel_file, csv_output_file):
    """
    Function to convert an Excel file to a CSV file using LibreOffice command line.

    Args:
    excel_file (str): The path of the Excel file to be converted.
    csv_output_file (str): The path where the converted CSV file should be saved.

    Returns:
    str: The path of the output CSV file.
    """
    # Define the command to convert excel to csv using LibreOffice
    command = f'soffice --headless --convert-to csv --outdir "{os.path.dirname(csv_output_file)}" "{excel_file}"'
    
    print(command)
    # Run the command
    subprocess.run(command, shell=True)
    return csv_output_file


def convert_excel_files(excel_files, destination_folder, directory):
    """
    Function to convert a list of Excel files to CSV format.

    Args:
    excel_files (list): A list of Excel file paths to convert.
    destination_folder (str): The folder where to store the converted files.
    directory (str): The root directory from where the Excel files were obtained.
    """
    # Loop over each Excel file in the list
    for file_path in tqdm(excel_files):
        relative_path = os.path.relpath(file_path, directory)
        destination_path = os.path.join(destination_folder, relative_path)
        # Replace the file extension with .csv
        destination_path = os.path.splitext(destination_path)[0] + '.csv'
        # Make sure the directory exists, if not create it
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        # Convert the Excel file to CSV
        convert_excel_to_csv(file_path, destination_path)


# Define source and destination folders
src_folder = 'new_data/Rawdata 2023'
destination_folder = 'to_csv_all/Rawdata 2023'

# Find all Excel files in the source folder
excel_files = find_excel_files(src_folder)
# Convert all found Excel files to CSV format
convert_excel_files(excel_files, destination_folder, src_folder)
