import pandas as pd
import json
import yaml
from yaml import SafeLoader
import re
import os


def csv_to_json_converter(filename,filename_csv):
    df = pd.read_csv(filename_csv)
    return df.to_dict(orient="records")


def yml_to_json_converter(filename,filename_yml):
    f = open(filename_yml, "r")
    yml_format_data = f.read()
    python_dict = yaml.load(yml_format_data, Loader=SafeLoader)
    return python_dict

def dict_for_modality():
    # Opening JSON file
    absolute_path = os.getcwd()
    #relative_path = "SDS_assembler/modality.json"
    relative_path = os.path.join("SDS_assembler","modality.json")
    full_path = os.path.join(absolute_path, relative_path)
    f = open(full_path,'r')
    data = json.load(f)
    return data

def filename_fieldname_mapper():
    absolute_path = os.getcwd()
    #relative_path = "SDS_assembler/JSON_Fieldnames_Filenames_Required_Information.csv"
    relative_path = os.path.join("SDS_assembler","JSON_Fieldnames_Filenames_Required_Information.csv")

    full_path = os.path.join(absolute_path, relative_path)
    df_conversion = pd.read_csv(full_path)
    d_json_to_filename = df_conversion.set_index('Field name in JSON')['Field name in file name'].to_dict()
    return d_json_to_filename

def filename_json_mandatory_mapper():
    absolute_path = os.getcwd()
    #relative_path = "SDS_assembler/JSON_Fieldnames_Filenames_Required_Information.csv"
    relative_path = os.path.join("SDS_assembler","JSON_Fieldnames_Filenames_Required_Information.csv")
    full_path = os.path.join(absolute_path, relative_path)
    df_conversion = pd.read_csv(full_path)
    d_json_mandatory_optional = df_conversion.set_index('Field name in JSON')['Required in JSON?'].to_dict()
    return d_json_mandatory_optional

def mandatory_fields_json_checker(json_info,filename_info,file_extension):
    d_json_mandatory_optional = filename_json_mandatory_mapper()
    json_mandatory_keys = [k for k, v in d_json_mandatory_optional.items() if v == 'mandatory']
    json_optional_keys = [k for k, v in d_json_mandatory_optional.items() if v == 'optional']
    data=json_info
    all_json_file_name_keys = list(data.keys())
    all_json_mandatory_key_list_from_file = []
    for json_key in all_json_file_name_keys:
        if json_key in json_mandatory_keys:
            all_json_mandatory_key_list_from_file.append(json_key)

    final_mandatory_missing_values = list(set(json_mandatory_keys)-set(all_json_mandatory_key_list_from_file))
    for missing_values in final_mandatory_missing_values:
        print("Missing_Mandatory_files "+str(missing_values)+" not found in "+str(filename_info))
    if len(final_mandatory_missing_values)==0:
        return [json_info, filename_info, file_extension], True
    else:
        return None, False

    print("#############################################################################################")

def convert_camel_case(list_items):
    list_values =  re.split('\s|(?<!\d)[,.]|[,.](?!\d)', list_items)
    if len(list_values)>1:
        word_value = list_values[0]
        world_value_updated = word_value[0].lower()+word_value[1:]
        test = []
        for i in range(1,len(list_values)):
            test.append(list_values[i])
        s = ''.join(test)
        final_word = world_value_updated+s
    else:
        word = list_values[0]
        final_word =word[0].upper()+word[1:]
    return final_word


def file_name_creator(json_info):
    d_fieldname_mapper = filename_fieldname_mapper()
    final_string = []
    for key,value in d_fieldname_mapper.items():
        if key in json_info.keys():
            if str(key)!="Modality":
                final_string.append(str(d_fieldname_mapper[key])+"-"+str(json_info[key]))
            elif key=="Modality":
                if json_info[key] in d_fieldname_mapper[key]:
                    final_string.append(str(json_info[key]))

    fullname = []
    for sub_values in final_string:
        if len(sub_values.split("-"))==2:
            word_value = convert_camel_case(sub_values.split("-")[1])
            fullname.append(sub_values.split("-")[0]+"-"+word_value)
        else:
            fullname.append(sub_values)
    return "_".join(fullname)

def folder_structure_creator(raw_folder_path,modified_filename):
    modality_mapper = dict_for_modality()
    d_fieldname_mapper = filename_fieldname_mapper()
    lst = ["sub", "ses", "rgb","rgba","rgbd","rgbad", "depth", "audio", "other"]
    list_all_fields_info = modified_filename.split("_")
    for field_name in list_all_fields_info:
        if field_name.startswith(lst[0]):
            folder_path_sub = os.path.join(raw_folder_path,field_name)
            if not os.path.exists(folder_path_sub):
               os.makedirs(folder_path_sub)
        if field_name.startswith(lst[1]):
            folder_path_ses = os.path.join(folder_path_sub,field_name)
            if not os.path.exists(folder_path_ses):
               os.makedirs(folder_path_ses)
        if field_name in lst[2:]:
            mapped_modality_folder = [k for k, v in modality_mapper.items() if field_name in v]
            if os.path.exists(folder_path_ses):
                folder_ses_modality = os.path.join(folder_path_ses,mapped_modality_folder[0])
                if not os.path.exists(folder_ses_modality):
                    os.makedirs(folder_ses_modality)
                return folder_ses_modality
            elif not os.path.exists(folder_path_ses):
                folder_sub_modality = os.path.join(folder_path_sub, mapped_modality_folder[0])
                if not os.path.exists(folder_sub_modality):
                    os.makedirs(folder_sub_modality)
                return folder_sub_modality
            else:
                pass













