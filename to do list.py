tasks = []

def add_task():
    new_task = input("Enter the task you want to add: ").strip()
    tasks.append(new_task)
    print(f'Task "{new_task}" added to the list.')
    

def delete_task():
    del_task = input("Enter the task you want to delete: ").strip()
    tasks.remove(del_task)
    print(f'Task "{del_task}" removed from the list.')
   

def list_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

if __name__ == "__main__":
    print("Welcome to your TO do list")
    while True:
        print()
        print("Please select one of the following options:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Quit")

        choice = input("Enter your choice: (1-4) ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
   