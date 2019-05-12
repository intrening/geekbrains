from file_operations import render_template
from faker import Faker
import random

AVATARS_NUMBER = 10
SKILLS_NUMBER = 3
CHARACT_MIN = 8
CHARACT_MAX = 14

fake = Faker("ru_RU")

dic = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋'
}

def new_context():
  with open ('skills.txt') as f:
    skills = f.read().strip().split('\n')

  random_skills = random.sample(skills, SKILLS_NUMBER)

  for skill_num in range(len(random_skills)):
    for key, value in dic.items():
      random_skills[skill_num] = random_skills[skill_num].replace(key, value)

  context = {
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'job': fake.job(),
    'town': fake.city(),
    'strength': random.randint(CHARACT_MIN,CHARACT_MAX),
    'agility': random.randint(CHARACT_MIN,CHARACT_MAX),
    'endurance': random.randint(CHARACT_MIN,CHARACT_MAX),
    'intelligence': random.randint(CHARACT_MIN,CHARACT_MAX),
    'luck': random.randint(CHARACT_MIN,CHARACT_MAX),
    'skill_1': random_skills[0],
    'skill_2': random_skills[1],
    'skill_3': random_skills[2]
  }
  return context


def main():
  for avatars in range(AVATARS_NUMBER):
    render_template ('charsheet.svg','charsheets/charsheet_{}.svg'.format(avatars),new_context())

if __name__ == '__main__':
  main()
  