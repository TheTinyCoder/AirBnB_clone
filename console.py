#!/usr/bin/python3
"""Command Interpreter Module"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Implements functions from cmd"""
    prompt = ("(hbnb)")

    def do_quit(self, line):
        """Exits the program on quit"""
        return True

    def do_EOF(self, line):
        """Exits the program after SIGQUIT: CTRL + D"""
        return True

    def emptyline(self):
        """Executes nothing if line is empty on enter"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        saves to JSON file and prints to console
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in list(models.classes.keys()):
            print("** class doesn't exist **")
        else:
            model = models.classes[line]()
            print(model.id)
            model.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in list(models.classes.keys()):
            print("** class doesn't exist **")
        elif args[1] is None:
            print("** instance id missing **")
        elif ".".join(args) not in models.storage.all():
            print("** no instance found **")
        else:
            print(self.storage.all()[".".join(args)])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in list(models.classes.keys()):
            print("** class doesn't exist **")
        elif args[1] is None:
            print("** instance id missing **")
        elif ".".join(args) not in models.storage.all():
            print("** no instance found **")
        else:
            self.storage.all().pop(".".join(args))
            self.storage.save()

    def do_all(self, line):
        args = line.split(' ')
        if len(args) == 1:
            for v in self.storage.all().values():
                print(v)
        else:
            if args[1] not in list(models.classes.keys()):
                print("** class doesn't exist **")
            else:
                for (k, v) in self.storage.all().items():
                    if args[1] in k:
                        print(v)

    def do_update(self, line):
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in list(models.classes.keys()):
            print("** class doesn't exist **")
        elif args[1] is None:
            print("** instance id missing **")
        elif ".".join(args[:2]) not in models.storage.all():
            print("** no instance found **")
        elif args[2] is None:
            print("** attribute name id missing **")
        elif args[3] is None:
            print("** value missing **")
        else:
            self.storage.all()[".".join(args[:2])][args[2]] = args[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
