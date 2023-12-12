from SDSValidator.sds_validator_evaluator import JSON_to_SDS_recommended_mandatory_path_convertors,get_file_paths,rulers_Validator,Validator_error_all,file_exists_rules,file_exists_rules_single
from SDSValidator.sds_validator import SDSValidatorTest
import os

def validateFolder(path_to_raw_folder):
    #SDS_recommed_mandatory = "SDSValidator\\recommend_mandatory_and_details_check.json"
    SDS_recommed_mandatory = os.path.join("SDSValidator","recommend_mandatory_and_details_check.json")
    sds_raw_path = path_to_raw_folder
    JSON_data = JSON_to_SDS_recommended_mandatory_path_convertors(SDS_recommed_mandatory)
    SDS_files = get_file_paths(sds_raw_path)
    validator = SDSValidatorTest()
    boolean_rules_validator = rulers_Validator(validator, SDS_files, JSON_data)
    Errors_validator,Warnings_validator  = file_exists_rules(validator, JSON_data, sds_raw_path)
    status, message = Validator_error_all(boolean_rules_validator,Errors_validator,Warnings_validator)
    return status, message