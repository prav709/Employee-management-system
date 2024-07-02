import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to MySQL database
def database():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="9721",
        database="database"
    )
    

     

# Add Employee
def add_employee():
    conn = database()
    cursor = conn.cursor()
    sql = "INSERT INTO employees (name, age, job profile , salary) VALUES (%s, %s, %s, %s)"
    val = ("name_var.get(), age_var.get(), job profile.get(), salary_var.get()")
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Employee added successfully")
    conn.close()

# View Employees
def view_employees():
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        employee_list.insert(END, row)
    conn.close()

# Delete Employee
def delete_employee():
    conn = database()
    cursor = conn.cursor()
    sql = "DELETE FROM employees WHERE id = %s"
    val = (id_var.get(), )
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Employee deleted successfully")
    conn.close()

# Update Employee
def update_employee():
    conn = database()
    cursor = conn.cursor()
    sql = "UPDATE employees SET name = %s, age = %s, jpb profil = %s, salary = %s WHERE id = %s"
    val = (name_var.get(), age_var.get(), jobprofile_var.get(), salary_var.get(), id_var.get())
    cursor.execute(sql, val)
    conn.commit()
    messagebox.showinfo("Success", "Employee updated successfully")
    conn.close()

# GUI
root = Tk()
root.title("Employee Management System")

# Labels and Entry widgets
Label(root, text="Employee ID").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
Label(root, text="Age").grid(row=2, column=0, padx=10, pady=10)
Label(root, text="job profile").grid(row=3, column=0, padx=10, pady=10)
Label(root, text="Salary").grid(row=4, column=0, padx=10, pady=10)

id_var = StringVar()
name_var = StringVar()
age_var = StringVar()
jobprofile_var = StringVar()
salary_var = StringVar()

Entry(root, textvariable=id_var).grid(row=0, column=1, padx=10, pady=10)
Entry(root, textvariable=name_var).grid(row=1, column=1, padx=10, pady=10)
Entry(root, textvariable=age_var).grid(row=2, column=1, padx=10, pady=10)
Entry(root, textvariable=jobprofile_var).grid(row=3, column=1, padx=10, pady=10)
Entry(root, textvariable=salary_var).grid(row=4, column=1, padx=10, pady=10)

# Buttons
Button(root, text="Add Employee", command=add_employee).grid(row=5, column=0, padx=10, pady=10)
Button(root, text="View Employees", command=view_employees).grid(row=5, column=1, padx=10, pady=10)
Button(root, text="Delete Employee", command=delete_employee).grid(row=6, column=0, padx=10, pady=10)
Button(root, text="Update Employee", command=update_employee).grid(row=6, column=1, padx=10, pady=10)

# Listbox to display employees
employee_list = Listbox(root, width=50, height=10)
employee_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
