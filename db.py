import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)

cursor.execute("DROP TABLE IF EXISTS flat")
cursor.execute("DROP TABLE IF EXISTS house")

request = ("CREATE TABLE IF NOT EXISTS flat"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255),"
           "price INTEGER,"
           "rooms INTEGER,"
           "square INTEGER"
           "image_name VARCHAR(255))")
cursor.execute(request)

request = ("CREATE TABLE IF NOT EXISTS house"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "town VARCHAR(255),"
           "price INTEGER,"
           "rooms INTEGER,"
           "square INTEGER"
           "image_name VARCHAR(255))")
cursor.execute(request)

insert_request = ("INSERT INTO flat"
                  "(name, description, price, rooms, square, image_name) VALUES (?, ?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("квартира №1", "Ця квартира була недавно збудована, тут нова мебель, гарний краєвид і вона розташована неподалеку від торгового центру."))
cursor.execute(insert_request, ("квартира №2", "Двоккімнатна квартира у центрі містаБ чудовий варіант для того хто працює удома.", ""))
cursor.execute(insert_request, ("квартира №3", "Ця квартира ідеальний варіант для багатодітної сім'ї. Це трикімнатна квартира неподалеку від центрального парку.", ""))
cursor.execute(insert_request, ("квартира №4", "Однокімнатна квартира, для того хто живе один, розташована неподалеку від центру міста", ""))
cursor.execute(insert_request, ("квартира №5", "Чудовий варіант для одинкокої людини яка проводе багату часу на роботі, томущо ця квартира розташована у центрі міста.", ""))
cursor.execute(insert_request, ("квартира №6", "Трикімнатна квартира на останньому поверсі хмарочоса.", ""))
cursor.execute(insert_request, ("квартира №7", "Квартира на окраєні міста підійте тим хто любить тишину та покой.", ""))


insert_request = ("INSERT INTO house"
                  "(name, description, price, rooms, square, image_name) VALUES (?, ?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("Чудова квартира! Вся мебель в чудовому стані.", "5"))
cursor.execute(insert_request, ("На лінолеумі є подряпини та сліди залишивший вогонь. Всеодно можу порадити.", "3"))
cursor.execute(insert_request, ("Ідеальний варіант для нашої сім'ї ми у захваті.", "5"))
cursor.execute(insert_request, ("Квартира не подалеку від моєї роботи, чудовий варіант для мене.", "5"))
cursor.execute(insert_request, ("Все чудово але було б ще краще якби був гарний краєвид з вікна, а не вид на завод", "4"))

connection.commit()
connection.close()