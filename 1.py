name = input('Введите имя: ') 
surname = input('Введите фамилию: ') 
birth = int(input('Введите год рождения: ')) 
print(name, surname, birth, sep = '_') 
name, surname = surname, name 
print(name, surname, birth + 60, sep = '_')
