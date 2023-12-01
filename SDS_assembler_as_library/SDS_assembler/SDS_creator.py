import os
import warnings
from utility_fuctions import csv_to_json_convertor,yml_to_json_convertor,mandatory_fields_json_checker,file_name_creator,folder_structure_creator
import json
import shutil
import pandas as pd
import argparse

class SdsCreator:
    def __init__(self,source_folder_name,raw_folder_name):
        self.source_folder_name = source_folder_name
        self.raw_folder_name =  raw_folder_name

    def file_system_copy_and_organizer(self):
        try:
            video_full_path_to_copy = self.fileextension
            filenameinfowithextenstion = self.fileextension.split(os.sep)[-1]
            filename_extension_updated = self.fileextension.split(".")[1]
            json_filename_in_path_copy = self.modified_filename_info+".json"
            full_json_path = os.path.join(self.folder_content,json_filename_in_path_copy)
            filejson = open(full_json_path, "w")
            with open(full_json_path, 'w') as f:
                json.dump(self.json_info_, f)
            shutil.copy(video_full_path_to_copy,self.folder_content)
            final_copied_path_location_name = os.path.join(self.folder_content,filenameinfowithextenstion)
            os.rename(final_copied_path_location_name,os.path.join(self.folder_content,self.modified_filename_info+"."+filename_extension_updated))
            shutil.copy(self.full_data_description_path,self.raw_folder_name)
            shutil.copy(self.README, self.raw_folder_name)
        except FileExistsError as e:
            print("remove files once more if you want to override"+str(e))

    def folder_structure_creator(self):
        self.folder_content = folder_structure_creator(self.raw_folder_name,self.modified_filename_info)

    def file_name_modifier(self,fields_filename_mandatory_info_correct):
        for json_info_mandatory_filename in fields_filename_mandatory_info_correct:
            self.modified_filename_info = file_name_creator(json_info_mandatory_filename[0])
            self.filename_full_path = json_info_mandatory_filename[1]
            self.fileextension = json_info_mandatory_filename[2]
            self.folder_structure_creator()
            self.file_system_copy_and_organizer()

    def mandatory_feild_info_checker_info_extractor(self, all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders):
        file_creators_list = []
        for csv_file_extenders in all_csv_file_extenders:
            field_values_csv = mandatory_fields_json_checker(csv_file_extenders[0], csv_file_extenders[1],csv_file_extenders[2])
            if field_values_csv!=None:
                file_creators_list.append(field_values_csv)
        for json_file_extenders in all_json_file_extenders:
            field_values_json = mandatory_fields_json_checker(json_file_extenders[0], json_file_extenders[1],json_file_extenders[2])
            if field_values_json!=None:
                file_creators_list.append(field_values_json)
        for yaml_file_extenders in all_yaml_file_extenders:
            field_values_yaml = mandatory_fields_json_checker(yaml_file_extenders[0],yaml_file_extenders[1],yaml_file_extenders[2])
            if field_values_yaml!=None:
                file_creators_list.append(field_values_yaml)
        return file_creators_list
    def csv_creator(self, all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders,write_location):
        data_list = []
        for csv_file_extenders in all_csv_file_extenders:
            dict_csv_extender = csv_file_extenders[0]
            dict_csv_extender["filename"] = csv_file_extenders[2]
            data_list.append(dict_csv_extender)
        for json_file_extenders in all_json_file_extenders:
            dict_json_extender = json_file_extenders[0]
            dict_json_extender["filename"] = json_file_extenders[2]
            data_list.append(dict_json_extender)
        for yaml_file_extenders in all_yaml_file_extenders:
            dict_yml_extender = yaml_file_extenders[0]
            dict_yml_extender["filename"] = yaml_file_extenders[2]
            data_list.append(dict_yml_extender)
        df = pd.DataFrame.from_dict(data_list, orient='columns')
        df.insert(0, column="filename_details",value=df["filename"].tolist())
        df = df.drop('filename', axis=1)
        df.to_csv(write_location,index=False)


    def file_extension_check(self, all_location_extractor):
        all_csv_file_extenders = []
        all_json_file_extenders= []
        all_yaml_file_extenders = []

        for filename in all_location_extractor:
            if filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi"):
                #print("Names here are:")
                filename_video_info = filename
                filename_other_csv = filename.split(".")[0]+".csv"
                filename_other_json = filename.split(".")[0] +".json"
                filename_other_yml = filename.split(".")[0] +".yml"
                if filename_other_csv in all_location_extractor:
                   json_file_from_csv = csv_to_json_convertor(filename,filename_other_csv)
                   all_csv_file_extenders.append([json_file_from_csv[0],filename_other_csv,filename_video_info])

                elif filename_other_json in all_location_extractor:
                    f = open(filename_other_json, 'r')
                    json_data = json.load(f)
                    all_json_file_extenders.append([json_data,filename_other_json,filename_video_info])
                elif filename_other_yml in all_location_extractor:
                    json_from_yml = yml_to_json_convertor(filename,filename_other_yml)
                    all_yaml_file_extenders.append([json_from_yml,filename_other_yml,filename_video_info])
                else:
                    print("This filename doesn't have a extension")
                    print(filename)
                    warnings.showwarning("skipping this filename",filename=filename,lineno=40,category=Warning)
                    warnings.warn("skipped for processing further for the above described filename")
        return all_csv_file_extenders,all_json_file_extenders,all_yaml_file_extenders
    def folder_structure_extractor(self):
        All_files_captured = []
        for (root, dirs, files) in os.walk(self.source_folder_name, topdown=False):
                if len(files)!=0 and len(dirs)==0:
                    for filename in files:
                       All_files_captured.append(os.path.join(root,filename))
        files_all = []

        for file in os.listdir(self.source_folder_name):
            if os.path.isfile(os.path.join(self.source_folder_name, file)):
                files_all.append(file)
        if "dataset_description.json" in files_all:
            print("success:"+"dataset_description.json"+"file present in"+str(self.source_folder_name))
            self.full_data_description_path =os.path.join(self.source_folder_name,"dataset_description.json")
        else:
            print("Mandatory_File_missing"+str(file)+"in"+str(self.source_folder_name))
        if "README" in files_all:
            print("success:"+"README"+"present in"+str(self.source_folder_name))
            self.README = os.path.join(self.source_folder_name, "README")
        else:
            print("Mandatory_File_missing"+str(file)+"in"+str(self.source_folder_name))
        return All_files_captured


def main():
    basepath = os.getcwd()
    path_source_folder, path_raw_folder, path_csv_writer_location = argument_parser(argparse.ArgumentParser())
    if path_source_folder!=None:
        source_folder_name = path_source_folder
    else:
        source_folder_name = os.path.join(basepath, "source")

    if path_raw_folder!=None:
        raw_folder_name = path_raw_folder
    else:
        raw_folder_name = os.path.join(basepath, "raw")

    if path_csv_writer_location!=None:
        path_csv_writer_location= path_csv_writer_location
    else:
        path_csv_writer_location= os.path.join(basepath,"detailed_info_json_all_fields_filenames.csv")

    if not os.path.exists(raw_folder_name):
        os.makedirs(raw_folder_name)
    sdsCreator = SdsCreator(source_folder_name,raw_folder_name)
    all_files_location = sdsCreator.folder_structure_extractor()
    all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders = sdsCreator.file_extension_check(all_files_location)
    files_field_names_mandatory_correct = sdsCreator.mandatory_feild_info_checker_info_extractor(all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders)
    sdsCreator.file_name_modifier(files_field_names_mandatory_correct)
    sdsCreator.csv_creator(all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders,path_csv_writer_location)

def argument_parser(parser):

    """

    argument_parser: This function is used to parse the python command line arguments provided by user input

    :return all information related to inputs passed by the user

    """

    parser.add_argument("--path_source_folder", help="Add the path to location of source folder once cloned",type=str)
    parser.add_argument("--path_raw_folder", help="Add the path to location of source folder once cloned", type=str)
    parser.add_argument("--write_csv_detailed_info_location_path", help="Add the path to location of source folder once cloned", type=str)
    args = parser.parse_args()

    path_source_folder = args.path_source_folder
    path_raw_folder = args.path_raw_folder
    path_csv_writer_location = args.write_csv_detailed_info_location_path

    return path_source_folder,path_raw_folder,path_csv_writer_location


if __name__=="__main__":
    main()

