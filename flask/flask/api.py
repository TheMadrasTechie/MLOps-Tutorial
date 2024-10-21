### Put and Delete-HTTP Verbs
### Working With API's--Json

from flask import Flask, jsonify, request

app = Flask(__name__)

##Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
    {"id": 4, "name": "Item 4", "description": "This is item 4"},
    {"id": 5, "name": "Item 5", "description": "This is item 5"},
    {"id": 6, "name": "Item 6", "description": "This is item 6"},
    {"id": 7, "name": "Item 1231", "description": "This is item 134"},
    {"id": 8, "name": "Item 2qwe", "description": "This is item 232"},
    {"id": 9, "name": "Item 3qew", "description": "This is item 3121"},
    {"id": 10, "name": "Item qwe4", "description": "This is item 4212"},
    {"id": 11, "name": "Item 5qwe", "description": "This is item 512"},
    {"id": 12, "name": "Item 6qe", "description": "This is item 61"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"

## Get: Retrieve all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retireve a specific item by Id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## Post :create a new task- API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]


    }
    items.append(new_item)
    return jsonify(new_item)

# Put: Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id): 
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})


if __name__ == '__main__':
    print("Samples \n This workss well and gives us the reults.")
    app.run(debug=True)
