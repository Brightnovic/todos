def find_item_list(list, cb):
     
    for item , index in enumerate(list):
        if cb(index, item,list):  
            return item
        
""" 
item = [
    {"name": "bright", "email": "bright"},
    {"name": "bright", "email": "bright"},
    {"name": "bright", "email": "bright"},
    {"name": "div", "email": "bright"},
]



def get_name_obi(value,index,array):
    return value.get("name") == "div"

res = find_item_list(item, get_name_obi)
print(res) """