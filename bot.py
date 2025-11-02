from telegram.ext import Application, CommandHandler
import random
import os
import asyncio
from flask import Flask
from threading import Thread
import requests

# Создаем Flask приложение для поддержания активности
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "🤖 Бот активен и работает!"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app_flask.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()

# Запускаем веб-сервер
keep_alive()

# Токен бота
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN не найден!")
    exit(1)

print("✅ Токен загружен успешно")

flirt_phrases = [
    "@luzha_ki Я красивый, а ты лужа, у нас будут прекрасные дети))~~",
    "@luzha_ki Так мило смотреть как моя милая девочка злится, когда не понимает, почему ее называют гадалачкой, но, скажу по секрету, что даже я знаю в чем дело ~)))",
    "@luzha_ki Ну лужечка((( зачем тебе этот Сгылпа?~ если есть я! Тот, который проживет с тобой долгую жизнь 😻 и будет поливать тебя, чтобы ты не высохла 😌",
    "@luzha_ki Мне нравится твой тихий голосок)~ может, нууу~ ты хочешь луну? Я куплю тебе все луны~ которые найду))",
    "@luzha_ki Хоть лужа и отвергает меня, но я вижу в этом нечто большее~~ не зря же говорят, если девушка на вас злится, значит ей не все равно)))",
    "@luzha_ki Знаешь, в Тейвате мы лучшая пара по реакциям~ я дендро, ты гидро, и у нас совместные бутончики))",
    "@luzha_ki Мне не очень нравится, когда мое имя сокращают, но, если это сделаешь ты~ я буду самым счастливым человеком на земле)) 🥰",
    "@luzha_ki Думаю отряд для двоих идеален, особенно если там есть я — организм😝, которому нужна лишь крупится нежной и сочной водички~ как ты) 😍",
    "@luzha_ki как бы я хотел, чтобы наш нерушимый брак был настоящим😌... это ведь так романтично🤭~ ты, я..)) и не смотря на будущие невзгоды~ мы все равно будем считаться парой~ пока смерть не разлучит нас)))))😝",
    "@luzha_ki я надеюсь, что тебя никогда не снесут как твою невероятную подругу Руби, но, даже если это случится, я найду способ отыскать тебя!",
    "@luzha_ki говорят вода это самое главное в жизни живых существ, но сложнее всего конечно же природе~) ведь без нее не будет кислорода, а без кислорода не будет тебя ~~",
    "@luzha_ki ты случайно не Царица? Просто ты очень смахиваешь на богиню любви😏😉",
    "@luzha_ki я не люблю смотреть вперед, Взрослеть, умнеть, наоборот, Хочу вернуться.. И словно первый раз люббя, Увидеть сон, а в нем тебя, И... не проснуться.",
    "@luzha_ki Я помню чудное мгновение... Передо мной явилась ты. Как очень вкусное варенье, как геи чистой красоты",
    "@luzha_ki оу оу оу деточка, да ты вся промокла~~",
    "@luzha_ki Все для тебя - рассветы и туманы Для тебя - моря и океаны Для тебя - цветочные поляны Для тебя Лишь для тебя – горят на небе звезды Для тебя – безумный мир наш создан Для тебя – живу и я под солнцем Для тебя Лишь для тебя – живу и я под солнцем Для тебя",
    "@luzha_ki ребят, хватит меня использовать, ей не приятно (продолжайте~)",
    "@luzha_ki знаю ли я твою любимую песню? Конечно) это же: TOXIC ."
]

async def start(update, context):
    welcome_text = """
🤖 Привет! Я жених лужи со следующими командами:

/tignari - Хочешь узнать обо мне?
/flirt - Флиртующие сообщения для возлюбленной 
/throw - Бросить игральную кость 🎲
    """
    await update.message.reply_text(welcome_text)

async def tignari(update, context):
    await update.message.reply_text("хочешь узнать обо мне?")

async def flirt(update, context):
    flirt_message = random.choice(flirt_phrases)
    await update.message.reply_text(flirt_message)

async def throw(update, context):
    await update.message.reply_text("🎲")

async def error_handler(update, context):
    print(f"❌ Ошибка: {context.error}")

if __name__ == "__main__":
    try:
        app = Application.builder().token(BOT_TOKEN).build()
        
        # Добавляем обработчики
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("tignari", tignari))
        app.add_handler(CommandHandler("flirt", flirt))
        app.add_handler(CommandHandler("throw", throw))
        
        # Обработчик ошибок
        app.add_error_handler(error_handler)
        
        print("🤖 Бот запущен на Render!")
        print(f"📝 Доступно {len(flirt_phrases)} флирт-фраз")
        print("🌐 Веб-сервер запущен для поддержания активности")
        
        # Запускаем бота
        app.run_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query"]
        )
        
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        # Перезапуск через 10 секунд при критической ошибке
        asyncio.run(asyncio.sleep(10))
        os.execv(__file__, sys.argv)
