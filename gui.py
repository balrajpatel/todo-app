import functions
import time
import PySimpleGUI as sg

clock = sg.Text("",key="clock")
sg.theme("Black")

label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
ad_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.open_fn(), key="todos",
                      enable_events=True, size=(40, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
Window = sg.Window('My To Do App',
                   layout=[[clock],
                           [label],
                           [input_box, ad_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Arial", 20))
while True:
    event, values = Window.read(timeout=200)
    Window["clock"].update(time.strftime("%b-%d, %H:%M:%S"))

    match event:
        case "Add":
            todo = functions.open_fn()
            new_todo = values["todo"] + "\n"
            todo.append(new_todo)
            functions.write_todo(todo)
            Window['todos'].update(values=todo)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todo = functions.open_fn()
                index = todo.index(todo_to_edit)
                todo[index] = new_todo
                functions.write_todo(todo)
                Window['todos'].update(values=todo)
            except IndexError:
                sg.popup("Please select the todo item first", font=("Arial", 15))
        case "Complete":
            try:
                todo_to_remove = values["todos"][0]
                todo = functions.open_fn()
                todo.remove(todo_to_remove)
                functions.write_todo(todo)
                Window['todos'].update(values=todo)
                Window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select the todo item first", font=("Arial", 15))
        case "Exit":
            break
        case "todos":
            Window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

Window.close()
