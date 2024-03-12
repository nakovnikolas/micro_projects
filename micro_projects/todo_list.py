def print_menu() -> None:
    menu = """
    ===== To-Do List Menu =====
    1. Add a new task
    2. Mark a task as completed
    3. View all tasks
    4. Quit
            """
    print(menu)


def set_task(tasks: list[str]) -> list[str]:
    task = input("Enter a task description: ")
    task = "[ ] " + task
    tasks.append(task)
    print(f"Task {task[3:]} added successfully!")

    return tasks


def mark_task(tasks: list[str]) -> list[str]:
    if tasks:
        print("===== Tasks =====")
        show_tasks(tasks)

        mark = int(input("Enter the index of the task to mark as completed: "))

        marked_task = tasks[mark].replace("[ ]", "[X]")
        tasks[mark] = marked_task
        print(f"Task {tasks[mark][3:]} marked as completed!")
    else:
        print("There are still no tasks.\nYou can add one by choosing 1.")
    return tasks


def view_tasks(tasks: list[str]) -> list[str]:
    if tasks:
        show_tasks(tasks)
    else:
        print("There are still no tasks.\nYou can add one by choosing 1.")


def show_tasks(tasks: list[str]) -> list[str]:
    for index, task in enumerate(tasks):
        print(str(index) + ". " + task)


def todo_list() -> None:
    tasks = []
    num = 0
    while True:

        print_menu()
        choice = input("Enter your choice (1-4): ")

        try:
            num = int(choice)
        except ValueError:
            pass

        print()
        if 0 <= num <= 4 and choice.isdigit():
            if choice == "4":
                print("Exiting the program. Goodbye!")
                break
            if choice == "1":
                tasks = set_task(tasks)
                continue
            elif choice == "2":
                tasks = mark_task(tasks)
                continue
            elif choice == "3":
                view_tasks(tasks)
                continue
        else:
            print("Incorrect input.\nPlease, enter a number from 1 to 4.")


if __name__ == "__main__":
    todo_list()
