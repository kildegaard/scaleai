class StudySession:
    def __init__(self, subject, start_time, end_time):
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.subject}: {self.start_time} - {self.end_time}"


class StudyScheduler:
    def __init__(self):
        self.scheduler = {}

    def add_study_session(self, student_name, subject, start_time, end_time):
        if student_name not in self.scheduler:
            self.scheduler[student_name] = []
        self.scheduler[student_name].append(StudySession(subject, start_time, end_time))

    def view_study_sessions(self, student_name):
        if student_name in self.scheduler:
            for i, session in enumerate(self.scheduler[student_name], 1):
                print(f"{i}. {session}")
        else:
            print("No study sessions found for this student.")

    def delete_study_session(self, student_name, session_number):
        if student_name in self.scheduler:
            try:
                del self.scheduler[student_name][session_number - 1]
            except IndexError:
                print("Invalid session number.")
        else:
            print("No study sessions found for this student.")


def main():
    scheduler = StudyScheduler()
    while True:
        print("\n1. Add study session")
        print("2. View study sessions")
        print("3. Delete study session")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            student_name = input("Enter student name: ")
            subject = input("Enter subject: ")
            start_time = input("Enter start time: ")
            end_time = input("Enter end time: ")
            scheduler.add_study_session(student_name, subject, start_time, end_time)
        elif choice == "2":
            student_name = input("Enter student name: ")
            scheduler.view_study_sessions(student_name)
        elif choice == "3":
            student_name = input("Enter student name: ")
            session_number = int(input("Enter session number to delete: "))
            scheduler.delete_study_session(student_name, session_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()