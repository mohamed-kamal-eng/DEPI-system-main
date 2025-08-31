from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import *
from ministry_database import *
import json


app = Flask(__name__)

def q_student_table(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
                select st.name , st.s_id, t.t_name, c.ct_name, i.name from Student st
join track_student ts 
on ts.s_id = st.s_id
join Track t 
on ts.t_id = t.t_id
join City c
on c.ct_id = st.ct_id
join student_instructor si
on si.s_id = st.s_id
join Instructor i
on i.i_id = si.i_id
where st.s_id = {id} and i.type = 'tech';

                """)
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
def q_student_sess(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
                select s.ses_id , s.type, s.date ,i.name, s.state from student_session ss
join student st 
on st.s_id = ss.s_id
join Session s
on ss.ses_id = s.ses_id 
join Instructor i
on s.i_id = i.i_id
where st.s_id = {id} and ss.attendance = 'not taken';

                """)
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

def Q_student_attend(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
               select count(ss.attendance) from student_session ss
join student st 
on st.s_id = ss.s_id
join Session s
on ss.ses_id = s.ses_id 
where st.s_id = {id} and ss.attendance = 'true';


                """)

        true = cursor.fetchall()[0][0]

        cursor.execute(f"""select count(ss.attendance) from student_session ss
join student st 
on st.s_id = ss.s_id
join Session s
on ss.ses_id = s.ses_id 
where st.s_id = {id} and ss.attendance <> 'not taken';""")
        all = cursor.fetchall()[0][0]

        per =( true / all) * 100
        conn.close()
        return per
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
def Q_coor(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
              select co.cor_id , co.name, t.t_name , c.c_name, g.g_name from Coordinator co
join Track t
on co.t_id = t.t_id 
join Company c
on c.c_id = co.c_id
join group_coordinator gc
on gc.cor_id = co.cor_id
join "Group" g
on gc.g_id = g.g_id
where co.cor_id = {id};

                """)

        true = cursor.fetchall()
        conn.close()
       
        return true
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
def Q_coor_feed(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
              select st.name , feedback, i.name from Student st
join student_instructor si 
on si.s_id = st.s_id
join Instructor i 
on i.i_id = si.i_id
join student_coordinator sc 
on st.s_id = sc.s_id 
join Coordinator co
on co.cor_id = sc.cor_id
where co.cor_id = {id};

                """)

        true = cursor.fetchall()
        conn.close()
       
        return true
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")




def Q_coor_attend(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
SELECT 
    s.s_id, 
    s.name, 
    g.g_name, 
    CAST(
        (CAST(COUNT(ss.attendance) AS FLOAT) / 
        (SELECT COUNT(attendance) 
         FROM student_session AS ss2 
         WHERE ss2.s_id = s.s_id 
           AND ss2.attendance != 'not taken')
        ) * 100 AS INTEGER
    ) AS attendance_percentage
FROM Student AS s 
JOIN student_session AS ss ON s.s_id = ss.s_id
JOIN group_student AS gs ON s.s_id = gs.s_id
JOIN "Group" AS g ON g.g_id = gs.g_id
JOIN student_coordinator AS sc ON sc.s_id = s.s_id
WHERE ss.attendance = 'true' 
  AND sc.cor_id = {id}
GROUP BY s.s_id, s.name, g.g_name;
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")
def Q_ins_name(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
              
select i.name , i.i_id, r.round_name, t.t_name, c.c_name, i.type from Instructor as i 
join round_instructor as ri on ri.i_id = i.i_id 
join round as r on r.r_id = ri.r_id 
join Track as t on t.t_id = i.t_id 
join company_instructor as ci on ci.i_id = i.i_id
join Company as c on c.c_id = ci.c_id
where i.i_id={id};
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

def Q_inst_feed(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        cursor.execute(f"""
select st.name, si.feedback
from  student st
join student_instructor si 
on st.s_id = si.s_id 
join Instructor i 
on si.i_id = i.i_id 
where i.i_id = {id} ;
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")

        
def Q_inst_att(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
              
SELECT 
    s.s_id, 
    s.name, 
    g.g_name, 
    CAST(
        (CAST(COUNT(ss.attendance) AS FLOAT) / 
        (SELECT COUNT(attendance) 
         FROM student_session AS ss2 
         WHERE ss2.s_id = s.s_id 
           AND ss2.attendance != 'not taken')
        ) * 100 AS INTEGER
    ) AS attendance_percentage
FROM Student AS s 
JOIN student_session AS ss ON s.s_id = ss.s_id
JOIN group_student AS gs ON s.s_id = gs.s_id
JOIN "Group" AS g ON g.g_id = gs.g_id
JOIN student_instructor AS si ON si.s_id = s.s_id
WHERE ss.attendance = 'true' 
  AND si.i_id = {id}
GROUP BY s.s_id, s.name, g.g_name;
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")


def Q_comp_data(id):
    try:
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        

        cursor.execute(f"""
              
select 
	c.c_id,c.c_name, 
	(select count(*) from coordinator where c.c_id = c_id) as "Count Coordinator",
	(select count(*) from company_instructor where c.c_id = c_id) as "Count Instructor",
	(select count(*) from company_student where c.c_id = c_id) as "Count Student",
	(select count(distinct gi.g_id) from company_instructor as ci 
	 join group_instructor as gi on ci.i_id =  gi.i_id 
	 where c.c_id = ci.c_id) as "Count Group",
	(select count(*) from track_company where c.c_id = c_id) as "Count Tracks"
	from company as c 
	where c.c_id={id};
                """)

        all = cursor.fetchall()
        conn.close()

        return all
    except sqlite3.Error as e:
        print(f"Error fetching records: {e}")




@app.route("/")
def home():
    return render_template("home.html")


@app.route("/ins-log", methods=["GET", "POST"])
def log_inst():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()

            email = request.form["email"]
            passw = request.form["pass"]


            cursor.execute("SELECT i_id FROM instructor WHERE email = ? AND password = ?", (email, passw))
            result = cursor.fetchall()
            conn.close()

            if result:   # لو فيه طالب
                ins_id = result[0][0]
                return redirect(url_for("instruc", id=ins_id))
            else:
                return render_template("log-ins.html", error="Invalid email or password")
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("log-ins.html", error="Database error, try again later")

    # لو GET → رجع صفحة تسجيل الدخول
    return render_template("log-ins.html")


@app.route("/min-log", methods=["GET", "POST"])
def log_min():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()

            email = request.form["email"]
            passw = request.form["pass"]


            cursor.execute("SELECT ministry_id FROM ministry WHERE email = ? AND password = ?", (email, passw))
            result = cursor.fetchall()
            conn.close()

            if result:   # لو فيه طالب
                min_id = result[0][0]
                return redirect(url_for("ministry", id=min_id))
            else:
                return render_template("min_log.html", error="Invalid email or password")
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("min_log.html", error="Database error, try again later")

    # لو GET → رجع صفحة تسجيل الدخول
    return render_template("min_log.html")







@app.route("/cor-log", methods=["GET", "POST"])
def log_coor():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()

            email = request.form["email"]
            passw = request.form["pass"]


            cursor.execute("SELECT cor_id FROM coordinator WHERE email = ? AND password = ?", (email, passw))
            result = cursor.fetchall()
            conn.close()

            if result:   # لو فيه طالب
                cor_id = result[0][0]
                return redirect(url_for("coord", id=cor_id))
            else:
                return render_template("log-cor.html", error="Invalid email or password")
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("log-cor.html", error="Database error, try again later")

    # لو GET → رجع صفحة تسجيل الدخول
    return render_template("log-cor.html")



@app.route("/min-log/ministry/<int:id>", methods=["GET", "POST"])
def ministry(id):
        print("Route accessed with method:", request.method)
        if request.method == "POST":
            if request.form.get("form") == "company_form":
                id = request.form.get("cid")
                name = request.form.get("cname")
                email = request.form.get("cemail")
                passw = request.form.get("cpassword")
                phone = request.form.get("cphone")
                r_id = request.form.get("cround")

                insert_Company(id, name, email, phone, passw)
                insert_round_company(r_id, id)
                return redirect(url_for("ministry", id=id))
            elif request.form.get("form") == "city_form":
                id = request.form.get("ctid")
                name = request.form.get("ctname")
                r_id = request.form.get("ctround")
                
                insert_City(id, name)
                insert_round_city(r_id, id)
                return redirect(url_for("ministry", id=id))
            elif request.form.get("form") == "track_form":
                id = request.form.get("tid")
                name = request.form.get("tname")
                from_date = request.form.get("tfrom")
                to_date = request.form.get("tto")
                r_id = request.form.get("tround")
                
                insert_Track(id, name, from_date, to_date)
                insert_round_track(r_id, id)
                return redirect(url_for("ministry", id=1))
            

        company = company_Query()
        instructor = instructor_Query()
        city = city_Query()
        track = track_Query()
        coordinator = coordinator_Query()
        student = student_Query()
        dash = dashboard_Query()
        return render_template("ministry.html",dash = dash , student = student , instructor = instructor ,company = company, city = city, track = track, coordinator = coordinator)




@app.route("/cor-log/coordinator/<int:id>", methods=["GET", "POST"])
def coord(id):
    print("Route accessed with method:", request.method)
    if request.method == "POST":
       
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        stid = request.form["stid"]
        sesid = request.form["sesid"]
        tr = request.form["attendance"]
        print(stid, sesid, tr)
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()


            cursor.execute("update student_session set attendance = ? where s_id = ? and ses_id = ?;", (tr, stid, sesid))
            conn.commit()
            conn.close()

            return redirect(url_for("coord", id=id))
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("coord.html", error="Database error, try again later")

            
    data = Q_coor(id)[0]
    feed = Q_coor_feed(id)  # [(studentName, feedback, instructor), ...]
    # تحويل tuple list لـ list of dicts
    feed_dict = [{"studentName": s, "feedback": f, "instructor": i} for s, f, i in feed]
    att = Q_coor_attend(id)  # [(id, studentName, group, attendanceRate), ...]

    att_list = [
        {"id": student_id, "name": s, "group": g, "attendanceRate": i}
        for student_id, s, g, i in att
    ]

    
           

    # لو GET → رجع صفحة تسجيل الدخول

    return render_template(
        "coor.html",
        data=data,
        feed_json = json.dumps(feed_dict),
        att_json = json.dumps(att_list)
    )
        
    
  
@app.route("/ins-log/instructor/<int:id>", methods=["GET", "POST"])
def instruc(id):
    print("Route accessed with method:", request.method)
    if request.method == "POST":
       
        conn = sqlite3.connect("newDEPI.db")
        cursor = conn.cursor()

        stid = request.form["stid"]
        feedback = request.form["feedback"]
        
       
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()


            cursor.execute("update student_instructor set feedback = ? where s_id = ? and i_id = ?; ", (feedback, stid, id))
            conn.commit()
            conn.close()

            return redirect(url_for("instruc", id=id))
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("Instructor.html", error="Database error, try again later")


    data = Q_ins_name(id)[0]
    feed = Q_inst_feed(id)
    att = Q_inst_att(id) 
    
    return render_template("instructor.html", data = data, feed = feed, att = att)





  
@app.route("/com-log/company/<int:id>", methods=["GET", "POST"])
def company(id):
    print("Route accessed with method:", request.method)
    if request.method == "POST":
        if request.form.get("form") == "g_form":
            # id = request.form.get("gid")
            name = request.form.get("gname")
            city = request.form.get("gcity")
            r_id = request.form.get("ground")
            t_id = request.form.get("gtid")
            print("", name, city)
            insert_Group(t_id, r_id, id, city, name)
            return redirect(url_for("company", id=id))

        elif request.form.get("form") == "cor_form":
             cid = request.form.get("cid")
             name = request.form.get("cname")
             city = request.form.get("ccity")
             frm = request.form.get("cfrom")
             age = request.form.get("cage")
             email = request.form.get("cemail")
             passw = request.form.get("cpassword")
             gid = request.form.get("cgroupId")
             t_id = request.form.get("ct_id")

             print ("", name, city, frm)
             insert_Coordinator(cid, id, city, t_id, name, frm, age, email, passw)
             insert_group_coordinator(gid, cid)
             return redirect(url_for("company", id=id))
        
        elif request.form.get("form") == "ins_form":
             iid = request.form.get("iid")
             name = request.form.get("iname")
             type = request.form.get("itype")
             ph = request.form.get("iphone")
             bach = request.form.get("ibachelors")
             frm = request.form.get("ifrom")
             gen = request.form.get("igender")
             email = request.form.get("iemail")
             passw = request.form.get("ipassword")
             r_id = request.form.get("iroundId")
             t_id = request.form.get("itrackId")
             cor_id = request.form.get("icorId")
             ct_id = request.form.get("ict_id")
             g_id = request.form.get("igroupId")
           
             insert_Instructor(iid, t_id, cor_id, name, type, ph, bach, frm, gen, email, passw)
             insert_city_instructor(ct_id, iid)
             insert_group_instructor(g_id, iid)
             insert_company_instructor(id, iid)
             insert_round_instructor(r_id, iid)
             return redirect(url_for("company", id=id))
        elif request.form.get("form") == "std_form":
             s_id = request.form.get("sid")
             name = request.form.get("sname")
             gender = request.form.get("sgender")
             university = request.form.get("suniversity")
             college = request.form.get("scollege")
             grade = request.form.get("sgrade")
             email = request.form.get("semail")
             phone = request.form.get("sph")
             password = request.form.get("spassword")
             cor_id = request.form.get("scor")
             g_id = request.form.get("sg")
             t_id = request.form.get("st")
             ct_id = request.form.get("scity")
             
             
             insert_Student(s_id, ct_id, name, gender, university, college, grade, email, phone, password)
             insert_student_coordinator(s_id, cor_id)
             insert_group_student(s_id, g_id)
             insert_company_student(id, s_id)
             insert_track_student(t_id, s_id)
             return redirect(url_for("company", id=id))

            
            
            
    data = Q_comp_data(id)[0]
    ins = Q_comp_ins(id)
    cor = Q_comp_cor(id)
    std = Q_comp_std(id)
    gr = Q_comp_grp(id)
    return render_template("company.html", data = data, ins = ins, cor = cor , std = std, gr = gr)







@app.route("/std-log/student/<int:id>")
def student(id):
    data = q_student_table(id)[0]
    id = data[1]
    name = data[0]
    track = data[2]
    city = data[3]
    inst = data[4]
    ses = q_student_sess(id)[0]
    per = int(Q_student_attend(id))

    return render_template("student.html", id = id, name = name,track = track,city = city, inst = inst, per = per, ses = ses)


@app.route("/std-log", methods=["GET", "POST"])
def std_log():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()

            email = request.form["email"]
            passw = request.form["pass"]


            cursor.execute("SELECT s_id FROM student WHERE email = ? AND password = ?", (email, passw))
            result = cursor.fetchall()
            conn.close()

            if result:   # لو فيه طالب
                student_id = result[0][0]
                return redirect(url_for("student", id=student_id))
            else:
                return render_template("log-in.html", error="Invalid email or password")
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("log-in.html", error="Database error, try again later")

    # لو GET → رجع صفحة تسجيل الدخول
    return render_template("log-in.html")


@app.route("/com-log", methods=["GET", "POST"])
def log_comp():
    if request.method == "POST":
        try:
            conn = sqlite3.connect("newDEPI.db")
            cursor = conn.cursor()

            email = request.form["email"]
            passw = request.form["pass"]


            cursor.execute("SELECT c_id FROM company WHERE c_email = ? AND c_password = ?", (email, passw))
            result = cursor.fetchall()
            conn.close()

            if result:   # لو فيه طالب
                comp_id = result[0][0]
                return redirect(url_for("company", id=comp_id))
            else:
                return render_template("log-com.html", error="Invalid email or password")
        
        except sqlite3.Error as e:
            print(f"Error fetching records: {e}")
            return render_template("log-com.html", error="Database error, try again later")
    return render_template("log-com.html")



if __name__ == "__main__":
    app.run(debug=True)
