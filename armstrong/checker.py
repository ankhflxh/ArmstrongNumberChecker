import tkinter as tk

def armstrong_num(num):
    #calculate the sum of cubes of each digit
    numsum = sum(int(number) ** 3 for number in str(num))
    return num == numsum

def check_number():
    try: 
        num = int(entry.get())
        if 100 <= num <= 999:
            result = "IS" if armstrong_num(num) else "IS NOT"
            message_label.config(text=f"{num} {result} AN ARMSTRONG NUMBER.")
        else:
            message_label.config(text="PLEASE ENTER A 3-DIGIT NUMBER (BETWEEN 100 and 999). ")
    except ValueError:
        message_label.config(text="INVALID INPUT. PLEASE ENTER A 3-DIGIT NUMBER. ")

#To create the main app window
app = tk.Tk()
app.title("My Armstrong Number Checker")
app.geometry("400x200")

#To create and palce widgets
title_label = tk.Label(app, text="ENTER A 3-DIGIT NUMBER:")
title_label.pack(pady=10)

entry = tk.Entry(app)
entry.pack()

check_button = tk.Button(app, text="CHECK", command=check_number)
check_button.pack(pady=10)

message_label = tk.Label(app, text="")
message_label.pack()

#Start the main loop
app.mainloop()


if __name__=="__name__":
    app.run(debug=True)