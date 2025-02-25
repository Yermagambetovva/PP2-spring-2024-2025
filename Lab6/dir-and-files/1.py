#program to list only directories, files and all directories, files in a specified path.

import os

path = "/"
dir_list = os.listdir(path)

print("files and directories in '", path, "' :")
print(dir_list)