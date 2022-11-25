from tkinter import *
from tkinter import ttk

# root properties
root = Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Learn Kanji!')
# label
label = ttk.Label(text="Select exam level:")
label.pack(fill=X, padx=5, pady=5)
selected_level = StringVar()
# level selection combobox
level_selection_cb = ttk.Combobox(root, textvariable=selected_level)
level_selection_cb['values'] = ('N2', 'N3', 'N4', 'N5')
level_selection_cb['state'] = 'readonly'
level_selection_cb.pack(fill=X, padx=5, pady=5)
# confirm button
confirm = ttk.Button(text="Confirm", command=root.destroy)
confirm.pack(fill=X, padx=5, pady=5)
root.mainloop()