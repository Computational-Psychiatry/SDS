import os
import colorama
from SDS_validator_as_library.SDSValidator.sds_validator import SDSValidatorTest
import json
import argparse

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
    boolean_rules = []
    for SDS_file in SDS_files:
        path = '/' + SDS_file
        print("The paths are in boolean:")
        print(path)
        passes, satisfies = validator.is_sds_filepath(path, JSON_data)
        if passes:
            status = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
            status_boolean=1
            boolean_rules.append([status_boolean, satisfies, path])
        else:
            status = colorama.Fore.RED + '\u2717' + colorama.Fore.RESET
            status_boolean = 0
            boolean_rules.append([status_boolean, satisfies, path])
    return boolean_rules

def rules_validator_single_file(validator, single_file, JSON_data):
    boolean_rules=[]
    k = single_file.split("\\")
    test = ""
    count = 0
    test_dict = {}
    for file_val in k:
        test_dict[file_val] = count
        count = count + 1
    count_value = test_dict["raw"]
    print(count_value)
    for key, value in test_dict.items():
        if test_dict[key] > count_value:
            test = test + key + "\\"
    print(test[0:-2])
    passes, satisfies = validator.is_sds_filepath("/"+test[0:-1], JSON_data)
    if passes:
        status = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        status_boolean = 1
        boolean_rules.append([status_boolean, satisfies, "/"+test[0:-1]])
    else:
        status = colorama.Fore.RED + '\u2717' + colorama.Fore.RESET
        status_boolean = 0
        boolean_rules.append([status_boolean, satisfies, "/"+test[0:-1]])

    return boolean_rules



def Validator_error_all(boolean_rules_validator,Errors_validator,Warnings_validator):
    print("Boolean validator")
    boolean_error_list = []
    message_details = []
    for boolean_rules in boolean_rules_validator:
        boolean_error_dict = {}
        print(boolean_rules)
        if int(boolean_rules[0])==0:
            boolean_error_dict[boolean_rules[2]]=boolean_rules[1]
            boolean_error_list.append(boolean_error_dict)
    print("###############################################")
    print("Errors validator")
    if len(Errors_validator)!=0:
        for errors_val in Errors_validator:
            print(errors_val)
        print("###############################################")

    print("Warnings validator")
    if len(Warnings_validator)!=0:
        for warnings_val in Warnings_validator:
            print(warnings_val)
        print("###############################################")
    if len(Errors_validator)!=0 or len(Warnings_validator)!=0 or len(boolean_error_list)!=0:
        message_details.append(Errors_validator+Warnings_validator+boolean_error_list)
        status = False
        return status,message_details
    else:
        status=True
        return status, None


#def warnnings_reported():
def pathloaders(SDS_Json_file,JSON_file_location_path):
    basepath = os.path.dirname(os.path.abspath(SDS_Json_file))
    full_path = os.path.join(basepath, SDS_Json_file)
    return full_path

def JSON_to_SDS_recommended_mandatory_path_convertors(SDS_path_mandatory):
    f = open(SDS_path_mandatory)
    data = json.load(f)
    f.close()
    return data

def file_exists_rules(validator,data,SDS_path):
    print(SDS_path)
    Errors_validator = []
    Warnings_validator = []

    status_value_recommended, status_value_mandatory, status_check_file_json_video_present,Error_Json_File_For_video_name_not_present = validator.is_file_exists(data,SDS_path)
    if len(Error_Json_File_For_video_name_not_present)==0:
        for key, value in status_check_file_json_video_present.items():
            print(status_check_file_json_video_present[key])
            if status_check_file_json_video_present[key] == True:
                status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
                print(status_check + "JSON File and Video File with same name present in :"+str(key))
    else:
        print(Error_Json_File_For_video_name_not_present)
        Errors_validator.append(Error_Json_File_For_video_name_not_present)
    if status_value_mandatory:
        print("Error: missing files in"+str(status_value_mandatory))
        Errors_validator.append(status_value_mandatory)

    if status_value_recommended:
        print("recommended: missing files in" + str(status_value_recommended))
        Warnings_validator.append(status_value_recommended)
    return Errors_validator,Warnings_validator

def file_exists_rules_single(validator,data,SDS_path):
    print(SDS_path)
    Errors_validator = []
    Warnings_validator = []

    status_value_recommended, status_value_mandatory, status_check_file_json_video_present,Error_Json_File_For_video_name_not_present = validator.if_file_exists_single(data,SDS_path)
    if len(Error_Json_File_For_video_name_not_present)==0:
        for key, value in status_check_file_json_video_present.items():
            print(status_check_file_json_video_present[key])
            if status_check_file_json_video_present[key] == True:
                status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
                print(status_check + "JSON File and Video File with same name present in :"+str(key))
    else:
        print(Error_Json_File_For_video_name_not_present)
        Errors_validator.append(Error_Json_File_For_video_name_not_present)
    if status_value_mandatory:
        print("Error: missing files in"+str(status_value_mandatory))
        Errors_validator.append(status_value_mandatory)
        #status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        #print(status_check+"Mandatory Files Present"+str(data["Mandatory_recommended_file_info"]["Mandatory_files"]))

    if status_value_recommended:
        print("recommended: missing files in" + str(status_value_recommended))
        #status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        #print(status_check+"recommended Files Present"+str(data["Mandatory_recommended_file_info"]["recommended_files"]))
        Warnings_validator.append(status_value_recommended)
    return Errors_validator,Warnings_validator


def ValidateFolder(path_to_raw_folder):
    SDS_recommed_mandatory = "recommend_mandatory_and_details_check.json"
    sds_raw_path = path_to_raw_folder
    JSON_data = JSON_to_SDS_recommended_mandatory_path_convertors(SDS_recommed_mandatory)
    SDS_files = get_file_paths(sds_raw_path)
    validator = SDSValidator()
    boolean_rules_validator = rulers_Validator(validator, SDS_files, JSON_data)
    #boolean_rules_info(boolean_rules_validator)
    Errors_validator,Warnings_validator  = file_exists_rules(validator, JSON_data, sds_raw_path)
    status, message = Validator_error_all(boolean_rules_validator,Errors_validator,Warnings_validator)
    return status, message

def ValidateFile(path_to_file):
    with open(path_to_file) as f:
        lines = f.readlines()
        all_raw_paths_info = []
        for line in lines:
            all_raw_paths_info.append(line)
    SDS_recommed_mandatory = "recommend_mandatory_and_details_check.json"
    sds_raw_path = all_raw_paths_info[0]
    JSON_data = JSON_to_SDS_recommended_mandatory_path_convertors(SDS_recommed_mandatory)
    SDS_files = get_file_paths(sds_raw_path)
    validator = SDSValidatorTest()
    boolean_rules_validator = rulers_Validator(validator, SDS_files, JSON_data)
    #boolean_rules_info(boolean_rules_validator)
    Errors_validator, Warnings_validator = file_exists_rules(validator, JSON_data, sds_raw_path)
    Validator_error_all(boolean_rules_validator, Errors_validator, Warnings_validator)


