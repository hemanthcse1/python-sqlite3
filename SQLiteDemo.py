import sqlite3


connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", None),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

cursor.executemany(
    "insert into gta values (?, ?, ?)",release_list)

# print database
for row in cursor.execute("select * from gta"):
    print(row)

# print specific rows
print("******************************")
cursor.execute("select * from gta where city=:c", {"c":"Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

cursor.execute("CREATE TABLE IF NOT EXISTS cities (gta_city text, real_city text)")
cursor.execute("INSERT INTO cities VALUES (?,?)", ("Liberty City","New York"))
cursor.execute("select * from cities where gta_city=:c", {"c":"Liberty City"})
cities = cursor.fetchall()

print(cities)

# Manipulate database cities
print("******************************")
for i in gta_search:
    adjusted = [cities[0][1] if value==cities[0][0] else value for value in i]
    print(adjusted)

connection.close()