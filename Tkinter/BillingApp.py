import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from random import randint
import math

# GUI
top = Tk()
top.geometry("1200x700")
top.title("Billing Meter")
bg_color = "#FF731D"

# --------------------------- variable ---------------#
cus = StringVar()
cont = StringVar()
x = random.randint(1000, 9999)
bill = StringVar()
bill.set(str(x))
soap = IntVar()
face = IntVar()
hair = IntVar()
gel = IntVar()
mois = IntVar()
wash = IntVar()

rice = IntVar()
oil = IntVar()
pulses = IntVar()
wheat = IntVar()
sugar = IntVar()
oats = IntVar()

coffee = IntVar()
thumbs = IntVar()
desi = IntVar()
pepse = IntVar()
shikanji = IntVar()
tea = IntVar()

tgroc = StringVar()
tcos = StringVar()
tcod = StringVar()

taxgr = StringVar()
taxcos = StringVar()
taxcod = StringVar()

# ------------------------------- Parent Frames---------------------#


f1 = Frame(top, height=60, width=1200, bg=bg_color, bd=10, relief=GROOVE)
f1.place(x=0, y=0)
f2 = Frame(top, height=65, width=1200, bg=bg_color, bd=10, relief=GROOVE)
f2.place(x=0, y=60)
f3 = Frame(top, height=415, width=1200)
f3.place(x=0, y=125)
f4 = Frame(top, height=160, width=1200, bg=bg_color)
f4.place(x=0, y=540)

labelMAIN = Label(f1, text="Billing Meter By Ajay", font=("times new roman", 20, "bold"), bg=bg_color, fg="Yellow")
labelMAIN.place(x=460, y=2)


# ---------- GET----------------------#


def cos_sum():
    global total_items, total_tax, grand_total
    global c_s_t, c_f_t, c_g_t, c_w_t, c_h_t, c_m_t

    c_s_t = int(e_a.get()) * 20
    c_f_t = int(e_b.get()) * 40
    c_h_t = int(e_c.get()) * 60
    c_g_t = int(e_d.get()) * 80
    c_m_t = int(e_f.get()) * 100
    c_w_t = int(e_g.get()) * 110

    total = float(c_s_t
                  + c_f_t
                  + c_h_t
                  + c_g_t
                  + c_m_t
                  + c_w_t
                  )

    tgroc.set(total)
    taxcosmetic = total * 18 / 100
    taxcos.set(taxcosmetic)

    tcos.set(total)

    global g_r_t, g_f_t, g_p_t, g_w_t, g_s_t, g_o_t

    g_r_t = (int(e_aa.get()) * 20)
    g_f_t = (int(e_bb.get()) * 40)
    g_p_t = (int(e_cc.get()) * 60)
    g_w_t = (int(e_dd.get()) * 80)
    g_s_t = (int(e_ff.get()) * 100)
    g_o_t = (int(e_gg.get()) * 110)

    total2 = float(g_r_t
                   + g_f_t
                   + g_o_t
                   + g_s_t
                   + g_w_t
                   + g_p_t
                   )
    tgroc.set(total2)
    taxgrocery = total2 * 18 / 100
    taxgr.set(taxgrocery)

    global d_c_t, d_th_t, d_p_t, d_d_t, d_s_t, d_t_t

    d_c_t = (int(e_aaa.get()) * 20)
    d_th_t = (int(e_bbb.get()) * 40)
    d_p_t = (int(e_ccc.get()) * 60)
    d_d_t = (int(e_ddd.get()) * 80)
    d_s_t = (int(e_fff.get()) * 100)
    d_t_t = (int(e_ggg.get()) * 110)

    total3 = float(d_c_t
                   + d_s_t
                   + d_d_t
                   + d_p_t
                   + d_t_t
                   + d_th_t
                   )

    tcod.set(total3)
    taxcoldrink = total3 * 18 / 100
    taxcod.set(taxcoldrink)

    total_items = total + total3 + total2
    total_tax = round(taxgrocery + taxcoldrink + taxcosmetic, 2)
    grand_total = total_items + total_tax


def welcome_bill():
    txtarea.delete("1.0", END)

    txtarea.insert(END, "\tWelcome to Our Shop")
    txtarea.insert(END, f"\nBill no : {bill.get()}")
    txtarea.insert(END, f"\nCustomer Name : {cus.get()}")
    txtarea.insert(END, f"\nPhone Number : {cont.get()}")
    txtarea.insert(END, f"\n======================================")
    txtarea.insert(END, f"\n Products\t\tQty\t  Price ")
    txtarea.insert(END, f"\n======================================")


def bill_area():
    if cus.get() == "" or cont.get() == "":
        messagebox.showerror("Error", " Customer detail must be entered")

    elif tcod.get() == "0.0" and tgroc.get() == "0.0" and tcos.get() == "0.0":
        messagebox.showerror("Error", "No product has Selected")

    else:
        welcome_bill()

        # Cosmetic Conditions

        if soap.get() != 0:
            txtarea.insert(END, f"\nBath soap  \t\t{soap.get()}\t {c_s_t}  ")

        if face.get() != 0:
            txtarea.insert(END, f"\nFace Cream \t\t{face.get()}\t {c_f_t} ")

        if hair.get() != 0:
            txtarea.insert(END, f"\nHair spray\t\t{hair.get()}\t {c_h_t} ")

        if gel.get() != 0:
            txtarea.insert(END, f"\nHair gel  \t\t{gel.get()}\t {c_g_t} ")

        if mois.get() != 0:
            txtarea.insert(END, f"\nMoisturizer\t\t{mois.get()}\t {c_m_t} ")

        if wash.get() != 0:
            txtarea.insert(END, f"\nFace Wash \t\t{wash.get()}\t {c_w_t} ")

        # Grocery Conditions

        if rice.get() != 0:
            txtarea.insert(END, f"\nRice      \t\t{rice.get()}\t {g_r_t} ")

        if oil.get() != 0:
            txtarea.insert(END, f"\nFood oil \t\t{oil.get()}\t {g_f_t} ")

        if pulses.get() != 0:
            txtarea.insert(END, f"\nPulses    \t\t{pulses.get()}\t {g_p_t} ")

        if wheat.get() != 0:
            txtarea.insert(END, f"\nWheat     \t\t{wheat.get()}\t {g_w_t} ")

        if sugar.get() != 0:
            txtarea.insert(END, f"\nSugar      \t\t{sugar.get()}\t {g_s_t} ")

        if oats.get() != 0:
            txtarea.insert(END, f"\nOats        \t\t{oats.get()}\t {g_o_t} ")

        # Drinks Condiitons

        if coffee.get() != 0:
            txtarea.insert(END, f"\nCoffee    \t\t{coffee.get()}\t {d_c_t} ")

        if thumbs.get() != 0:
            txtarea.insert(END, f"\nThumbs Up \t\t{thumbs.get()}\t {d_th_t} ")

        if pepse.get() != 0:
            txtarea.insert(END, f"\nPepsi    \t\t{pepse.get()}\t {d_p_t} ")

        if desi.get() != 0:
            txtarea.insert(END, f"\nDesi      \t\t{desi.get()}\t {d_d_t} ")

        if shikanji.get() != 0:
            txtarea.insert(END, f"\nShikanji   \t\t{shikanji.get()}\t {d_s_t} ")

        if tea.get() != 0:
            txtarea.insert(END, f"\nTea       \t\t{tea.get()}\t {d_t_t} ")

        txtarea.insert(END, f"\n--------------------------------------")
        txtarea.insert(END, f"\nCosmetics Tax\t\t  {taxcos.get()} ")
        txtarea.insert(END, f"\nGroceries Tax\t\t  {taxgr.get()} ")
        txtarea.insert(END, f"\nCold Drinks Tax\t\t  {taxcod.get()} ")
        txtarea.insert(END, f"\n--------------------------------------")
        txtarea.insert(END, f"\nTotal of Items\t\t  {total_items} ")
        txtarea.insert(END, f"\nTotal of Tax\t\t  {total_tax} ")
        txtarea.insert(END, f"\nTotal Amount\t\t  {grand_total} ")
        save_bill()


def save_bill():
    op = messagebox.askyesno("Save", "Do yo want to save the bill?")
    if op > 0:
        bill_data = txtarea.get("1.0", END)
        f1 = open("bills/" + str(bill.get()) + ".txt", "w")
        f1.write(bill_data)
        f1.close()
        messagebox.showinfo("Saved!", "Bill has saved successfully")
    else:
        return


def bill_check():
    flag = "no"
    for i in os.listdir("bills/"):
        if i.split(".")[0] == bill.get():
            f1 = open(f"bills/{i}", "r")
            txtarea.delete("1.0", END)
            for d in f1:
                txtarea.insert(END, d)
            f1.close()
            flag = "yes"

    if flag == "no":
        messagebox.showerror("Error", "Invalid bill no.")


def clear():
    cus.set("")
    cont.set("")
    x = random.randint(1000, 9999)
    bill.set("")
    bill.set(str(x))
    soap.set(0)
    face.set(0)
    hair.set(0)
    gel.set(0)
    mois.set(0)
    wash.set(0)

    rice.set(0)
    oil.set(0)
    pulses.set(0)
    wheat.set(0)
    sugar.set(0)
    oats.set(0)

    coffee.set(0)
    thumbs.set(0)
    desi.set(0)
    pepse.set(0)
    shikanji.set(0)
    tea.set(0)

    tgroc.set("")
    tcos.set("")
    tcod.set("")

    taxgr.set("")
    taxcos.set("")
    taxcod.set("")

    welcome_bill()


def exit():
    op = messagebox.askyesno("Exit", "Are you Sure?")
    if op > 0:
        top.destroy()


# ---------------------------------Child Frames and Elements F(2)-------------------------------#


l1 = Label(f2, text="Customer Name", font="bold 15", bg=bg_color)
l1.place(x=25, y=10)
E1 = Entry(f2, font="arial 10 bold", textvariable=cus)
E1.place(x=180, y=13)

l2 = Label(f2, text="Contact No.", font="bold 15", bg=bg_color)
l2.place(x=380, y=10)
e2 = Entry(f2, font="arial 10 bold", textvariable=cont)
e2.place(x=500, y=13)

l3 = Label(f2, text="Bill No.", font="bold 15", bg=bg_color)
l3.place(x=700, y=10)
e3 = Entry(f2, font="arial 10 bold", textvariable=bill)
e3.place(x=780, y=13)

# -------------------------------------Nesting of frames (F3)-------------------------------------#

f2_1 = Frame(f3, height=420, width=300, bg=bg_color, bd=10, relief=GROOVE)
f2_1.place(x=0, y=0)
f2_2 = Frame(f3, height=420, width=300, bg=bg_color, bd=10, relief=GROOVE)
f2_2.place(x=300, y=0)
f2_3 = Frame(f3, height=420, width=300, bg=bg_color, bd=10, relief=GROOVE)
f2_3.place(x=600, y=0)
f2_4 = Frame(f3, height=420, width=300, bg="white")
f2_4.place(x=900, y=0)

# --------------------------------------Sub elements of F3---------------------------------#
l11 = Label(f2_1, text="Cosmectics", font=("times new roman", 20, "bold"), bg=bg_color, fg="yellow")
l11.place(x=80, y=6)

fl1 = Label(f2_1, text="Bath Soap", font="bold 15", bg=bg_color)
fl1.place(x=10, y=60)
fl3 = Label(f2_1, text="Face cream", font="bold 15", bg=bg_color)
fl3.place(x=10, y=120)
fl4 = Label(f2_1, text="Hair spray", font="bold 15", bg=bg_color)
fl4.place(x=10, y=180)
fl5 = Label(f2_1, text="Hair gel", font="bold 15", bg=bg_color)
fl5.place(x=10, y=240)
fl6 = Label(f2_1, text="Moisturizer", font="bold 15", bg=bg_color)
fl6.place(x=10, y=300)
fl2 = Label(f2_1, text="Face wash", font="bold 15", bg=bg_color)
fl2.place(x=10, y=360)

e_a = Entry(f2_1, font="arial 10 bold", textvariable=soap)
e_a.place(x=130, y=60)
e_b = Entry(f2_1, font="arial 10 bold", textvariable=face)
e_b.place(x=130, y=120)
e_c = Entry(f2_1, font="arial 10 bold", textvariable=hair)
e_c.place(x=130, y=180)
e_d = Entry(f2_1, font="arial 10 bold", textvariable=gel)
e_d.place(x=130, y=240)
e_f = Entry(f2_1, font="arial 10 bold", textvariable=mois)
e_f.place(x=130, y=300)
e_g = Entry(f2_1, font="arial 10 bold", textvariable=wash)
e_g.place(x=130, y=360)

# --------------------------------- Sub elements of F3(second)------------------#
l12 = Label(f2_2, text="Groceries", font=("times new roman", 20, "bold"), bg=bg_color, fg="yellow")
l12.place(x=80, y=6)

fl11 = Label(f2_2, text="Rice", font="bold 15", bg=bg_color)
fl11.place(x=10, y=60)
fl33 = Label(f2_2, text="Food Oil", font="bold 15", bg=bg_color)
fl33.place(x=10, y=120)
fl44 = Label(f2_2, text="Pulses", font="bold 15", bg=bg_color)
fl44.place(x=10, y=180)
fl55 = Label(f2_2, text="Wheat", font="bold 15", bg=bg_color)
fl55.place(x=10, y=240)
fl66 = Label(f2_2, text="Sugar", font="bold 15", bg=bg_color)
fl66.place(x=10, y=300)
fl22 = Label(f2_2, text="Oats", font="bold 15", bg=bg_color)
fl22.place(x=10, y=360)

e_aa = Entry(f2_2, font="arial 10 bold", textvariable=rice)
e_aa.place(x=130, y=60)
e_bb = Entry(f2_2, font="arial 10 bold", textvariable=oil)
e_bb.place(x=130, y=120)
e_cc = Entry(f2_2, font="arial 10 bold", textvariable=pulses)
e_cc.place(x=130, y=180)
e_dd = Entry(f2_2, font="arial 10 bold", textvariable=wheat)
e_dd.place(x=130, y=240)
e_ff = Entry(f2_2, font="arial 10 bold", textvariable=sugar)
e_ff.place(x=130, y=300)
e_gg = Entry(f2_2, font="arial 10 bold", textvariable=oats)
e_gg.place(x=130, y=360)

# --------------------------------- Sub elements of F3(third)------------------#

l11 = Label(f2_3, text="Drinks", font=("times new roman", 20, "bold"), bg=bg_color, fg="yellow")
l11.place(x=80, y=6)

fl111 = Label(f2_3, text="Coffee", font="bold 15", bg=bg_color)
fl111.place(x=10, y=60)
fl333 = Label(f2_3, text="Thumbs Up", font="bold 15", bg=bg_color)
fl333.place(x=10, y=120)
fl444 = Label(f2_3, text="Pepsi", font="bold 15", bg=bg_color)
fl444.place(x=10, y=180)
fl555 = Label(f2_3, text="Desi", font="bold 15", bg=bg_color)
fl555.place(x=10, y=240)
fl666 = Label(f2_3, text="Shikanji", font="bold 15", bg=bg_color)
fl666.place(x=10, y=300)
fl222 = Label(f2_3, text="Tea", font="bold 15", bg=bg_color)
fl222.place(x=10, y=360)

e_aaa = Entry(f2_3, font="arial 10 bold", textvariable=coffee)
e_aaa.place(x=130, y=60)
e_bbb = Entry(f2_3, font="arial 10 bold", textvariable=thumbs)
e_bbb.place(x=130, y=120)
e_ccc = Entry(f2_3, font="arial 10 bold", textvariable=pepse)
e_ccc.place(x=130, y=180)
e_ddd = Entry(f2_3, font="arial 10 bold", textvariable=desi)
e_ddd.place(x=130, y=240)
e_fff = Entry(f2_3, font="arial 10 bold", textvariable=shikanji)
e_fff.place(x=130, y=300)
e_ggg = Entry(f2_3, font="arial 10 bold", textvariable=tea)
e_ggg.place(x=130, y=360)

# -------------------------------- Bill area -------------#
bframe = Frame(f2_4, height=50, width=300, bg="white", bd=6, relief=GROOVE)
bframe.place(x=0, y=0)
blabel = Label(bframe, text="Bill Area", font="arial 15", fg="black", bg="white")
blabel.place(x=94, y=5)
txtarea = Text(f2_4, height=370, width=300)
txtarea.place(x=0, y=50)

b = ttk.Button(f2, text="Search", command=bill_check)
b.place(x=960, y=12)

# ----------------------- Nesting of frames(F4)----------#


f3_1 = Frame(f4, height=160, width=650, bg=bg_color, bd=10, relief=GROOVE)
f3_1.place(x=0, y=0)
f3_2 = Frame(f4, height=160, width=550, bg=bg_color, bd=10, relief=GROOVE)
f3_2.place(x=650, y=0)

# --------------------------------- Sub elements of F4(First)------------------#

f41_1 = Label(f3_1, text="Total of Groceries ", font="arial", bg=bg_color)
f41_1.place(x=10, y=30)
f41_2 = Label(f3_1, text="Total of Cosmetics", font="arial", bg=bg_color)
f41_2.place(x=10, y=70)
f41_3 = Label(f3_1, text="Total of Cold drinks", font="arial", bg=bg_color)
f41_3.place(x=10, y=110)

f42_1 = Label(f3_1, text="Grocery Tax ", font="arial", bg=bg_color)
f42_1.place(x=320, y=30)
f42_2 = Label(f3_1, text="Cosmetic Tax", font="arial", bg=bg_color)
f42_2.place(x=320, y=70)
f42_3 = Label(f3_1, text="Cold drinks Tax", font="arial", bg=bg_color)
f42_3.place(x=320, y=110)

e4_1 = Entry(f3_1, font="arial 10 bold", textvariable=tgroc)
e4_1.place(x=160, y=30)
e4_2 = Entry(f3_1, font="arial 10 bold", textvariable=tcos)
e4_2.place(x=160, y=70)
e4_3 = Entry(f3_1, font="arial 10 bold", textvariable=tcod)
e4_3.place(x=160, y=110)

e4_4 = Entry(f3_1, font="arial 10 bold", textvariable=taxgr)
e4_4.place(x=440, y=30)
e4_5 = Entry(f3_1, font="arial 10 bold", textvariable=taxcos)
e4_5.place(x=440, y=70)
e4_6 = Entry(f3_1, font="arial 10 bold", textvariable=taxcod)
e4_6.place(x=440, y=110)

# --------------------------------- Sub elements of F4(second)------------------#

b2 = Button(f3_2, text="Total", height=3, width=11, font="arial", command=cos_sum)
b2.place(x=20, y=40)
b3 = Button(f3_2, text="Generate Bill", height=3, width=11, font="arial", command=bill_area)
b3.place(x=150, y=40)
b4 = Button(f3_2, text="Clear", height=3, width=11, font="arial", command=clear)
b4.place(x=280, y=40)
b5 = Button(f3_2, text="Exit", height=3, width=11, font="arial", command=exit)
b5.place(x=410, y=40)

top.mainloop()
