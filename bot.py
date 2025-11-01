from telegram.ext import Application, CommandHandler
import random
import os

# Безопасное получение токена из переменных окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Проверяем, что токен установлен
if not BOT_TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN не найден в переменных окружения!")
    print("📝 Добавьте переменную BOT_TOKEN в настройках Render")
    exit(1)

print("✅ Токен успешно загружен из переменных окружения")

flirt_phrases = [
    "@luzha_ki Я красивый, а ты лужа, у нас будут прекрасные дети))~~",
    "@luzha_ki Так мило смотреть как моя милая девочка злится, когда не понимает, почему ее называют гадалачкой, но, скажу по секрету, что даже я знаю в чем дело ~)))",
    "@luzha_ki Ну лужечка((( зачем тебе этот Сгылпа?~ если есть я! Тот, который проживет с тобой долгую жизнь 😻 и будет поливать тебя, чтобы ты не высохла 😌",
    "@luzha_ki Мне нравится твой тихий голосок)~ может, нууу~ ты хочешь луну? Я куплю тебе все луны~ которые найду))",
    "@luzha_ki Хоть лужа и отвергает меня, но я вижу в этом нечто большее~~ не зря же говорят, если девушка на вас злится, значит ей не все равно)))",
    "@luzha_ki Знаешь, в Тейвате мы лучшая пара по реакциям~ я дендро, ты гидро, и у нас совместные бутончики))"
]

async def start(update, context):
    welcome_text = """
🤖 Привет! я жених лужи со следующими командами:

/tignari - Хочешь узнать обо мне?
/flirt - Флиртующие сообщения для @luzha_ki  
/throw - Бросить игральную кость 🎲

Выбери команду и наслаждайся общением!
    """
    await update.message.reply_text(welcome_text)

async def tignari(update, context):
    await update.message.reply_text("хочешь узнать обо мне?")

async def flirt(update, context):
    flirt_message = random.choice(flirt_phrases)
    await update.message.reply_text(flirt_message)

async def throw(update, context):
    await update.message.reply_text("🎲")

if __name__ == "__main__":
    try:
        app = Application.builder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("tignari", tignari))
        app.add_handler(CommandHandler("flirt", flirt))
        app.add_handler(CommandHandler("throw", throw))
        
        print("🤖 Бот запущен на Render!")
        app.run_polling()
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {e}")
