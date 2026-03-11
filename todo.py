tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        show_tasks()
        task_num = int(input("Enter task number to remove: "))
        tasks.pop(task_num - 1)
        print("Task removed!")

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")