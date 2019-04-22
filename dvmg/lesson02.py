import smtplib
import os


message = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. После окончания курса у тебя будет 2 месяца, чтобы догнать программу. 
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

message = message.replace('%website%','dvmn.org')
name = 'Иван'
message = message.replace('%friend_name%',name)
my_name = 'Николай'
message = message.replace('%my_name%',my_name)

login = os.getenv("login")
password = os.getenv("password")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)

message = message.encode("UTF-8")
email_from = 'interworni@ya.ru'
email_to = 'wol87@ya.ru'
server.sendmail(email_from, email_to, message)
server.quit()