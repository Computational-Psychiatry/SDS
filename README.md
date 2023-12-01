# SDS
Developing a File standardization software for sensor data structure

## SDS_Assembler_as_library(Description)

from SDSAssembler import compileSource, createRaw 
## compileSource:
### compile source 
#### path_to_source_directory: a list including a single directory, or multiple directories 
#### path_to_compiled_CSV: where to write the output 
#### data = compileSource(path_to_source_directory, path_to_compiled_CSV) 

## createRaw
#### data: the same CSV in a Pandas DataFrame format  
#### input: either path_to_compiled_CSV or data (Pandas DataFrame) 
#### path_to_raw_directory: where to create Raw. You will create a raw directory, if it is not already there. You will create empty README and dataset_description.JSON files, if there are not already there. For all other files (video, JSON, etc.) you can overwrite.  

### status = createRaw(input, path_to_raw_directory) 
status: True/False 


## SDS_Assembler_as_executable

```
C:\Users\pargim\PycharmProjects\SDS_assembler_as_executable>python3 main.py -s "C:\Users\pargim\PycharmProjects\SDS_assembler_as_executable\SDS_assembler\source_details_doc.txt" -o "C:\\Users\\pargim\\PycharmProjects\\SDS_assembler_as_executable\\SDS_assembler\\testo_new_executable_updated_1.csv"

```

