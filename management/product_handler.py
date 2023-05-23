from menu import products
def get_product_by_id (id):
   for items in products:
      if items['_id'] == id:
         return items
   return {}      
     
item_id_found = get_product_by_id(10)

def get_products_by_type (type):
   list_for_tags = []
   for items in products:
      if items['type'] == type:
         list_for_tags.append(items)
   return list_for_tags
     
item_tag_found = get_products_by_type('bakery')