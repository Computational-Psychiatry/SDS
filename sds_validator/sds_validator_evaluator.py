import os
import colorama
from sds_validator import SDSValidator
import json

colorama.init()

def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(os.path.relpath(file_path, directory))
    return file_paths

def Json_to_folder_path_convertor(SDS_JSON):
    f = open(SDS_JSON)
    data = json.load(f)
    raw_folder_path = data['raw_folderpath']
    f.close()
    return raw_folder_path


def rulers_Validator(validator, SDS_files, JSON_data):
    for SDS_file in SDS_files:
        path = '/' + SDS_file
        #path = os.path.join(SDS_file)
        print("the path is:")
        print(path)

        passes, satisfies = validator.is_sds_filepath(path, JSON_data)
        if passes:
            status = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        else:
            status = colorama.Fore.RED + '\u2717' + colorama.Fore.RESET
        print(status, satisfies, path)

def pathloaders(SDS_Json_file,JSON_file_location_path):
    basepath = os.path.dirname(os.path.abspath(SDS_Json_file))
    #full_path = basepath + JSON_file_location_path +"\\"+ SDS_Json_file
    full_path = os.path.join(basepath, SDS_Json_file)
    return full_path

def JSON_to_SDS_recommended_mandatory_path_convertors(SDS_path_mandatory):
    f = open(SDS_path_mandatory)
    data = json.load(f)
    f.close()
    return data

def file_exists_rules(validator,data,SDS_path):
    status_value_recommended, status_value_mandatory, status_check_file_json_video_present = validator.is_file_exists(data,SDS_path)
    if status_value_mandatory==True:
        status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        print(status_check+"Mandatory Files Present"+str(data["Mandatory_recommended_file_info"]["Mandatory_files"]))
    if status_value_recommended==True:
        status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        print(status_check+"recommended Files Present"+str(data["Mandatory_recommended_file_info"]["recommended_files"]))
    #print(status_check_file_json_video_present)
    for key, value in status_check_file_json_video_present.items():
        print(status_check_file_json_video_present[key])
        if status_check_file_json_video_present[key] == True:
            status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
            print(status_check + "JSON File and Video File with same name present in :"+str(key))


def main():
    SDS_Json_file = "dataset_raw_folder_path.json"
    SDS_recommed_mandatory = "recommend_mandatory_and_details_check.json"
    #JSON_file_location_path = "\\SDS_grant\\sds_validator"
    JSON_file_location_path = os.path.join("SDS_grant", "sds_validator")
    full_path = pathloaders(SDS_Json_file, JSON_file_location_path)
    print(full_path)
    SDS_path = Json_to_folder_path_convertor(full_path)
    full_path_mandatory = pathloaders(SDS_recommed_mandatory, JSON_file_location_path)
    JSON_data = JSON_to_SDS_recommended_mandatory_path_convertors(full_path_mandatory)
    SDS_files = get_file_paths(SDS_path)
    validator = SDSValidator()
    rulers_Validator(validator, SDS_files, JSON_data)
    file_exists_rules(validator, JSON_data, SDS_path)

main()
