# from functions import open_fn,write_todo
import functions
import time
now=time.strftime("%b-%d, %H:%M:%S")
print("Is is ",now)

while True:
    user_action=input("type add, show , edit , complete or exit: ")
    user_action   ==user_action.strip()


    if user_action.startswith("add"):
        todos = user_action[4:] +"\n"

        todo=functions.open_fn()
        todo.append(todos)

        functions.write_todo(todo)
    elif user_action.startswith("show"):
        todo=functions.open_fn()

        for index, item in enumerate(todo):
            item=item.strip("\n")
            item =item.title()
            pf=f"{index+1}_{item}"
            print(pf)
    elif user_action.startswith("edit") :
        try:
            no=int(user_action[5:])
            print(no)
            no=no-1
            new_todo =input("Enter new todo: ") +"\n"
            print("existing to do is ",todo)
            todo=functions.open_fn('todo.txt')
            todo[no]=new_todo


            functions.write_todo(todo)
            print("new todo is ",todo)
        except ValueError or IndexError:
            print("Command is not valid::")
            continue
    elif user_action.startswith("complete"):
        try:
            no = int(user_action[9:])
            number = no - 1
            todo_to_remove = todo[number].strip('\n')
            todo = functions.open_fn()
            todo.pop(number)
            functions.write_todo(todo)
            message = f"{todo_to_remove} was removed from the todo"
        except IndexError:
            print("there's no todo exist with that number::")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye")