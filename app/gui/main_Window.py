from tkinter import messagebox
from app.db.orders import insert_order,get_all_order_data

def handle_add(name_entry, product_entry, qty_entry, price_entry, tree):
    try:
        name = name_entry.get().strip()
        product = product_entry.get().strip()
        quantity = int(qty_entry.get())
        price = float(price_entry.get())

        if not name or not product or quantity < 0 or price < 0:
            raise ValueError("All fields are required and must be valid.")

        insert_order(name, product, quantity, price)
        refresh_table(tree)

        name_entry.delete(0, 'end')
        product_entry.delete(0, 'end')
        qty_entry.delete(0, 'end')
        price_entry.delete(0, 'end')

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def refresh_table(tree):
    for row in tree.get_children():
        tree.delete(row)
    for order in get_all_order_data():
        tree.insert("", "end", values=order)

