#!/usr/bin/python3
"""Command Interpreter Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Implements functions from cmd"""
    def do_quit(self, line):
        return True
    def do_EOF(self, line):
        return True
    def prompt = "(hbnb)"
    def emptyline():
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
