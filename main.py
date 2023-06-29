import shutil
import subprocess
import yaml
import requests
import json

from rich import print

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    WORKLOAD_DEFINITIONS = r"C:\ProgramData\Salad\workload-definitions"
    NDM_WORKLOAD = r"C:\ProgramData\Salad\workloads\ndm"

    # Create venv
    subprocess.run(["python", "-m", "venv", f"{NDM_WORKLOAD}\\venv"])

    # Backup ndm.yaml
    shutil.copyfile(f"{WORKLOAD_DEFINITIONS}\\ndm.yaml", f"{WORKLOAD_DEFINITIONS}\\ndm_BACKUP.yaml")

    # Copy spoof
    shutil.copyfile(f"./spoof.py", f"{NDM_WORKLOAD}\\spoof.py")

    with open(f'{WORKLOAD_DEFINITIONS}\\ndm.yaml', 'r') as file:
        ndm_data = yaml.safe_load(file)
        
    ndm_data["definition"]["exe"] = f"{NDM_WORKLOAD}\\venv\\scripts\\python.exe"
    ndm_data["definition"]["args"] = f"{NDM_WORKLOAD}\\spoof.py" 

    with open(f'{WORKLOAD_DEFINITIONS}\\ndm.yaml', 'w') as file:
        yaml.dump(ndm_data, file)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

