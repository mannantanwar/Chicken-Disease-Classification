import os 
from pathlib import Path 
import logging 

logging.basicConfig(level= logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files= [
    "github/workflows/.gitkeep", #gitkeep file has been stored kyuki we donot want to store empty folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", #init file has been stored to make this a local package taaki khi se bhi import hojaye ye 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html" 
]

for filepath in list_of_files:
    filepath = Path(filepath) #making this a windows path as window me \ use hota hia nand we have used / here 
    filedir, filename = os.path.split(filepath)

    if filedir!="" :
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"Creating directory; {filedir} for file; {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath ,"w") as f:
            pass 
            logging.info(f"Creating empty file ; {filepath}")
    else:
        logging.info(f"{filepath} is already created ")


