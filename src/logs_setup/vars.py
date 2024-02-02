import os
import platform
from dotenv import load_dotenv

load_dotenv()
windows_dir = os.getenv("path_main")

target_dir = "logs"
print(f'target: {target_dir}')
if platform.system() == "Linux":
    root_dir = "home/tgserver"
    print(f'root: {root_dir}')
else:
    disk = "F:\\"
    dir = f"""{windows_dir}"""
    root_dir = os.path.join(disk, dir)
path = os.path.join(root_dir, target_dir)
