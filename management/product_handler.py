from menu import products
from collections import Counter
import math


def add_product(menu,**new_product):
   new_id  = 0
   max_id = 0
   if len(menu) != 0:
      for item in menu:
         max_id = item.get('_id', 0)
         new_id = max_id 
   new_product["_id"] = new_id + 1
   menu.append(new_product)
   
   return new_product

def get_product_by_id(id: int):
   if type(id) != int:
      raise TypeError ("product id must be an int")
    
   for item in products:
        if item['_id'] == id:
            return item

   return {}  
     
def get_products_by_type (tag: str):
   list_for_tags = []

   if type(tag) != str:
      raise TypeError ("product type must be a str")
      
   for items in products:
      if items['type'] == tag:
         list_for_tags.append(items)
   return list_for_tags
     

def menu_report ():
   prices_items = []
   types_items = []

   for item in products:
     prices_items.append(item["price"])
     types_items.append(item["type"])

   counter_type = Counter(types_items)
   most_common_type = counter_type.most_common(1)[0][0]
   
   total_in_menu = len(products) 
   test = sum([product["price"] for product in products])
   total_price_menu = round((test/total_in_menu),2)
   return f"Products Count: {total_in_menu} - Average Price: ${total_price_menu} - Most Common Type: {most_common_type}"