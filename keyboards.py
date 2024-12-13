from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить субтитры к видео", callback_data='simple_subtitles')],
        [KeyboardButton(text="Добавить субтитры к Youtube видео", callback_data='youtube_subtitles')],
        [KeyboardButton(text="Конвертировать видео в аудио", callback_data='video_to_audio')],
        [KeyboardButton(text="Скачать Youtube видео как аудио", callback_data='download_as_audio')],
        [KeyboardButton(text="Скачать видео с Youtube", callback_data='download')],
        [KeyboardButton(text="Сделать краткое содержание к видео?")],
    ],
    resize_keyboard=True, 
    input_field_placeholder='Choose:'
)


settings = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/')]
  ])
 


# iz bazy dannyh esli budem delat knopki
# cars = ['Tesls', 'Mers', 'BMW']

# async def inline_cars():
#   keyboard = InlineKeyboardBuilder()
#   for car in cars: 
#     keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
#   return keyboard.adjust(2).as_markup()