import sqlite3

def create_all():
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS "
        "users "
        "("
        "id INTEGER, "
        "name TEXT, "
        "user TEXT, "
        "coin INTEGER DEFAULT 100, "
        "diamond INTEGER DEFAULT 0, "
        "ban INTEGER DEFAULT 0, "
        "wearpet BLOB DEFAULT 1, "
        "channelbonus INTEGER DEFAULT 0, "
        "vip INTEGER DEFAULT 0, "
        "promo INTEGER DEFAULT 0, "
        "PRIMARY KEY(id)"
        ")"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS "
        "pets "
        "("
        "id INTEGER, "
        "allpet INTEGER DEFAULT 1, "
        "butterfly INTEGER DEFAULT 1, "
        "butterflyGOLD INTEGER DEFAULT 0, "
        "dog INTEGER DEFAULT 0, "
        "dogGOLD INTEGER DEFAULT 0, "
        "pig  INTEGER DEFAULT 0, "
        "pigGOLD INTEGER DEFAULT 0, "
        "pumbkin INTEGER DEFAULT 0, "
        "cow INTEGER DEFAULT 0, "
        "cowGOLD INTEGER DEFAULT 0, "
        "vip INTEGER DEFAULT 0, "
        "lugia INTEGER DEFAULT 0, "
        "bulbosour INTEGER DEFAULT 0, "
        "tortank INTEGER DEFAULT 0, "
        "skwirtl INTEGER DEFAULT 0, "
        "PRIMARY KEY(id)"
        ")"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS "
        "inventory "
        "("
        "id INTEGER, "
        "glove INTEGER DEFAULT 0, "
        "PRIMARY KEY(id)"
        ")"
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS "
        "eggs "
        "("
        "id INTEGER, "
        "defaultEgg INTEGER DEFAULT 0, "
        "premiumEgg INTEGER DEFAULT 0, "
        "PRIMARY KEY(id)"
        ")"
    )
    connection.commit()