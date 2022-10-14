#создаем калькулятор
import tkinter as tk
from tkinter import messagebox   #модуль работы со всплывающими окнами
num = 0
win = tk.Tk()

def add_digit(digit):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)
    calc['state'] = tk.DISABLED

def add_operation(operation):
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculet()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED

def calculet():
    calc['state'] = tk.NORMAL
    value = calc.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
        calc['state'] = tk.DISABLED
    except (NameError, SystemError):
        messagebox.showinfo('Внимание', 'Нужно вводить только числа!') #показать информацию
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!') #показать информацию
        calc.insert(0, 0)
    calc['state'] = tk.DISABLED


def make_digit_button(arg):
    return tk.Button(text=arg, bd=5, font=('Arial', 13),
                    command= lambda: add_digit(arg))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                    command= lambda: add_operation(operation))

def make_calc_button(symbol):
    return tk.Button(text=symbol, bd=5, font=('Arial', 13), fg='red',
                    command= calculet)

def make_clear_button(symbol):
    return tk.Button(text=symbol, bd=5, font=('Arial', 13), fg='red',
                    command= clear)

def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED

def press_key(event):
    calc['state'] = tk.NORMAL
    #print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r' or event.char == '=':
        calculet()
    else:
        event = calc.get()
        calc.delete(0, tk.END)
        calc.insert(0, event)
    calc['state'] = tk.DISABLED


win.geometry(f'240x270+100+200')
win.resizable(False, False) #изменение размеров окна
win['bg'] = '#91E5F6'
win.title('Калькулятор')
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)


make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)


win.mainloop()