students = []

# Create Student Profile
def create_profile():
    print("\n===== Create Student Profile =====")

    name = input("Enter Student Name: ").strip()
    roll_no = input("Enter Roll Number: ").strip()
    branch = input("Enter Branch: ").strip()
    year = input("Enter Year: ").strip()
    career_goal = input("Enter Career Goal: ").strip()

    if name == "" or roll_no == "":
        print("Error: Name and Roll Number cannot be empty.")
        return

    # Check duplicate Roll Number
    for profile in students:
        if profile["roll_no"] == roll_no:
            print("Student with this Roll Number already exists!")
            return

    profile = {
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "year": year,
        "career_goal": career_goal
    }

    students.append(profile)

    print("Student profile created successfully!")


# View Student Profiles
def view_profiles():
    print("\n===== Student Profiles =====")

    if len(students) == 0:
        print("No student profiles found.")
        return

    for index, profile in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name: {profile['name']}")
        print(f"Roll Number: {profile['roll_no']}")
        print(f"Branch: {profile['branch']}")
        print(f"Year: {profile['year']}")
        print(f"Career Goal: {profile['career_goal']}")


# Update Student Profile
def update_profile():
    print("\n===== Update Student Profile =====")

    roll = input("Enter Roll Number to Update: ")

    for profile in students:
        if profile["roll_no"] == roll:

            print("Leave blank if you don't want to change")

            name = input(f"New Name ({profile['name']}): ")
            branch = input(f"New Branch ({profile['branch']}): ")
            year = input(f"New Year ({profile['year']}): ")
            goal = input(f"New Career Goal ({profile['career_goal']}): ")

            if name:
                profile["name"] = name
            if branch:
                profile["branch"] = branch
            if year:
                profile["year"] = year
            if goal:
                profile["career_goal"] = goal

            print("Profile updated successfully!")
            return

    print("Student not found!")


# Delete Student Profile
def delete_profile():
    print("\n===== Delete Student Profile ====")

    roll = input("Enter Roll Number to Delete: ")

    for profile in students:
        if profile["roll_no"] == roll:
            students.remove(profile)
            print("Student profile deleted successfully!")
            return

    print("Student not found!")


# Main Menu
while True:

    print("\n========== CareerPilot ==========")
    print("1. Create Student Profile")
    print("2. View Student Profiles")
    print("3. Update Student Profile")
    print("4. Delete Student Profile")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_profile()

    elif choice == "2":
        view_profiles()

    elif choice == "3":
        update_profile()

    elif choice == "4":
        delete_profile()

    elif choice == "5":
        print("Thank you for using CareerPilot!")
        break

    else:
        print("Invalid Choice")