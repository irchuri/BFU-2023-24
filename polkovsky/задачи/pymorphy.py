import pymorphy3

morph = pymorphy3.MorphAnalyzer()

user_name_lower = (morph.parse(input('Здравствуйте! Как вас зовут?\n'))[0]).inflect({'ablt'}).word
user_name = str(user_name_lower).capitalize()

print(f'Плохого человека {user_name} не назовут.')

answer = input('Вы играете в Dota 2?\n')
if answer.lower() == 'да':
    character_lower = (morph.parse(input('Какой ваш любимый персонаж? \n'))[0]).inflect({'loct'}).word
    character = str(character_lower).capitalize()
    print(f'Играйте дальше, однажды весь мир узнает о вашем мастерстве на {character}!')
if answer.lower() == 'нет':
    print('Очень жаль. Был рад с вами пообщаться!')
