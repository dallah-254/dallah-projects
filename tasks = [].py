tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task():
    display_tasks()
    if tasks:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

def main():
    # Allow the user to add three tasks initially
    print("Please add three tasks to start with:")
    for i in range(3):
        add_task()

    while True:
        print("\nChoose an option:")
        print("1: View to-do list")
        print("2: Add a task")
        print("3: Delete a task")
        print("4: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
