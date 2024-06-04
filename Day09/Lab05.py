from tkinter import *

def dam_sang_km():
    dam = nhap_dam.get()
    if dam:
        km = float(dam) * 1.6093
        nhap_km.delete(0, END)
        nhap_km.insert(0, str(km))

def km_sang_dam():
    km = nhap_km.get()
    if km:
        dam = float(km) * 0.6214
        nhap_dam.delete(0, END)
        nhap_dam.insert(0, str(dam))

giao_dien = Tk()
giao_dien.title("Chuyển đổi dặm - km")
giao_dien.geometry("400x200")

nhap_dam_label = Label(giao_dien, text="Dặm:")
nhap_dam_label.pack()

nhap_dam = Entry(giao_dien)
nhap_dam.pack()
nhap_dam.bind('<KeyRelease>', lambda event: dam_sang_km())

nhap_km_label = Label(giao_dien, text="Kilômét:")
nhap_km_label.pack()

nhap_km = Entry(giao_dien)
nhap_km.pack()
nhap_km.bind('<KeyRelease>', lambda event: km_sang_dam())

giao_dien.mainloop()