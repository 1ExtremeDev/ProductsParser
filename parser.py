import json
from os import error

docs = {
    "elipsis": False,
    "set": set()
}

class Products:
    def __init__(self, action=None, values=None) -> None:
        if values is None or action not in ["add", "remove", "edit"] or action is None: return None 
        self.values = values; self.action = action
        if self.action.lower() == 'add': self.add()
        elif self.action.lower() == 'remove': self.remove()
        elif self.action.lower() == 'edit': self.edit()

    def add(self):
        self.id = self.values['id']
        before = json.load(open('products.json'))
        try: before[str(self.id)]; self.error = True
        except:
            before[str(self.id)] = {
                "id": self.id,
                "details": self.values['details'],
                "picture": self.values['picture'],
                "price": self.values['price'],
                "name": self.values['name']       
            }
            try:
                open('products.json', 'w').write(json.dumps(before, indent=4, sort_keys=True))
                self.error = False
            except:
                self.error = True

    def remove(self):
        self.id = self.values['id']
        before = json.load(open('products.json'))
        try: 
            del before[str(self.id)]
            try:
                open('products.json', 'w').write(json.dumps(before, indent=4, sort_keys=True))
                self.error = False
            except:
                self.error = True
        except:
            self.error = True
    def edit(self):
        self.id = self.values['id']
        before = json.load(open('products.json'))
        try: 
            before[str(self.id)] = self.values
            try:
                open('products.json', 'w').write(json.dumps(before, indent=4, sort_keys=True))
                self.error = False
            except:
                self.error = True
        except:
            self.error = True
Products(action='add', values={
    "id": 7,
    "details": "Z",
    "picture": "https://picture.com/",
    "price": 100,
    "name": "Product Name"
})
