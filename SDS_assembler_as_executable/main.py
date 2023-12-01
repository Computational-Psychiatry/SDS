import pandas as pd

from SDS_assembler import compileSource,createRaw

import argparse


def csv_from_source(source_path_directory_files, path_to_csv):
    with open(source_path_directory_files,'r') as source_read:
        list_paths = []
        for line in source_read:
            line = line.strip()
            list_paths.append(line)
        if len(list_paths)==0:
            print("There are no file paths for the source please add them")
        elif len(list_paths)>=1:
            print(list_paths)
            print(path_to_csv)
            path_to_directory = list_paths
            path_to_csv = path_to_csv
            data = compileSource.compileSource(path_to_directory, path_to_csv)
        else:
            pass

def raw_folder_from_csv(path_to_csv,path_to_raw_folder):
    path_to_complied_csv = path_to_csv
    path_to_raw_folder = path_to_raw_folder

    if path_to_complied_csv:
        df = pd.read_csv(path_to_complied_csv)
        status = createRaw.createRaw(df, path_to_raw_folder)
    else:
        status = createRaw.createRaw(data, path_to_raw_folder)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', type=str, help='Specify the source path of the folder')
    parser.add_argument('--o', type=str, help='Specify the output path of file or raw folder.')
    parser.add_argument('--i', type=str, help='Specify the input path of the CSV file')
    args = parser.parse_args()
    if args.s and args.o:
       data = csv_from_source(args.s,args.o)
    elif args.i and args.o:
       status = raw_folder_from_csv(args.i,args.o)
    else:
        print("the arguments combination specified is not correct test")



