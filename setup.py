import sqlite3

# works, apparently
# Holds setup methods
# could be moved to main


class Setup:
    # Create table method
    def createTable(self, dbName, sql):
        with sqlite3.connect(dbName) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()

    # Main setup method
    def startSetup(self, name, country, city):
        dbName = "UserData.db"

        # Create userinfo
        sql = """CREATE TABLE userInfo
                 (Name text,
                  Country text,
                  City text,
                  primary key(Name))"""
        self.createTable(dbName, sql)

        with sqlite3.connect("UserData.db") as db:
            cursor = db.cursor()
            sql = """INSERT INTO userInfo (Name, Country, City) VALUES ('""" + name + """', '""" + country + """', '""" + city + """')"""
            cursor.execute(sql)
            db.commit

        # Alarms table
        sql = """CREATE TABLE Alarms
                    (AlarmID integer,
                    Title text,
                    Days text,
                    Time time,
                    CreationDate datetime,
                    Repeats boolean,
                    primary key(AlarmID))"""
        self.createTable(dbName, sql)

        # Notes table
        sql = """CREATE TABLE Notes
                    (NoteID integer,
                    Title text,
                    Content text,
                    Date datetime,
                    primary key(NoteID))"""
        self.createTable(dbName, sql)

        # Reminders table
        sql = """CREATE TABLE Reminders
                    (ReminderID integer,
                    Title text,
                    Content text,
                    Days text,
                    Time time,
                    CreationDate datetime,
                    Repeats boolean,
                    primary key(ReminderID))"""
        self.createTable(dbName, sql)


# Testing
c = Setup()
c.startSetup("jake", "france", "paris")
