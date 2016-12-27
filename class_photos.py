import argparse
import sys
import os
import re
import logging

class picutre_tidy(object):
    def __init__(self, path):
        '''
        Initialise the path to parse
        path = the path to parse
        '''
        self.path = self.check_path_without_slash(path)
        self.check_path_without_slash(path)
        self.pattern_file_name = re.compile('.*(jpg|mp4)')
        self.pattern_get_folder_name = 'IMG_(\d*)_.*\.jpg'
        self.folder_names = []
        self.get_images()
        self.get_folder_names()
        self.folder_out = self.path

    def check_path_without_slash(self, path):
        '''
        Checks that the path does not finish with a slash
        '''
        if path[-1] is "/":
            return path[:-1]
        else:
            return path

    def get_images(self):
        '''
        Get a list of the files in the folder
        '''
        logging.info("Getting all the images/mp4 from " + self.path)
        self.pictures = os.listdir(self.path)

    def _check_image_extention(self, name):
        '''
        Checks that the files are jpgs
        '''
        # if the filename finishes is an image/video
        if self.pattern_file_name.match(name) is not None:
            return True

    def _get_folder_name_from_filename(self, filename):
        '''
        Extract the date from the filename.
        If the pattern is found: returns the file name
        If not: returns None
        '''
        if self._check_image_extention(filename):
            m = re.search(self.pattern_get_folder_name, filename)
            if m is not None:
                regex_result_tmp = m.group(1)
                return regex_result_tmp[4:6] + "-" + regex_result_tmp[0:4]
            else:
                return None

    def get_folder_names(self):
        '''
        Goes through the file names and get the folder names
        if they do not exists.
        '''
        logging.info("Generates the folder names from the filenames")
        date_tmp = ""
        for pic in self.pictures:
            date_tmp = self._get_folder_name_from_filename(pic)
            if date_tmp is not None:
                if date_tmp not in self.folder_names:
                    self.folder_names.append(date_tmp)
        logging.debug(self.folder_names)

    def add_out_folder(self, path):
        '''
        Adds the path of the destination folder and creates it if needed.
        '''
        logging.info("Creating the destination folder if it doesn't exist")
        self.destination_folder_path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def create_folders(self):
        '''
        Creates the folders
        '''
        logging.info("Creating the folders on disk for each month")
        for folder in self.folder_names:
            logging.debug("Creating folder " + self.path + "/" + folder)
            if not os.path.exists(self.destination_folder_path + '/' + folder):
                os.makedirs(self.destination_folder_path + '/' + folder)

    def copy_files(self):
        '''
        Copy each file to its corresponding folder.
        '''
        logging.info("Copying each files to its corresponding folder")
        for pic in self.pictures:
            print(self._get_folder_name_from_filename(pic))
        


#print(os.listdir("/home/rkouere/Pictures"))



def main():
    logging.basicConfig(level=logging.DEBUG)
    # Install the argument parser. Initiate the description with the docstring
    argparser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__)
    # this is a option which need one extra argument
    argparser.add_argument("-i",
                           '--folder_in',
                           required=True,
                           help="The path of the folder where the pics are")
    argparser.add_argument("-o",
                           '--folder_out',
                           help="The path of the folder where the pics have to be copied")
    arguments = argparser.parse_args()
    prog = picutre_tidy(arguments.folder_in)
    if arguments.folder_out is not None:
        prog.add_out_folder(arguments.folder_out)
    prog.create_folders()
    prog.copy_files()

# This is a Python's special:
# The only way to tell wether we are running the program as a binary,
# or if it was imported as a module is to check the content of
# __name__.
# If it is `__main__`, then we are running the program
# standalone, and we run the main() function.
if __name__ == "__main__":
    main()
