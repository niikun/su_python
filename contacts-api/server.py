from flask import Flask, jsonify

app = Flask(__name__)

contacts = [
    {"name": "Alice", "phone": "123-456-7890"},
    {"name": "Bob", "phone": "987-654-3210"},
    {"name": "Charlie", "phone": "555-555-5555"},
    {"name": "Diana", "phone": "444-444-4444"},
]

@app.route('/')
def home():
    return "<h1>Welcome to the Contacts API!</h1>"

@app.get("/contacts")
def list_all_contacts():
    return jsonify(contacts)

@app.get("/contacts/<name>")
def list_contacts(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return jsonify(contact)
    return jsonify({"error": "Contact not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)