import os
from pathlib import Path
list_of_files = [
    "a/b/c.txt"
]



for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)


print(file_name)    