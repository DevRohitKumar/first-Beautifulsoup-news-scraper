import mysql.connector as myconnector
from mysql.connector import errorcode

class my_database:
    def __init__(self, db_config):
        try:
            self.db_conn = myconnector.connect(
                host= db_config['HOST'] ,
                user= db_config['USERNAME'] ,
                password= db_config['PASSWORD'] ,
                database= db_config['DATABASE'] ,
            )
        except myconnector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                
    def save_to_india_db(self, collected_news):
        cursor = self.db_conn.cursor()
        db_command = """INSERT INTO news_india (news_title, news_date, news_time, news_link )
        VALUES (%s,%s, %s, %s)"""
        cursor.executemany(db_command, collected_news)
        self.db_conn.commit()
        
    def save_headline_to_db(self, headline_data):
        cursor = self.db_conn.cursor()
        db_command = """INSERT INTO news_india_headline 
        (headline_title, headline_date, headline_time, headline_link) 
        VALUES (%s,%s,%s,%s)"""
        cursor.execute(db_command, headline_data)
    
    def get_db_headline(self, ):
        cursor = self.db_conn.cursor()
        db_command = "SELECT headline_title FROM news_india_headline"        
        cursor.execute(db_command)
        result = cursor.fetchone()    
   
    def clean_headline_db(self, ):
        cursor = self.db_conn.cursor()
        db_command = "DELETE FROM news_india_headline"     
        cursor.execute(db_command, collected_news)
        self.db_conn.commit()
        
    def close_db_conn(self):
        self.db_conn.close()