# try again, from techTFQ tutorial about Git
# from YouTube https://www.youtube.com/watch?v=kY5HtrkjSj0

from tkinter import Tk, Label

window = Tk()
window.geometry("600x300")
window.title("Digital Clock")
window.config(bg="steelblue")

label = Label(window, text="Welcome", font=("Arial Black",78,"bold"), bg="steelblue",fg="white")
label.pack(pady=100)
#testing
window.mainloop()
