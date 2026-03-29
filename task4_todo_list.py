# task4_todo_list.py

# 1. Create an empty list to store tasks
tasks = []

# 2. Function to add a task
def add_task(task_name):
    tasks.append(task_name)
    print("Task added: " + task_name)

# 3. Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("Your To-Do list is empty!")
    else:
        print("\n--- Your Tasks ---")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])  # Shows task number!
        print("------------------\n")

# 4. The Main Menu Loop
while True:
    print("\nMenu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        new_task = input("Enter the task: ")
        add_task(new_task)

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")