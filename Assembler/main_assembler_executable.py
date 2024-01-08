import pandas as pd
from SDS_assembler import compileSource,createRaw
import argparse
import os

def csv_from_source(source_path_directory_files, path_to_csv):
    """
    Reads file paths from a source file and compiles data from those files into a CSV file.

    Args:
        source_path_directory_files (str): Path to the file containing list of file paths.
        path_to_csv (str): Path to the output CSV file where compiled data will be saved.

    Returns:
        pd.DataFrame: Compiled data as a Pandas DataFrame (if single file path provided)
        None: If no file paths or multiple paths are found.

    Raises:
        FileNotFoundError: If the source file does not exist.

    """
    with open(source_path_directory_files, 'r') as source_read:
        list_paths = [line.strip() for line in source_read]

    if not list_paths:
        print("There are no file paths for the source. Please add them to the source file.")
        return None

    if len(list_paths) == 1:
        # Single file path - compile data and save to CSV
        path_to_directory = list_paths[0]
        data = compileSource.compileSource(path_to_directory, path_to_csv)
        return data

    else:
        # Multiple paths - currently not supported (could be implemented if needed)
        print("Multiple file paths found in source file. This functionality is not currently supported.")
        return None

def raw_folder_from_csv(path_to_csv, path_to_raw_folder,data):
    """
    Creates a raw folder structure based on the data in a provided CSV file.

    Args:
        path_to_csv (str): Path to the input CSV file containing data for the raw folder structure.
        path_to_raw_folder (str): Path to the directory where the raw folder will be created.

    Raises:
        FileNotFoundError: If the input CSV file does not exist.
        FileExistsError: If the output raw folder already exists.
        ValueError: If any error occurs during folder creation or data processing.

    """
    path_to_complied_csv = path_to_csv

    if os.path.exists(path_to_raw_folder):
        raise FileExistsError(f"Output raw folder already exists: {path_to_raw_folder}")

    if os.path.exists(path_to_complied_csv):
        df = pd.read_csv(path_to_complied_csv)
        createRaw.createRaw(df, path_to_raw_folder)
    else:
        createRaw.createRaw(data, path_to_raw_folder)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, help='Specify the source path of the folder (for generating CSV)')
    parser.add_argument('-o', type=str, help='Specify the output path of file or raw folder.')
    parser.add_argument('-i', type=str, help='Specify the input path of the CSV file (for creating raw folder)')
    args = parser.parse_args()
    data_list = []
    if args.s and args.o:
        data = csv_from_source(args.s, args.o)
        data_list.append(data)
    elif args.i and args.o:
        if len(data_list)==0:
            raw_folder_from_csv(args.i, args.o, 0)
        else:
            raw_folder_from_csv(args.i, args.o, data_list[0])
    else:
        print("Invalid arguments provided. Please refer to the help for usage.")


