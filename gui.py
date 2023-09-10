import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
ad_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.open_fn(), key="todos",
                      enable_events=True, size=(40, 10))
edit_button = sg.Button("Edit")
Window = sg.Window('My To Do App',
                   layout=[[label], [input_box, ad_button], [list_box, edit_button]],
                   font=("", 20))
while True:
    event, values = Window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todo = functions.open_fn()
            new_todo = values["todo"] + "\n"
            todo.append(new_todo)
            functions.write_todo(todo)
            Window['todos'].update(values=todo)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todo = functions.open_fn()
            index = todo.index(todo_to_edit)
            todo[index] = new_todo
            functions.write_todo(todo)
            Window['todos'].update(values=todo)
        case "todos":
            Window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

Window.close()
