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
           "description VARCHAR(255),"
           "price INTEGER,"
           "rooms INTEGER,"
           "square INTEGER"
           "image_name VARCHAR(255))")
cursor.execute(request)

insert_request = ("INSERT INTO flat"
                  "(name, description, price, rooms, square) VALUES (?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("квартира №1", "Ця квартира була недавно збудована, тут нова мебель, гарний краєвид і вона розташована неподалеку від торгового центру.", "1500$", "2 кімнати", "45м²"))
cursor.execute(insert_request, ("квартира №2", "Двоккімнатна квартира у центрі містаБ чудовий варіант для того хто працює удома.", "950$", "2 кімнати", "40м²"))
cursor.execute(insert_request, ("квартира №3", "Ця квартира ідеальний варіант для багатодітної сім'ї. Це трикімнатна квартира неподалеку від центрального парку.", "1640$", "3 кімнати", "45м²"))
cursor.execute(insert_request, ("квартира №4", "Однокімнатна квартира, для того хто живе один, розташована неподалеку від центру міста", "900$", "1 кімната", "30м²"))
cursor.execute(insert_request, ("квартира №5", "Чудовий варіант для одинкокої людини яка проводе багату часу на роботі, томущо ця квартира розташована у центрі міста.", "1050$", "2 кімнати", "40м²"))
cursor.execute(insert_request, ("квартира №6", "Трикімнатна квартира на останньому поверсі хмарочоса.", "1850$", "3 кімнати", "50м²"))
cursor.execute(insert_request, ("квартира №7", "Квартира на окраєні міста підійте тим хто любить тишину та спокій.", "800$", "1 кімната", "35м²"))


insert_request = ("INSERT INTO house"
                  "(name, description, price, rooms, square) VALUES (?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("дім №1", "Двоповерховий дім на горі, підійде для тих хто любить свіже повітря.", "2800$", "5 кімнат 2 туалети", "65м²"))
cursor.execute(insert_request, ("дім №2", "Дім у центрі спокійного та безпечного району.", "1900$", "3 кімнати 1 туалет", "55м²"))
cursor.execute(insert_request, ("дім №3", "Цей дім знаходиться неподалеку від популярного коледжу.", "1750$", "2 кімнати 1 туалет", "50м²"))
cursor.execute(insert_request, ("дім №4", "Сімейний дім в безпечному районі.", "1800$", "3 кімнати 1 туалет", "55м²"))
cursor.execute(insert_request, ("дім №5", "Дім з горищем, щоб зберігати більше потрібніх речей.", "2050$", "2 кімнати 1 туалет", "47м²"))
cursor.execute(insert_request, ("дім №6", "Двоповерховий дім з балконом.", "2200$", "4 кімнати 2 туалети", "57м²"))
cursor.execute(insert_request, ("дім №7", "Одноповерховий дім з гаражем, та басейном.", "2600$", "3 кімнати 2 туалети", "60м²"))

connection.commit()
connection.close()