import os
import colorama
from sds_validator import SDSValidator
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

def Validator_error_all(boolean_rules_validator,Errors_validator,Warnings_validator):
    print("Boolean validator")
    for boolean_rules in boolean_rules_validator:
        print(boolean_rules)
    print("###############################################")
    print("Errors validator")
    for errors_val in Errors_validator:
        print(errors_val)
    print("###############################################")
    print("Warnings validator")
    for warnings_val in Warnings_validator:
        print(warnings_val)
    print("###############################################")


#def errors_to_be_raised():


#def warnnings_reported():
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
        #status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        #print(status_check+"Mandatory Files Present"+str(data["Mandatory_recommended_file_info"]["Mandatory_files"]))

    if status_value_recommended:
        print("recommended: missing files in" + str(status_value_recommended))
        #status_check = colorama.Fore.GREEN + '\u2713' + colorama.Fore.RESET
        #print(status_check+"recommended Files Present"+str(data["Mandatory_recommended_file_info"]["recommended_files"]))
        Warnings_validator.append(status_value_recommended)
    return Errors_validator,Warnings_validator

def main():
    SDS_recommed_mandatory = "recommend_mandatory_and_details_check.json"
    sds_base_path = argument_parser(argparse.ArgumentParser())
    sds_base_path = "C:\\Users\\pargim\\PycharmProjects\\SDS_grant\\"
    sds_raw_folder_loc = os.path.join("20230628_example_SDS","raw")
    sds_validator_path = os.path.join(sds_base_path,"sds_validator")
    sds_raw_path = os.path.join(sds_base_path,sds_raw_folder_loc)
    full_path_mandatory = pathloaders(SDS_recommed_mandatory, sds_validator_path)
    JSON_data = JSON_to_SDS_recommended_mandatory_path_convertors(full_path_mandatory)
    SDS_files = get_file_paths(sds_raw_path)
    validator = SDSValidator()
    boolean_rules_validator = rulers_Validator(validator, SDS_files, JSON_data)
    #boolean_rules_info(boolean_rules_validator)
    Errors_validator,Warnings_validator  = file_exists_rules(validator, JSON_data, sds_raw_path)
    Validator_error_all(boolean_rules_validator,Errors_validator,Warnings_validator)


def argument_parser(parser):

    """

    argument_parser: This function is used to parse the python command line arguments provided by user input

    :return all information related to inputs passed by the user

    """

    parser.add_argument("--path_sds_folder", help="Add the path to sds folder once cloned",type=str)
    args = parser.parse_args()

    path_sds_folder = args.path_sds_folder

    return path_sds_folder


if __name__ == "__main__":
   main()

