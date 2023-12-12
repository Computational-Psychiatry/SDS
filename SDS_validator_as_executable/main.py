import argparse
# Import custom validation functions from SDSValidator module
from SDSValidator import ValidateFile, ValidateFolder


def _print_validation_summary(status, message_list):
    """
    Prints a summary of the validation results to the console.

    Args:
        status (bool): Overall validation status (True for success, False for errors).
        message_list (list[str]): List of validation messages.
    """
    print("Validation Summary:")
    if status:
        print("  - Success!")
    else:
        print(f"  - {len(message_list)} errors detected.")
    print("")


def _write_validation_messages(message_list, output_file_path):
    """
    Writes the validation messages to a specified file.

    Args:
        message_list (list[str]): List of validation messages.
        output_file_path (str): Path to the output file.
    """
    print("The message list is:")
    print(message_list)
    with open(output_file_path, 'w') as f:
        for message in message_list:
            f.write(str(message))

    print(f"Validation messages written to: {output_file_path}")


def main():
    """
    Main function to handle user input and perform validation.
    """

    # Create argument parser for user input
    parser = argparse.ArgumentParser()

    # Define arguments for raw folder directory, output message rules, and single file
    parser.add_argument('-d', type=str, help='Specify the path of the raw folder directory to validate.')
    parser.add_argument('-o', type=str, help='Specify the output file to write validation messages (optional).')
    parser.add_argument('-f', type=str, help='Specify a single file within the raw directory to validate (optional).')

    # Parse user arguments
    args = parser.parse_args()

    # Handle different user input combinations
    if args.d:
        # Validate entire raw folder
        status, message_list = ValidateFolder.validateFolder(args.d)
        _print_validation_summary(status, message_list)

        if args.o:
            _write_validation_messages(message_list, args.o)

    elif args.f:
        # Validate a single file within the raw directory
        status, message_list = ValidateFile.validateFile(args.f)
        _print_validation_summary(status, message_list)

        if args.o:
            _write_validation_messages(message_list, args.o)

    else:
        # Handle invalid argument combination
        print("Invalid combination of arguments provided. Please refer to the help for usage instructions.")


if __name__ == "__main__":
    main()