import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        for i in range(4):
            self.tasks.append(task)
            print(f"Task '{task}' added successfully.")
            due_date = input("Enter due date in YYYY-MM-DD format: ")
            try:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date. Please enter a valid date in YYYY-MM-DD format.")
            if i == 3:
                break
            print("You have exceeded the maximum number of attempts. Please try again.")
        

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully.")
        else:
            print(f"Task '{task}' not found.")
    
    def list_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks.")
    
    def mark_task_completed(self, task):
        if task in self.tasks:
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found.")
    
    def display_tasks_due_today(self):
        today = datetime.date.today()
        print("Tasks due today:")
        for task in self.tasks:
            due_date = task.due_date
            if due_date == today:
                print(task)
def main():
    todo_list = TodoList()
    while True:
        list_of_choices = [
            "1. Add task",
            "2. Remove task",
            "3. List tasks",
            "4. Mark task as completed",
            "5. Display tasks due today",
            "6. Exit"
        ]
        
        
        choice = input("\n".join(list_of_choices) + "\n")
        print("enter a number to perform an action: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            task = input("Enter task: ")
            todo_list.mark_task_completed(task)
        elif choice == '5':
            todo_list.display_tasks_due_today()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

main()