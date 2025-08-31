import sqlite3
def company_Query():
    try:   
        conn=sqlite3.connect('newDEPI.db')
        cursor=conn.cursor()
        cursor.execute(
            '''SELECT 
	com.c_id,
	com.c_name,
	ct.ct_name,
	(SELECT COUNT(*) 
	FROM company_instructor com_i 
	WHERE com_i.c_id = com.c_id) AS instructors_count,
	(SELECT COUNT(*) 
	FROM company_student com_st  
	WHERE com_st.c_id = com.c_id) AS student_count
FROM Company com
JOIN round_company r_c
	ON r_c.c_id = com.c_id
JOIN round r
	ON r.r_id = r_c.r_id
JOIN round_city r_ct
	ON r.r_id = r_ct.r_id
JOIN City ct
	ON ct.ct_id = r_ct.ct_id
GROUP BY com.c_id, com.c_name;

''')  # Passing parameters as a tuple
        conn.commit()


        all = cursor.fetchall()
        conn.close()
        return all
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")

def instructor_Query():
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''select i.i_id, i.name, i.type, email, t.t_name, g.g_name, c.c_name   from Instructor as i 
                        join track as t on t.t_id = i.t_id 
                        join group_instructor gi on gi.i_id = i.i_id 
                        join "group" as g on g.g_id = gi.g_id 
                        join company_instructor as ci on ci.i_id = i.i_id 
                        join Company as c on c.c_id = ci.c_id 
                        order by i.i_id;''') 
            all=cursor.fetchall()
            return all
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

def city_Query():
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''select ct_id, ct_name,
                        (SELECT COUNT(*) FROM city_instructor WHERE ct_id = ct.ct_id) as instructor_count,
                        (SELECT COUNT(*) FROM student WHERE ct_id = ct.ct_id) as student_count
                        from city as ct ;''')  
            all=cursor.fetchall()
            return all
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
def track_Query():
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''SELECT 
                        t.t_id, 
                        t.t_name,
                        ROUND(JULIANDAY(t.to_date) - JULIANDAY(t.from_date)) as duration_days,
                        (SELECT COUNT(*) FROM Instructor WHERE t_id = t.t_id) as instructor_count,
                        (SELECT COUNT(*) FROM track_student WHERE t_id = t.t_id) as student_count
                    FROM Track as t
                    ORDER BY t.t_id;''')  
            all=cursor.fetchall()
            return all
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

def coordinator_Query():
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''select cor_id, name, email, age, "from" from Coordinator;''')  
            all=cursor.fetchall()
            return all
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

def student_Query():
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''select s.s_id, name, email, phone, gender, university, college, t.t_name from Student as s 
                    join track_student as ts on ts.s_id = s.s_id
                    join Track as t on t.t_id = ts.t_id
					order by s.s_id;''')  
            all=cursor.fetchall()
            return all
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False


def dashboard_Query():
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''SELECT  
                        (SELECT COUNT(*) FROM round_company WHERE r_id = r.r_id) as company_count,
                        (SELECT COUNT(*) FROM round_instructor WHERE r_id = r.r_id) as instructor_count,
                        (SELECT COUNT(*) FROM round_student WHERE r_id = r.r_id) as student_count,
                        (SELECT COUNT(*) FROM round_coordinator WHERE r_id = r.r_id) as coordinator_count,
                        (SELECT COUNT(*) FROM round_track WHERE r_id = r.r_id) as track_count,
                        (SELECT COUNT(*) FROM round_city WHERE r_id = r.r_id) as city_count
                    FROM round as r 
                    WHERE r.r_id = 3;''')  
            all=cursor.fetchall()
            return all[0]
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

def insert_Company(c_id, c_name, c_email, c_phone, c_password):
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''INSERT INTO Company (c_id, c_name, c_email, c_phone, c_password)
                  VALUES (?, ?, ?, ?, ?);''',
                (c_id, c_name, c_email, c_phone, c_password))  
            conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        
def insert_round_company(r_id, c_id):
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''INSERT INTO round_company (r_id, c_id) 
                  VALUES (?, ?);''',
                (r_id, c_id))  
            conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

def insert_track_company(t_id, c_id):
        try:   
            conn=sqlite3.connect('newDEPI.db')
            cursor=conn.cursor()
            cursor.execute(
                '''INSERT INTO track_company (t_id, c_id)
                  VALUES (?, ?);''',
                (t_id, c_id))  
            conn.commit()
            return True
        except sqlite3.Error as e:      
            print(f"Error inserting record: {e}")
            return False
        

def insert_City(ct_id, ct_name):
    try:   
        conn=sqlite3.connect('newDEPI.db')
        cursor=conn.cursor()
        cursor.execute(
            '''INSERT INTO City (ct_id, ct_name)
                VALUES (?, ?);''',
            (ct_id, ct_name))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
        

def insert_round_city(r_id, ct_id):
    try:   
        conn=sqlite3.connect('newDEPI.db')
        cursor=conn.cursor()
        cursor.execute(
            '''INSERT INTO round_city (r_id, ct_id) 
                VALUES (?, ?);''',
            (r_id, ct_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    

def insert_Track(t_id, t_name, from_date, to_date):
    try:  
        conn=sqlite3.connect('newDEPI.db')
        cursor=conn.cursor() 
        cursor.execute(
            '''INSERT INTO Track (t_id, t_name, from_date, to_date)
                VALUES (?, ?, ?, ?);''',
            (t_id, t_name, from_date, to_date))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
        
def insert_round_track(r_id, t_id):
    try:   
        conn=sqlite3.connect('newDEPI.db')
        cursor=conn.cursor()
        cursor.execute(
            '''INSERT INTO round_track (r_id, t_id)
                VALUES (?, ?);''',
            (r_id, t_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
