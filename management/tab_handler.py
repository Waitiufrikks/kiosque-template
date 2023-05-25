from menu import products

def calculate_tab(table):
    sub_total = 0  
    for item in table:
        item_selected = item["_id"]
        amount_item = item["amount"]
        for items_menu in products:
            if items_menu["_id"] == item_selected:
                total_table = amount_item * items_menu["price"]
                sub_total += total_table

    return {"subtotal": f"${round(sub_total,2)}"}

   