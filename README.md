# SDS

<p> Sensor Data Structure(SDS) is a Python library for creating raw directory from source folders and validating the filename standards of raw directory.<br>

**SDS** consists of two main components:</p>

* **Assembler** : Creating standardized raw directory and it's folder/filenames structure from source folder using json metadata information.
* **Validator** :  Validating standardized raw filenames for any anamolies.
  

### Table of contents: 
1. [General Instructions](#requirements)
2. [Assembler](#Assembler)
3. [Validator](#Validator)
4. [Docker setup](#Docker)


## General instructions:
#### Pre-requisties:
* Python3(Required)
* Docker(optional)
#### Installation and Basic information 
* pip install -r requirments.txt
* The sample dataset is located in the sample_test_dataset directory
* All the outputs are stored in the sample_outputs directory


## Assembler

<p>Assembler converts a source folder to the raw directory format</p>

#### Two main steps in Assembler

* **compileSource** : Converting the source folder to a csv format. This CSV contains all the details of the source folder.
* **createRaw** : Generating the raw folder structure from the Complied csv. 

#### Details of sample source dataset and sample compiled csv outputs
* A sample source directory is provided in sample_test_dataset. 
* The sample outputs for complied csv and raw folder structure is provided in sample_outputs directory.

### Assembler as library

```python
from SDS_Assembler import compileSource, createRaw 
```

* #### compileSource:
* Input :path_to_source_directory
* Output: path_to_compiled_csv

* Change directory to Assembler as library(cd Assembler)
* Provide Source directory path in the main_assembler_library.py
* Provide the path of the compiled csv in the main_assembler_library.py

```python
data = compileSource(path_to_source_directory, path_to_compiled_CSV)
```

* #### createRaw:
* Input: path_to_complied_csv
* Output: path_to_raw_folder

* Provide the path for complied csv 
* Provide path for the creation of the raw folder

```python
status = createRaw(input, path_to_raw_directory) 
status: True/False 
```
### Assembler as executable


#### compileSource:
* Input :path_to_source_directory
* Output: path_to_compiled_csv

* Change directory to Assembler as executable 
* Provide Source directory path in the main_assembler_as_executable.py
* Provide the path of the compiled csv in the main_assembler_executable.py

```
Example Windows os:

C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables\SDS_assembler_as_executable>python3 main_assembler_executable.py -s "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_test_dataset\\source_details_doc.txt" --o "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\source_test.csv


Example linux os:

python3 main_assembler_executable.py -s "/home/SDS_master_cloned/SDS/sample_test_dataset/source_details_doc.txt" -o "/home/SDS_master_cloned/SDS/sample_outputs/source_test_exe_1.csv"

```
Inputs and outputs for running on command line:
* -s : specify the path of source folder in a text file
* -o : specify the path of output complied csv


### createRaw:
* Input: path_to_complied_csv
* Output: path_to_raw_folder

1. Change directory to Assembler 
2. Provide Source directory path in the main_assembler_as_executable.py
3. Provide the path of the compiled csv in the main_assembler_executable.py


```python

on windows:

###To generate raw from csv
(base) C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables\SDS_assembler_as_executable>python3 main_assembler_executable.py -i "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\source_test.csv" -o "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\raw"

on linux:
###  

python3 main_assembler_executable.py -o "/home/SDS_master_cloned/SDS/sample_outputs/raw/" -i "/home/SDS_master_cloned/SDS/sample_outputs/source_test_exe_1.csv"

```

## Validator

<p>Validator validates the raw directory format created by assembler for any anamolies.</p>



#### Details of sample raw dataset and sample raw dataset validated outputs
* Valdiation can be performed either on a single file or the whole raw directory 
* Validation directory: A sample raw dataset is provided in sample_outputs/raw/. 
* Validation File: The sample outputs for validation are raw_file_validator.txt and raw_folder_validator.txt located in the sample_outputs directory.

## Validator as Library

```python
from SDSValidator import validateFile, validateDirectory 

```
#### Validating a single file:
* Input: Provide the path of single file in raw folder to be validated
* Output :  {message: warning or error message; None if it is successful}  
```python
status, message = validateFile(path_to_a_single_file) 
status: True/False
{filename:message}
```
### Validating the whole raw directory:

* Input: Provide the path of raw folder to be validated
* Output : {message: warning or error messages for all directories and files; None if all are successful} 

```python
status, messages = validateDirectory(path_to_raw_root) 
``` 

## Validator as Executable

#### Validating a single file
* Input: -f - path to single file. <path-to-a-single-file>, a single video or audio file. Program checks for file-level-rule. The path has to be given relative to Raw root 
* Output: -o - path to output file.  True/False, whether it satisfies the rules or not 
  
#### OPTIONAL: if -o is used, write messages to the file  

```Python
*Windows
(base) C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables_updated\Validator>python3 main_validator_executable.py -f "C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables_updated\sample_outputs\raw\sub-ACES007\ses-1\sdsvideo\sub-ACES007_ses-1_task-CASS_cnd-Bored_tgt-Participant_run-2_dev-goProHero11Black_rgba.mp4" -o "C:\Users\pargim\PycharmProjects\All_SDS_libraries_and_executables_updated\sample_outputs\test_validator_outcome_exe_single_file_1.txt"

*Linux
/home/SDS_master_cloned/SDS/Validator# python3 main_validator_executable.py -f "/home/SDS_master_cloned/SDS/sample_outputs/raw/sub-ACES007/ses-1/sdsvideo/sub-ACES007_ses-1_task-CASS_cnd-Bored_tgt-Participant_run-2_dev-goProHero11Black_rgba.mp4" -o "/home/SDS_master_cloned/SDS/sample_outputs/raw_file_validated.txt"
```

#### Validating the raw folder


* Input: -d <path-to-raw-root>, a single video or audio file. Program checks for file-level-rule. The path has to be given relative to Raw root 
* Output: -o - path to output file.  True/False, whether all directories and files satisfy all rules or not. Also print warnings and errors (but not success).  OPTIONAL: if -o is used, write messages to the file   

```Python
*Windows
python3 main_validator_executable.py -d "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\raw" -o "C:\\Users\\pargim\\PycharmProjects\\All_SDS_libraries_and_executables_updated\\sample_outputs\\test_validator_outcome_exe_1.txt"

*Linux
python3 main_validator_executable.py -d "/home/SDS_master_cloned/SDS/sample_outputs/raw" -o "/home/SDS_master_cloned/SDS/sample_outputs/raw_folder_validated.txt"
```

## Docker
#### Install of docker:
https://docs.docker.com/get-docker/
https://docs.docker.com/engine/install/
https://www.digitalocean.com/community/tutorial-collections/how-to-install-and-use-docker

## SDS_docker_contariner located on docker_hub:
* create an account on docker hub([docker_hub](https://hub.docker.com/))
* Link <a href="[http://www.something.com](https://hub.docker.com/repository/docker/7090496133/sds_format_generator/general)"> Docker hub link SDS container </a>
* Link <a href="[http://www.something.com](https://hub.docker.com/repository/docker/7090496133/sds_format_generator/general)"> Docker hub link SDS container </a>
  

## Instructions to run docker on our server(ws03):
*   systemctl restart docker
*   docker ps -a(to view all the docker images)
*   docker start 7f16 (docker starting of the image instance)
*   docker exec -it 7f16 bash(This command will take you inside the docker container)

### Insider the docker container:

*  Running of Assembler (root@<Container ID>):
  ```
   1.  cd  /home/SDS_latest/SDS/Assembler/
   2. Creating csv from source: /home/SDS_latest/SDS/Assembler/# python3 main_assembler_executable.py -s "/home/SDS_latest/SDS/sample_test_dataset/source_details_doc.txt" -o "/home/SDS_latest/SDS/sample_outputs/source_test_exe_1.csv"
   3. Creating raw folder/files from csv : python3 main_assembler_executable.py -o "/home/SDS_latest/SDS/sample_outputs/raw/" -i "/home/SDS_latest/SDS/sample_outputs/source_test_exe_1.csv"
 ```
* Running of Validator(root@<container_id>):
```
  1. cd /home/SDS_latest/SDS/Validator/
  2. Validating a file : /home/SDS_latest/SDS/Validator# python3 main_validator_executable.py -d "python3 main_validator_executable.py -f "/home/SDS_latest/SDS/sample_outputs/raw/sub-ACES007/ses-1/sdsvideo/sub-ACES007_ses-1_task-CASS_cnd-Bored_tgt-Participant_run-2_dev-goProHero11Black_rgba.mp4" -o ""/home/SDS_latest/SDS/sample_outputs/raw/raw_file_validated.txt"  "/home/SDS/outputs/Validation_outcomes_docker_updated.txt"):  
  3. Validating a folder:  python3 main_assembler_executable.py -d ""/home/SDS_latest/SDS/sample_outputs/raw/" -o ""/home/SDS_latest/SDS/sample_outputs/raw/Validation_outcomes_docker_updated.txt"  
```

#### Commands to run on linux or Mac to exec :
* docker pull 7090496133/sds_format_generator:version
* docker run -it 7090496133/sds_format_generator:version 
* exit out of docker using exit command
* docker exec -it 7090496133/sds_format_generator:version bash or docker exec -it <Container ID> bash













