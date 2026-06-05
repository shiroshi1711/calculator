import tkinter as tk
import customtkinter as ctk
import re
 
root = tk.Tk()
root.title("Calculator")
root.geometry("220x400")

def display_input(_input):
    input_box.insert(index=tk.INSERT, string=_input)
    display_result()

def display_result():
    try:
        calculation = input_box.get()
        if re.search(pattern=r"[\+\-\*\%\/]",string=calculation):
            result = eval(calculation)
            result_label.config(text=f'={result}')
        else:
            result_label.config(text="")
    except Exception as error:
        print(error)

def delete_input():
    index =  input_box.index(tk.INSERT)
    if index > 0:
        input_box.delete(index-1)
    display_result()

def clear_all():
    input_box.delete(0,tk.END)
    result_label.config(text="")
    input_box.config(font=("Bold", 20))
    result_label.config(font=("Bold", 15))

def highlight_result():
    input_box.config(font=("Bold", 15))
    result_label.config(font=("Bold", 20))

def theme_switch():
    if root.cget('bg') == 'SystemButtonFace':
        root.tk_setPalette("black")
        mode_btn.configure(text="🔆")
        input_box.config(bg="black")
    else:
        root.tk_setPalette("SystemButtonFace") 
        mode_btn.configure(text="🌙") 

input_box = tk.Entry(root, font=("Bold", 20), justify=tk.RIGHT, bd=0, bg='SystemButtonFace')
input_box.place(x=15, y=10, width=190, height=50)

result_label = tk.Label(root, font=("Bold", 15), justify=tk.RIGHT, bd=0, fg="gray", anchor=tk.E)
result_label.place(x=15, y=75, width=190, height=40)

clear_btn = ctk.CTkButton(root,text="C", width=40, height=40, font=("Bold", 25),
                           fg_color="#2B0070", corner_radius=7, hover_color="#a95e07",
                           command=clear_all)
clear_btn.place(x=15, y=135)

delete_btn = ctk.CTkButton(root, text="D", width=40, height=40, font=("Bold",25),
                           fg_color="#2B0070", corner_radius= 7, hover_color="#a95e07",
                           command=delete_input)
delete_btn.place(x=65, y=135)

percent_btn = ctk.CTkButton(root, text="%", width=40, height=40, font=("Bold", 25),
                            fg_color="#2B0070", corner_radius= 7, hover_color="#a95e07",
                            command= lambda: display_input(_input="%"))
percent_btn.place(x=115, y=135)

division_btn = ctk.CTkButton(root, text=":", width=40, height=40, font=("Bold", 25),
                             fg_color= "#2B0070", corner_radius=7, hover_color="#a95e07",
                             command= lambda: display_input(_input="/"))
division_btn.place(x=165, y=135)

multiply_btn = ctk.CTkButton(root, text="x", width=40, height=40, font=("Bold", 25),
                            fg_color="#2B0070", corner_radius= 7, hover_color="#a95e07",
                            command= lambda: display_input(_input="*"))
multiply_btn.place(x=165, y=185)

minus_btn = ctk.CTkButton(root, text="-", width=40, height=40, font=("Bold",25),
                             fg_color="#2B0070", corner_radius=7, hover_color="#a95e07",
                             command= lambda: display_input(_input="-"))
minus_btn.place(x=165, y=235)

plus_btn = ctk.CTkButton(root, text="+", width=40, height=40, font=("Bold",25),
                             fg_color="#2B0070", corner_radius=7, hover_color="#a95e07",
                             command= lambda: display_input(_input="+"))
plus_btn.place(x=165, y=285)

result_btn = ctk.CTkButton(root, text="=", width=40, height=40, font=("Bold",25),
                             fg_color="#2B0070", corner_radius=7, hover_color="#a95e07",
                             command=highlight_result)
result_btn.place(x=165, y=335)

btn_7 = ctk.CTkButton(root, text="7", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="7"))
btn_7.place(x=15,y=185)

btn_8 = ctk.CTkButton(root, text="8", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="8"))
btn_8.place(x=65,y=185)

btn_9 = ctk.CTkButton(root, text="9", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="9"))
btn_9.place(x=115,y=185)

btn_4 = ctk.CTkButton(root, text="4", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="4"))
btn_4.place(x=15,y=235)

btn_5 = ctk.CTkButton(root, text="5", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="5"))
btn_5.place(x=65,y=235)

btn_6 = ctk.CTkButton(root, text="6", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="6"))
btn_6.place(x=115,y=235)

btn_1 = ctk.CTkButton(root, text="1", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="1"))
btn_1.place(x=15,y=285)

btn_2 = ctk.CTkButton(root, text="2", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="2"))
btn_2.place(x=65,y=285)

btn_3 = ctk.CTkButton(root, text="3", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="3"))
btn_3.place(x=115,y=285)

mode_btn =ctk.CTkButton(root, text="🌙", width=40, height=40, font=("Bold", 25),
                      fg_color="#2B0070", corner_radius= 7, hover_color="#a95e07",
                      command=theme_switch)
mode_btn.place(x=15,y=335)

btn_0 =ctk.CTkButton(root, text="0", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="0"))
btn_0.place(x=65,y=335)

btn_decimal = ctk.CTkButton(root, text=".", width=40, height=40, font=("Bold", 25),
                      fg_color="#a95e07", corner_radius= 7, hover_color="#2B0070",
                      command= lambda: display_input(_input="."))
btn_decimal.place(x=115,y=335)


root.mainloop()