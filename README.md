# image_tidy

The aim of this program is to take the images from an android phone, extract the information regarding the date, create the necessary folders and move the images in the folders.

It will work on any jpg or 3gp file which follows the following pattern: [any letter]_[year][month][day]_[anything]

Usage:
```
usage: class_photos.py [-h] -i FOLDER_IN [-o FOLDER_OUT]
                       [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
class_photos.py: error: the following arguments are required: -i/--folder_in
```

If no FOLDER_OUT is provided, the program will use the FOLDER_IN folder as a destination folder.

If some files have not been recognised, the program will list them at the end.
