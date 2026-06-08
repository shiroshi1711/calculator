import tkinter as tk
import customtkinter as ctk
import re


class Calculator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("300 X 400")
        self.current_theme = "dark"
        self.root._set_appearance_mode(self.current_theme)
        self.root.title("Calculator")
        
        self.input_box = ctk.CTkEntry(self.root, width=195, height=20, border_width=0,
                                      text_color="#ffffff",justify= ctk.RIGHT, font=("Bold", 30))
        self.input_box.pack(pady= 20)

        self.result_box = ctk.CTkLabel(self.root, width=195, height=20, text_color= "#787575",
                                       font=("Bold", 20),anchor= ctk.E  , text="")
        self.result_box.pack(pady =20)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["c", "d", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["☾☼", "0", ".", "="]
        ]

        btn_frame = ctk.CTkFrame(self.root, border_width=0, border_color="#ffffff00")
        btn_frame.pack(pady=10)
        for row, button_row in enumerate (buttons):
            for col, value in enumerate(button_row):
                btn = ctk.CTkButton(
                    btn_frame, text=value, height=40, width=40, fg_color="#4f06f8"
                    ,corner_radius= 10, hover_color= "#d907a1",
                    command=lambda v = value: self.display_input(v))
                btn.grid(row = row,
                         column = col,
                        padx= 5, 
                        pady= 5)
                if value == "d":
                    btn.configure(command=self.delete)
                elif value == "c":
                    btn.configure(command=self.clear_all)
                elif value == "=":
                    btn.configure(command=self.highlight)
                elif value == "☾☼" :
                    btn.configure(command=self.theme_switch)

    def delete(self):
        index = self.input_box.index(tk.INSERT)
        if index > 0 :
            self.input_box.delete(index - 1)
        self.calculate()

    def display_input(self, value):
        self.input_box.insert(tk.INSERT, value)
        self.calculate()

    def calculate(self):
        try:
            calculation = self.input_box.get()
            if re.search(pattern=r"[\+\-\*\%\/]",string=calculation):
                result = eval(calculation)
                self.result_box.configure(text=f'= {result}')
            else:
                self.result_box.configure(text="")
        except Exception:
            self.result_box.configure(text="Error")

    def clear_all(self):
        self.input_box.delete(0, tk.END)
        self.result_box.configure(text="")
        self.input_box.configure(font=("Bold", 30))
        self.result_box.configure(font=("Bold", 20))

    def highlight(self):
        self.input_box.configure(font=("Bold", 20))
        self.result_box.configure(font=("Bold", 30), text_color ="#ffffff")

    def theme_switch(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        self.root._set_appearance_mode(self.current_theme)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":

    app = Calculator()
    app.run()



#result box bug = displaying error when insert box like "1+"
#btn frame and result box still has bg not blending with the overall theme
#maybe differentiate the color for the operators btn 
