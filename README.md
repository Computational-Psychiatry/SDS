# SDS(Repository and README underconstruction)
Developing a streamlined software for sensor data structure
## SDS_Validator 
### Rules information:
-	Each file satisfies naming requirements
-	All necessary files exists
1. Top_level_rules    
2. Session_level_rules
3. File_level_rules
4. Check for Mandatory Files: dataset_description.json and README are mandatory files
5. Recommeded Files are: 'CHANGES', 'LICENSE' filenames
6. Each data file should a corresponding JSON file
7. if the file is under “ses-xxx” directory, the file name must have “ses-xxx” as well

### Instructions to Run the code to evaluate all the rules

```
python3 sds_validator_evaluator.py
```

### The output of this running this code is shown as below:

```
✓ ['top_level_rules'] /dataset_description.json
/README
✓ ['top_level_rules'] /README
/sub-tbx001\sub-tbx001_scans.json
✓ ['session_level_rules'] /sub-tbx001\sub-tbx001_scans.json
/sub-tbx001\sub-tbx001_scans.tsv
✓ ['session_level_rules'] /sub-tbx001\sub-tbx001_scans.tsv
/sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_events.json
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_events.json
/sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_events.tsv
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_events.tsv
/sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_rgbd.json
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_rgbd.json
/sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_rgbd.mkv
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsmix\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-kinectazure_rgbd.mkv
/sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_events.json
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_events.json
/sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_events.tsv
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_events.tsv
/sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_rgba.json
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_rgba.json
/sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_rgba.mov
✓ ['file_level_rules', 'Folder ses and File contains ses'] /sub-tbx001\ses-001\sdsvideo\sub-tbx001_ses-001_task-if_cnd-anger_run-1_dev-sonya6400_rgba.mov
✓Mandatory Files Present['dataset_description.json', 'README']
True
✓JSON File and Video File with same name present in :C:\Users\pargim\PycharmProjects\SDS_grant\20230628_example_SDS\raw\sub-tbx001\ses-001\sdsmix
True
✓JSON File and Video File with same name present in :C:\Users\pargim\PycharmProjects\SDS_grant\20230628_example_SDS\raw\sub-tbx001\ses-001\sdsvideo
C:\Users\pargim\PycharmProjects\SDS_grant\sds_validator\sds_validator.py:211: UserWarning: Recommeded files not present
  warnings.warn("Recommeded files not present")
```

