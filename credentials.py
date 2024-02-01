import os

from dotenv import load_dotenv

load_dotenv()

server_id = os.getenv("server_id")
telegram_token = os.getenv("tg_token")
hetzner_token = os.getenv("hetzner_token")
ip = os.getenv("host_ip")
login = os.getenv("login")
password = os.getenv("password")
command = os.getenv("command")
command_main = os.getenv('command_main')
key_fingerprint = os.getenv("key_fingerprint")
ssh_key = os.getenv("ssh_key")
rcon = os.getenv("rcon")
server_pass = os.getenv("cs2_server_password")

