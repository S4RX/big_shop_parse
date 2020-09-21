from __future__ import unicode_literals
from unicodedata import normalize

import sqlite3
from sqlite3 import Error

path_to_db = [('м. Київ', 'бул. Чоколівський, 28/1'),
	('м. Київ', 'просп. Маяковського, 75/2'),
	('м. Київ', 'вул. Січових Стрільців, 37/41'),
	('м. Київ', 'вул. Закревського Миколи, 61/2'),
	('м. Київ', 'вул. Стальського, 22/10'),
	('м. Київ', 'просп. Маяковського, 43/2'),
	('м. Дніпро', 'просп. Слобожанський, 76/78'),
	('м. Маріуполь', 'вул. Київська, 27/1'),
	('м. Одеса', 'вул. Єврейська, 50/1'),
	('м. Одеса', 'вул. Героїв Крут, 17/1'),
	('м. Одеса', 'вул. Катеринінська, 27/1'),
	('м. Полтава', 'вул. Зіньківська, 6/1а'),
	('м. Полтава', 'вул. Мазепи Гетьмана, 45/4'),
	('м. Суми', 'вул. Харківська, 2/2'),
	('м. Суми', 'просп. Лушпи Михайла, 4/1'),
	('м. Харків', 'просп. Московський, 206/1'), 
	('м. Харків', 'просп. Тракторобудівників, 59/56'),
	('м. Харків', 'просп. Гагаріна Юрія, 167/1'),
	('м. Черкаси', 'бул. Шевченка, 208/1'),
	('м. Васильків', 'вул. Соборна, 64/1'),
	('м. Кам’янець-Подільський', 'шосе Нігинське, 41/1'),
	('м. Миргород', 'вул. Гоголя Миколи, 98/6'),
	('м. Ніжин', 'вул. Незалежності, 36/1'),
	('м. Радомишль', 'вул. Велика Житомирська, 1/2'),
	('м. Самбір', 'вул. Валова, 24/1')]

for adress in path_to_db:
	if '/' in adress[1]:
		fir_adr = adress[0]
		sec_adr = adress[1].replace('/', '-')
		print(fir_adr, sec_adr)
	


#def create_connection(path_to_db):
#    """ create a database connection to a SQLite database """
#    conn = None
#    try:
#        conn = sqlite3.connect(path_to_db)
#        print(sqlite3.version)
#    except Error as e:
#        print(path_to_db)
#    finally:
#        if conn:
#            conn.close()
#
#def main():
#	for adress in path_to_db:
#		path_to_db = r"db\\" + str(adress) + ".db"
#		create_connection(path_to_db)
#
#if __name__ == '__main__':
#    main()
#    #create_connection(r"D:\project price\db\pythonsqlite.db")

#full = []
#
#a = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
#b = ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
#for pair in zip(a, b):
#	full.append(pair)
#print(full)
#
#for smth in full:
#	print(smth[0])


#x = u'\u0413\u0435\u043b\u044c \u043a\u0430\u043f\u0441\u0443\u043b\u0438 Tide 3\u043c\u0441 12\u0448\u0442 \u0430\u043b\u044c\u043f\u0456\u0439\u0441\u044c\u043a\u0430 c\u0432\u0456\u0436\u0456\u0441\u0442\u044c'
#y = x.encode().decode()

#print(y)
#print(type(x))
#exit()


#def normalize_special_char(txt):
#	return normalize('NFC', txt).encode('ASCII', 'ignore').decode('ASCII')

#def main():
#	handle = open('data.json', 'r')
#	data = handle.readlines()
#	print(str(data.encode().decode())
#	handle.close()
#	#print(data.read())
#	#atad = data.read()
#	#text = atad.encode().decode()
#	#print(text)
#
#
#if __name__ == '__main__':
#	main()#