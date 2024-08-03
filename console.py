#!/usr/bin/env python3
"""consle.py
----to start the file : ./console.py"""
from models import storage
from models.base_model import BaseModel
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
            models.storage.new(obj)
            print(obj.id)
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

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
        """ Shows all objects, or all objects of a class"""
        """show all instance"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in models.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(args).items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all(args).items():
                print_list.append(str(v))
        print('[%s]' % ', '.join(print_list))  # Fixed syntax error

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
