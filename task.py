class Task:
    def __init__(self, title, subject, deadline, difficulty, estimated_time):
        self.title = title
        self.subject = subject
        self.deadline = deadline
        self.difficulty = difficulty
        self.estimated_time = estimated_time
        self.completed = False
        self.subtasks = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def complete_task(self):
        self.completed = True

    def display_task(self):
        status = "Completed" if self.completed else "Incomplete"

        print(f"\nGoal: {self.title}")
        print(f"Subject: {self.subject}")
        print(f"Deadline: {self.deadline}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Estimated Time: {self.estimated_time} minutes")
        print(f"Status: {status}")

        if self.subtasks:
            print("Subtasks:")
            for i, subtask in enumerate(self.subtasks, 1):
                status = "✓" if subtask["completed"] else " "
                print(f"  [{status}] {i}. {subtask['title']}")