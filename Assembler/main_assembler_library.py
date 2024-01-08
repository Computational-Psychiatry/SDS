import pandas as pd
from SDS_assembler import compileSource,createRaw
import os

def main():
    """
        This function compiles SDS source files, generates raw data, and saves it to a specified directory.

        Args:
            None

        Returns:
            None
        """

    # Base directory paths for source , raw  and outputs
    BASE_DIR = "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\"
    BASE_SOURCE_DIR = os.path.join(BASE_DIR,"sample_test_dataset","source")
    BASE_RAW_DIR = os.path.join(BASE_DIR,"sample_outputs","raw")
    BASE_DIR_CSV_output = os.path.join(BASE_DIR,"sample_outputs","Source_SDS_details_complied.csv")

    print(BASE_SOURCE_DIR)
    print(BASE_DIR_CSV_output)

    # Path to the directory containing SDS source files
    source_dir_path = f"{BASE_SOURCE_DIR}"

    # Path to the CSV file containing compiled SDS data
    compiled_csv_path = f"{BASE_DIR_CSV_output}"

    # Path to the CSV file containing raw data (to be generated)
    raw_data_path = f"{BASE_RAW_DIR}"  # Update to desired filename
    print("the source dir path is:")
    print(source_dir_path)
    # Compile the SDS source files
    compiled_data = compileSource.compileSource(source_dir_path, compiled_csv_path if compiled_csv_path else None)

    # Check if a compiled CSV file exists
    if compiled_csv_path and os.path.exists(compiled_csv_path):
        # Read the compiled data as a Pandas DataFrame
        data = pd.read_csv(compiled_csv_path)
    else:
        # Use the directly generated data from compileSource
        data = compiled_data

    # Create the raw data file using the processed data
    status = createRaw.createRaw(data, raw_data_path)

    # Print the status message
    print(f"Raw data creation status: {status}")


main()





