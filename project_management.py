tasks=[]

while True:

    print("\n========== Project Task Management System ==========")

    print("1. Add Task")

    print("2. View Tasks")

    print("3. Search Task")

    print("4. Update Task")

    print("5. Delete Task")

    print("6. Count Tasks")

    print("7. Exit")

    choice = input("Enter your choice: ")


    if(choice=='1'):
        task=input("enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

 
    elif(choice=='2'):
       if len(tasks)==0:
        print("No tasks available.")
       else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

    elif(choice=='3'):
           search_task=input("Enter the task to search: ")
           if search_task in tasks:
            print(f"Task '{search_task}' found.")
           else:
            print(f"Task '{search_task}' not found.")

    elif(choice=='4'):
      update_task=input("Enter the task to update: ")
      if update_task in tasks:
        new_task=input("Enter the new task: ")
        index=tasks.index(update_task)
        tasks[index]=new_task
        print(f"Task '{update_task}' updated to '{new_task}'.")
      else:
        print(f"Task '{update_task}' not found.")


    elif(choice=='5'):
      delete_task=input("Enter the task to delete: ")
      if delete_task in tasks:
        tasks.remove(delete_task)
        print(f"Task '{delete_task}' deleted successfully.")
      else:
        print(f"Task '{delete_task}' not found.")

    elif(choice=='6'):
      print(f"Total number of tasks: {len(tasks)}")

    else:
      print("Exiting the program. Goodbye!")
      break


