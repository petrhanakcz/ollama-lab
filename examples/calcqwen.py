import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=35, 
borderwidth=5)
        self.display.grid(row=0, column=0, 
columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, width=10, 
height=2,
                              command=lambda t=text: 
self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, value)

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()