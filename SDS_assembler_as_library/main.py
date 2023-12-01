import os

import pandas as pd
import argparse

from SDS_assembler import compileSource,createRaw

def main():
    list_of_directories = ["C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\source"]
    source_directory_counters = 0
    for directory in list_of_directories:
        path_to_directory = directory
        path_to_csv= "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\source_csv"+str(source_directory_counters)+".csv"
        data = compileSource.compileSource(path_to_directory,path_to_csv)
        #path_to_complied_csv = "Z:\\Molab_active\\SDS_Development\\MLIDs_csv_all_files_info_tested_headers_added.csv"
        path_to_complied_csv = "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\source_csv"+str(source_directory_counters)+".csv"
        path_to_raw_folder = "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\raw"+str(source_directory_counters)
        if not os.path.exists(path_to_raw_folder):
            os.mkdir(path_to_raw_folder)
        if path_to_complied_csv:
            df = pd.read_csv(path_to_complied_csv)
            status = createRaw.createRaw(df, path_to_raw_folder)
        else:
            status = createRaw.createRaw(data, path_to_raw_folder)

        print("The status is:")
        print(status)

if __name__ == "__main__":
    main()



