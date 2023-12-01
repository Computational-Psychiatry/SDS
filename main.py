import os

import pandas as pd
import argparse

from SDS_assembler import compileSource,createRaw

def code():
    path_to_directory = "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\source"
    path_to_csv= "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\testo_new_2.csv"
    data = compileSource.compileSource(path_to_directory,path_to_csv)
    #path_to_complied_csv = "Z:\\Molab_active\\SDS_Development\\MLIDs_csv_all_files_info_tested_headers_added.csv"
    path_to_complied_csv = "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\testo_new_3.csv"
    path_to_raw_folder = "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_library\\SDS_assembler\\raw"

    if path_to_complied_csv:
        df = pd.read_csv(path_to_complied_csv)
        status = createRaw.createRaw(df, path_to_raw_folder)
    else:
        status = createRaw.createRaw(data, path_to_raw_folder)

    print("The status is:")
    print(status)

if __name__ == "__main__":
    code()

#ML00025 - annotation mistakes


