#!/usr/bin/python3
"""Command Interpreter Module"""
import cmd


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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
