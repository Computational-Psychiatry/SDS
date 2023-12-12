import os
from SDS_validator_as_library.SDSValidator import ValidateFile, ValidateFolder

def main():
    """

    This function validates either a raw folder or a specific file,
    and writes the validation results to separate output files.

    Args:
        None

    Returns:
        None

    """

    # Define base directory paths
    BASE_DIR = "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables\\"
    RAW_FOLDER_DIR = os.path.join(BASE_DIR, "raw")
    RAW_FILE_PATH = "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables\\20230628_example_SDS\\raw\\sub-ACES007\\ses-1\\sdsvideo\\sub-ACES007_ses-1_task-CASS_cnd-Bored_tgt-Participant_run-2_dev-goProHero11Black_rgba.mp4"
    OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

    # Check if raw folder exists
    if os.path.exists(RAW_FOLDER_DIR):
        # Validate the raw folder
        status, message = ValidateFolder.validateFolder(RAW_FOLDER_DIR)
        print("Done validating raw folder.")
        print("Status:", status)
        print("Message:", message)

        # Write validation results to a file
        output_file = os.path.join(OUTPUTS_DIR, "raw_folder_validation.txt")
        with open(output_file, "w") as f:
            f.write(f"{status}\n{message}")

    # Check if raw file exists, otherwise check for folder info file
    if os.path.exists(RAW_FILE_PATH):
        # Validate the raw file
        status, message = ValidateFile.validateFile(RAW_FILE_PATH)
        print("Done validating raw file.")
        print("Status:", status)
        print("Message:", message)

        # Write validation results to a file
        output_file = os.path.join(OUTPUTS_DIR, "raw_file_validation.txt")
        with open(output_file, "w") as f:
            f.write(f"{status}\n{message}")

    else:
        # No valid input provided
        print("Please provide either the raw folder path or a file containing the raw folder information.")


main()
