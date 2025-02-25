#program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
if os.path.exists("demofile3.txt"):
  os.remove("demofile3.txt")
else:
  print("The file does not exist")