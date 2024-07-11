import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("700x600")

outer_frame = tk.Frame(root, borderwidth=2, relief="groove")
outer_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

f1 = tk.Frame(outer_frame, borderwidth=0, highlightthickness=0)
f2 = tk.Frame(outer_frame, borderwidth=0, highlightthickness=0)
f3 = tk.Frame(outer_frame, borderwidth=0, highlightthickness=0)

tk.Label(f1, text="Child Frame 1").pack(fill="both", expand=True)
tk.Label(f2, text="Child Frame 2").pack(fill="both", expand=True)
tk.Label(f3, text="Child Frame 3").pack(fill="both", expand=True)

s1 = ttk.Separator(outer_frame, orient="horizontal")
# s2 = ttk.Separator(outer_frame, orient="horizontal")

f1.pack(side="top", fill="both", expand=True)
s1.pack(side="top", fill="x", expand=False)
f2.pack(side="top", fill="both", expand=True)
# s2.pack(side="top", fill="x", expand=False)
f3.pack(side="top", fill="both", expand=True)

root.mainloop()