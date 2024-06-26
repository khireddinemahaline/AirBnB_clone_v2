#!/usr/bin/env python3
"""consle.py
----to start the file : ./console.py"""


from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb)"

    def do_create(self, args):
        """Create new instance"""
        if len(args) < 2:
            print('** class name missing **')
        else:
            try:
                new = eval(args)()
                print(new.id)
                models.storage.save()
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
                pass
        return

    def do_show(self, args):
        """string representation based on the class name and id"""
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            keyU = arg[0] + '.' + str(arg[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, args):
        """Destroy an instance"""
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif arg[0] not in models.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            keyU = arg[0] + '.' + str(arg[1])
            if keyU in dic:
                del dic[keyU]
                models.storage.save()
            else:
                print("** no instance found **")
        return

    def do_all(self, args):
        """show all instance"""
        arg = shlex.split(args)
        list_all = []
        dic = models.storage.all()
        if len(arg) == 0:
            for key in dic:
                class_represntation = str(dic[key])
                list_all.append(class_represntation)
            print(list_all)
            return
        if arg[0] not in models.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                class_name = key.split('.')
                if class_name[0] == arg[0]:
                    class_represntation = str(dic[key])
                    list_all.append(class_represntation)
            print(list_all)
        return

    def do_update(self, args):
        """Updates an instance based on the class name and id """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        elif arg[0] not in models.classes:
            print("** class doesn't exist **")
            return
        key = arg[0] + '.' + arg[1]
        dic = models.storage.all()
        try:
            obj = dic[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            ins_one = type(getattr(obj, arg[2]))
            arg[3] == ins_one(arg[3])
        except AttributeError:
            pass
        setattr(obj, arg[2], arg[3])
        models.storage.save()
        return

    def do_quit(self, arg):
        """quit"""
        return True

    def do_EOF(self, args):
        """handel EOF"""
        return True

    def emptyline(self):
        """No action"""
        pass


if __name__ == '__main__':
    """HBNBCommand()"""
    HBNBCommand().cmdloop()
