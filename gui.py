import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
ad_button=sg.Button("Add")

Window=sg.Window('My To Do App', layout=[[label],
                                         [input_box,ad_button]],
                                         font=("helow",20))

while True:
    event , value = Window.read()
    match event:
        case "Add":
            todo = functions.open_fn()
            new_todo=value["todo"] +"\n"
            todo.append(new_todo)
            functions.write_todo(todo)
        case sg.WIN_CLOSED:
            break

Window.close()