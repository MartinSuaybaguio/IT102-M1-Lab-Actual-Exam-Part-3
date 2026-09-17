from student import Student
from task import Task
from task_manager import TaskManager
from mission_manager import MissionManager
from achievement import AchievementSystem


def main():

    student = Student("Jessie")

    task_manager = TaskManager()
    mission_manager = MissionManager()

    science_project = Task(
        "Finish Science Project",
        "Science",
        "September 18",
        "Hard",
        240
    )

    science_project.add_subtask({
        "title": "Complete Research",
        "completed": False
    })

    science_project.add_subtask({
        "title": "Write Introduction",
        "completed": False
    })

    science_project.add_subtask({
        "title": "Add References",
        "completed": False
    })

    science_project.add_subtask({
        "title": "Review Final Draft",
        "completed": False
    })

    task_manager.add_task(science_project)

    mission = mission_manager.create_mission(science_project)

    while True:

        print("\n==============================")
        print("       STUDY LOOP")
        print("==============================")
        print("1. View Profile")
        print("2. View Tasks")
        print("3. View Daily Mission")
        print("4. Complete Mission")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            student.display_profile()

        elif choice == "2":
            task_manager.display_tasks()

        elif choice == "3":
            mission_manager.display_missions()

        elif choice == "4":

            if not mission.completed:

                mission.complete_mission()

                student.add_points(mission.reward)
                student.update_streak()

                AchievementSystem.check_achievements(
                    student,
                    science_project
                )

                print("\nMission completed!")
                print(f"+{mission.reward} XP earned!")

            else:
                print("\nMission already completed.")

        elif choice == "5":
            print("\nThank you for using Study Loop!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()