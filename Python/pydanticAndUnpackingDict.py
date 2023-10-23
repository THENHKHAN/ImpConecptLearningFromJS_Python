from pydantic import BaseModel

# Define the User Pydantic model
class User(BaseModel):
    id: int
    name: str
    email: str

# JSON data as a dictionary
user_data = {
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}

# Parse JSON data into a User object
user = User(**user_data)

# Access attributes of the User object
print(user.id)    # Output: 1
print(user.name)  # Output: "John"
print(user.email) # Output: "john@example.com"
