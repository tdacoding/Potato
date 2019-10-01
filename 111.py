import tkinter as tk

root = tk.Tk()
root.title("Hello World!")
root.geometry('300x140')

def button_clicked(label):
    print("Hello World!")
    label.config(text = label['text'] + '1')

def close():
    root.destroy()
    root.quit()

label1 = tk.Label(root, text = 'ww')
label1.pack(fill="y")
button = tk.Button(root, text="Press Me", command=button_clicked(label1))
button.pack(fill="both")

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()