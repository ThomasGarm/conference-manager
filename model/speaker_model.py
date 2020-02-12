from conneclass.connection import Connection



class request_model_speaker():
    def __init__(self):
        self.db = Connection()

    def add_speaker(self, arg):
        sql ="""INSERT INTO speaker (firstname, lastname, description, profession) VALUES (%s, %s, %s, %s );"""
        arguments = (arg.firstname, arg.lastname, arg.description, arg.profession)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def del_speaker_cascade(self):
        sql = "DELETE FROM speaker WHERE lastname=%s AND firstname= %s);"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        self.db.connection.commit()
        self.db.close_connection()

            


    def get_all_speaker(self, date):
        sql = "SELECT * FROM speaker WHERE lastname = %s AND firstname=%s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date,))
        speak = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(rdv):
            speak [key] = Speaker(value)
            return speak

    def get_rdv(self, date, hour):
        sql = "SELECT * FROM calendar WHERE date = %s and hour=%s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        rdv = self.db.cursor.fetchone()
        self.db.close_connection()
        return Rdv(rdv)