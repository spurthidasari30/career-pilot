class Student:
    def __init__(self, name, roll_no, branch, year, career_goal):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.year = year
        self.career_goal = career_goal

    def display_profile(self):
        print("===== Student Profile =====")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Branch: {self.branch}")
        print(f"Year: {self.year}")
        print(f"Career Goal: {self.career_goal}")


class StudentProfileManager:
    def __init__(self):
        self.students = []

    def create_profile(self):
        print("\n===== Create Student Profile =====")
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        career_goal = input("Enter Career Goal: ")

        if name == "" or roll_no == "":
            print("Error: Name and Roll Number cannot be empty.")
            return

        student = Student(name, roll_no, branch, year, career_goal)
        self.students.append(student)
        print("Student profile created successfully!")

    def view_profiles(self):
        print("\n===== Student Profiles =====")

        if len(self.students) == 0:
            print("No student profiles found.")
            return

        for index, student in enumerate(self.students, start=1):
            print(f"\nStudent {index}")
            student.display_profile()

    def update_profile(self):
        print("Update Profile feature not implemented yet.")


class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

    def display_task(self):
        print("===== Task Details =====")
        print(f"Title: {self.title}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        print("\n===== Add Task =====")

        title = input("Enter Task Title: ")
        due_date = input("Enter Due Date: ")

        if title == "" or due_date == "":
            print("Error: Title and Due Date cannot be empty.")
            return

        task = Task(title, due_date)
        self.tasks.append(task)

        print("Task added successfully!")

    def view_tasks(self):
        print("\n===== Task List =====")

        if len(self.tasks) == 0:
            print("No tasks found.")
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"\nTask {index}")
            task.display_task()

    def complete_task(self):
        self.view_tasks()

        if len(self.tasks) == 0:
            return

        task_no = int(input("Enter Task Number to Complete: "))

        if 1 <= task_no <= len(self.tasks):
            task = self.tasks[task_no - 1]
            task.mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")


def student_menu(profile_manager):
    while True:
        print("\n===== Student Menu =====")
        print("1. Create Student Profile")
        print("2. View Student Profiles")
        print("3. Update Student Profile")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            profile_manager.create_profile()
        elif choice == "2":
            profile_manager.view_profiles()
        elif choice == "3":
            profile_manager.update_profile()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def task_menu(task_manager):
    while True:
        print("\n===== Task Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_manager.complete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


profile_manager = StudentProfileManager()
task_manager = TaskManager()

while True:
    print("\n===== Career Planner =====")
    print("1. Student Profile")
    print("2. Task Manager")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_menu(profile_manager)
    elif choice == "2":
        task_menu(task_manager)
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")