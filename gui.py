from tkinter import *
import backend
import app


def server_command():
    entry = app.server_command(server_text.get())
    list1.insert(END, entry[0], entry[1], f"{entry[2]}/{entry[3]}", "")
    e1.delete(0, END)
    backend.insert(entry[0])


window = Tk()
window.wm_title("CS:GO Notifier")

# small_font = tkFont.Font(size=5)

l1 = Label(window, text="Server IP")
l1.grid(row=0, column=0)

l2 = Label(window, text="Favorites")
l2.grid(row=0, column=3)

server_text = StringVar()
e1 = Entry(window, textvariable=server_text, width=55)
e1.insert(0, "216.52.148.47:27015")
e1.grid(row=0, column=1)

favorites_text = StringVar()
e2 = Entry(window, textvariable=favorites_text, width=55)
e2.grid(row=0, column=4)

b1 = Button(window, text="Add", width=3, command=server_command)
b1.grid(row=0, column=2)

b2 = Button(window, text="Add", width=3)
b2.grid(row=0, column=5)

list1 = Listbox(window, height=8, width=55, font=small_font)
list1.grid(row=2, column=1)
# list1.grid(row=2, column=1, columnspan=2)

list2 = Listbox(window, height=8, width=55)
list2.grid(row=2, column=4)
# list2.grid(row=2, column=4, rowspan=6, columnspan=2)

# sb1 = Scrollbar(window)
# sb1.grid(row=2, column=4, rowspan=6)

# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview())
# list1.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()
