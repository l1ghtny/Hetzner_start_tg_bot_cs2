from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from src.hltv.parser import get_results
from src.logs_setup import logger

logger = logger.logging.getLogger("bot")

MAP, STAR, MATCH = range(3)


async def start_hltv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = ['mirage', 'overpass', 'inferno', 'vertigo', 'anubis', 'ancient', 'nuke']
    await update.message.reply_text('Привет, я помогу тебе скачать демки с hltv. Для начала выбери '
                                    'карту, демки на которой тебя интересуют',
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                                     one_time_keyboard=True,
                                                                     input_field_placeholder="Какая карта?"
                                                                     ),
                                    )

    return MAP


async def get_star(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    de_map = update.message.text
    context.user_data['de_map'] = de_map
    reply_keyboard = ['*', '**', '***', '****', '*****']
    await update.message.reply_text('Теперь давай выберем количество звёздочек',
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                                     one_time_keyboard=True,
                                                                     input_field_placeholder="Сколько?"
                                                                     ),
                                    )
    return STAR


async def get_match(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    stars = update.message.text
    context.user_data['stars'] = stars
    results = await get_results(star=len(context.user_data['stars']), de_map=f'de_{context.user_data['de_map']}')
    reply_keyboard = []
    for result in results:
        reply_keyboard.append(result)
    await update.message.reply_text('Выбери матч, который тебя интересует:',
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                                     one_time_keyboard=True,
                                                                     input_field_placeholder="Какой матч?"
                                                                     ),
                                    )

    return MATCH
