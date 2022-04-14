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
    print(selection.split(" | "))
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