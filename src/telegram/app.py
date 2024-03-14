import asyncio
import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes

from credentials import telegram_token, ip, server_pass, rcon
from src.hetzner.hetzner_main import start_server, start_cs2_server, shutdown_server
from src.logs_setup import logger

logger = logger.logging.getLogger("bot")


async def start_cs2_server_full(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await update.effective_message.reply_text('Включаю сервер...')
    await start_server()
    await asyncio.sleep(15)
    result = await start_cs2_server()
    if result:
        await message.edit_text(
            f"""Сервер включен и готов к использованию\\. \nНапоминаю ip `connect {ip}:27015; password {server_pass}` \nНе забудь выключить сервер командой /shutdown как закончишь""",
            parse_mode='MarkdownV2')
        logger.info('Server is on, message sent')
    else:
        await message.edit_text('Чет сломалось, сорян')
        logger.error('Connection problem with ssh')


async def turn_off_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await update.effective_message.reply_text('Выключаем...')
    result = await shutdown_server()
    await message.edit_text('Сервер выключен. Текущий статус: \n'
                            f'{result}')


async def bot_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.effective_message.reply_text(
            f"""1 Включение сервера требует где\\-то секунд 15\\-20, это норм \n"""
            f'2 Для управления сервером нужно написать в консоль `fake\\_rcon\\_password {rcon}` \n'
            f'3 Для режима разминки надо написать `fake\\_rcon exec w`', parse_mode='MarkdownV2')
    except:
        logger.error('Не сработало')


async def update_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await update.effective_message.reply_text('Обновляем...')


def main():
    application = Application.builder().token(telegram_token).build()

    main_start_handler = CommandHandler('start_server', start_cs2_server_full)
    main_shutdown_handler = CommandHandler('shutdown', turn_off_server)
    main_info_handler = CommandHandler('info', bot_info)
    # hltv_conv_handler = ConversationHandler(
    #
    # )

    application.add_handler(main_start_handler)
    application.add_handler(main_shutdown_handler)
    application.add_handler(main_info_handler)

    logger.info(f'bot started at {datetime.datetime.now()}')

    application.run_polling(allowed_updates=Update.ALL_TYPES)
