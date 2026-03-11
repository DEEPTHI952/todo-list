import json
import os

FILE_NAME = "tasks.json"

class TodoList:

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
            return

        print("\nYour Tasks:\n")
        for i, task in enumerate(self.tasks, start=1):
            status = "✔ Completed" if task["done"] else "❌ Pending"
            print(f"{i}. {task['task']} [{status}]")
        print()

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print("Task added successfully!")

    def delete_task(self):
        self.show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            removed = self.tasks.pop(num - 1)
            self.save_tasks()
            print(f"Deleted task: {removed['task']}")
        except:
            print("Invalid task number")

    def mark_complete(self):
        self.show_tasks()
        try:
            num = int(input("Enter task number to mark complete: "))
            self.tasks[num - 1]["done"] = True
            self.save_tasks()
            print("Task marked as completed!")
        except:
            print("Invalid task number")


def menu():
    todo = TodoList()

    while True:
        print("\n====== TO-DO LIST ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            todo.show_tasks()

        elif choice == "2":
            todo.add_task()

        elif choice == "3":
            todo.delete_task()

        elif choice == "4":
            todo.mark_complete()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


menu()