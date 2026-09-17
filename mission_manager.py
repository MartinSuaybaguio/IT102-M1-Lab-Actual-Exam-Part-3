from mission import DailyMission


class MissionManager:
    def __init__(self):
        self.missions = []

    def create_mission(self, task):
        mission = DailyMission(task)
        self.missions.append(mission)
        return mission

    def display_missions(self):
        print("\n===== TODAY'S MISSIONS =====")

        if not self.missions:
            print("No missions available.")
            return

        for mission in self.missions:
            mission.display_mission()

    def prioritize_tasks(self, tasks):

        difficulty_order = {
            "Hard": 1,
            "Medium": 2,
            "Easy": 3
        }

        return sorted(
            tasks,
            key=lambda task: difficulty_order.get(
                task.difficulty, 3
            )
        )