import datetime
import time
import threading

class StudyScheduler:
    def __init__(self):
        self.study_plans = {}

    def create_study_plan(self, student_name):
        if student_name not in self.study_plans:
            self.study_plans[student_name] = []
            print(f"Study plan created for {student_name}.")
        else:
            print(f"A study plan for {student_name} already exists.")

    def add_study_session(self, student_name, subject, start_time, end_time):
        if student_name in self.study_plans:
            self.study_plans[student_name].append({
                "subject": subject,
                "start_time": start_time,
                "end_time": end_time
            })
            print(f"Study session added for {student_name}.")
        else:
            print(f"No study plan found for {student_name}. Please create a study plan first.")

    def view_study_plan(self, student_name):
        if student_name in self.study_plans:
            print(f"Study plan for {student_name}:")
            for i, session in enumerate(self.study_plans[student_name], start=1):
                print(f"{i}. {session['subject']} - {session['start_time']} to {session['end_time']}")
        else:
            print(f"No study plan found for {student_name}.")

    def delete_study_session(self, student_name, session_number):
        if student_name in self.study_plans:
            try:
                del self.study_plans[student_name][session_number - 1]
                print(f"Study session {session_number} deleted for {student_name}.")
            except IndexError:
                print(f"Invalid session number for {student_name}.")
        else:
            print(f"No study plan found for {student_name}.")

class Student:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")

class Reminder:
    def __init__(self, study_scheduler):
        self.study_scheduler = study_scheduler

    def remind_study_session(self, student_name, session_number):
        if student_name in self.study_scheduler.study_plans:
            try:
                session = self.study_scheduler.study_plans[student_name][session_number - 1]
                print(f"Reminder: You have a study session for {session['subject']} from {session['start_time']} to {session['end_time']}.")
            except IndexError:
                print(f"Invalid session number for {student_name}.")
        else:
            print(f"No study plan found for {student_name}.")

    def schedule_reminder(self, student_name, session_number, reminder_time):
        if student_name in self.study_scheduler.study_plans:
            try:
                session = self.study_scheduler.study_plans[student_name][session_number - 1]
                reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M")
                session_start_time = datetime.datetime.strptime(session['start_time'], "%H:%M")
                time_diff = (session_start_time - reminder_time).total_seconds() / 60
                if time_diff > 0:
                    print(f"Reminder scheduled for {student_name} at {reminder_time.strftime('%H:%M')}.")
                    threading.Timer(time_diff * 60, self.remind_study_session, args=(student_name, session_number)).start()
                else:
                    print(f"Reminder time is after the session start time.")
            except IndexError:
                print(f"Invalid session number for {student_name}.")
        else:
            print(f"No study plan found for {student_name}.")

def main():
    scheduler = StudyScheduler()
    reminder = Reminder(scheduler)
    students = {}
    while True:
        print("\n1. Create Study Plan")
        print("2. Add Study Session")
        print("3. View Study Plan")
        print("4. Delete Study Session")
        print("5. Create Student Profile")
        print("6. View Student Profile")
        print("7. Schedule Reminder")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_name = input("Enter student name: ")
            scheduler.create_study_plan(student_name)
        elif choice == "2":
            student_name = input("Enter student name: ")
            subject = input("Enter subject: ")
            start_time = input("Enter start time (HH:MM): ")
            end_time = input("Enter end time (HH:MM): ")
            scheduler.add_study_session(student_name, subject, start_time, end_time)
        elif choice == "3":
            student_name = input("Enter student name: ")
            scheduler.view_study_plan(student_name)
        elif choice == "4":
            student_name = input("Enter student name: ")
            session_number = int(input("Enter session number to delete: "))
            scheduler.delete_study_session(student_name, session_number)
        elif choice == "5":
            student_name = input("Enter student name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            students[student_name] = Student(student_name, email, phone_number)
            print(f"Student profile created for {student_name}.")
        elif choice == "6":
            student_name = input("Enter student name: ")
            if student_name in students:
                students[student_name].display_details()
            else:
                print(f"No student profile found for {student_name}.")
        elif choice == "7":
            student_name = input("Enter student name: ")
            session_number = int(input("Enter session number: "))
            reminder_time = input("Enter reminder time (HH:MM): ")
            reminder.schedule_reminder(student_name, session_number, reminder_time)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()