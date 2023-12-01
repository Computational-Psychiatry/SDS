import os
import json
import pandas as pd
from SDS_assembler.utility_fuctions import (csv_to_json_converter, yml_to_json_converter)
#from SDS_assembler.compileSource import complieSource

class SourceCompiler:
    def __init__(self, source_folder_name):
        # Initialize the SourceCompiler class with source folder name and output CSV path
        self.source_folder_name = source_folder_name


    def file_extension_check(self, all_location_extractor,all_csv_extenders,all_json_extenders,all_yaml_extenders,files_with_no_extenders):
        # Check file extensions and return data for CSV, JSON, YAML, and files with no extensions
        for filename in all_location_extractor:
            name, ext = os.path.splitext(filename)

            # Check if the file extension is in a specific list
            if ext in (".mp4", ".mkv", ".avi", ".m4v", ".MTS", ".iPiVideo"):
                filename_video_info = filename
                filename_other_csv = name + ".csv"
                filename_other_json = name + ".json"
                filename_other_yml = name + ".yml"

                # Check if corresponding files exist
                if filename_other_csv in all_location_extractor:
                    json_file_from_csv = csv_to_json_converter(filename, filename_other_csv)
                    all_csv_extenders.append([json_file_from_csv[0], filename_other_csv, filename_video_info])

                elif filename_other_json in all_location_extractor:
                    with open(filename_other_json, 'r') as f:
                        json_data = json.load(f)
                    all_json_extenders.append([json_data, filename_other_json, filename_video_info])

                elif filename_other_yml in all_location_extractor:
                    json_from_yml = yml_to_json_converter(filename, filename_other_yml)
                    all_yaml_extenders.append([json_from_yml, filename_other_yml, filename_video_info])

                else:
                    files_with_no_extenders.append(filename_video_info)

        return all_csv_extenders, all_json_extenders, all_yaml_extenders, files_with_no_extenders

    def folder_structure_extractor(self):
        # Extract all files from the source folder and check for mandatory files

        all_files_captured = []
        print("the source folder details is :")
        print(self.source_folder_name)
        for (root, _, files) in os.walk(self.source_folder_name, topdown=False):
            for filename in files:
                all_files_captured.append(os.path.join(root, filename))

        files_all = [file for file in os.listdir(self.source_folder_name) if
                     os.path.isfile(os.path.join(self.source_folder_name, file))]

        if len(files_all) != 0:
            if "dataset_description.json" in files_all:
                print("Success: 'dataset_description.json' file present in", self.source_folder_name)
                self.full_data_description_path = os.path.join(self.source_folder_name, "dataset_description.json")
            else:
                print("Mandatory file missing: 'dataset_description.json' in", self.source_folder_name)

            if "README" in files_all:
                print("Success: 'README' file present in", self.source_folder_name)
                self.README = os.path.join(self.source_folder_name, "README")
            else:
                print("Mandatory file missing: 'README' in", self.source_folder_name)

        return all_files_captured

"""
def compileSource(source_folder_name, output_csv_path):
    csv_creator = SourceCompiler(source_folder_name, output_csv_path)
    all_files_location = csv_creator.folder_structure_extractor()
    all_csv_extenders, all_json_extenders, all_yaml_extenders, files_with_no_extenders = csv_creator.file_extension_check(
        all_files_location)
    df = csv_creator.create_csv(all_csv_extenders, all_json_extenders, all_yaml_extenders, files_with_no_extenders)
    return df
"""


def create_csv(all_csv_extenders, all_json_extenders, all_yaml_extenders, files_with_no_extenders,output_csv_path):
    # Create a CSV file containing information about files in the source folder

    data_list = []
    fieldnamepath = os.path.join(os.getcwd(), "SDS_assembler", "json_fields_info.txt")

    # Check for CSV file extenders
    if all_csv_extenders:
        for extender in all_csv_extenders:
            extender[0]["filename"] = extender[2]
            extender[0]["filename_extended"] = extender[1]
            data_list.append(extender[0])

    # Check for JSON file extenders
    if all_json_extenders:
        for extender in all_json_extenders:
            extender[0]["filename"] = extender[2]
            extender[0]["filename_extended"] = extender[1]
            data_list.append(extender[0])

    # Check for YAML file extenders
    if all_yaml_extenders:
        for extender in all_yaml_extenders:
            extender[0]["filename"] = extender[2]
            extender[0]["filename_extended"] = extender[1]
            data_list.append(extender[0])

    # Add files with no extenders
    for filename in files_with_no_extenders:
        data_list.append({"filename": filename})

    # Read the list of fields from a file
    with open(fieldnamepath, 'r') as all_fields:
        list_all_fields = all_fields.readline().strip().split(",")

    # Create a DataFrame from the data
    df = pd.DataFrame.from_dict(data_list)

    # Find the fields that are missing and fill with empty values
    diff_columns = list(set(list_all_fields) - set(df.columns))
    df.insert(0, "filename_details", df["filename"])

    # Add filename extensions if available
    if any([all_csv_extenders, all_json_extenders, all_yaml_extenders]):
        df.insert(1, "filename_extensions", df["filename_extended"])

    df.drop(columns=["filename", "filename_extended"], inplace=True)

    for diffcol in diff_columns:
        df[diffcol] = ""

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_path, index=False)

    return df


def compileSource(source_folder_names, output_csv_path):
    all_csv_extenders = []
    all_json_extenders = []
    all_yaml_extenders = []
    files_with_no_extenders = []

    for source_folder in source_folder_names:
        csv_creator = SourceCompiler(source_folder)
        all_files_location = csv_creator.folder_structure_extractor()
        all_csv_extenders, all_json_extenders, all_yaml_extenders, files_with_no_extenders = csv_creator.file_extension_check(
            all_files_location,all_csv_extenders,all_json_extenders,all_yaml_extenders,files_with_no_extenders)
    df = create_csv(all_csv_extenders, all_json_extenders, all_yaml_extenders, files_with_no_extenders,output_csv_path)
    return df

