import time, random, playsound, os, keyboard, pyautogui
from aiogram import Bot, Dispatcher, executor, types
from ctypes import *

API_TOKEN = '5759247653:AAFU4QMA7PU0hS6RmnkqIZfmkizW_HsR2eE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

Response = ['Кто обзывается, тот сам так называется', 'Обзывай меня весь век, все равно, я человек',
            'А ты в доту играешь', 'Обзываешь ты меня, перводишь на себя.', 'Закрой гроб и не греми костями.',
            'Чей там голос из помойки?', 'Все сказал? Запей водичкой!', 'Шел, шел крокодил, твое слово проглотил.',
            'Не суй свой нос в чужой вопрос, а то вопрос откусит нос.', 'Я тебя не слушаю, посолю и скушаю.',
            'Дотера спросить забыли', 'Сам такой']

width = (windll.user32.GetSystemMetrics(0))
height = (windll.user32.GetSystemMetrics(1))
music = False


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    #print('start')
    await message.reply(
        "Привет!\nМоя жизнь хуже саппортов 5 позиции, потому что я даже не прислужник, я бот по доте *****\nДля помощи в командах "
        "используй /help.")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    #print('help')
    await message.reply(
        "/start - ну старт, сообрази, гений\n/go - когда нажал поиск, жми сюда\n/musicon - для включения звукового "
        "оповещения на компьютере.\n/musicoff - да(yes)")


@dp.message_handler(commands=['musicon'])
async def send_mon(message: types.Message):
    #print('mon')
    global music
    music = True
    await message.reply('Сам напросился')


@dp.message_handler(commands=['musicoff'])
async def send_moff(message: types.Message):
    #print('moff')
    global music
    music = False
    await message.reply('Ну и зря...')


@dp.message_handler(commands=['go'])
async def send_go(message: types.Message):
    await message.reply("Бот работает")
    print('go')
    while 1:
        if pyautogui.locateOnScreen('button.png', confidence=0.7) is not None:
            for n in range(0, 3):
                pyautogui.click(width / 2, height / 2)
                time.sleep(1)
            await message.reply("Игра нашлась")
            print(music)
            if music:
                playsound.playsound('9.mp3')
            exit(0)


@dp.message_handler()
async def answer(message: types.Message):
    random_number = random.randint(0, 11)
    await message.answer(Response[random_number])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)