import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        title = input("Task: ")
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        index = int(input("Task number: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)

    elif choice == "4":
        show_tasks(tasks)
        index = int(input("Task number: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
