import ptbot
import os
from pytimeparse import parse

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
  iteration = min(total, iteration)
  percent = "{0:.1f}"
  percent = percent.format(100 * (iteration / float(total)))
  filled_length = int(length * iteration // total)
  pbar = fill * filled_length + zfill * (length - filled_length)
  return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def notify_progress(secs_left, id, total):
  bar = render_progressbar (total, total-secs_left)
  text = '''Осталось {} секунд
  {}'''.format(secs_left,bar)
  bot.update_message(chat_id, id, text)

def reply(text):
  timer = parse (text)
  bot.send_message(chat_id,"Таймер запущен на {} секунд".format(timer))

  bar = render_progressbar (timer, 0)
  text = '''Осталось {} секунд
  {}'''.format(timer,bar)
  message_id = bot.send_message(chat_id, text)
  
  bot.create_countdown(timer, notify_progress, id=message_id, total=timer)
  bot.create_timer(timer, bot.send_message, chat_id, "Время вышло") 

def main():
  bot.send_message(chat_id, "На сколько запустить таймер?")
  bot.wait_for_msg(reply)

if __name__ == '__main__':
  token = os.getenv("token")
  chat_id = os.getenv("chat_id")
  bot = ptbot.Bot(token)
  main()
  