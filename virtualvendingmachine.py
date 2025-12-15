# Virtual Vending Machine 
import tkinter as tk
import customtkinter as ctk
import time as t
from vendingmachineproducts import vm_products

# master frame, for creating general layout
class master_frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

# displays products, prices, and their ids
class vending_display(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)
        product_name_1 = "Cookie"
        product_id_price_1 = "100 - 2.00"
        
        product_name_2 = "Spicy Potato Chips"
        product_id_price_2 = "101 - 4.00"

        product_name_3 = "Cheesy Potato Chips"
        product_id_price_3 = "102 - 4.00"

        product_name_4 = "Cheese Nachos"
        product_id_price_4 = "103 - 4.00"

        product_name_5 = "Spicy Nachos"
        product_id_price_5 = "104 - 4.00"

        product_name_6 = "Chocolate Milk"
        product_id_price_6 = "105 - 2.00"

        product_name_7 = "Strawberry Milk"
        product_id_price_7 = "106 - 2.00"
        
        product_name_8 = "M & M's"
        product_id_price_8 = "107 - 4.00"

        product_name_9 = "Orange Juice"
        product_id_price_9 = "108 - 3.00"

        product_name_10 = "Chocolate Bar"
        product_id_price_10 = "109 - 4.00"

        product_name_11 = "Dark Chocolate Bar"
        product_id_price_11 = "110 - 4.00"

        product_name_12 = "Canned Ice Tea"
        product_id_price_12 = "111 - 2.00"

        product_name_13 = "Bottled Water"
        product_id_price_13 = "112 - 4.00"

        product_name_14 = "Packaged BLT Sandwich"
        product_id_price_14 = "113 - 4.00"

        product_name_15 = "Fruit Cake Slice"
        product_id_price_15 = "114 - 2.00"

        self.display_name_1 = ctk.CTkLabel(self, text = product_name_1)
        self.display_idprice_1 = ctk.CTkLabel(self, text = product_id_price_1)

        self.display_name_2 = ctk.CTkLabel(self, text = product_name_2)
        self.display_idprice_2 = ctk.CTkLabel(self, text = product_id_price_2)

        self.display_name_3 = ctk.CTkLabel(self, text = product_name_3)
        self.display_idprice_3 = ctk.CTkLabel(self, text = product_id_price_3)

        self.display_name_4 = ctk.CTkLabel(self, text = product_name_4)
        self.display_idprice_4 = ctk.CTkLabel(self, text = product_id_price_4)

        self.display_name_5 = ctk.CTkLabel(self, text = product_name_5)
        self.display_idprice_5 = ctk.CTkLabel(self, text = product_id_price_5)

        self.display_name_6 = ctk.CTkLabel(self, text = product_name_6)
        self.display_idprice_6 = ctk.CTkLabel(self, text = product_id_price_6)

        self.display_name_7 = ctk.CTkLabel(self, text = product_name_7)
        self.display_idprice_7 = ctk.CTkLabel(self, text = product_id_price_7)

        self.display_name_8 = ctk.CTkLabel(self, text = product_name_8)
        self.display_idprice_8 = ctk.CTkLabel(self, text = product_id_price_8)

        self.display_name_9 = ctk.CTkLabel(self, text = product_name_9)
        self.display_idprice_9 = ctk.CTkLabel(self, text = product_id_price_9)

        self.display_name_10 = ctk.CTkLabel(self, text = product_name_10)
        self.display_idprice_10 = ctk.CTkLabel(self, text = product_id_price_10)

        self.display_name_11 = ctk.CTkLabel(self, text = product_name_11)
        self.display_idprice_11 = ctk.CTkLabel(self, text = product_id_price_11)

        self.display_name_12 = ctk.CTkLabel(self, text = product_name_12)
        self.display_idprice_12 = ctk.CTkLabel(self, text = product_id_price_12)

        self.display_name_13 = ctk.CTkLabel(self, text = product_name_13)
        self.display_idprice_13 = ctk.CTkLabel(self, text = product_id_price_13)

        self.display_name_14 = ctk.CTkLabel(self, text = product_name_14)
        self.display_idprice_14 = ctk.CTkLabel(self, text = product_id_price_14)

        self.display_name_15 = ctk.CTkLabel(self, text = product_name_15)
        self.display_idprice_15 = ctk.CTkLabel(self, text = product_id_price_15)

        self.display_name_1.grid(row = 0, column = 0, padx = 5, pady = 2)
        self.display_idprice_1.grid(row = 1, column = 0, padx = 5, pady = 2)

        self.display_name_2.grid(row = 0, column = 1, padx = 5, pady = 2)
        self.display_idprice_2.grid(row = 1, column = 1, padx = 5, pady = 2)

        self.display_name_3.grid(row = 0, column = 2, padx = 5, pady = 2)
        self.display_idprice_3.grid(row = 1, column = 2, padx = 5, pady = 2)

        self.display_name_4.grid(row = 2, column = 0, padx = 5, pady = 2)
        self.display_idprice_4.grid(row = 3, column = 0, padx = 5, pady = 2)

        self.display_name_5.grid(row = 2, column = 1, padx = 5, pady = 2)
        self.display_idprice_5.grid(row = 3, column = 1, padx = 5, pady = 2)

        self.display_name_6.grid(row = 2, column = 2, padx = 5, pady = 2)
        self.display_idprice_6.grid(row = 3, column = 2, padx = 5, pady = 2)

        self.display_name_7.grid(row = 4, column = 0, padx = 5, pady = 2)
        self.display_idprice_7.grid(row = 5, column = 0, padx = 5, pady = 2)

        self.display_name_8.grid(row = 4, column = 1, padx = 5, pady = 2)
        self.display_idprice_8.grid(row = 5, column = 1, padx = 5, pady = 2)

        self.display_name_9.grid(row = 4, column = 2, padx = 5, pady = 2)
        self.display_idprice_9.grid(row = 5, column = 2, padx = 5, pady = 2)

        self.display_name_10.grid(row = 6, column = 0, padx = 5, pady = 2)
        self.display_idprice_10.grid(row = 7, column = 0, padx = 5, pady = 2)

        self.display_name_11.grid(row = 6, column = 1, padx = 5, pady = 2)
        self.display_idprice_11.grid(row = 7, column = 1, padx = 5, pady = 2)

        self.display_name_12.grid(row = 6, column = 2, padx = 5, pady = 2)
        self.display_idprice_12.grid(row = 7, column = 2, padx = 5, pady = 2)

        self.display_name_13.grid(row = 8, column = 0, padx = 5, pady = 2)
        self.display_idprice_13.grid(row = 9, column = 0, padx = 5, pady = 2)

        self.display_name_14.grid(row = 8, column = 1, padx = 5, pady = 2)
        self.display_idprice_14.grid(row = 9, column = 1, padx = 5, pady = 2)

        self.display_name_15.grid(row = 8, column = 2, padx = 5, pady = 2)
        self.display_idprice_15.grid(row = 9, column = 2, padx = 5, pady = 2)

# selection mechanism for choosing and buying items
class vending_selector(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)
        
        def get_product_id(product_id):
            key = str(product_id).upper().strip()
            return vm_products.get(key)

        def select_product_id():
            pid = id_var.get()
            sel = get_product_id(pid)
            id_var.set("")
            if sel:
                status = f"{sel['name']} — ${sel['price']:.2f}"
                self.result_label.configure(text=status)
            else:
                status = "Product not found"
                self.result_label.configure(text=status)
        
        id_var = tk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable = id_var)

        self.button1 = ctk.CTkButton(self, text = "1", command = lambda:self.entry.insert('end', '1'))
        self.button2 = ctk.CTkButton(self, text = "2", command = lambda:self.entry.insert('end', '2'))
        self.button3 = ctk.CTkButton(self, text = "3", command = lambda:self.entry.insert('end', '3'))
    
        self.button4 = ctk.CTkButton(self, text = "4", command = lambda:self.entry.insert('end', '4'))
        self.button5 = ctk.CTkButton(self, text = "5", command = lambda:self.entry.insert('end', '5'))
        self.button6 = ctk.CTkButton(self, text = "6", command = lambda:self.entry.insert('end', '6'))

        self.button7 = ctk.CTkButton(self, text = "7", command = lambda:self.entry.insert('end', '7'))
        self.button8 = ctk.CTkButton(self, text = "8", command = lambda:self.entry.insert('end', '8'))
        self.button9 = ctk.CTkButton(self, text = "9", command = lambda:self.entry.insert('end', '9'))

        self.button0 = ctk.CTkButton(self, text = "0", command = lambda:self.entry.insert('end', '0'))
        self.button_ok = ctk.CTkButton(self, text = "Ok", command = select_product_id)
        self.button_del = ctk.CTkButton(self, text = "X", command = lambda:self.entry.delete(0, 'end'))

        self.button1.configure(height = 25, width = 70)
        self.button2.configure(height = 25, width = 70)
        self.button3.configure(height = 25, width = 70)

        self.button4.configure(height = 25, width = 70)
        self.button5.configure(height = 25, width = 70)
        self.button6.configure(height = 25, width = 70)

        self.button7.configure(height = 25, width = 70)
        self.button8.configure(height = 25, width = 70)
        self.button9.configure(height = 25, width = 70)

        self.button0.configure(height = 25, width = 70)
        self.button_ok.configure(height = 25, width = 70)
        self.button_del.configure(height = 25, width = 70) 

        self.entry.grid(row = 4, column = 1, padx = 2, pady = 2)

        self.button1.grid(row = 0, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button2.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button3.grid(row = 0, column = 2, padx = 2, pady = 5, sticky = "s")

        self.button4.grid(row = 1, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button5.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button6.grid(row = 1, column = 2, padx = 2, pady = 5, sticky = "s")

        self.button7.grid(row = 2, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button8.grid(row = 2, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button9.grid(row = 2, column = 2, padx = 2, pady = 5, sticky = "s")

        self.button0.grid(row = 3, column = 1, padx = 2, pady = 5, sticky = "s")
        self.button_ok.grid(row = 3, column = 0, padx = 2, pady = 5, sticky = "s")
        self.button_del.grid(row = 3, column = 2, padx = 2, pady = 5, sticky = "s") 

        def purchase_func():
            self.result_label.configure(text = "purchase successful!")
            self.dispenser_state.set("Collect your item here.")
            return self.dispenser_state.get()
            
            
        self.result_label = ctk.CTkLabel(self, text = "")
        self.result_label.grid(row = 8, column = 1, padx = 2, pady = 2)

        credit_card = 150

        wallet_label = f"{'Credit Balance: '}{int(credit_card)}"
        self.wallet = ctk.CTkLabel(self, text = wallet_label)
        self.vert_pad = ctk.CTkLabel(self, text = "")
        self.receipt = ctk.CTkLabel(self, text = "placeholder")
        self.buy = ctk.CTkButton(self, text = "Purchase", command = purchase_func)

        self.vert_pad.grid(row = 5, column = 1, padx = 0, pady = 5, sticky = "nsew")
        self.wallet.grid(row = 6, column = 1, padx = 0, pady = 5, sticky = "nsew")
        self.buy.grid(row = 7, column = 1, padx = 0, pady = 5, sticky = "nsew")

        self.update_idletasks()
        t.sleep(2)

# dispenses purchased items
class vending_dispenser(ctk.CTkFrame):
    def __init__(self, master_frame, **kwargs):
        super().__init__(master_frame, **kwargs)

        def collect_item():
            self.dispenser_state.set("No item purchased yet.")
            return self.dispenser_state.get()
        
        self.dispenser_state = tk.StringVar("No item purchased yet.")
        self.dispenser = ctk.CTkButton(self, textvariable = self.dispenser_state, command = collect_item)

        self.dispenser.grid(row = 0, column = 0, padx = 115, pady = 75, sticky = "nsew")

        collect_item(self)

# lays out all the frames in the window
class App(ctk.CTk):
    def __init__(self):    
        super().__init__()
    
        self.title("Vending Machine Simulator")

        self.Master_Frame = master_frame(master = self, height = 2700, width = 2700, corner_radius = 0, fg_color = "transparent")
        self.Master_Frame.grid(row = 0, column = 0, sticky = "nsew")

        self.display = vending_display(self.Master_Frame)
        self.display.grid(row = 0, column = 0, sticky = "nw")

        self.selector = vending_selector(self.Master_Frame)
        self.selector.grid(row = 0, column = 1, sticky = "nse")

        self.dispenser = vending_dispenser(self.Master_Frame)
        self.dispenser.grid(row = 1, column = 0, sticky = "sew")

app = App()
app.mainloop()
