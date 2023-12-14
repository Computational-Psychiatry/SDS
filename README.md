#### SDS - (Sensor Data Strcuture)
Description to be added by John
Developing a file name standard for sensor data structure

Pre-requisties:
Installation of python version 

#### General instructions:
1. pip install -r requirmenets_updated.txt
2. The sample dataset is located in the source directory
3. Provide the location of source folder when you download this repository in "source_file_details.txt"


#### Sensor Data strcuture instructions to run the Assembler 
1. Change directory to SDS_Assembler_as_library 
2. Provide Source directory path
3. Provide the path of the complied csv containing the details of all the filenames and field names associated with it.

## SDS_Assembler_as_library
```python
from SDSAssembler import compileSource, createRaw 
```
## compileSource:
### compile source 
#### path_to_source_directory: a list including a single directory, or multiple directories 
#### path_to_compiled_CSV: where to write the output 

```python
data = compileSource(path_to_source_directory, path_to_compiled_CSV)
```

Output: The sample csv file is located in : 


## createRaw
#### data: the same CSV in a Pandas DataFrame format  
#### input: either path_to_compiled_CSV or data (Pandas DataFrame) 
#### path_to_raw_directory: where to create Raw. You will create a raw directory, if it is not already there. You will create empty README and dataset_description.JSON files, if there are not already there. For all other files (video, JSON, etc.) you can overwrite.  

```python
status = createRaw(input, path_to_raw_directory) 
status: True/False 
```

## SDS_Assembler_as_executable
- Creating CSV containing all details of JSON Fieldnames of all source files

#### sdsAssembler -s path-to-source-directory-text-file -o path-to-CSV-file 
#### Input: Path-to-directory-in-a-text-file-containing-source-folder-locations, a simple text file including source directories, each in a separate line 
#### Output: Path-to-CSV-file : It creates a CSV file compiling all available video/audio files 
```
C:\Users\pargim\PycharmProjects\SDS_assembler_as_executable>python3 main.py -s "C:\Users\pargim\PycharmProjects\SDS_assembler_as_executable\SDS_assembler\source_details_doc.txt" -o "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_executable\\SDS_assembler\\testo_new_executable_updated_1.csv"
```
- Creating raw folder from the CSV filenames containing the details of the source
#### sdsAssembler -i path-to-CSV-file -o path-to-raw-directory 

#### Input: path-to-CSV-file

#### Output: <path-to-raw-directory> You will create a raw directory, if it is not already there. You will create empty README and dataset_description.JSON files, if there are not already there. For all other files (video, JSON, etc.) you can overwrite.  

```
C:\Users\pargim\PycharmProjects\SDS_assembler_as_executable>python3 main.py --s "C:\Users\pargim\PycharmProjects\SDS_assembler_as_executable\SDS_assembler\source_details_doc.txt" --o "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_executable\\SDS_assembler\\testo_new_executable_updated_1.csv"

```

## SDS_Validator_as_Library

```python
from SDSValidator import validateFile, validateDirectory 
```
- ### Input : path_to_a_single_file(relative to Raw root) 

```python
status, message = validateFile(path_to_a_single_file) 
status: True/False
{filename:message}
```
#### output {message: warning or error message; None if it is successful}  

- ### Input : path_to_raw_root_directory

#### message: warning or error messages for all directories and files(Dictionary) 
#### {filename: message} 
#### None if all are successful 
```python
status, messages = validateDirectory(path_to_raw_root) 
``` 
## SDS_Validator_as_Executable

### - sdsValidator -f path-to-a-single-file [-o path-to-output-file] 

#### Input: <path-to-a-single-file>, a single video or audio file. Program checks for file-level-rule. The path has to be given relative to Raw root 

#### Output: True/False, whether it satisfies the rules or not 

#### OPTIONAL: if -o is used, write messages to the file  

```Python
(base) C:\Users\pargim\PycharmProjects\SDS_evaluator_as_executable>python3 main.py -f "C:\\Users\\pargim\\PycharmProjects\\SDS_evaluator_as_library\\20230628_example_SDS\\raw\\sub-ACES007\\ses-1\\sdsvideo\\sub-ACES007_ses-1_task-CASS_cnd-Bored_tgt-Participant_run-2_dev-goProHero11Black_rgba.mp4" -o "C:\\Users\\pargim\\PycharmProjects\\test_validator_outcome_exe_single_file_1.txt"
```

 

### - sdsValidator -d path-to-raw-root [-o path-to-output-file] 

#### Input: <path-to-raw-root> 

#### Output: True/False, whether all directories and files satisfy all rules or not. Also print warnings and errors (but not success). 

#### <File or directory name> : <warning or error message> 

#### OPTIONAL: if -o is used, write messages to the file  

```Python
(base) C:\Users\pargim\PycharmProjects\SDS_evaluator_as_executable>python3 main.py -d "C:\\Users\\pargim\\PycharmProjects\\SDS_evaluator_as_library\\20230628_example_SDS\\raw\\" -o "C:\\Users\\pargim\\PycharmProjects\\test_validator_outcome_exe_1.txt"
```













