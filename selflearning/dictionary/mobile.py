# Dictionary of contacts
contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display contact names in alphabetical order
print("Contacts in alphabetical order:")
for name in sorted(contacts):
    print(name)

# Count total contacts
print("\nTotal contacts:", len(contacts))

# Search for a contact
search_name = input("\nEnter contact name to search: ")

for name in contacts:
    if name == search_name:
        print("Contact Found:", name, "-", contacts[name])
        break
else:
    print("Contact not found")

# Create a list of contacts starting with a vowel
vowel_contacts = []

for name in contacts:
    if name[0].lower() in "aeiou":
        vowel_contacts.append(name)

print("\nContacts starting with a vowel:")
print(vowel_contacts)