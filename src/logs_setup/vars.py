import os
import platform
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()
try:
    windows_dir = os.getenv("path_main")
except:
    print('not successful..')

target_dir = "logs"
if platform.system() == "Linux":
    root_dir = "home/tg-server-bot"
else:
    disk = "F:\\"
    dir = f"""{windows_dir}"""
    root_dir = os.path.join(disk, dir)
path = os.path.join(root_dir, target_dir)
print(path)
