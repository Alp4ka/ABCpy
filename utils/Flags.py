import typing

FLAG_IDENTIFIER = '-'

class FlagHandler:
    def __init__(self, known_flags: 'list[Flag]'):
        self.known_flags = known_flags
    # -i value_i -o value_o
    def from_args(self, args):
        for flag in self.known_flags:
            flag.get_from_args(args)

    def activate_all(self):
        for flag in self.known_flags:
            flag.activate()

    def handle_all(self):
        for flag in self.known_flags:
            flag.handle()


class Flag:
    def __init__(self, representation:str, value: typing.Any = None, activator: typing.Callable = None, state: bool = False):
        self.representation = representation
        self.prefix = FLAG_IDENTIFIER
        self.state = state
        self.value = value
        self.activator = activator  # function we have to call in case we want to activate this flag.

    @staticmethod
    def get_by_type(item: str) -> typing.Union[int, str]:
        try:
            item = int(item)
            return item
        except:
            return item

    def get_from_args(self, args) -> bool:  # True in case flag found.
        index = -1
        for arg_i in range(len(args)):
            if(args[arg_i] == f"{self.__str__()}"):
                index = arg_i
                break
        check_size = (len(args) - index > 1)
        if index > -1 and check_size:
            self.state = True
            self.value = Flag.get_by_type(args[arg_i+1])
        else:
            self.state = False
            self.value = None
            return False

    def set_activator(self, activator: typing.Callable):
        self.activator = activator

    # TODO: global exception is not really correct.
    def activate(self):
        if self.activator != None:
            self.activator(self.value)


    def handle(self):
        if(self.state):
            self.activate()

    def __str__(self):
        return f"{self.prefix}{self.representation}"

    def __repr__(self):
        return f"({self.__class__}) object at {id(self)} (repr: {self.__str__()}, " \
               f"value: {self.value}, " \
               f"state: {self.state}, " \
               f"activator: {self.activator.__repr__()})"