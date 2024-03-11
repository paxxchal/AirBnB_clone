#!/usr/bin/python3
"""AirBnB clone console."""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command-line interpreter for AirBnB clone."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the console."""
        print()
        sys.exit()

    def do_quit(self, line):
        """Exit the console."""
        sys.exit()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
