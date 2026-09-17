class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\n===== ALL TASKS =====")

        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks, 1):
            print(f"\n--- Task {i} ---")
            task.display_task()

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]

        return None