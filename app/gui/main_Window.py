# Darsan Sabu George 
# 2025-04-16
# PROG2390 
# 8959922

from tkinter import messagebox
from app.db.orders import insert_order,get_all_order_data

def handle_add(name_box, product_box, quantity_box, price_box, tree):
    try:
        name = name_box.get().strip()
        product = product_box.get().strip()
        quantity = int(quantity_box.get())
        price = float(price_box.get())

        if not name or not product or quantity < 0 or price < 0:
            raise ValueError("All fields are requiread .")

        insert_order(name, product, quantity, price)
        
        refresh_table(tree)
        
        name_box.delete(0, 'end')
        product_box.delete(0, 'end')
        quantity_box.delete(0, 'end')
        price_box.delete(0, 'end')

    except Exception as e:
        messagebox.showerror("Input Errore", str(e))

def refresh_table(tree):
    for row in tree.get_children():
        tree.delete(row)
    for order in get_all_order_data():
        tree.insert("", "end", values=order)

