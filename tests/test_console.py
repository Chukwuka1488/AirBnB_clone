#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()

# Testing "show" command
print("-- Reloaded objects with 'show' command --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd(f"{obj.__class__.__name__}.show(\"{obj.id}\")")
    std_output = f.getvalue().strip()
    print(std_output)

# Testing "create" command
print("-- Create a new User with 'create' command --")
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("create User")
std_output = f.getvalue().strip()
print(f"[User] ({std_output})")  # Print the ID of the created User

# Assuming you have set attributes feature in "update" command
print("-- Update user attributes with 'update' command --")
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd(f"User.update(\"{std_output}\", \"first_name\", \"Betty\")")
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd(f"User.update(\"{std_output}\", \"last_name\", \"Bar\")")
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd(f"User.update(\"{std_output}\", \"email\", \"airbnb@mail.com\")")
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd(f"User.update(\"{std_output}\", \"password\", \"root\")")

# Display the created and updated User
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd(f"User.show(\"{std_output}\")")
std_output = f.getvalue().strip()
print(std_output)
