"""Validation class for BIDS projects."""
import re
import os
import json
import warnings

class MandatoryFilenameError(Exception):
    pass

class JsonVideoFilenameMismatchError(Exception):
    pass

class SesFolderNameNotPresentInFile(Exception):
    pass

class SDSValidator():
    """Object for BIDS (Brain Imaging Data Structure) verification.

    The main method of this class is `is_bids()`. You should use it for
    checking whether a file path is compatible with BIDS.

    """

    def __init__(self, index_associated=True):
        """Initialize SDSValidator object.

        Parameters
        ----------
        index_associated : bool
            Specifies if an associated data should be checked. If it is true
            then any file paths in directories `code/`, `derivatives/`,
            `sourcedata/` and `stimuli/` will pass the validation, else they
            won't. Defaults to True.

        """
        self.dir_rules = os.path.join(os.path.dirname(__file__)) + "/rules/"
        self.index_associated = index_associated



    def is_sds_filepath(self, path, Json_data):
        """Check if file path adheres to BIDS.

        Main method of the validator. uses other class methods for checking
        different aspects of the file path.

        Parameters
        ----------
        path : str
            Path of a file to be checked. Must be relative to root of a BIDS
            dataset.

        Notes
        -----
        When you test a file path, make sure that the path is relative to the
        root of the BIDS dataset the file is part of. That is, as soon as the
        file path contains parts outside of the BIDS dataset, the validation
        will fail. For example "home/username/my_dataset/participants.tsv" will
        fail, although "participants.tsv" is a valid BIDS file.

        Examples
        --------
        >>> from bids_validator import SDSValidator
        >>> validator = SDSValidator()
        >>> filepaths = ["/sub-01/anat/sub-01_rec-CSD_T1w.nii.gz",
        ... "/sub-01/anat/sub-01_acq-23_rec-CSD_T1w.exe", # wrong extension
        ... "home/username/my_dataset/participants.tsv", # not relative to root
        ... "/participants.tsv"]
        >>> for filepath in filepaths:
        ...     print(validator.is_bids(filepath))
        True
        False
        False
        True

        """
        status = False
        satisfies = []
        if self.is_top_level(path):
            status = True
            satisfies.append('top_level_rules')
            
        if self.is_associated_data(path):
            status = True
            satisfies.append('associated_data_rules')
            
        if self.is_session_level(path):
            status = True
            satisfies.append('session_level_rules')
            
        if self.is_subject_level(path):
            status = True
            satisfies.append('subject_level_rules')
            
        if self.is_phenotypic(path):
            status = True
            satisfies.append('phenotypic_rules')
            
        if self.is_file(path):
            status = True
            satisfies.append('file_level_rules')

        if self.is_file_with_sess_name_containing_sess_dir(path,Json_data):
            if self.is_file(path):
                status = True
                satisfies.append("Folder ses and File contains ses")
        return (status, satisfies)

    def is_top_level(self, path):
        """Check if the file has appropriate name for a top-level file."""
        regexps = self.get_regular_expressions(self.dir_rules +
                                               'top_level_rules.json')

        conditions = [False if re.compile(x).search(path) is None else True for
                      x in regexps]

        return (any(conditions))

    def is_associated_data(self, path):
        """Check if file is appropriate associated data."""
        if not self.index_associated:
            return False

        regexps = self.get_regular_expressions(self.dir_rules +
                                               'associated_data_rules.json')

        conditions = [(re.compile(x).search(path) is not None) for
                      x in regexps]

        return any(conditions)

    def is_session_level(self, path):
        """Check if the file has appropriate name for a session level."""
        regexps = self.get_regular_expressions(self.dir_rules +
                                               'session_level_rules.json')

        conditions = [self.conditional_match(x, path) for x in regexps]

        return (any(conditions))

    def is_subject_level(self, path):
        """Check if the file has appropriate name for a subject level."""
        regexps = self.get_regular_expressions(self.dir_rules +
                                               'subject_level_rules.json')

        conditions = [(re.compile(x).search(path) is not None) for
                      x in regexps]

        return (any(conditions))

    def is_phenotypic(self, path):
        """Check if file is phenotypic data."""
        regexps = self.get_regular_expressions(self.dir_rules +
                                               'phenotypic_rules.json')

        conditions = [(re.compile(x).search(path) is not None) for
                      x in regexps]

        return (any(conditions))

    def is_file(self, path):
        """Check if file is phenotypic data."""
        regexps = self.get_regular_expressions(self.dir_rules +
                                               'file_level_rules.json')

        conditions = [(re.compile(x).search(path) is not None) for
                      x in regexps]

        return (any(conditions))

    def get_regular_expressions(self, file_name):
        """Read regular expressions from a file."""
        regexps = []

        with open(file_name) as fin:
            rules = json.load(fin)

        for key in list(rules.keys()):
            rule = rules[key]

            regexp = rule["regexp"]

            if "tokens" in rule:
                tokens = rule["tokens"]

                for token in list(tokens):
                    regexp = regexp.replace(token, "|".join(tokens[token]))

            regexps.append(regexp)

        return regexps

    def conditional_match(self, expression, path):
        """Find conditional match."""
        match = re.compile(expression).findall(path)
        match = match[0] if len(match) >= 1 else False
        # adapted from JS code and JS does not support conditional groups
        if (match):
            if ((match[1] == match[2][1:]) | (not match[1])):
                return True
            else:
                return False
        else:
            return False

    def is_recommeded_files(self,recommended_files,list_files):
        result = all(elem in recommended_files for elem in list_files)
        if result:
            return True
        else:
            warnings.warn("Recommeded files not present")
            return None

    def is_file_with_sess_name_containing_sess_dir(self,sds_path,Json_data):
        File_video_data_formats_supported = Json_data["Mandatory_recommended_file_info"][
            'File_video_data_formats_supported']
        dir_list = [x[0] for x in os.walk(sds_path)]
        dir_list_of_list = [x.split("\\") for x in dir_list]
        SDS_file_location_directories = ["sdsvideo", "sdsmix",
                                         "sdsdepth"]  ### currently hardcoded should load from file
        list_of_file_directories = []
        for list_value, dir in zip(dir_list, dir_list_of_list):
            for sds_file_location_directory in SDS_file_location_directories:
                if sds_file_location_directory in dir:
                    list_of_file_directories.append(list_value)
        all_video_files = {}
        count_sess = 0
        for list_of_file_directory in list_of_file_directories:
            for file in os.listdir(list_of_file_directory):
                if file.endswith(tuple(File_video_data_formats_supported)):
                    all_video_files[list_of_file_directory] = file
                    sess_name_in_key = [t for t in list_of_file_directory.split("\\") if t.startswith('ses')]
                    sess_name_in_value = [t for t in list_of_file_directory.split("\\") if t.startswith('ses')]
                    if sess_name_in_value == sess_name_in_key:
                        count_sess = count_sess + 1
        if len(list_of_file_directories) == count_sess:
           return True
        else:
            raise SesFolderNameNotPresentInFile("Ses folder name missing in file")

    def is_mandatory_files(self,Mandatory_files,list_files):
        result = all(elem in Mandatory_files for elem in list_files)
        if result:
            return True
        else:
            raise MandatoryFilenameError("Mandatory files missing")


    def is_file_present_video_and_json(self,sds_path,File_video_data_formats_supported):
        dir_list = [x[0] for x in os.walk(sds_path)]
        dir_list_of_list = [x.split("\\") for x in dir_list]
        SDS_file_location_directories = ["sdsvideo", "sdsmix", "sdsdepth"] ### currently hardcoded should load from file
        list_of_file_directories = []
        for list_value, dir in zip(dir_list,dir_list_of_list):
            for sds_file_location_directory in SDS_file_location_directories:
                if sds_file_location_directory in dir:
                    list_of_file_directories.append(list_value)
        status_video_json_files = {}

        for list_of_file_directory in list_of_file_directories:
            all_video_files = []
            all_json_files = []

            for file in os.listdir(list_of_file_directory):
                if file.endswith(tuple(File_video_data_formats_supported)):
                    all_video_files.append(file)
            number_of_video_files = len(all_video_files)
            for video_file in all_video_files:
                if video_file.split(".")[0]+".json" in os.listdir(list_of_file_directory):
                    all_json_files.append(video_file.split(".")[0]+".json")
            number_of_json_files = len(all_json_files)
            if number_of_json_files==number_of_video_files:
                status_video_json_files[list_of_file_directory]=True
            else:
                raise JsonVideoFilenameMismatchError("Json file corresponding to video not found for"+str(list_of_file_directory))

        return status_video_json_files


    def is_file_exists(self,json_data,sds_path):
        recommended_files = json_data["Mandatory_recommended_file_info"]['recommended_files']
        Mandatory_files = json_data["Mandatory_recommended_file_info"]['Mandatory_files']
        File_video_data_formats_supported = json_data["Mandatory_recommended_file_info"]['File_video_data_formats_supported']
        list_files = [f for f in os.listdir(sds_path) if os.path.isfile(os.path.join(sds_path,f))]
        status_value_recommended = self.is_recommeded_files(recommended_files, list_files)
        status_value_mandatory = self.is_mandatory_files(Mandatory_files, list_files)
        status_check_file_json_video_present = self.is_file_present_video_and_json(sds_path,File_video_data_formats_supported)
        return status_value_recommended, status_value_mandatory, status_check_file_json_video_present

