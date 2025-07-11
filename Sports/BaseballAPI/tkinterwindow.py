from tkinter import *

root = Tk()
root.title("Today's MLB Games")
root.geometry("800x650")
#root.configure(bg="green")

schedule = open("todaysgames.txt", "r")
content = schedule.read()       

my_text = Text(root, width=100, height=100, font=("Helvetica", 20))
my_text.pack(expand=True, fill="both",pady=60)
my_text.tag_configure("center", justify='center')
my_text.insert(END, content)
my_text.tag_add("center", "1.0", "end")

root.mainloop()
