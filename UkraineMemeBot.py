import telebot

bot = telebot.TeleBot("5834732958:AAE92_retPsHMnrSqvcpgfkf-NXihRMWlkY")

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "Вітаю! Будь ласка, оберіть команду у меню")

@bot.message_handler(commands = ["cat"])
def cat(message):
    cat = open("cat.mp4", "rb")
    bot.send_video(message.chat.id, cat)

@bot.message_handler(commands = ["kuchma"])
def kuchma(message):
    kuchma = open("kuchma.mp4", "rb")
    bot.send_video(message.chat.id, kuchma)

@bot.message_handler(commands = ["timoshenko"])
def timoshenko(message):
    timoshenko = open("yula.mp4", "rb")
    bot.send_video(message.chat.id, timoshenko)

@bot.message_handler(commands = ["kolada"])
def kolada(message):
    kolada = open("kolada.mp4", "rb")
    bot.send_video(message.chat.id, kolada)

@bot.message_handler(commands = ["mcpetya"])
def mcpetya(message):
    mcpetya = open("mcpetro.mp4", "rb")
    bot.send_video(message.chat.id, mcpetya)

@bot.message_handler(commands = ["klichko"])
def klichko(message):
    klichko = open("klichko.mp4", "rb")
    bot.send_video(message.chat.id, klichko)

@bot.message_handler(commands = ["ostonovites"])
def ostonovites(message):
    ostonovites = open("ostonovites.mp4", "rb")
    bot.send_video(message.chat.id, ostonovites)

@bot.message_handler(commands = ["ya_iz_bogatoi"])
def YaIzBogatoi(message):
    YaIzBogatoi = open("yaizbogatoi.mp4", "rb")
    bot.send_video(message.chat.id, YaIzBogatoi)

@bot.message_handler(commands = ["tzi_ruki_nicho_ne_kraly"])
def hands(message):
    hands = open("hands.mp4", "rb")
    bot.send_video(message.chat.id, hands)

@bot.message_handler(commands = ["de_smetana"])
def de_smetana(message):
    de_smetana = open("desmetana.mp4", "rb")
    bot.send_video(message.chat.id, de_smetana)

@bot.message_handler(commands = ["kit_havae"])
def cat2(message):
    cat2 = open("cat2.mp4", "rb")
    bot.send_video(message.chat.id, cat2)

@bot.message_handler(commands = ['solovev_dolboeb'])
def solovev_dolboeb(message):
    solovev_dolboeb = open("solovev_dolboeb (1).mp4", "rb")
    bot.send_video(message.chat.id, solovev_dolboeb)

@bot.message_handler(commands = ['gordon'])
def gordon(message):
    gordon = open("gordon.mp4", "rb")
    bot.send_video(message.chat.id, gordon)


bot.polling(none_stop = True)
