import os.path
import argparse
import pandas as pd

from SDSValidator import ValidateFile, ValidateFolder

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, help='Specify the path of raw folder directory')
    parser.add_argument('-o', type=str, help='Specify the output message rules of raw folder structure or not')
    parser.add_argument('-f', type=str, help='Specify the single file  for validation in raw directories')

    args = parser.parse_args()
    if args.o:
        if args.d and args.o:
            status,message = ValidateFolder.validateFolder(args.d)
            with open(args.o,'w') as f:
                f.write("\n".join(map(lambda x: str(x), message)))
                f.close()
        elif args.f and args.o:
            status,message = ValidateFile.validateFile(args.f)
            with open(args.o,'w') as f:
                f.write("\n".join(map(lambda x: str(x), message)))
                f.close()
    elif args.d:
        status,message = ValidateFolder.validateFolder(args.d)
    elif args.f:
        status,message = ValidateFile.validateFile(args.f)
    else:
        print("the arguments combination specified is not correct")


