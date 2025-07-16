def task():
    task = []  # empty list
    print("Welcome to the Task Management App")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        task.append(task_name)

    print(f"Today's tasks are:\n{task}")

    while True:
        operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))

        if operation == 1:
            add = input("Enter task you want to add = ")
            task.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in task:
                up = input("Enter new task = ")
                ind = task.index(updated_val)
                task[ind] = up
                print(f"Updated task: {up}")
            else:
                print("Task not found!")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete = ")
            if del_val in task:
                task.remove(del_val)
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found!")

        elif operation == 4:
            print("Current tasks are:")
            for t in task:
                print("-", t)

        elif operation == 5:
            print("Exiting Task Management App.")
            break

        else:
            print("Invalid input! Please choose a valid option.")


task()