import sqlite3


def Q_comp_ins(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        cursor.execute(f"""
select i.i_id, i.name, i.type, i.phone, i.bachelor, "from", i.gender, i.email, i.password, i.i_id, i.t_id  from Instructor i
join company_instructor ci
on ci.i_id = i.i_id
where c_id={id};
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

def Q_comp_cor(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        cursor.execute(f"""
select coo.cor_id, name, ct.ct_name, "from", age ,email, g.g_name   from Coordinator as coo 
join city as ct on ct.ct_id = coo.ct_id
join group_coordinator as gc on gc.cor_id = coo.cor_id
join "group" as g on g.g_id = gc.g_id
join Company as c on c.c_id = coo.c_id 
where c.c_id={id};
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
        
def Q_comp_std(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        cursor.execute(f"""
SELECT 
    s.s_id, s.name, s.university, s.college, g.g_name
FROM Student AS s 
JOIN group_student AS gs ON s.s_id = gs.s_id
JOIN "Group" AS g ON g.g_id = gs.g_id
join company as com on com.c_id = g.c_id 
WHERE  com.c_id = {id}
GROUP BY s.s_id, s.name, g.g_name;
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")


def Q_comp_grp(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        cursor.execute(f"""
select g_id, g_name, ct.ct_name, r.round_name, c.c_name, t.t_name from "group" as g
join city as ct on g.ct_id = ct.ct_id 
join round as r on r.r_id = g.r_id 
join Company as c on c.c_id = g.c_id 
join Track as t on t.t_id = g.t_id
where c.c_id ={id};
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

def insert_Group( t_id, r_id, c_id, ct_id, g_name):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO "Group" (t_id, r_id, c_id, ct_id, g_name)
                VALUES ( ?, ?, ?, ?, ?);''',
            (t_id, r_id, c_id, ct_id, g_name))  
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False        
    
def insert_Coordinator(cor_id, c_id, ct_id, t_id, name, city, age, email, password):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO Coordinator (cor_id, c_id, ct_id, t_id, name, "from", age, email, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''',
            (cor_id, c_id, ct_id, t_id, name, city, age, email, password))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    

def insert_group_coordinator(g_id, cor_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO group_coordinator (g_id, cor_id)
                VALUES (?, ?);''',
            (g_id, cor_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    



def insert_Instructor(i_id, t_id, cor_id, name, type, phone, bachelor, city, gender, email, password):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO Instructor (i_id, t_id, cor_id, name, type, phone, bachelor, "from", gender, email, password)
                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
            (i_id, t_id, cor_id, name, type, phone, bachelor ,city, gender, email, password))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    
def insert_round_instructor(r_id, i_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO round_instructor (r_id, i_id)
                VALUES (?, ?);''',
            (r_id, i_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    

def insert_city_instructor(ct_id, i_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO city_instructor (ct_id, i_id)
                VALUES (?, ?);''',
            (ct_id, i_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    
def insert_group_instructor(g_id, i_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO group_instructor (g_id, i_id)
                VALUES (?, ?);''',
            (g_id, i_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False

def insert_company_instructor(c_id, i_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO company_instructor (c_id, i_id)
                VALUES (?, ?);''',
            (c_id, i_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    



def insert_Student(s_id, ct_id, name, gender, university, college, grade, email, phone, password):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO Student (s_id, ct_id, name, gender, university, college, grade, email, phone, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
            (s_id, ct_id, name, gender, university, college, grade, email, phone, password))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    
def insert_student_coordinator(s_id, cor_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO student_coordinator (s_id, cor_id)
                VALUES (?, ?);''',
            (s_id, cor_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False

def insert_student_instructor(s_id, i_id, feedback):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO student_instructor (s_id, i_id, feedback)
                VALUES (?, ?, ?);''',
            (s_id, i_id, feedback))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
def insert_group_student(s_id, g_id):
    try:   
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()
        cursor.execute(
            '''INSERT INTO group_student (s_id, g_id)
                VALUES (?, ?);''',
            (s_id, g_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False

def insert_company_student(c_id, s_id):
    try: 
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()  
        cursor.execute(
            '''INSERT INTO company_student (c_id, s_id)
                VALUES (?, ?);''',
            (c_id, s_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False

def insert_track_student(t_id, s_id):
    try:  
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor() 
        cursor.execute(
            '''INSERT INTO track_student (t_id, s_id)
                VALUES (?, ?);''',
            (t_id, s_id))  
        conn.commit()
        return True
    except sqlite3.Error as e:      
        print(f"Error inserting record: {e}")
        return False
    

