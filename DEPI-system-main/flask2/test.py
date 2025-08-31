import sqlite3

def Q_coor_attend(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
              
select  count(attendance)  from Student as s 
join student_session as ss on s.s_id= ss.s_id
join group_student as gs on s.s_id= gs.s_id
join student_coordinator as sc on sc.s_id = s.s_id
where attendance != 'not taken' and sc.cor_id={id}
group by s.s_id
limit 1;

                """)

        all = cursor.fetchall()[0][0]
        
        
        cursor.execute(f"""
              
select s.s_id, s.name , gs.g_id, count(attendance)  from Student as s 
join student_session as ss on s.s_id= ss.s_id
join group_student as gs on s.s_id= gs.s_id
join student_coordinator as sc on sc.s_id = s.s_id
where attendance='true' and sc.cor_id= {id}
group by s.s_id;


                """)
        data = cursor.fetchall()

        
        conn.close()
       

       
        return data
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")


d = Q_coor_attend(1)
print(d)

