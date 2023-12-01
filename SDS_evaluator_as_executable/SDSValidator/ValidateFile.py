from SDSValidator.sds_validator_evaluator import JSON_to_SDS_recommended_mandatory_path_convertors,get_file_paths,rules_validator_single_file,Validator_error_all,file_exists_rules,file_exists_rules_single
from SDSValidator.sds_validator import SDSValidatorTest

def validateFile(path_to_file):
    SDS_recommed_mandatory = "SDSValidator\\recommend_mandatory_and_details_check.json"
    sds_raw_path = path_to_file
    JSON_data = JSON_to_SDS_recommended_mandatory_path_convertors(SDS_recommed_mandatory)
    SDS_files = sds_raw_path
    validator = SDSValidatorTest()
    boolean_rules_validator = rules_validator_single_file(validator, SDS_files, JSON_data)
    #boolean_rules_info(boolean_rules_validator)
    Errors_validator, Warnings_validator = file_exists_rules_single(validator, JSON_data, sds_raw_path)
    status, message = Validator_error_all(boolean_rules_validator, Errors_validator, Warnings_validator)
    return status,message