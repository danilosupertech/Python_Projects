from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["contact_manager"]
contacts = db["contacts"]

def menu():
    print("\n--- CONTACT MANAGER ---")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact by name")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.insert_one({"name": name, "phone": phone, "email": email})
    print("✅ Contact added.")

def list_contacts():
    for c in contacts.find():
        print(f"- {c['name']} | {c['phone']} | {c['email']}")

def search_contact():
    name = input("Search name: ")
    result = contacts.find_one({"name": name})
    if result:
        print(f"📇 {result['name']} | {result['phone']} | {result['email']}")
    else:
        print("❌ Contact not found.")

def update_contact():
    name = input("Name of contact to update: ")
    contact = contacts.find_one({"name": name})
    if contact:
        new_phone = input("New phone: ")
        new_email = input("New email: ")
        contacts.update_one(
            {"name": name},
            {"$set": {"phone": new_phone, "email": new_email}}
        )
        print("✅ Contact updated.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Name of contact to delete: ")
    result = contacts.delete_one({"name": name})
    if result.deleted_count > 0:
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

# Menu loop
while True:
    menu()
    option = input("Choose: ")
    if option == "1":
        add_contact()
    elif option == "2":
        list_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        update_contact()
    elif option == "5":
        delete_contact()
    elif option == "6":
        break
    else:
        print("Invalid option.")
