# SDS_Assembler(Repository under construction)
SDS_Assembler - Developing a streamlined software for validation of sensor data structure

## To run the code for csv generator 
```
python CSV_creator_from_filenames.py --path_source_folder "path_to_source_folder" --path_raw_folder "path_to_raw_folder" --write_csv_detailed_info_location_path "path_to_csv_location"

```

```
example:

>python CSV_creator_from_filenames.py --path_source_folder "C:\Users\pargim\PycharmProjects\SDS_grant_assembler\SDS_assembler\source" --path_raw_folder "C:\Users\pargim\PycharmProjects\SDS_grant_assembler\SDS_assembler\raw" --write_csv_detailed_info_location_path "C:\Users\pargim\PycharmProjects\SDS_grant_assembler\SDS_assembler\detailed_info_json_all_fields_filenames.csv"
```

## To run the code for csv generator 
```
python csv_sds_creator.py --path_source_folder "path_to_source_folder" --path_raw_folder "path_to_raw_folder" --read_csv_detailed_info_location_path "path_to_csv_location"

```

```
example:

python csv_sds_creator.py --path_source_folder "C:\Users\pargim\PycharmProjects\SDS_grant_assembler\SDS_assembler\source" --path_raw_folder "C:\Users\pargim\PycharmProjects\SDS_grant_assembler\SDS_assembler\raw" --read_csv_detailed_info_location_path "C:\Users\pargim\PycharmProjects\SDS_grant_assembler\SDS_assembler\detailed_info_json_all_fields_filenames.csv"

```


### Instructions run
##### Clear all files and folders within the raw folder
##### Run the csv_generator.py by provding the source_folder_path, raw_folder_path and path_to_write_csv. 
##### Run the csv_sds_creator.py by provding the source_folder_path, raw_folder_path and path_to_read_csv. 

