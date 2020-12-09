import json
import os.path
import tkinter

filename = 'tasks.json'

def read(filename):
    with open(filename, 'r') as fread:
        global load 
        load = json.load(fread)

if os.path.isfile(filename):
    read(filename)
else:
    load = []

def zakaz():
    new_task = {'Задача:': entry_task.get(), 'Категория:': entry_cat.get(), 'Время:': entry_time.get()}
    load.append(new_task)
    entry_task.delete(0, 'end')
    entry_cat.delete(0, 'end')
    entry_time.delete(0, 'end')

def spisok():
    if load:
        text.delete(1.0, 'end')
        for elem in load:
            print(elem.items())
            for i, j in elem.items():
                text.insert('end', i + ' ' + j + '; ')
            text.insert('end', '\n\n')

def exxxit():
    with open(filename, 'w') as file:
        json.dump(load, file)
        window.destroy()

window = tkinter.Tk()
window.title('Менеджер задач')

label_task = tkinter.Label(window, text = 'Задача')
label_task.grid(row = 0, column = 0)
entry_task = tkinter.Entry(window)
entry_task.grid(row = 0, column = 1)

label_cat = tkinter.Label(window, text = 'Категория')
label_cat.grid(row = 1, column = 0)
entry_cat = tkinter.Entry(window)
entry_cat.grid(row = 1, column = 1)

label_time = tkinter.Label(window, text = 'Время')
label_time.grid(row = 2, column = 0)
entry_time = tkinter.Entry(window)
entry_time.grid(row = 2, column = 1)

zakaz_btn = tkinter.Button(window, text = 'Заказать', command = zakaz)
zakaz_btn.grid(row = 3, column = 1)

spisok_btn = tkinter.Button(window, text = 'Список задач', command = spisok)
spisok_btn.grid(row = 4, column = 1)

text = tkinter.Text(width=100, height = 20)
text.grid(row = 0, column = 3, rowspan = 30, columnspan = 5)

exit_btn = tkinter.Button(window, text = 'Выход', command = exxxit)
exit_btn.grid(row = 5, column = 1)

window.mainloop()
