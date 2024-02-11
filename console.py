#!/usr/bin/python3
"""AirBnB console"""


import json
import re
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Ensures nothing is executed when an empty line is passed"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class and saves it"""
        if arg:
            args_list = arg.split()
            class_dicts = {'BaseModel': BaseModel,
                           'User': User,
                           'Place': Place,
                           'Review': Review,
                           'City': City,
                           'Amenity': Amenity,
                           'State': State,
                           }
            my_instance = None
            for key in class_dicts:
                if args_list[0] == key:
                    my_instance = class_dicts[key]()
            if my_instance is not None:
                my_instance.save()
                print(my_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Shows an instance using its ID"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
            if args_list[0] not in available_classes:
                print("** class doesn't exist **")
                return
            if len(args_list) == 1:
                print("** instance id missing **")
                return
            key_name = f'{args_list[0]}.{args_list[1]}'
            if key_name not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key_name])
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Destroys an instance using its ID"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
            if args_list[0] not in available_classes:
                print("** class doesn't exist **")
                return
            if len(args_list) == 1:
                print("** instance id missing **")
                return
            key_name = f'{args_list[0]}.{args_list[1]}'
            if key_name not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key_name]
                models.storage.save()
        else:
            print("** class name missing **")

    def do_all_list(self, arg):
        """return all instances of a certain class or simply all instances"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
            if arg not in available_classes:
                print("** class doesn't exist **")
                return
            all_list = []
            for key, val in models.storage.all().items():
                if arg == key[0:len(args_list[0])]:
                    all_list.append(str(val))
        else:
            all_list = []
            for key, val in models.storage.all().items():
                all_list.append(str(val))
        return all_list

    def do_all(self, arg):
        """Print all instances of a certain class"""
        all_list = self.do_all_list(arg)
        if all_list is not None:
            print(all_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
            if args_list[0] not in available_classes:
                print("** class doesn't exist **")
                return
            if len(args_list) == 1:
                print("** instance id missing **")
                return
            key_name = f'{args_list[0]}.{args_list[1]}'
            if key_name not in models.storage.all():
                print("** no instance found **")
            elif len(args_list) == 2:
                print("** attribute name missing **")
            elif len(args_list) == 3:
                print("** value missing **")
            else:
                if args_list[3][0] == "'" or args_list[3][0] == '"':
                    args_list[3] = args_list[3][1:(len(args_list[3]) - 1)]
                setattr(models.storage.all()[key_name], str(args_list[2]),
                        str(args_list[3]))
                models.storage.save()
        else:
            print("** class name missing **")

    def default(self, arg):
        arg = arg.strip()
        args = arg.split()
        commands_list = args[0].split('.')
        if len(commands_list) == 1:
            print(f'*** Unknown syntax: {arg}')
            return
        func = commands_list[1]
        if func == 'all()':
            self.do_all(commands_list[0])
        elif func == 'count()':
            print(len(self.do_all_list(commands_list[0])))
        elif func[0:4] == 'show':
            arg = commands_list[0] + ' ' + func[6:-2]
            self.do_show(arg)
        elif func[0:7] == 'destroy':
            arg = commands_list[0] + ' ' + func[9:-2]
            self.do_destroy(arg)
        elif func.split('(')[0] == 'update':
            pattern = r"update\((.*?)\)"
            match = re.search(pattern, arg.split('.')[1])
            if match:
                elements_str = match.group(1)
                elements_list = [elem.strip().strip("'\"")
                                 for elem in elements_str.split(',')]
            else:
                elements_list = None
            if elements_list is None or elements_list == ['']:
                self.do_update(commands_list[0])
            else:
                if len(elements_list) > 1 and elements_list[1][0] == '{':
                    my_str = ''
                    for i in range(1, len(elements_list)):
                        my_str += elements_list[i] + "', '"
                    my_str = my_str[:-4]
                    string = ''
                    for ch in my_str:
                        if ch == "'":
                            string += '"'
                        else:
                            string += ch
                    dict_rep = json.loads(string)
                    for key, val in dict_rep.items():
                        arg = commands_list[0] + ' ' + elements_list[0]
                        arg += ' ' + str(key) + ' ' + str(val)
                        self.do_update(arg)
                else:
                    self.do_update(" ".join([commands_list[0]] +
                                            elements_list))
        else:
            print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
