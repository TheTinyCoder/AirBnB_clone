#!/usr/bin/python3
"""Command Interpreter Module"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Implements functions from cmd"""
    prompt = ("(hbnb) ")

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
        if not line:
            print("** class name missing **")
            return
        try:
            model = models.classes[line]()
            model.save()
            print(model.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            print(models.storage.all()[".".join(args)])
        except Exception:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ".".join(args) not in models.storage.all():
            print("** no instance found **")
        else:
            models.storage.all().pop(".".join(args))
            models.storage.save()

    def do_all(self, line):
        if not line:
            for v in list(models.storage.all().values()):
                print(v)
        else:
            args = line.split(' ')
            if args[0] not in models.classes:
                print("** class doesn't exist **")
            else:
                for (k, v) in models.storage.all().items():
                    if args[0] in k:
                        print(v)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in list(models.classes.keys()):
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif ".".join(args[:2]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) <= 2:
            print("** attribute name missing **")
        elif len(args) <= 3:
            print("** value missing **")
        else:
            setattr(
                models.storage.all()[".".join(args[:2])], args[2], args[3])
            models.storage.save()

    def default(self, line):
        methods = {"all": self.do_all, "show": self.do_show,
                   "destroy": self.do_destroy, "update": self.do_update}
        args = line.split('.')
        model = args[0]
        args1 = args[1].split('(')
        method = args1[0]
        arguments = args1[1].replace(')', '').replace(',', '')
        if model in models.classes and method in methods:
            if len(arguments) == 0:
                methods[method](model)
            else:
                methods[method](model + " " + arguments)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
