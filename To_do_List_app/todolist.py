import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task():
    """Add a new task."""
    task = input("Enter the task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def delete_task():
    """Delete a task by index."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available to delete.")
        return

    print("Current tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("Current tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    """Main function to run the application."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
