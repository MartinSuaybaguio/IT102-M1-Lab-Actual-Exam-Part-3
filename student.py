class Student:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.streak = 0
        self.achievements = []

    def add_points(self, points):
        self.points += points

    def update_streak(self):
        self.streak += 1

    def add_achievement(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)

    def display_profile(self):
        print("\n===== STUDENT PROFILE =====")
        print(f"Name: {self.name}")
        print(f"Points: {self.points}")
        print(f"Study Streak: {self.streak} days")

        print("\nAchievements:")
        if self.achievements:
            for achievement in self.achievements:
                print(f"- {achievement}")
        else:
            print("No achievements yet.")