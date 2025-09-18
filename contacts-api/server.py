from flask import Flask, jsonify, request

app = Flask(__name__)

next_id = "5"
contacts = [
    {"id":"1","name": "Alice", "phone": "123-456-7890"},
    {"id":"2","name": "Bob", "phone": "987-654-3210"},
    {"id":"3","name": "Charlie", "phone": "555-555-5555"},
    {"id":"4","name": "Diana", "phone": "444-444-4444"},
]

@app.route('/')
def home():
    return "<h1>Welcome to the Contacts API!</h1>"

@app.get("/contacts")
def list_all_contacts():
    return jsonify(contacts)

@app.get("/contacts/<id>")
def list_contacts(id):
    for contact in contacts:
        if contact["id"] == id:
            return contact
    return "that contact does not exist", 404

@app.post("/contacts")
def create_contact():
    global next_id
    new_contact = {
        "id": next_id,
        "name": request.json["name"],
        "phone": request.json["phone"]
    }
    contacts.append(new_contact)
    next_id = str(int(next_id) + 1) 

    print(request.json)
    return new_contact, 201

# GET /contacts ->list for all contacts
# GET /contacts/<id> -> get a specific contact 
# POST /contacts -> add a new contact

if __name__ == "__main__":
    app.run(debug=True)