class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the list.')
        else:
            print(f'Task "{task}" not found in the list.')

    def view_tasks(self):
        if self.tasks:
            print("Your to-do list:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("Your to-do list is empty.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("\n2. Delete task")
        print("\n3. View tasks")
        print("\n4. Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
