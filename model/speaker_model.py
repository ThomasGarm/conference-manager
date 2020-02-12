from conneclass.connection import Connection
from conneclass.speaker import Speaker



class request_model_speaker(Speaker):
    def __init__(self):
        self.db = Connection()
        super().__init__()

    def add_speaker(self, arg):
        sql ="""INSERT INTO speaker (firstname, lastname, description, profession) VALUES (%s, %s, %s, %s );"""
        arguments = (arg.firstname, arg.lastname, arg.description, arg.profession)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_speaker_cascade(self):
        sql = "DELETE FROM speaker WHERE lid=%s);"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        self.db.connection.commit()
        self.db.close_connection()

            


    def get_all_speaker(self, lastname, firstname):
        sql = "SELECT * FROM speaker ;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,)
        speak = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(speak):
            speak [key] = Speaker(value)
            return speak

    def get_speaker(self, lastname, firstname):
        sql = "SELECT * FROM speaker WHERE id=%s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (id,))
        speak = self.db.cursor.fetchone()
        self.db.close_connection()
        return speak