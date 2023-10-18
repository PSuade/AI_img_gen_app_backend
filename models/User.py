import get_db_info
import psycopg2

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save(self):
        db_params = get_db_info.get_db_params()        
        conn = psycopg2.connect(**db_params);
        cur = conn.cursor()
        cur.execute("""
                INSERT INTO users (first_name, last_name, email, password) 
                VALUES 
                (%s, %s, %s, %s)
            """, (self.first_name, self.last_name, self.email, self.password)) 
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_user_by_email(email):
        db_params = get_db_info.get_db_params()        
        conn = psycopg2.connect(**db_params);
        cur = conn.cursor()
        cur.execute("""
                SELECT * FROM users WHERE email = %s; 
                
            """, (email,)) 
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user
