class AchievementSystem:

    @staticmethod
    def check_achievements(student, task):
        if task.completed:
            student.add_achievement("Project Starter")

        if student.streak >= 5:
            student.add_achievement("Study Streak Master")

        if student.points >= 300:
            student.add_achievement("Task Crusher")