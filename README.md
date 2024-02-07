# SDS

<p> Sensor Data Structure(SDS) is a Python library for creating and validating a filename standards for raw video files.<br>

**SDS** consists of two main components:</p>

* **Assembler** : Creating standardized dervied filenames from raw files using json metadata information.
* **Validator** :  Validating dervied filenames for any anamolies.
  

### Table of contents: 
1. [General Instructions](#requirements)
2. [Assembler](#Assembler)
3. [Validator](#Validator)
4. [Docker setup](#Docker)


## General instructions:
### Pre-requisties:
Python3(Required)
Docker(optional)
### Installation and Basic information 
* pip install -r requirments.txt
* The sample dataset is located in the sample_test_dataset directory
* All the outputs are stored in the sample_outputs directory

#### Sensor Data strcuture instructions to run the Assembler and Validator

## Assembler

Assembler converts a source folder to the raw directory format. There are two main steps involved:

a) Converting the source folder to a csv format. This CSV contains all the details of the source folder.
b) Generating the raw folder structure from the Complied csv. 

A sample source directory is provided in sample_test_dataset. 
The sample outputs for complied csv and raw folder structure is provided in sample_outputs directory.

### Assembler as library

```python
from SDS_Assembler import compileSource, createRaw 
```

### A) Steps to capture all source directory details into a complied csv:

#### compileSource:
Input :path_to_source_directory
Output: path_to_compiled_csv

1. Change directory to Assembler 
2. Provide Source directory path in the main_assembler_library.py
3. Provide the path of the compiled csv in the main_assembler_library.py

```python
data = compileSource(path_to_source_directory, path_to_compiled_CSV)
```

### B) To create raw folder structure from the complied csv source files:

### createRaw:
Input: path_to_complied_csv
Output: path_to_raw_folder

1. Provide the path for complied csv 
2. Provide path for the creation of the raw folder

```python
status = createRaw(input, path_to_raw_directory) 
status: True/False 
```
### Assembler as executable

### A) Steps to capture all source directory details into a complied csv:

#### compileSource:
Input :path_to_source_directory
Output: path_to_compiled_csv

1. Change directory to Assembler 
2. Provide Source directory path in the main_assembler_as_executable.py
3. Provide the path of the compiled csv in the main_assembler_executable.py

```
Example Windows os:

C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables\SDS_assembler_as_executable>python3 main_assembler_executable.py -s "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_test_dataset\\source_details_doc.txt" --o "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\source_test.csv

Example Linux os:

/home/SDS/SDS_assembler_as_executable# python3 main.py -s "/home/SDS/source_details_doc.txt" -o "/home/SDS/outputs/source_test.csv"
```
Inputs and outputs for running on command line:
a) -s : specify the path of source folder in a text file
b) -o : specify the path of output complied csv

### B) To create raw folder structure from the complied csv source files:

### createRaw:
Input: path_to_complied_csv
Output: path_to_raw_folder

1. Change directory to Assembler 
2. Provide Source directory path in the main_assembler_as_executable.py
3. Provide the path of the compiled csv in the main_assembler_executable.py


```python

on windows:

###To generate raw from csv
(base) C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables\SDS_assembler_as_executable>python3 main_assembler_executable.py -i "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\source_test.csv" -o "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\raw"

on linux:
###  


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
## Docker
#### Install of docker:
https://docs.docker.com/get-docker/
https://docs.docker.com/engine/install/
https://www.digitalocean.com/community/tutorial-collections/how-to-install-and-use-docker

## SDS_docker_contariner located on docker_hub:
create an account on docker hub(provide link)
Use the command to pull docker image:
docker pull 7090496133/sds_format_generator:version
https://hub.docker.com/repository/docker/7090496133/sds_format_generator/general
https://hub.docker.com/repository/docker/7090496133/sds_format_generator/tags?page=1&ordering=last_updated

### Instructions to run docker on our server(ws03):
1. systemctl restart docker
2. docker ps -a(to view all the docker images)
3. docker start sds_container (docker starting of the image instance)
b)           docker exec -it sds_container bash(This command will take you inside the docker container)
Insider the docker container:
c)            Running of SDS_assembler_as_exceutable(root@ba8fd8ab4a84:/home/SDS/SDS_assembler_as_executable# python3 main.py --s "/home/SDS/source_details_doc.txt" --o "/home/SDS/outputs/source_test_exe_1.csv"):
1. cd /home/SDS/SDS_assembler_as_executable
2. python3 main.py --s "/home/SDS/source_details_doc.txt" --o "/home/SDS/outputs/source_test_exe_1.csv"
d)           Running of SDS_validator_as_exceutable(root@ba8fd8ab4a84:/home/SDS/SDS_assembler_as_executable# python3 main.py -d "/home/SDS/outputs/raw/" -o "/home/SDS/outputs/Validation_outcomes_docker_updated.txt"):
1. cd /home/SDS/SDS_validator_as_executable
2. python3 main.py -d "/home/SDS/outputs/raw/" -o "/home/SDS/outputs/Validation_outcomes_docker_updated.txt"  


Instructions to run on other linux machine or macos:
a) Create an account on dockerhub
b) docker pull 7090496133/sds_format_generator:version
c) docker run -it 7090496133/sds_format_generator:version 
d) docker run -it <mynewimage:latest> 7090496133/sds_format_generator:version
e) exit out of docker using exit command
f) docker exec -it <mynewimage:latest> bash

Same instructions

docker start 














