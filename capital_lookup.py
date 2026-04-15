# A dictionary storing 10 African countries and their capitals
african_capitals = {
    "Nigeria": "Abuja",
    "Egypt": "Cairo",
    "Kenya": "Nairobi",
    "South Africa": "Pretoria",
    "Ghana": "Accra",
    "Morocco": "Rabat",
    "Senegal": "Dakar",
    "Tanzania": "Dodoma",
    "Uganda": "Kampala",
    "Rwanda": "Kigali"
}

query = input("Enter an African country to find its capital: ").strip().title()

if query in african_capitals:
    print(f"The capital of {query} is {african_capitals[query]}.")
else:
    print(f"Sorry, {query} is not in our current records.")
