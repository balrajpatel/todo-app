import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo:")
input_box = sg.InputText(tooltip="Enter  todo")
ad_button=sg.Button("Add")

Window=sg.Window('My To Do App', layout=[[label], [input_box,ad_button]])
Window.read()
Window.close()