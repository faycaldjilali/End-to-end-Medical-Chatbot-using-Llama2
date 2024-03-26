import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html",
    "requirements.txt"

]


for filepath in list_of_files:
   filepath = Path(filepath)# is to use it for windows
   filedir, filename = os.path.split(filepath) # split the files and the folder

   if filedir !="": # it mean if filedir is not empty
      os.makedirs(filedir, exist_ok=True)#if the folder exist dont create reacreate the file dont replace 
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")
      
      
    