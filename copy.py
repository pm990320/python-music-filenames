import os
import shutil

# specify the search directory here
TOP_DIRECTORY = "C:/Users/Patrick/Music"
RESULTS_DIRECTORY = "C:/Users/Patrick/Desktop/ALL_MUSIC"

for dirpath, dirnames, filenames in os.walk(TOP_DIRECTORY):
    for file in filenames:
        combined_filename = os.path.join(dirpath, file)
        print combined_filename
        shutil.copyfile(combined_filename, RESULTS_DIRECTORY + '/' + os.path.basename(file))


