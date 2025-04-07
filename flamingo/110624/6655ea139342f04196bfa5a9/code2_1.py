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

def main():
    scheduler = StudyScheduler()
    while True:
        print("\n1. Create Study Plan")
        print("2. Add Study Session")
        print("3. View Study Plan")
        print("4. Delete Study Session")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_name = input("Enter student name: ")
            scheduler.create_study_plan(student_name)
        elif choice == "2":
            student_name = input("Enter student name: ")
            subject = input("Enter subject: ")
            start_time = input("Enter start time: ")
            end_time = input("Enter end time: ")
            scheduler.add_study_session(student_name, subject, start_time, end_time)
        elif choice == "3":
            student_name = input("Enter student name: ")
            scheduler.view_study_plan(student_name)
        elif choice == "4":
            student_name = input("Enter student name: ")
            session_number = int(input("Enter session number to delete: "))
            scheduler.delete_study_session(student_name, session_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()