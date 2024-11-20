import telebot
from telebot import types

token = "token"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def nachalo(message):
    markup999 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Начать игру")
    button2 = types.KeyboardButton("Начать игру")
    markup999.add(button1, button2)
    nick = message.from_user.username
    bot.send_message(message.chat.id, 'РАБОТУ ВЫПОЛНИЛ КАРТАШОВ АРСЕНИЙ 10Н КЛАСС \n\n'
                                      'Добро пожаловать '+ f"@{nick}"+'.\n'
                                      'Это бот - игра, напишите "Начать игру" и игра запустится'.format(message.from_user), reply_markup=markup999)

@bot.message_handler(content_types=["text"])
def igra(message):

    markupres = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Заного")
    markupres.add(button1)
    global checkup
    if "Начать игру" in message.text or "начать игру" in message.text or "Заного" in message.text or "заного" in message.text:
        checkup = 0
        checkup = 1
        bot.send_message(message.chat.id, "И так пройдемся по правилам.\n"
                                          "1. Тут нет контрольных точек, ошибка - и вы начинаете заного.\n"
                                          "2. Неограниченное число попыток.\n"
                                          "3. Для удобства будут выведены кнопки с текстом, вы можете использовать их или писать текст сами."
                                          "Ну что же, начнем!")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Первая дверь")
        button2 = types.KeyboardButton("Вторая дверь")
        button3 = types.KeyboardButton("Третья дверь")
        button4 = types.KeyboardButton("Четвертая дверь")
        markup.add(button1, button2, button3, button4)
        bot.send_photo(message.chat.id,'https://blog.d-it.ru/upload/resize_cache/main/201/800_800_1/closed1.png', 'Внимательно читайте условие. У вас есть 3 двери, за одной горит огонь который НЕВОЗМОЖНО потушить, за второй дверью находится открытый космос без признаков жизни рядом, в третьей двери лев, который не ел уже 15 лет. Ну а в четвертой двери находится бесплатный сыр. Внимание вопрос, в какую дверь вы пойдете?'.format(message.from_user), reply_markup=markup)
    elif "Первая дверь" in message.text:
        if checkup == 1:
            checkup = 0
            bot.send_message(message.chat.id, "Вы зашли в дверь где горит огонь, у вас нет защитного костюма, GAME OVER. Для старта новой игры напишите Заного".format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id, 'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Вторая дверь" in message.text:
        if checkup == 1:
            checkup = 0
            bot.send_message(message.chat.id, 'В Космосе нет кислорода, а у вас нет скафандра, GAME OVER. Для старта новой игры напишите Начать игру или заного'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Четвертая дверь" in message.text:
        if checkup == 1:
            checkup = 0
            bot.send_message(message.chat.id, 'Здесь нет четвертой двери, читайте условие внимательно, GAME OVER. Для старта новой игры напишите Начать игру или заного'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Третья дверь" in message.text:
        if checkup == 1:
            checkup = 2
            bot.send_message(message.chat.id, 'Правильно! Ведь лев не может выжить без еды 15 лет, вы проходите дальше!')
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Работник фабрики")
            button2 = types.KeyboardButton("Охранник")
            button3 = types.KeyboardButton("Водитель грузовика")
            markup1.add(button1, button2, button3)
            bot.send_photo(message.chat.id, 'https://school-of-inspiration.ru/wp-content/uploads/2020/11/5ae1ce7200f5c794801760.jpg', 'Вы - частный детектив, который расследует серьезные дела. В этот раз у вас очень ответственное дело... На фабрике, которая переплавляет золото '
                                              'украли большую поставку этого драгоценного камня. у вас есть 3 подозреваемых, стоит заметить, что на улице сейчас январь и -25 градусов. И так, подозреваемые \n\n'
                                              'Первый подозреваемый Работник фабрики: "На момент ограбления я был на обеденном перерыве, все таки это произошло в период с часу до двух... \n\n'
                                              'Второй подозреваемый Охранник: "Я сидел на рабочем месте и услышал шум снаружи, но так как я ношу очки, при выходе из помещения они запотели и я не разглядел машину... \n\n'
                                              'Третий подозреваемый Водитель грузовика: "Все было как обычно, я привез груз, находясь под охраной и после отчитался перед начальством." \n\n'
                                              'Подумав несколько минут, Детектив понял, кто ему соврал и арестовал его. ВНИМАНИЕ ВОПРОС, кто украл ИЛИ помог украсть золото?'.format(message.from_user), reply_markup=markup1)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Работник фабрики" in message.text:
        if checkup == 2:
            checkup = 0
            bot.send_message(message.chat.id, "Работник фабрики сказал абсолютную правду... GAME OVER. Для старта новой игры напишите Начать игру или заного".format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Водитель грузовика" in message.text:
        if checkup == 2:
            checkup = 0
            bot.send_message(message.chat.id, "В словах водителя грузовика детектив не нашел ничего критического. GAME OVER. Для старта новой игры напишите Начать игру или заного".format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Охранник" in message.text:
        if checkup == 2:
            checkup = 3
            bot.send_message(message.chat.id, "Все верно, детектив арестовал охранника потому что он ему соврал, вспомним, что на улице -25 градусов и охранник вышел из теплого помещения в холодное, а процесс запотевания происходит"
                                              " если выйти из холода в тепло, тем самым охранник соврал.")
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Вперед")
            button2 = types.KeyboardButton("Влево")
            button3 = types.KeyboardButton("Вправо")
            markup2.add(button1, button2, button3)
            bot.send_photo(message.chat.id,'https://otvet.imgsmail.ru/download/u_1bb6f2accaf45c87c578bc74c0726210_800.jpg', 'Проверим вашу удачу, куда вы пойдете?'.format(message.from_user), reply_markup=markup2)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Вперед" in message.text or "Влево" in message.text or "Вправо" in message.text:
        if checkup == 3:
            checkup = 4
            bot.send_message(message.chat.id, 'Поздравляю, вопрос был с подвохом) Вы прошли дальше!')
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Бензин")
            button2 = types.KeyboardButton("Свечка")
            button3 = types.KeyboardButton("Газовая горелка")
            button4 = types.KeyboardButton("Нет правильного варианта")
            markup3.add(button1,button2,button3,button4)
            bot.send_photo(message.chat.id,'https://masterpiecer-images.s3.yandex.net/5ce90ca28ac411ee9d0c261105627a54:upscaled', 'Вы находитесь в полной темноте, у вас есть спички, бензин, свечка, газовая горелка. Внимание вопрос, что вы зажжете в первую очередь'.format(message.from_user), reply_markup=markup3)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Бензин" in message.text:
        if checkup == 4:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, вы проиграли GAME OVER, напишите "Начать игру" или "Заного" для перезапуска игры'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Газовая горелка" in message.text:
        if checkup == 4:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, вы проиграли GAME OVER, напишите "Начать игру" или "Заного" для перезапуска игры'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Свечка" in message.text:
        if checkup == 4:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, вы проиграли GAME OVER, напишите "Начать игру" или "Заного" для перезапуска игры'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Нет правильного варианта" in message.text:
        if checkup == 4:
            checkup = 5
            bot.send_message(message.chat.id, 'Верно, первым делом необходимо зажечь спичку!')
            markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Его догнал лев")
            button2 = types.KeyboardButton("На него упал кирпич")
            button3 = types.KeyboardButton("Его задавил слон")
            markup4.add(button1,button2,button3)
            bot.send_photo(message.chat.id, 'https://img.freepik.com/premium-photo/lion-cabin-plane-concept-business-travel_627050-3514.jpg', 'В самолете было 100 кирпичей, 1 упал, осталось 99 кирпичей. \n'
                                              'Как положить слона в холдильник в 3 действия? Открыть холодильник, положить слона в холодильник, закрыть холодтльник. \n\n'
                                              'А как полжить жирафа в 4 действия? Открыть холодильик, вытащить слона, положить жирафа, закрыть холодильник. \n\n'
                                              'У льва сегодня день рождения, он позвал всех зверей праздновать, но один не пришел, кто? верно, жираф, потому что он в холодильникею \n\n'
                                              'Стикман кукла шел по непроходимым болотам, казалось, он обречен, но после них он выжил. \n'
                                              'Но по непредвиденной ситуации стикман все таки погиб, и так, почему же стикман погиб?'.format(message.from_user), reply_markup=markup4)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Его задавил слон" in message.text:
        if checkup == 5:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, слон отдыхает после праздника, GAME OVER, напишите "Начать игру" или "Заного" для перезапуска игры'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Его догнал лев" in message.text:
        if checkup == 5:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, лев сегодня в хорошем настроении, GAME OVER, напишите "Начать игру" или "Заного" для перезапуска игры'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "На него упал кирпич" in message.text:
        if checkup == 5:
            checkup = 6
            bot.send_message(message.chat.id, 'Верно! В самом начале из самолета упал 1 кирпич, ведь тут нет ограничений по временным рамкам')
            markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Майнкрафт")
            button2 = types.KeyboardButton("Тетрис")
            button3 = types.KeyboardButton("Симулятор строителя")
            markup5.add(button1,button2,button3)
            bot.send_photo(message.chat.id, 'https://www.anatomiyasna.ru/uploads/images/product/divan-chepers-niu-iork-uglovoi-06.jpg', 'В прямоугольной комнате, которая абсолютно пустая, в углу стоит диван в форме буквы Г, позже там поставили квадратный стол, прямо перед этим диваном, тем самым \n'
                                                                                                                                        'заполонили пространство и буква Г превратилась в прямоугольник, вопрос, на какую игру присутствует отсылка в данном примере?'.format(message.from_user), reply_markup=markup5)
        else:
            bot.send_message(message.chat.id,'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)

    elif "Майнкрафт" in message.text:
        if checkup == 6:
            checkup = 0
            bot.send_message(message.chat.id, "Увы, вы не угадали, GAME OVER, напишите Начать игру или Заного".format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Симулятор строителя" in message.text:
        if checkup == 6:
           checkup = 0
           bot.send_message(message.chat.id, "Увы, вы не угадали, GAME OVER, напишите Начать игру или Заного".format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Тетрис" in message.text:
        if checkup == 6:
            checkup = 7
            markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Первый человек")
            button2 = types.KeyboardButton("Второй человек")
            button3 = types.KeyboardButton("Третий человек")
            button4 = types.KeyboardButton("Четвертый человек")
            markup9.add(button1,button2,button3,button4)
            bot.send_message(message.chat.id, 'Правильно! Вы молодцы что вспомнили эту игру.')
            bot.send_photo(message.chat.id, 'https://i.imgur.com/ckrH58m.png', 'Предыстория. Вы - Максим и работаете в офисе, вы всегда носите браслет со своим именем, браслет не на правой руке, и часов нет, также как и у вашего лучшего друга.\n\n'
                                                  'Максим сидел на работе и внезапно выиграл в лотерею джекпот. Он сказал своему бухгалтеру что хочет разделить выигрыш '
                                                  'с неким Андреем. Внезапно, все его знакомые начали представлятся Андреями, чтобы обмануть бухгалтера и забрать выйгрыш себе. Кто же все таки настоящий Андрей? \n\n'
                                                  'ВНИМАНИЕ НА КАРТИНКУ '
                                                  ''.format(message.from_user),reply_markup=markup9)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Первый человек" in message.text:
        if checkup == 7:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, вы отдали выигрыш не тому человеку, GAME OVER'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Второй человек" in message.text:
        if checkup == 7:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, вы отдали выигрыш не тому человеку, GAME OVER'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Четвертый человек" in message.text:
        if checkup == 7:
            checkup = 0
            bot.send_message(message.chat.id, 'Неверно, вы отдали выигрыш не тому человеку, GAME OVER'.format(message.from_user), reply_markup=markupres)
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
    elif "Третий человек" in message.text:
        if checkup == 7:
            checkup = 8
            bot.send_message(message.chat.id, 'Верно! Ведь только у него такой же браслет как и у вас!')
        else:
            bot.send_message(message.chat.id,
                             'Что же вы торопитесь, вам нужно сначала дойти до этого вопроса! напишите Начать игру или Заного'.format(message.from_user), reply_markup=markupres)
        if checkup == 8:
            bot.send_message(message.chat.id, 'Поздравляю вас, вы справились с 7 очень сложными загадками, с которыми не справляется 99.9999999%, поздравляю вас и дарю тортик!')
            bot.send_photo(message.chat.id, 'https://storage.saastra.ru/main/__sized__/uploads/products/ZHP01575-thumbnail-1500x1500-100.jpg')
    else:
        bot.send_message(message.chat.id, "Вы видимо не поняли условие задания, такого выбора нет".format(message.from_user), reply_markup=markupres)


bot.infinity_polling()