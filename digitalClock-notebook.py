{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1215c310-ac6c-497c-bdfa-dcaf0ab2c098",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "%config IPCompleter.greedy=True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30179e74-6430-4bf7-81f2-fabd2760675f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# reference techTFQ for Git tutorial\n",
    "# https://www.youtube.com/watch?v=kY5HtrkjSj0 , 17:43\n",
    "from tkinter import Tk, Label\n",
    "\n",
    "\n",
    "window = Tk()\n",
    "window.title(\"Digital Clock\")\n",
    "window.geometry(\"600x300\")\n",
    "window.configure(bg=\"steelblue\")\n",
    "\n",
    "label = Label(window, text=\"Welcome!\", font=(\"Arial Black\", 78, \"bold\"),bg=\"steelblue\",fg=\"white\")\n",
    "label.pack(pady=100)\n",
    "\n",
    "\n",
    "window.mainloop()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
