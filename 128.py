from tkinter import *

def km_converter():
    km = textbox1.get()
    km = int(km)
    message = km * 0.6214
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, " miles")
    
def miles_converter():
    mile = textbox1.get()
    mile = int(mile)
    message = mile * 1.6093
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, " km")


window = Tk()
window.title("Расстояние")
window.geometry("300x200")

msg = Label(text = "Введи число которое надо преобразовать: ")
msg.place(x = 30, y = 20)

textbox1 = Entry()
textbox1.place(x = 30, y = 50, width = 200, height = 25)

textbox1["justify"] = "center"
textbox1.focus()

convert1 = Button(text = "Преоброзовать милли в киллометр", command = km_converter)
convert1.place(x = 30, y = 80, width = 200, height = 25)

convert2 = Button(text = "Преобразовать киллометр в мили", command = miles_converter)
convert2.place(x = 30, y = 110, width = 200, height = 25)

textbox2 = Entry()
textbox2.place(x = 30, y = 140, width = 200, height = 25)
textbox2["justify"] = "center"

window.mainloop()