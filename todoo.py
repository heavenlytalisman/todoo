
file_name = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                tasks.append(line.strip())

    except FileNotFoundError:
        pass
    
    return tasks


def update_task(tasks):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def main():
    tasks = list(load_tasks())
    while True:
        print("\n YOUR TASKS \n")
        if not tasks:
            print("You have no pending tasks ")
        else:
            for id, task in enumerate(tasks, 1):
                print (f"{id}:{task}")
        
        print("\n Options:")
        print("[A]dd    [R]emove    [Q]uit")
        choice = str(input("Enter your choice: ").lower())

        if choice == 'a':
            new_task = str(input("Enter a task to add: "))
            tasks.append(new_task)
            update_task(tasks)
        
        elif choice == "r":
            task_id = int(input("Enter task id to remove : "))
            if task_id >= 1 and task_id <= len(tasks):
                tasks.pop(task_id - 1)
                update_task(tasks)

        elif choice == "q":
            break
        
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
    