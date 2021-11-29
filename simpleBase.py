import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('test_database.db')
cur = conn.cursor()
print('бд подключена к SQLite успешно!')

print('1) Создать базу данных')
print('2) Добавить информацю в БД')
print('3) Считать информацию из БД')
print('4) Удалить информацию из БД')
enter = int(input('Выберите пункт> '))

def add_bd():
	try:
		table = """CREATE TABLE IF NOT EXISTS table_1 (
				id INTEGER PRIMARY KEY,
				phone_number INT,
				name TEXT,
				familia TEXT,
				otchestvo TEXT,
				city TEXT,
				street TEXT,
				home INT,
				appartament INT,
				vk TEXT);"""

		cur.execute(table)
		conn.commit()
		print('Таблица бд создана!')

	except sqliteError as error:
		print('Ошибка!', error)

def add_info_bd():
	phone_number = input('Введите номер телефона (в формате 79126457233) > ')
	print('Введите именные данные лица (в формате Иван Иванов Иванович):') 
	name = input('Имя > ')
	familia = input('Фамилия >  ')
	otchestvo = input('Отчество > ')
	print('Введите адресные данные лица (в формате Москва Краснооктябрьская):')
	city = input('Город > ')
	street = input('Улица > ')
	home = input('Дом > ')
	appartament = input('Квартира > ')
	vk = input('Введите его id вк > ')
	user = (phone_number, name, familia, otchestvo, city, street, home, appartament, vk)

	cur.execute("INSERT INTO table_1(phone_number, name, familia, otchestvo, city, street, home, appartament, vk) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
	conn.commit()

	print('Информация успешно добавлена в базу данных.')

def read_info_bd():
	print('По какому параметру будет поиск:')
	print('1) По фамилии')
	print('2) По номеру телефона')
	print('3) По id ВК')
	print('4) По улице')
	par_search = int(input('>>> '))

	if par_search == 1:
		search_familia = input('Введите фамилию лица (в формате Иванов) > ')
		cur.execute("SELECT * FROM table_1 WHERE familia=?;", (search_familia,))
		familia_results = cur.fetchall()
		for row in familia_results:
			print('--------------------------------------------------')
			print('ID:', row [0])
			print('Номер телефона:', row [1])
			print('Имя:', row [2])
			print('Фамилия:', row [3])
			print('Отчество:', row [4])
			print('Город:', row [5])
			print('Улица:', row [6])
			print('Дом:', row [7])
			print('Квартира:', row [8])
			print('id ВК:', row [9])
			print('--------------------------------------------------')
	elif par_search == 2:
		search_phone_number = input('Введите номер телефона лица (в формате 79005553322) > ')
		cur.execute("SELECT * FROM table_1 WHERE phone_number=?;", (search_phone_number,))
		phone_results = cur.fetchall()
		for row in phone_results:
			print('--------------------------------------------------')
			print('ID:', row [0])
			print('Номер телефона:', row [1])
			print('Имя:', row [2])
			print('Фамилия:', row [3])
			print('Отчество:', row [4])
			print('Город:', row [5])
			print('Улица:', row [6])
			print('Дом:', row [7])
			print('Квартира:', row [8])
			print('id ВК:', row [9])
			print('--------------------------------------------------')
	elif par_search == 3:
		search_vk = input('Введите номер телефона лица (в формате id1 или rovenskih1) > ')
		cur.execute("SELECT * FROM table_1 WHERE vk=?;", (search_vk,))
		vk_results = cur.fetchall()
		for row in vk_results:
			print('--------------------------------------------------')
			print('ID:', row [0])
			print('Номер телефона:', row [1])
			print('Имя:', row [2])
			print('Фамилия:', row [3])
			print('Отчество:', row [4])
			print('Город:', row [5])
			print('Улица:', row [6])
			print('Дом:', row [7])
			print('Квартира:', row [8])
			print('id ВК:', row [9])
			print('--------------------------------------------------')
	elif par_search == 4:
		search_street = input('Введите улицу лица (в формате Краснооктябрьская) > ')
		cur.execute("SELECT * FROM table_1 WHERE street=?;", (search_street,))
		street_results = cur.fetchall()
		for row in street_results:
			print('--------------------------------------------------')
			print('ID:', row [0])
			print('Номер телефона:', row [1])
			print('Имя:', row [2])
			print('Фамилия:', row [3])
			print('Отчество:', row [4])
			print('Город:', row [5])
			print('Улица:', row [6])
			print('Дом:', row [7])
			print('Квартира:', row [8])
			print('id ВК:', row [9])
			print('--------------------------------------------------')
	else:
		print('Неправильно выбран пункт. Попробуйте ещё раз.')

def del_info_bd():
	id_str = input('Введите id строки БД > ')
	confirm_del = input('Подтверждаете удаление? [Y/N] >>> ')
	
	if confirm_del == 'Y' or confirm_del == 'y':
		pass
	else:
		print('Удаление отменено.')

	cur.execute("DELETE FROM table_1 WHERE id=?;", (id_str,))
	conn.commit()
	print('Строка успешно удалена.')

if enter == 1:
	add_bd()
elif enter == 2:
	add_info_bd()
elif enter == 3:
	read_info_bd()
elif enter == 4:
	del_info_bd()
else:
	print('Неправильно выбран пункт, попробуйте ещё раз!')
