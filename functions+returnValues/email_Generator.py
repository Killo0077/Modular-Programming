# Exercise 2 — Email Generator

# Create a function that returns an email address.

def create_email (first: str, last: str) -> str:
    email = f"{first} . {last}@email.com "

    return email

if __name__ == "__main__":
    print(create_email("Pablo","Baena"))