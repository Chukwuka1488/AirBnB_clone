#!/usr/bin/python3
"""Creating console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Use a dictionary to map string class names to their respective classes
CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """HBNB command line interpreter"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        args_list = args.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            new_instance = CLASSES[args_list[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = args.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args_list = args.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances"""
        args_list = args.split()
        if not args:
            print([str(value) for value in storage.all().values()])
        elif args_list[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items() if args_list[0] in key])

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args_list = args.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args_list[0], args_list[1])
            if key in storage.all():
                setattr(storage.all()[key], args_list[2], args_list[3].strip("\""))
                storage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """Method called on an unrecognized command."""
        parts = line.split(".")
        if len(parts) == 2:
            class_name, remainder = parts
            if class_name in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                method_parts = remainder.split("(")
                if len(method_parts) == 2:
                    method_name, args_string = method_parts
                    args = args_string[:-1].split(",")  # Removing closing bracket and splitting by comma

                    if method_name == "show":
                        self.do_show(class_name + " " + args[0].strip("\""))
                    elif method_name == "all":
                        self.do_all(class_name)
                    elif method_name == "count":
                        self.do_count(class_name)
                    elif method_name == "destroy":
                        self.do_destroy(class_name + " " + args[0].strip("\""))
                    elif method_name == "update":
                        if len(args) == 2:  # This handles the dictionary representation update
                            instance_id = args[0].strip("\"")
                            try:
                                # Parse the dictionary string into a dictionary
                                update_dict = eval(args[1])
                                if isinstance(update_dict, dict):
                                    for key, value in update_dict.items():
                                        str_args = "{} {} {} {}".format(class_name, instance_id, key, value)
                                        self.do_update(str_args)
                                else:
                                    print("** value must be a dictionary **")
                            except Exception:
                                print("** value must be a dictionary **")
                        elif len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            str_args = "{} {} {} {}".format(class_name, args[0].strip("\""), args[1].strip("\""), args[2].strip("\""))
                            self.do_update(str_args)
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_count(self, class_name):
        """Counts the number of instances of a specified class."""
        count = sum(1 for key in storage.all().keys() if class_name in key)
        print(count)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
