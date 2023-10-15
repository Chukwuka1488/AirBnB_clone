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


class HBNBCommand(cmd.Cmd):
    """HBNB command line interpreter"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        args_list = arg.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args_list[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = args.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
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
        elif args_list[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
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
        elif args_list[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items() if args_list[0] in key])

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args_list = args.split()
        if not args:
            print("** class name missing **")
        elif args_list[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
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
        args = line.split(".")
        if len(args) == 2:
            class_name, method_name = args[0], args[1]

            if method_name == "all()":
                if class_name in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                    self.do_all(class_name)
                else:
                    print("** class doesn't exist **")

            elif method_name == "count()":
                if class_name in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
                    self.do_count(class_name)
                else:
                    print("** class doesn't exist **")

            else:
                print("*** Unknown syntax: {}".format(line))

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
