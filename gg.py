import telebot
from telebot import types
import random

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):

  bot.get_me()
  keyboard = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(text = "Біографія",callback_data="test")
  btn2 = types.InlineKeyboardButton(text = "Дитинство ",callback_data="test1")
  btn3 = types.InlineKeyboardButton(text = "Зворотній зв'язок", callback_data="helps")
  btn4 = types.InlineKeyboardButton(text = "Додатково про УГКЦ", callback_data="cerkwa")
  btn5 = types.InlineKeyboardButton(text = "більше українського контенту", callback_data="moreone")
  keyboard.add(btn1,btn2,btn3,btn4,btn5)
  bot.send_photo(message.chat.id,
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJed_LA5kk-GDZkPskh_U4pHV76dBwCjn_Yw&usqp=CAU",
                 caption = "Привіт, що хочеш дізнатися про Степана Андрійовча?"
                 ,reply_markup=keyboard)


  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="давай запиатння")
  keyboard.row("Додатково про УГКЦ")
  keyboard.row("Дитинство Степана Бандери")
  keyboard.row("Хто твій автор")
  bot.send_message(message.chat.id,"оберіть варіант",reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  if call.data == "test":
    text = "Тут ви зможете дізнатись біографію: Степан Бандера (01.12.09 - 15.10.59) Народився в с. Старий Угринів Калуського повіту на Станіславщині (тепер Івано-Франківщина) в родині греко-католицького священика. В 1919 - 1927 навчався у Стрийській гімназії. На поч. 1922 став членом Пласту, а згодом - Організації Вищих Класів Українських Гімназій.l і відео: https://www.youtube.com/watch?v=2d7AZ3-6VhA"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    d = types.InlineKeyboardButton(text="далі", callback_data="dali")
    keyboard.row(d)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "dali":
    text = "Після закінчення гімназії намагався виїхати у Чехо-Словаччину для навчання в Українській Господарській Академії у Подебрадах, але не дістав дозволу від польських властей. В 1928 Б., ставши членом Української Військової Організації, отримав призначення спочатку у відділ розвідки, пізніше - пропаганди. "
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    backm = types.InlineKeyboardButton(text="назад до меню", callback_data="backm")
    keyboard.row(backm)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "backm":
    text = "про що ще хочете дізнатися???"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bo1 = types.InlineKeyboardButton(text = "Біографія",callback_data="test")
    bo2 = types.InlineKeyboardButton(text = "Дитинство ",callback_data="test1")
    bo3 = types.InlineKeyboardButton(text = "Зворотній зв'язок", callback_data="helps")
    bo4 = types.InlineKeyboardButton(text = "Додатково про УГКЦ", callback_data="cerka")
    keyboard.row(bo1,bo2,bo3,bo4)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "test1":
    bot.send_message(call.message.chat.id, "Бандера ніколи не ходив до школи. Дитинство майбутнього провідника ОУН припало на Першу світову війну, коли школи в селах не діяли. Окрім того, хлопець хворів на ревматизм суглобів, тому не міг нормально ходити")
  if call.data == "cerkwa":
    text = "Українська греко-католицька церква (УГКЦ) - це одна з найбільших християнських церков української традиції, яка є частиною всесвітньої греко-католицької церковної спільноти. Історія УГКЦ починається в XVII столітті, коли українські вірні перейшли до греко-католицизму, тобто прийняли католицьку віру зі східним богослуженням. У кінці XIX століття УГКЦ стала незалежною від Римської католицької церкви і отримала статус самостійної церкви. Однак після Другої світової війни церква була переслідувана радянською владою і заборонена. Церква продовжувала існувати та діяти в таємниці, але після отримання Україною незалежності в 1991 році, УГКЦ стала відкритою і діє на території України та за її межами."
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    w = types.InlineKeyboardButton(text="вперед", callback_data="w")
    keyboard.row(w)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "w":
    text = "УГКЦ має свою власну ієрархію, яку очолює Глава УГКЦ - Митрополит. УГКЦ має багато парафій та монастирів на території України та за кордоном. Церква має свій власний календар свят та обрядів, які відрізняються від Римської католицької церкви. Наприклад, богослужіння проводяться на українській мові, а не на латині, а літургії проводяться зі східною традицією. УГКЦ активно займається благодійністю та соціальною діяльністю. Церква підтримує освітні та культурні ініціативи"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    ww = types.InlineKeyboardButton(text="назад до меню", callback_data="ww")
    keyboard.row(ww)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ww":
    text = "про що ще хочете дізнатися???"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    bo1 = types.InlineKeyboardButton(text = "Біографія",callback_data="test")
    bo2 = types.InlineKeyboardButton(text = "Дитинство ",callback_data="test1")
    bo3 = types.InlineKeyboardButton(text = "Зворотній зв'язок", callback_data="helps")
    bo4 = types.InlineKeyboardButton(text = "Додатково про УГКЦ", callback_data="cerka")
    keyboard.row(bo1,bo2,bo3,bo4)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "helps":
    bot.send_message(call.message.chat.id," виникли скарги або пропозиції??? тоді вам сюди: https://t.me/Cholovick" )
  if call.data == "moreone":
    text = "яка тематика тееб цікавить???"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    thems = types.InlineKeyboardButton(text="Ігри", callback_data="thems")
    thems1 = types.InlineKeyboardButton(text="пізнавальний контент", callback_data="thems1")
    thems2 = types.InlineKeyboardButton(text="музика", callback_data="thems2")
    thems3 = types.InlineKeyboardButton(text="анти російські і комедійні канали", callback_data="thems3")
    keyboard.row(thems,thems1,thems2,thems3)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "thems":
    text = "Виберіть соц мережу"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    social = types.InlineKeyboardButton(text="TikTok", callback_data="tt")
    social1 = types.InlineKeyboardButton(text="YouTube", callback_data="yt")
    keyboard.row(social,social1)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "tt":
    text = "https://www.tiktok.com/@checkpoint.arsenal?_t=8aX1Z9e0aqz&_r=1 - канал про ігри та новинки; https://www.tiktok.com/@fraugame_official?_t=8aX1cJsCcBa&_r=1 - Канал про геймерів та найдивніші ігри "
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    ttt = types.InlineKeyboardButton(text="назад", callback_data="ttt")
    keyboard.row(ttt)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ttt":
    text = "Виберіть соц мережу"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    social = types.InlineKeyboardButton(text="TikTok", callback_data="tt")
    social1 = types.InlineKeyboardButton(text="YouTube", callback_data="yt")
    keyboard.row(social,social1)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "yt":
    text = "https://youtube.com/@teoo - Канал майнкоафтера, раджу до перегляду; https://youtube.com/@misterparrot - Український мармок; https://youtube.com/@steffankaua - Ще одним майнкрафтер; https://youtube.com/@GameStreetUA - Канал про ігри; https://youtube.com/@oldboiua - Канал про дядечка який оглядає ігри та всякі ігрові штук; https://youtube.com/@RendarosUA - Схоже з OldBoy; https://youtube.com/@UkrainianGeek - Канал в переважній більшості про ігрові консолі та все в тому ж роді; https://youtube.com/@itpediachannel - Канал про ігри та консолі"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    ytt = types.InlineKeyboardButton(text="назад", callback_data="ytt")
    keyboard.row(ytt)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ytt":
    text = "Виберіть соц мережу"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    social = types.InlineKeyboardButton(text="TikTok", callback_data="tt")
    social1 = types.InlineKeyboardButton(text="YouTube", callback_data="yt")
    keyboard.row(social,social1)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "thems1":
    text = "Що оберете"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    social1 = types.InlineKeyboardButton(text="TikTok", callback_data="ttt")
    social2 = types.InlineKeyboardButton(text="YouTube", callback_data="yyt")
    keyboard.row(social1,social2)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ttt":
    text = "https://www.tiktok.com/@ikla.magazine?_t=8aX48Sx6NF7&_r=1 - Канал про пояснення різного та різне"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    ttt1 = types.InlineKeyboardButton(text="назад", callback_data="ttt1")
    keyboard.row(ttt1)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ttt1":
    text = "Що оберете"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    soc1 = types.InlineKeyboardButton(text="TikTok", callback_data="ttt")
    soc2 = types.InlineKeyboardButton(text="YouTube", callback_data="yyt")
    keyboard.row(soc1,soc2)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "yyt":
    text = "https://www.youtube.com/@BLOGMAYSTER - одним словом утопіа шоу; https://www.youtube.com/@zagin_kinomaniv - канал про огляди фільмів серіалів та їх розбір; https://www.youtube.com/@imtgsh - круто розказує про історію нашої неньки; https://www.youtube.com/@GeekJournal - огляди телепрограм та телеканалів; https://www.youtube.com/@AlexShevstsov - про все; https://www.youtube.com/@user-gf9zf8pg9k і https://www.youtube.com/@user-xl6nw4pn5k - пк тематика; https://www.youtube.com/@OstanniyCapitalist - багато цікавого "
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    ytt11 = types.InlineKeyboardButton(text="назад", callback_data="ytt11")
    keyboard.row(ytt11)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ytt11":
    text = "Що оберете"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    social1 = types.InlineKeyboardButton(text="TikTok", callback_data="ttt")
    social2 = types.InlineKeyboardButton(text="YouTube", callback_data="yyt")
    keyboard.row(social1,social2)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "thems3":
    text = "Чого бажаєте  обрати"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    socl1 = types.InlineKeyboardButton(text="TikTok", callback_data="t1t1t1")
    socl2 = types.InlineKeyboardButton(text="YouTube", callback_data="yttyt")
    keyboard.row(socl1,socl2)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "t1t1t1":
    text = "поки автор нічого не знайшов. Якшо ви заєте прикольний кнал то напишіть сюди: https://t.me/Cholovick"
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    t1t11 = types.InlineKeyboardButton(text="назад", callback_data="t1t11")
    keyboard.row(t1t11)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "t1t11":
    text = "Чого бажаєте  обрати"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    socl1 = types.InlineKeyboardButton(text="TikTok", callback_data="t1t1t1")
    socl2 = types.InlineKeyboardButton(text="YouTube", callback_data="yttyt")
    keyboard.row(socl1,socl2)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "yttyt":
    text = "https://www.youtube.com/@nade_cgt - огляяди різних мультів та історії з життя; https://www.youtube.com/@kkkopiyka - канал веселої жіночки яка робить огляди на різнісеріали, фільми та дорами; https://www.youtube.com/@PATRON_BANDERY - Харізма зустрічає москаліста; https://www.youtube.com/@AlekseyDurnev - знімає огляд на рос новини; https://www.youtube.com/@akordich_ua - співає про поразки сусіда; https://www.youtube.com/@user-xl6nw4pn5k - пк тематитика з жартами; https://www.youtube.com/@RoomFactoryy і https://www.youtube.com/@roomfactoryua - скетчі; https://www.youtube.com/@vohnepalnyi - Василь кіт; "
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    ytt1yt = types.InlineKeyboardButton(text="назад", callback_data="ytt1yt")
    keyboard.row(ytt1yt)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
  if call.data == "ytt1yt":
    text = "Чого бажаєте  обрати"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    socl1 = types.InlineKeyboardButton(text="TikTok", callback_data="t1t1t1")
    socl2 = types.InlineKeyboardButton(text="YouTube", callback_data="yttyt")
    keyboard.row(socl1,socl2)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def text(message):
  if message.text == "Хто твій автор":
    bot.reply_to(message,"його телеграм: https://t.me/Cholovick")
  if message.text == "Біографія Степана Банедри":
    bot.reply_to(message,"Тут ви зможете дізнатись біографію: https://ukrnationalism.com/the-nationalist-movement/staff/stepan-bandera/68-biohrafiia-s-bandery.html і відео: https://www.youtube.com/watch?v=2d7AZ3-6VhA")
  if message.text == "Дитинство Степана Бандери":
    bot.reply_to(message,"Бандера ніколи не ходив до школи. Дитинство майбутнього провідника ОУН припало на Першу світову війну, коли школи в селах не діяли. Окрім того, хлопець хворів на ревматизм суглобів, тому не міг нормально ходити")
  if message.text == "Додатково про УГКЦ":
    bot.send_message(message.chat.id,"https://osvita.ua/vnz/reports/relig/20320/")

@bot.message_handler(commands=["help"])
def help(message):
  bot.send_message(message.chat.id," Цей бот допоможе вам дізнатися багатенько про Степана Андрійовича Бандеру та дещо інше. Також цей бо знаходиться ще у розробці, тому ви зможете пропонувати свої ідеї щодо його вдосконалення.")

@bot.message_handler(content_types=['photo'])
def photo(message):
  bot.send_message(message.chat.id,"некоректне питання")
@bot.message_handler(content_types=['video'])
def video(message):
  bot.send_message(message.chat.id,"некоректне питання")
@bot.message_handler(content_types=['audio'])
def audio(message):
  bot.send_message(message.chat.id,"некоректне питання")
@bot.message_handler(content_types=['animation'])
def animation(message):
  bot.send_message(message.chat.id,"некоректне питання")
@bot.message_handler(content_types=['voice'])
def voice(message):
  bot.send_message(message.chat.id,"некоректне питання")
@bot.message_handler(content_types=['sticker'])
def sticker(message):
  bot.send_message(message.chat.id,"некоректне питання")

bot.polling(none_stop = True)