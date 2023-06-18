'''Создание эхо бота с помощью aiogram'''

# бот - это сервер, для взаимодесйтвия с API Telegram.

from aiogram import Bot, Dispatcher, executor, types  # импорт библиотеки aiogram из нее имортируем class "Bot",class "Dispatcher" импорт executor импортируем типы "types"

token_API = "6292164387:AAH8XmXaOd8_CT6V1rzT96V5hOwdeFtsF0Y"  # Токен для подключения телеграм API

bot = Bot(token_API)  # создание экземпляра класса Bot, куда передаем наш токен API
dispatch = Dispatcher(bot)  # Деспечер осуществляет анализ всех входящих апдейтов (то что будет отслеживать анализ входящих подключений, апдейты и т.д)
# создаем экземпляр класса Деспечер(Dispatcher) и передаем туда экземпляр класса Бот(bot)


@dispatch.message_handler()  # создаем декоратор и обращаемся к классу Диспечер(dispatch)

async def echo(message: types.Message):  # создаем асинхронную функцию. В качестве аргумента данная функция получает сообщение которе нам отправляет клиент
    await message.answer(text=message.text)  # написать сообщение. Передаем аргумент вида text


if __name__ == '__main__':  # данный модуль будет запускаться самостоятельно (вложенный внутри конструкции if)
    executor.start_polling(dispatch)  # запуск в режиме polling(запуск бота)
