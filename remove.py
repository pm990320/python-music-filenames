import os

DIRECTORY = "C:/Users/Patrick/Desktop/ALL_MUSIC"

for root, dirnames, filenames in os.walk(DIRECTORY):
    for filename in filenames:
        full_path = os.path.join(root, filename)
        extension = os.path.splitext(full_path)[1]
        if(extension == '.itc2' or extension == '.ipa'):
            os.remove(full_path)
            print "Removing" + filename