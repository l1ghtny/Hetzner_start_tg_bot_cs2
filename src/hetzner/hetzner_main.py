import asyncio

import hcloud
import paramiko
from hcloud import Client

from credentials import server_id, hetzner_token, ip, login, password, command_main
from src.logs_setup import logger

logger = logger.logging.getLogger("bot")


async def start_server():
    hcloud_key = hetzner_token
    client = Client(token=hcloud_key)
    server = client.servers.get_by_id(server_id)
    server.power_on()
    server_status = server.status
    logger.info('Started the server')
    return server_status


async def start_cs2_server():
    client = paramiko.client.SSHClient()
    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=ip, port=22, username=login, password=password)
        logger.info('ssh connected')
        _stdin, _stdout, _stderr = client.exec_command(command_main)
        client.close()
        return True
    except:
        logger.info('Error')
        return False


async def shutdown_server():
    client = Client(token=hetzner_token)
    server = client.servers.get_by_id(server_id)
    server.power_off()
    await asyncio.sleep(10)
    server_status = server.status
    return server_status
