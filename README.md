# SDS
Developing a File standardization software for sensor data structure

## SDS_Assembler_as_library

from SDSAssembler import compileSource, createRaw 
 

# path_to_source_directory: a list including a single directory, or multiple directories 

# path_to_compiled_CSV: where to write the output 

# data: the same CSV in a Pandas DataFrame format 

data = compileSource(path_to_source_directory, path_to_compiled_CSV) 

 
# input: either path_to_compiled_CSV or data (Pandas DataFrame) 

# path_to_raw_directory: where to create Raw. You will create a raw directory, if it is not already there. You will create empty README and dataset_description.JSON files, if there are not already there. For all other files (video, JSON, etc.) you can overwrite.  

# status: True/False 

status = createRaw(input, path_to_raw_directory) 


