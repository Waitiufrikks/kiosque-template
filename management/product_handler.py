from menu import products


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

add_product(products,
        description= "Healthy breakfast with cottage cheese and strawberry",
        price= 14.05,
        rating= 1,
        title= "Breakfast with cottage",
        type= "fruit")

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
