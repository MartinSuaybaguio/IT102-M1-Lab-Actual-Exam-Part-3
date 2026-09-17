class DailyMission:
    def __init__(self, task):
        self.task = task
        self.completed = False
        self.reward = 100

    def complete_mission(self):
        self.completed = True
        self.task.complete_task()

    def display_mission(self):
        print("\n===== DAILY MISSION =====")
        print(f"Goal: {self.task.title}")
        print(f"Subject: {self.task.subject}")
        print(f"Reward: +{self.reward} XP")

        print("\nTasks:")

        for i, subtask in enumerate(self.task.subtasks, 1):
            status = "✓" if subtask["completed"] else " "
            print(f"[{status}] {i}. {subtask['title']}")