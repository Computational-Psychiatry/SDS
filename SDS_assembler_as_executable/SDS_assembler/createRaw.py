import os
import warnings
from SDS_assembler.utility_fuctions import (csv_to_json_converter, yml_to_json_converter,mandatory_fields_json_checker,file_name_creator,folder_structure_creator)
import json
import shutil
import pandas as pd
#from SDS_assembler.createRaw import CreateRaw

class CreateRaw:

    def __init__(self,raw_folder_name):
        #self.source_folder_name = source_folder_name
        self.raw_folder_name =  raw_folder_name
        #self.source_folder_name = "C:\\Users\\pargim\\PycharmProjects\\SDS_grant_assembler\\SDS_assembler\\source\\"

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
            #shutil.copy(self.full_data_description_path,self.raw_folder_name)
            #shutil.copy(self.README, self.raw_folder_name)
        except FileExistsError as e:
            print("remove files once more if you want to override"+str(e))

    def folder_structure_creator(self):
        self.folder_content = folder_structure_creator(self.raw_folder_name,self.modified_filename_info)

    def file_name_modifier(self,fields_filename_mandatory_info_correct):
        for json_info_mandatory_filename in fields_filename_mandatory_info_correct:
            self.modified_filename_info = file_name_creator(json_info_mandatory_filename[0])
            self.filename_full_path = json_info_mandatory_filename[1]
            self.fileextension = json_info_mandatory_filename[2]
            self.json_info_= json_info_mandatory_filename[0]
            self.folder_structure_creator()
            self.file_system_copy_and_organizer()

    def mandatory_feild_info_checker_info_extractor(self, all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders):
        status = None
        file_creators_list = []
        for csv_file_extenders in all_csv_file_extenders:
            field_values_csv, status = mandatory_fields_json_checker(csv_file_extenders[0], csv_file_extenders[1],csv_file_extenders[2])
            if field_values_csv!=None:
                file_creators_list.append(field_values_csv)
        for json_file_extenders in all_json_file_extenders:
            field_values_json, status = mandatory_fields_json_checker(json_file_extenders[0], json_file_extenders[1],json_file_extenders[2])
            if field_values_json!=None:
                file_creators_list.append(field_values_json)
        for yaml_file_extenders in all_yaml_file_extenders:
            field_values_yaml, status = mandatory_fields_json_checker(yaml_file_extenders[0],yaml_file_extenders[1],yaml_file_extenders[2])
            if field_values_yaml!=None:
                file_creators_list.append(field_values_yaml)
        return file_creators_list, status

    def file_extension_check(self,df):
        #df = pd.read_csv(read_csv_from_location)
        print("in the function")
        print(df)
        if "filename_extensions" in list(df.columns):
            all_location_extractor = df["filename_details"].tolist()
            all_extension_extractor = df["filename_extensions"].tolist()
            all_csv_file_extenders = []
            all_json_file_extenders= []
            all_yaml_file_extenders = []

            for filename in all_location_extractor:
                status = None
                if filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi"):
                    #print("Names here are:")
                    filename_video_info = filename
                    filename_other_csv = filename.split(".")[0]+".csv"
                    filename_other_json = filename.split(".")[0] +".json"
                    filename_other_yml = filename.split(".")[0] +".yml"
                    if filename_other_csv in all_extension_extractor:
                       json_file_from_csv = csv_to_json_converter(filename,filename_other_csv)
                       all_csv_file_extenders.append([json_file_from_csv[0],filename_other_csv,filename_video_info,filename_other_csv])
                       #mandatory_fields_json_checker(json_file_from_csv[0],filename_other_csv)

                    elif filename_other_json in all_extension_extractor:
                        f = open(filename_other_json, 'r')
                        json_data = json.load(f)
                        all_json_file_extenders.append([json_data,filename_other_json,filename_video_info,filename_other_json])

                    elif filename_other_yml in all_extension_extractor:
                        json_from_yml = yml_to_json_converter(filename,filename_other_yml)
                        all_yaml_file_extenders.append([json_from_yml,filename_other_yml,filename_video_info,filename_other_yml])
                    else:
                        print("This filename doesn't have a extension")
                        print(filename)
                        warnings.showwarning("skipping this filename",filename=filename,lineno=40,category=Warning)
                        warnings.warn("skipped for processing further for the above described filename")
                        status = False
        else:
            print("columns of json not added")
            status=False
        return all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders,status

    def folder_structure_source_checker(self):
        files_all=[]
        for file in os.listdir(self.source_folder_name):
            if os.path.isfile(os.path.join(self.source_folder_name, file)):
                files_all.append(file)
        if "dataset_description.json" in files_all:
            print("success:"+"dataset_description.json"+"Json file present in"+str(self.source_folder_name))
            self.full_data_description_path =os.path.join(self.source_folder_name,"dataset_description.json")
        else:
            print("Mandatory_File_missing"+str(file)+"in"+str(self.source_folder_name))
        if "README" in files_all:
            print("success:"+"README"+"present in"+str(self.source_folder_name))
            self.README = os.path.join(self.source_folder_name, "README")
        else:
            print("Mandatory_File_missing"+str(file)+"in"+str(self.source_folder_name))
"""
    def csv_creator(self, all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders,write_location):
        data_list = []
        for csv_file_extenders in all_csv_file_extenders:
            dict_csv_extender = csv_file_extenders[0]
            dict_csv_extender["filename"] = csv_file_extenders[2]
            dict_csv_extender["filename_extended"] = csv_file_extenders[3]
            data_list.append(dict_csv_extender)
        for json_file_extenders in all_json_file_extenders:
            dict_json_extender = json_file_extenders[0]
            dict_json_extender["filename"] = json_file_extenders[2]
            dict_json_extender["filename_extended"] = json_file_extenders[3]
            data_list.append(dict_json_extender)
        for yaml_file_extenders in all_yaml_file_extenders:
            dict_yml_extender = yaml_file_extenders[0]
            dict_yml_extender["filename"] = yaml_file_extenders[2]
            dict_yml_extender["filename_extended"] = yaml_file_extenders[3]
            data_list.append(dict_yml_extender)
        df = pd.DataFrame.from_dict(data_list, orient='columns')
        print(df.head())
        df.insert(0, column="filename_details",value=df["filename"].tolist())
        df.insert(1, column="filename_extensions", value=df["filename_extended"].tolist())
        df = df.drop('filename', axis=1)
        df = df.drop("filename_extended",axis=1)
        df.to_csv(write_location,index=False)
"""

def createRaw(df,raw_folder_name):
        csvCreator = CreateRaw(raw_folder_name)
        all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders,status_file_extension_source = csvCreator.file_extension_check(df)
        #csvCreator.folder_structure_source_checker()
        files_field_names_mandatory_correct,status_json_checker = csvCreator.mandatory_feild_info_checker_info_extractor(all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders)
        csvCreator.file_name_modifier(files_field_names_mandatory_correct)
        #csvCreator.csv_creator(all_csv_file_extenders, all_json_file_extenders, all_yaml_file_extenders,df)
        if status_json_checker == False or status_file_extension_source == False:
            return False
        else:
            return True




