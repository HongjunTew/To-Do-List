# To-Do List Manager

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index] += " - Completed"
        print("Task marked as completed!")
    else:
        print("Invalid task index")

# Function to view the to-do list
def view_list():
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index")

# Main program
todo_list = []

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View To-Do List")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        complete_task(task_index)
    elif choice == '3':
        view_list()
    elif choice == '4':
        task_index = int(input("Enter the index of the task to remove: ")) - 1
        remove_task(task_index)
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
