import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("newDEPI.db")
        self.cursor = self.conn.cursor()

    def insert_student_coordinator(self,s_id, cor_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO student_coordinator (s_id, cor_id)
                  VALUES (?, ?);''',
                (s_id, cor_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
    

    def insert_student_instructor(self,s_id, i_id, feedback):
        try:   
            self.cursor.execute(
                '''INSERT INTO student_instructor (s_id, i_id, feedback)
                  VALUES (?, ?, ?);''',
                (s_id, i_id, feedback))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_company_coordinator(self,c_id, cor_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO company_coordinator (c_id, cor_id)
                  VALUES (?, ?);''',
                (c_id, cor_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_company_instructor(self,c_id, i_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO company_instructor (c_id, i_id)
                  VALUES (?, ?);''',
                (c_id, i_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_company_student(self,c_id, s_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO company_student (c_id, s_id)
                  VALUES (?, ?);''',
                (c_id, s_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
    
    def insert_group_coordinator(self,g_id, cor_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO group_coordinator (g_id, cor_id)
                  VALUES (?, ?);''',
                (g_id, cor_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_group_instructor(self,g_id, i_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO group_instructor (g_id, i_id)
                  VALUES (?, ?);''',
                (g_id, i_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_group_student(self,s_id, g_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO group_student (s_id, g_id)
                  VALUES (?, ?);''',
                (s_id, g_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_round_coordinator(self,r_id, cor_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO round_coordinator (r_id, cor_id)
                  VALUES (?, ?);''',
                (r_id, cor_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_round_instructor(self,r_id, i_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO round_instructor (r_id, i_id)
                  VALUES (?, ?);''',
                (r_id, i_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_round_student(self,r_id, s_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO round_student (r_id, s_id)
                  VALUES (?, ?);''',
                (r_id, s_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_round_company(self,r_id, c_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO round_company (r_id, c_id) 
                  VALUES (?, ?);''',
                (r_id, c_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_round_city(self,r_id, ct_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO round_city (r_id, ct_id) 
                  VALUES (?, ?);''',
                (r_id, ct_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_round_track(self,r_id, t_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO round_track (r_id, t_id)
                  VALUES (?, ?);''',
                (r_id, t_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_track_city(self,t_id, ct_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO track_city (t_id, ct_id)
                  VALUES (?, ?);''',
                (t_id, ct_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    def insert_track_company(self,t_id, c_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO track_company (t_id, c_id)
                  VALUES (?, ?);''',
                (t_id, c_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_track_student(self,t_id, s_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO track_student (t_id, s_id)
                  VALUES (?, ?);''',
                (t_id, s_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    
    def insert_Session(self,ses_id, g_id, t_id, r_id, c_id, ct_id, cor_id, i_id, week, date, type, state):
        try:   
            self.cursor.execute(
                '''INSERT INTO Session (ses_id, g_id, t_id, r_id, c_id, ct_id, cor_id, i_id, week, date, type, state)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?);''',
                (ses_id, g_id, t_id, r_id, c_id, ct_id, cor_id, i_id, week, date, type, state))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_Student(self,s_id, ct_id, name, gender, university, college, grade, email, phone, password):
        try:   
            self.cursor.execute(
                '''INSERT INTO Student (s_id, ct_id, name, gender, university, college, grade, email, phone, password)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                (s_id, ct_id, name, gender, university, college, grade, email, phone, password))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    
    def insert_Instructor(self,i_id, t_id, cor_id, name, type, phone, bachelor, birthdate, city, gender, email, password):
        try:   
            self.cursor.execute(
                '''INSERT INTO Instructor (i_id, t_id, cor_id, name, type, phone, bachelor, birthdate, "from", gender, email, password)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                (i_id, t_id, cor_id, name, type, phone, bachelor, birthdate, city, gender, email, password))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
    
    def insert_Coordinator(self,cor_id, c_id, ct_id, t_id, name, city, age, email, password):
        try:   
            self.cursor.execute(
                '''INSERT INTO Coordinator (cor_id, c_id, ct_id, t_id, name, "from", age, email, password)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                (cor_id, c_id, ct_id, t_id, name, city, age, email, password))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_Group(self, t_id, r_id, c_id, ct_id, g_name):
        try:   
            self.cursor.execute(
                '''INSERT INTO "Group" (t_id, r_id, c_id, ct_id, g_name)
                  VALUES ( ?, ?, ?, ?, ?);''',
                (t_id, r_id, c_id, ct_id, g_name))  
            self.conn.commit()
            self.conn.close()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
    

    def insert_Round(self,r_id, round_name, from_date, to_date, ministry_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO Round (r_id, round_name, from_date, to_date, ministry_id)
                  VALUES (?, ?, ?, ?, ?);''',
                (r_id, round_name, from_date, to_date, ministry_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_Company(self,c_id, c_name, c_email, c_phone, c_password):
        try:   
            self.cursor.execute(
                '''INSERT INTO Company (c_id, c_name, c_email, c_phone, c_password)
                  VALUES (?, ?, ?, ?, ?);''',
                (c_id, c_name, c_email, c_phone, c_password))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_Track(self,t_id, t_name, from_date, to_date):
        try:   
            self.cursor.execute(
                '''INSERT INTO Track (t_id, t_name, from_date, to_date)
                  VALUES (?, ?, ?, ?);''',
                (t_id, t_name, from_date, to_date))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    
    def insert_City(self,ct_id, ct_name):
        try:   
            self.cursor.execute(
                '''INSERT INTO City (ct_id, ct_name)
                  VALUES (?, ?);''',
                (ct_id, ct_name))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
    
    def insert_Ministry(self,ministry_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO ministry (ministry_id)
                  VALUES (?);''',
                (ministry_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_city_instructor(self,ct_id, i_id):
        try:   
            self.cursor.execute(
                '''INSERT INTO city_instructor (ct_id, i_id)
                  VALUES (?, ?);''',
                (ct_id, i_id))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

    def insert_student_session(self,s_id, ses_id, attendance):
        try:   
            self.cursor.execute(
                '''INSERT INTO student_session (s_id, ses_id, attendance)
                  VALUES (?, ?, ?);''',
                (s_id, ses_id, attendance))  
            self.conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
    
        
    #Close Function
    def close(self):
        self.cursor.close()
        self.conn.close()


