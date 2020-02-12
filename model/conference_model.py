from conneclass.connection import Connection
from conneclass.conference import Conference



class Request_model_conference(Conference):
    def __init__(self):
        self.db = Connection()
        super().__init__()

    def add_conference(self, arg):
        sql ="""INSERT INTO calendar (title, date, hour, description) VALUES (%s, %s, %s, %s );"""
        arguments = (arg.title, arg.date, arg.hour, arg.description)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

            


    def get_all_conference(self):
        sql = """SELECT * FROM conference AS c 
                INNER JOIN speaker AS s ON s.id = c.speaker_id
                ORDER BY c.date, c.hour"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        conf = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(conf):
            conf [key] = Conference(value)
            return conf

    def get_conf(self, date, hour):
        sql = "SELECT * FROM conference WHERE date = %s and hour=%s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (date, hour))
        conf = self.db.cursor.fetchone()
        self.db.close_connection()
        return conf