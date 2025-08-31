# 🎓 Simulation of the DEPI System

This project is a *web application* that simulates the *post-acceptance phase* of the *Digital Egypt Pioneers Initiative (DEPI)*.  
It was developed as part of the *Data Science track* with *EYouth* in the topic *Database with Python*.

---

## 🚀 Project Overview
The system is designed to manage different roles within DEPI, each with its own access level and control:

- *Student* 👨‍🎓  
- *Instructor* 👨‍🏫  
- *Coordinator* 👩‍💼  
- *Company* 🏢  
- *Ministry* 🏛  

This simulation helps visualize how the workflow and permissions are managed in real scenarios.

---

## 🔄 Workflow

Each user has their own *email and password* to log in to the system. Based on the role, different permissions are granted:

### 🏛 Ministry
- Can view *all system data* (global access).

### 🏢 Company
- Can view and manage *only its own data*.  
- Can interact with its assigned:
  - *Students* 👨‍🎓  
  - *Instructors* 👨‍🏫  
  - *Coordinators* 👩‍💼  
  - *Groups* 👥  

### 👨‍🏫 Instructor
- Can view *only their students*.  
- Can *add feedback* for students.  
- Can *edit feedback*.  
- Can view and manage *student attendance*.

### 👩‍💼 Coordinator
- Can *mark attendance* for their students.  
- Can *view feedback* given by instructors for their students.

### 👨‍🎓 Student
- Can view their *personal data only*:
  - Overall *attendance percentage*.  
  - Details of their *upcoming sessions*.  

---

## 🛠 Tech Stack
- *Backend:* Python, Flask  
- *Database:* SQLite  
- *Frontend:* HTML, CSS, JavaScript  

---

## 📂 Project Structure