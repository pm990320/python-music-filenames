import os, shutil, string


def copyFilesToDirectory(SOURCE_DIRECTORY, DESTINATION_DIRECTORY):
    for dirpath, dirnames, filenames in os.walk(SOURCE_DIRECTORY):
        for file in filenames:
            if file.find("Thumbs.db") != -1:
                continue
            combined_filename = os.path.join(dirpath, file)
            print combined_filename
            shutil.copyfile(combined_filename, DESTINATION_DIRECTORY + '/' + os.path.basename(file))


# Example of extensions list: [ '.jpg', '.html' ]
def removeFilesWithExtensions(DIRECTORY, EXTENSIONS_LIST):
    for root, dirnames, filenames in os.walk(DIRECTORY):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            extension = os.path.splitext(full_path)[1]
            if(extension in EXTENSIONS_LIST):
                os.remove(full_path)
                print "Removing " + filename


def renameMusicFiles(DIRECTORY):
    for root, dirnames, filenames in os.walk(DIRECTORY):
        for filename in filenames:
            new_filename = filename

            new_filename = new_filename.lstrip(' 0123456789-_()[]{}')

            new_full_path = os.path.join(root, new_filename)
            old_full_path = os.path.join(root, filename)

            if os.path.isfile(new_full_path):
                new_filename = "(2)" + new_filename
                new_full_path = os.path.join(root, new_filename)
            os.rename(old_full_path, new_full_path)



def removeAreasWithParenthesis(string):
    first = string.find('(')
    last = string.find(')')

    if first > last:
        raise Exception("closing parenthesis before opener")

    if string.find('(', first + 1) < last:
        # there is a nested parenthesis
        # recursive call to function
        substr = removeAreasWithParenthesis(string[ first+1 : last ])

        string = string[0:first] + substr + string[last:]

    new_str = string[0:first] + string[last:]
    return new_str
