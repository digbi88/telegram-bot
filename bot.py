from telegram.ext import Application, CommandHandler
import random
import os
import asyncio
from flask import Flask
from threading import Thread

# Веб-сервер для поддержания активности
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "🤖 Бот активен! Команды: /start, /tignari, /flirt, /throw, /symphony, /flirtspam"

@app_flask.route('/health')
def health():
    return "OK"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app_flask.run(host='0.0.0.0', port=port)

# Запускаем Flask в отдельном потоке
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN не найден!")
    exit(1)

print("✅ Бот запущен на Render!")

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

# Единственная симфония - Симфония Лужи и Любви
symphony_of_love = """
🎼 **Симфония Лужи и Любви** - Искусственный Интеллект

**I. Allegro Appassionato (Страсть)**
Струнные: бурное вступление, словно первые чувства
Деревянные духовые: нежные мелодии, как шепот любви
Медные: мощные аккорды - признание в любви

**II. Adagio Romantico (Романтика)**
Солирующая скрипка: нежная тема лужи
Виолончель: глубокий ответ влюбленного
Арфа: аккомпанемент, словно капли дождя

**III. Scherzo Giocoso (Игривость)**
Флейты: веселые переливы
Кларнеты: шутливые мелодии
Треугольник: блестящие капли

**IV. Finale Trionfale (Триумф)**
Весь оркестр: величественное соединение тем
Хор: 'Лужа и любовь навеки!'
Громоподобный финал: вечная связь

*Посвящается всем влюблённым душам, находящим красоту в простом*
"""

async def start(update, context):
    welcome_text = """
🤖 Привет! Я жених лужи со следующими командами:

/tignari - Хочешь узнать обо мне?
/flirt - Одна флиртующая фраза
/flirtspam - Заигрываю с лужей
/throw - Бросить игральную кость 🎲
/symphony - Симфония Лужи и Любви

Выбери команду и наслаждайся общением!
    """
    await update.message.reply_text(welcome_text)

async def tignari(update, context):
    await update.message.reply_text("хочешь узнать обо мне?")

async def flirt(update, context):
    flirt_message = random.choice(flirt_phrases)
    await update.message.reply_text(flirt_message)

async def flirtspam(update, context):
    # Предупреждение о возможной блокировке
    warning_message = await update.message.reply_text("⚠️ Лужа,все для тебя!")
    
    # Отправляем 50 фраз с задержкой 0.1 секунды (100 мс)
    for i in range(50):
        flirt_message = random.choice(flirt_phrases)
        await update.message.reply_text(f"{i+1}/50: {flirt_message}")
        # Задержка 0.1 секунды (100 мс)
        await asyncio.sleep(0.1)
    
    await update.message.reply_text("💖 Готово! Полюбил лужу еще больше")

async def throw(update, context):
    await update.message.reply_text("🎲")

async def symphony(update, context):
    await update.message.reply_text(symphony_of_love)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tignari", tignari))
    app.add_handler(CommandHandler("flirt", flirt))
    app.add_handler(CommandHandler("flirtspam", flirtspam))
    app.add_handler(CommandHandler("throw", throw))
    app.add_handler(CommandHandler("symphony", symphony))
    
    print(f"📝 Доступно {len(flirt_phrases)} флирт-фраз")
    print("🎵 Доступна Симфония Лужи и Любви")
    print("💌 Доступна команда /flirtspam (50 фраз)")
    print("🌐 Веб-сервер запущен")
    print("🚀 Бот готов к работе!")
    
    app.run_polling()
