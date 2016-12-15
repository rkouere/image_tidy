import argparse
import sys
import os
import re

class picutre_tidy(object):
    def __init__(self, path):
        '''
        Initialise the path to parse
        path = the path to parse
        '''
        self.path = path
        self.pattern_file_name = re.compile('.*(jpg|mp4)')
        self.pattern_get_folder_name = re.compile('IMG_(\d*)_\d*\.jpg')
        self.folder_names = []
        self.get_images()
        self.get_folder_names()

    def get_images(self):
        '''
        Get a list of the files in the folder
        '''
        self.pictures = os.listdir(self.path)

    def _check_image_is_ok(self, name):
        '''
        Checks that the files are jpgs
        '''
        # if the filename finishes is an image/video
        if self.pattern_file_name.match(pic) is not None:
            return True

    def get_folder_name_from_filename(self, filename):
        '''
        Extract the date from the filename.
        Returns the file name
        '''


    def get_folder_names(self):
        '''
        Goes through the file names and get the folder names
        if they do not exists.
        '''
        regex_result_tmp = ""
        date_tmp = ""
        for pic in self.pictures:
            if self._check_image_is_ok(pic):
                try:
                    regex_result_tmp = self.pattern_get_folder_name.search(pic).group(1)
                except Exception as e:
                    print(pic)
                    print(e)
                date_tmp = regex_result_tmp[4:6] + "-" + regex_result_tmp[0:4]
                if date_tmp not in self.folder_names:
                    self.folder_names.append(date_tmp)
        print(self.folder_names)



#print(os.listdir("/home/rkouere/Pictures"))



def main():
    # Install the argument parser. Initiate the description with the docstring
    argparser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__)
    # this is a option which need one extra argument
    argparser.add_argument("-f",
                           '--folder',
                           required=True,
                           help="The path of the folder where the pics are")
    arguments = argparser.parse_args()
    prog = picutre_tidy(arguments.folder)

# This is a Python's special:
# The only way to tell wether we are running the program as a binary,
# or if it was imported as a module is to check the content of
# __name__.
# If it is `__main__`, then we are running the program
# standalone, and we run the main() function.
if __name__ == "__main__":
    main()
