from tkinter import *
import backend


def view_command():
    list1.delete(0, END)
    for i in backend.view():
        entry = f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}"
        list1.insert(END, entry)


def search_command():
    list1.delete(0, END)
    for i in backend.search(title_text.get(), director_text.get(), year_text.get(), rating_text.get()):
        entry = f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]}"
        list1.insert(END, entry)


def add_command():
    backend.insert(title_text.get(), director_text.get(), year_text.get(), rating_text.get())
    entry = f"{backend.view()[-1][0]} | {title_text.get()} | {director_text.get()} | {year_text.get()} | {rating_text.get()}"
    list1.insert(END, entry)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def get_selected_row(event):
    global index
    index = list1.curselection()[0]+1
    selection = list1.get(list1.curselection())
    try:
        e1.delete(0, END)
        e1.insert(END, selection.split(" | ")[1])
        e2.delete(0, END)
        e2.insert(END, selection.split(" | ")[2])
        e3.delete(0, END)
        e3.insert(END, selection.split(" | ")[3])
        e4.delete(0, END)
        e4.insert(END, selection.split(" | ")[4])
    except IndexError:
        pass


def delete_command():
    backend.delete(index)
    list1.delete(list1.curselection())
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def update_command():
    backend.update(index, title_text.get(), director_text.get(), year_text.get(), rating_text.get())
    view_command()

window = Tk()
window.wm_title("Movies")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Director")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="Rating")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

director_text = StringVar()
e2 = Entry(window, textvariable=director_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

rating_text = StringVar()
e4 = Entry(window, textvariable=rating_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())
list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search", width=12, comman=search_command)
b2.grid(row=3, column=3)

b4 = Button(window, text="Add", width=12, command=add_command)
b4.grid(row=4, column=3)

b5 = Button(window, text="Update selected", width=12, command=update_command)
b5.grid(row=5, column=3)

b3 = Button(window, text="Delete", width=12, command=delete_command)
b3.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
