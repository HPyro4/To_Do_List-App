import os

def display_menu():
    print("")
    print("Todo List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Exit")
    print(".................................")
    print("")


def view_tasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")

def add_task():
    task = input("Enter the task: ")
    with open('tasks.txt', 'a') as file:
        file.write(f"{task}\n")
    print("Task added successfully.")

def mark_completed():
    view_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    if 0 <= task_index < len(tasks):
        tasks[task_index] = f"[Finished] {tasks[task_index]}"

        with open('tasks.txt', 'w') as file:
            file.writelines(tasks)

        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    if not os.path.exists('tasks.txt'):
        open('tasks.txt', 'w').close()

    main()
