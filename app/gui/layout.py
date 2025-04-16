# Darsan Sabu George 
# 2025-04-16
# PROG2390 
# 8959922

import tkinter as tk
from tkinter import ttk
# from db.orders import create_orders_DB
from app.db.orders import create_orders_DB
from app.gui.main_Window import handle_add, refresh_table

#\

def get_gui():
    global name_box, product_box, quantity_box, price_box, tree

    root = tk.Tk()
    root.title("Customer Orders Management System")
    root.geometry("950x400")

    create_orders_DB()

    form = tk.Frame(root)
    form.pack(pady=10)

    tk.Label(form, text="Customer Name").grid(row=0, column=0)
    name_box = tk.Entry(form)
    name_box.grid(row=1, column=0)

    tk.Label(form, text="Product").grid(row=0, column=1)
    product_box = tk.Entry(form)
    product_box.grid(row=1, column=1)

    tk.Label(form, text="Quantity").grid(row=0, column=2)
    quantity_box = tk.Entry(form)
    quantity_box.grid(row=1, column=2)

    tk.Label(form, text="Price").grid(row=0, column=3)
    price_box = tk.Entry(form)
    price_box.grid(row=1, column=3)

    tk.Button(form, text="Add Order", command=lambda: handle_add(
        name_box, product_box, quantity_box, price_box, tree)).grid(row=1, column=4, padx=10)

# on screen items.
    columns = ("ID", "Customer", "Product", "Qty", "Price", "Date")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.pack(fill="both", expand=True)

# refresh 
    refresh_table(tree)
    root.mainloop()
