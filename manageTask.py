taskData = {}
subTaskData = {}
# numberOfTaskAndSubTask = 0

def readTask():
    for key in taskData:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'\n{key} : {taskData[key]}')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
        

def CreateTask(name, userInput):
    taskData[name] = userInput
    return "task completed"

def updateTask(name, string):
    taskData[name] = string
    return f"Task {name} has been updated"

def deleteTask(name):
    taskData.pop(name)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(f'Task {name} has been deleted')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
    return f"\nTask {name} has been deleted\n"



def main():
    while(True):
        print("""\nplease select the task that you want to comelete\n[1] list Task [2] Create Task [3] Edit Task [4] Delete Task [5] Exit\n""")
        taskInput = input('Enter the task number: ')
        taskInput = int(taskInput)
        if(taskInput == 1):
            readTask()
        elif(taskInput == 2):
            name = input("Enter the name of the task you want to create: ")
            user_input = input("Enter the task: ")
            CreateTask(name, user_input)
        elif(taskInput == 3):
            readTask()
            name = input("Enter the name of the task you want to update: ")
            user_input = input("Enter the updated task: ")
            updateTask(name, user_input)
        elif(taskInput == 4):
            readTask()
            user_input = input("Enter the task you want to Delete: ")
            deleteTask(user_input)
        elif(taskInput == 5):
            print("Exiting the program...")
            break

if __name__ == "__main__":    main()
