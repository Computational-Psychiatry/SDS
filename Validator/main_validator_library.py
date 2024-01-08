import os
from SDSValidator import ValidateFile, ValidateFolder

def main():
    """

    This function validates either a raw folder or a specific file,
    and writes the validation results to separate output files.

    Args:
        None

    Returns:git commit -m "your commit message"
        None

    """

    # Define base directory paths
    BASE_DIR = "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\"
    RAW_FOLDER_DIR = os.path.join(BASE_DIR,"sample_outputs","raw")
    RAW_FILE_PATH = "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\raw\\sub-ACES007\\ses-1\\sdsvideo\\sub-ACES007_ses-1_task-CASS_cnd-Interested_tgt-Participant_run-1_dev-goProHero11Black_rgba.mp4"
    OUTPUTS_DIR = os.path.join(BASE_DIR, "sample_outputs")

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
