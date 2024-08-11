import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.get_me()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
    btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
    btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
    btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_photo(message.chat.id,
        "https://imglife.pravda.com.ua/images/doc/4/4/4443310-jadan-serhiy-2.jpg",
        caption=f"Привіт, {message.from_user.full_name}!\n Що ти хочеш дізнатись про Сергія Жадана?",
        reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "who":
      text = "Сергій Жадан - видатний український письменник, поет, перекладач, громадський діяч."
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      back4 = types.InlineKeyboardButton(text="назад до меню", callback_data="back4")
      keyboard.row(back4)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
    if call.data == "back4":
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://scontent-iev1-1.xx.fbcdn.net/v/t1.6435-9/188978400_349549693194054_6389259912542681903_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=53a332&_nc_ohc=o5f4AI-dIC8Q7kNvgGweIE9&_nc_ht=scontent-iev1-1.xx&oh=00_AYDzxL1IbY_fu5GZO31_RK6OjwY9O87Edkm7XKm2WOLr6Q&oe=66D86307",
                     caption= "головне меню",
                     reply_markup=keyboard)

    if call.data == "moreone":
      text = "Соцмережі Сергія Жадана: \nFacebook: https://www.facebook.com/zhadan \nInstagram: https://www.instagram.com/serhiy_zhadan/"
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      back2 = types.InlineKeyboardButton(text="назад до меню", callback_data="back2")
      keyboard.row(back2)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == "back2":
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://scontent-iev1-1.xx.fbcdn.net/v/t31.18172-8/28238614_1564485826933013_5972850099228727665_o.jpg?_nc_cat=103&ccb=1-7&_nc_sid=53a332&_nc_ohc=jIspYIbT25oQ7kNvgG3z1c7&_nc_ht=scontent-iev1-1.xx&oh=00_AYDLbMkzM6GJC__wkf9pwIW-HZ_FDcbCGQbNxBqe66VM0Q&oe=66D86A29",
                     caption= "головне меню",
                     reply_markup=keyboard)

    if call.data == "helps":
      text = "Виникли скарги або пропозиції? Тоді вам сюди: https://t.me/Cholovick"
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      back1 = types.InlineKeyboardButton(text="назад до меню", callback_data="back1")
      keyboard.row(back1)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == "back1":
      text = "головне меню"
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://scontent-iev1-1.xx.fbcdn.net/v/t1.18169-9/23031240_1456873707694226_5877592637444680769_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=53a332&_nc_ohc=tS3AX5bM4FAQ7kNvgFICdLY&_nc_ht=scontent-iev1-1.xx&oh=00_AYCJ4LbFlRzKI9cIluVcfx8JubTs3njnFPj9ZYjBl84qYg&oe=66D85ED0",
                     caption= "головне меню",
                     reply_markup=keyboard)


    if call.data == "tworchist":
      text = "творчість Батька як"
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      pusmunnuk = types.InlineKeyboardButton(text="письменника", callback_data="pis")
      muzikant = types.InlineKeyboardButton(text="музиканта", callback_data="muz")
      perecladac = types.InlineKeyboardButton(text="перекладача", callback_data="pere")
      back3 = types.InlineKeyboardButton(text="назад до меню", callback_data="back3")
      keyboard.row(back3, pusmunnuk, muzikant, perecladac)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == "back3":
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://scontent-iev1-1.xx.fbcdn.net/v/t1.6435-9/156698258_301903617958662_2768899525189669617_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=53a332&_nc_ohc=DN6QRsSyxEgQ7kNvgH05IS_&_nc_ht=scontent-iev1-1.xx&oh=00_AYCRocjwl1bfYGs2ypbQfh03slvun2DPf_LDNVXnRoQnxg&oe=66D86E7E",
                     caption= "головне меню",
                     reply_markup=keyboard)


    if call.data == "pis":
      text = """
          Сергій Жадан – всесвітньо відомий український письменник, автор 12 поетичних книг і 7 романів, лауреат понад десятка літературних премій.

          Писати вірші почав ще навчаючись у школі. У 1992 році, будучи студентом, разом із Ростиславом Мельником та Ігорем Пилипчуком Сергій Жадан заснував літературне об'єднання «Червона фіра», концепцією якого був неофутуризм (авангардна течія в мистецтві XXI століття, яке, руйнуючи стереотипи, передбачає створення нових, кращих культурних станів і цінностей).

          Жадан згадував: «Ми писали вірші, які фактично неможливо було надрукувати, тому що видавництва та книгарні закривалися. Але 1992 року в Україну зі США повернувся Осип Зінкевич зі своїм видавництвом «Смолоскип». Він вирішив видавати молодих авторів і створив для них конкурс. Це був наш шанс, нам усім випало бінго. Я став одним із перших лауреатів». Першими вийшли збірки «Генерал Юда» (1995 рік, Київ) та «Цитатник: вірші для коханок та коханців» (1995 рік, Київ), на яку написала схвальну рецензію Оксана Забужко. Наступними були перша прозова книжка – збірка оповідань «Біг-Мак» (2003),  романи «Депеш Мод» (2004) і «Anarchy in the UKR» (2005).

          В одному з інтерв’ю Жадан признався: «Сидіти вдома і писати про вигаданих героїв мене ніколи не приваблювало. Мені було цікаво писати з натури, з полів. У мене завжди було широке коло спілкування, ще з 1990-х років — і академічне коло, викладачі, студенти, професори, митці, а з іншого боку я завжди спілкувався з музикантами, з маргінальними типами, мені це завжди було цікаво. Це було природно і дещо подібне коло спілкування у мене досі залишилось, мабуть тільки в сотні разів збільшилось». А коли його запитали: «Що для вас література?» – відповів: «Для мене література, крім того що це велика любов, один із сенсів існування, це ще можливість поспілкуватися з людьми, які мені близькі – письменники, критики, видавці. Тому я розглядаю свою діяльність як велику пригоду. Інколи в ній трапляються неприємності, інколи хтось відверто дратує, але якщо ти концентруєшся не на цьому, а на тому, що тобі подобається, то це дуже цікаве середовище, за яке я неймовірно вдячний... Я дуже люблю писати, і це не спосіб самоствердитися, це спосіб реалізації тих речей, які є всередині».

          У 2010 році письменник опублікував роман «Ворошиловград», який став переможцем у конкурсі «Книга року» (Україна), а у 2014 р. – відзначений швейцарською літературною премією Jan Michalski Prize. Ще через чотири роки вийшла його книжка «Месопотамія» (2014), що включає роман у новелах та 30 віршів. У 2017 році – побачив світ роман «Інтернат». Письменник вважає його своїм найкращим твором і зазначає: «Роман «Інтернат» найкраще відповідає моєму розумінню світу, літератури та природи письма в принципі. Якщо «Інтернат» – найкраща книга прози, то «Життя Марії» і «Тамплієри» – найвдаліші поетичні збірки».
         """

      keyboard = types.InlineKeyboardMarkup(row_width=2)
      next = types.InlineKeyboardButton(text="далі", callback_data="nex")
      keyboard.add(next)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == "nex":
      text = """
             Великою мірою на коло творчого спілкування і на розмір аудиторії Жадана вплинула музика. У 2000 році в Харкові було засновано рок-гурт «Собаки в космосі». У 2007 році колектив випустив альбом «Хор монгольських міліціонерів», який записали на вірші Сергія Жадана. У 2008 році гурт випустив перший спільний альбом із письменником під назвою «Спортивний клуб армії», а в 2014 році гурт перейменували – він став називатися «Жадан і собаки». У травні 2022 року музиканти презентували композицію «Метро», присвячену дітям війни. С. Жадан є також фронтменом рок-гурту «Лінія Маннергейма», який був заснований у Харкові у 2017 році. Перший концерт музиканти відіграли в Ізюмі на площі Джона Леннона 16 лютого 2017 року. 26 лютого 2018 року гурт презентував дебютний мініальбом «Де твоя лінія?». Саме того ж року вийшла збірка «Бої без правил», а у 2021 році – «Зима/Сніг».

           Сам письменник про ці творчі проекти розповідає так: «Нас довгий час сприймали як суто літературний проект. Ми довго не могли знайти ні свій формат, ні своє звучання: це був неоковирний проект, який подобався тільки тим, хто глибоко перейнявся. І тільки з третього альбому у нас з’явилися слухачі. Зараз аудиторія «Собак» зовсім інша: багато тих, хто і читає, і слухає, але є багато молодих, дітей, які думають, що я співак. І потім дивуються, що в мене ще є якісь книжки. Я до цього з самоіронією ставлюсь».

           У жовтні 2021 року в Харківському національному академічному театрі опери та балету імені Лисенка відбулася прем'єра авангардної опери «Вишиваний. Король України». Автором лібрето опери був С. Жадан. У 2023 році видавництво Meridian Czernowitz випустило у світ нову книжку письменника – збірку поезій про мову під назвою «Скрипниківка», яку він почав готувати до друку ще навесні 2021 року. У 2023 році вийшло й оновлене видання «Гімн демократичної молоді», у якому вміщено шість ліричних історій про розвиток середнього бізнесу в умовах формування відкритого суспільства. Сюжет книги поєднує в собі ліричну оповідь із фаховими публіцистичними розвідками, присвяченими легалізації тіньового сектору економіки.

           С. Жадан спеціалізується на перекладах з німецької та англійської мови. Зокрема, він переклав поезії Пауля Целан і Чарльза Буковскі. Його власні твори перекладено німецькою, англійською, естонською, французькою, італійською, шведською, норвезькою, польською, сербською, хорватською, литовською, латвійською, білоруською, російською, угорською, вірменською та чеською мовами.

           Окремі твори Сергія Жадана введені в програму з української літератури середньої школи.
           """
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      back5 = types.InlineKeyboardButton(text="назад до меню", callback_data="back5")
      keyboard.add(back5)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == "back5":
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://scontent-iev1-1.xx.fbcdn.net/v/t1.6435-9/156698258_301903617958662_2768899525189669617_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=53a332&_nc_ohc=DN6QRsSyxEgQ7kNvgH05IS_&_nc_ht=scontent-iev1-1.xx&oh=00_AYCRocjwl1bfYGs2ypbQfh03slvun2DPf_LDNVXnRoQnxg&oe=66D86E7E",
                     caption= "головне меню",
                     reply_markup=keyboard)


    if call.data == "muz":
      text = """
          Жадан – фроетмент гурту Жадан і Собаки (ЖіС) та Лінія Маннергейма. Також батько має хіти записані з іншими виконавцями, таким як: Брати Гадюкіни, Христина Соловій та інші... \n А ось посилання на стріінгові сервіси: \n
           Spotify: https://open.spotify.com/artist/2Reqc0B9PCsI6t78c9k11o?si=WcN1Rq4yTkGkUzP_CklWcQ \n YouTube Music: https://music.youtube.com/channel/UCDinl507rIgCZvZErg_xZDg \n
           Spotify: https://open.spotify.com/artist/2IeDAlsxWzXuwU5i0kbE28?si=d4yJoO_bTpqcN20biQNKEQ \n YouTube Music: https://music.youtube.com/channel/UCk0y6EUzNVGaCa9qLEDHAcw
          """
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      back6 = types.InlineKeyboardButton(text="назад до меню", callback_data="back6")
      keyboard.add(back6)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
    if call.data == "back6":
      text = "головне меню"
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://static.dw.com/image/62273791_605.jpg",
                     caption= "головне меню",
                     reply_markup=keyboard)

    if call.data == "pere":
      text = """
      Письменницька і перекладацька творчість Пише романи, поезії, есеї. Темою творів письменника є пострадянська дійсність в Україні. Для стилю Жадана характерний вжиток розмовної та нецензурної лексики.

      Роман «Ворошиловград» став книжкою 2010 року за версією «Бі-бі-сі». Презентація роману в Старобільську, на батьківщині письменника, відбулася 7 квітня 2011 року під час Донбас-туру[27], проведеного Правозахисним центром «Поступ» і Літературним угрупованням СТАН у межах Громадської кампанії проти встановлення цензури в Україні. Через тиск місцевої влади деякі виступи, заплановані в рамках Донбас-туру, скасували.

      Перекладає поезію з німецької (в тому числі Пауля Целана), англійської (в тому числі Чарлза Буковскі), білоруської (в тому числі Андрія Хадановича), російської (в тому числі Кирила Медведєва, Данилу Давидова) мов.

      Тексти Жадана перекладалися німецькою, англійською, польською, французькою, італійською, нідерландською, данською, сербською, хорватською, литовською, естонською, білоруською, російською, вірменською та деякими іншими мовами.

      У 2014 році в рамках фестивалю відеопоезії CYCLOP брав участь у проєкті «роздІловІ».

      У 2023 році його вірш зачитав англійською відомий ірландський актор із Гри престолів Джек Ґлісон . Цей вірш перший був надрукований у Нью Йорк Таймс .[28] - подякуємо вікіпедії))
      """
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      back7 = types.InlineKeyboardButton(text="назад до меню", callback_data="back7")
      keyboard.add(back7)
      bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    if call.data == "back7":
      text = "головне меню"
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      btn1 = types.InlineKeyboardButton(text="Хто такий Жадан", callback_data="who")
      btn2 = types.InlineKeyboardButton(text="Творчість", callback_data="tworchist")
      btn3 = types.InlineKeyboardButton(text="Допомога", callback_data="helps")
      btn4 = types.InlineKeyboardButton(text="Соц мережі Батька", callback_data="moreone")
      keyboard.add(btn1, btn2, btn3, btn4)
      bot.send_photo(call.message.chat.id,
                     "https://lifeimg.pravda.com/images/doc/5/e/5e3ad45-jadan-serhiy-3.jpg",
                     caption= "головне меню",
                     reply_markup=keyboard)



@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, "Некоректне питання")
@bot.message_handler(content_types=['video'])
def video(message):
    bot.send_message(message.chat.id, "Некоректне питання")
@bot.message_handler(content_types=['audio'])
def audio(message):
    bot.send_message(message.chat.id, "Некоректне питання")
@bot.message_handler(content_types=['animation'])
def animation(message):
    bot.send_message(message.chat.id, "Некоректне питання")
@bot.message_handler(content_types=['voice'])
def voice(message):
    bot.send_message(message.chat.id, "Некоректне питання")
@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.send_message(message.chat.id, "Некоректне питання")


bot.polling(none_stop = True)