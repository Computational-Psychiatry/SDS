import os.path
from SDSValidator import ValidateFile, ValidateFolder

def main():
    path_to_raw_folder = "C:\\Users\\pargim\\PycharmProjects\\SDS_evaluator_as_library\\20230628_example_SDS\\raw\\"
    path_to_file=""
    #path_to_file = "C:\\Users\\pargim\\PycharmProjects\\raw_file_paths.txt"
    #path_to_raw_folder = ""
    #path_to_file = "C:\\Users\\pargim\\PycharmProjects\\Sds_grant_evaluavtor_as_library\\20230628_example_SDS\\raw\\sub-ACES007\\ses-1\\sdsvideo\\sub-ACES007_ses-1_task-CASS_cnd-Bored_tgt-Participant_run-2_dev-goProHero11Black_rgba.mp4"

    if os.path.exists(path_to_raw_folder) or os.path.exists(path_to_file):
        if path_to_raw_folder:
            status, message = ValidateFolder.validateFolder(path_to_raw_folder)
            print("Done#################################################################################################1")
            print("The status is:")
            print(status)
            print("The message is:")
            print(message)

        if path_to_file:
            print("here")
            status, message = ValidateFile.validateFile(path_to_file)
            print("The status is:")
            print(status)
            print("The message is:")
            print(message)
            print("Done#################################################################################################2")
    else:
        print("Please provide either the location of raw folder path or a file which contains the information of raw folder location")

main()

