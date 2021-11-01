import typing

FLAG_IDENTIFIER = '-'


class FlagHandler:
    """
        Flags handle class. You have to use it to parse or to activate specified flags.
    """
    def __init__(self, known_flags: 'list[Flag]'):
        self.known_flags = known_flags

    def from_args(self, args):
        """
            Parse flags information from input list of arguments.

            Args:
                args: collection of arguments.
        """
        for flag in self.known_flags:
            flag.get_from_args(args)

    def activate_all(self):
        """
            Activate all known flags despite of their status.
        """
        for flag in self.known_flags:
            flag.activate()

    def handle_all(self):
        """
            Activate all known flags according their status.
        """
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
        """
            Try to parse input string as int. In case of success returns int representation of input string. Otherwise -
            return the same string.

            Args:
                item: input string with int supposed to be in.
        """
        try:
            item = int(item)
            return item
        except Exception as ex:
            return item

    def get_from_args(self, args) -> bool:
        """
            Tres to parse current flag information from arguments collection.

            Args:
                args: collection of arguments.

            Returns:
                True in case we have found this flag and it's information in args. Otherwise - false.
        """
        index = -1
        for arg_i in range(len(args)):
            if args[arg_i] == f"{self.__str__()}":
                index = arg_i
                break
        check_size = (len(args) - index > 1)
        if index > -1 and check_size:
            self.state = True
            self.value = Flag.get_by_type(args[arg_i+1])
            return True
        else:
            self.state = False
            self.value = None
            return False

    def set_activator(self, activator: typing.Callable):
        """
            Pointer to a function we have to call in case we activate this flag.

            Args:
                activator: Pointer to an activator function for this flag.
        """
        self.activator = activator

    def activate(self):
        """
            Forced activation of a flag.
        """
        if self.activator is not None:
            self.activator(self.value)

    def handle(self):
        """
            Activate the flag in case its state is true(flag is found).
        """
        if self.state:
            self.activate()

    def __str__(self):
        return f"{self.prefix}{self.representation}"

    def __repr__(self):
        return f"({self.__class__}) object at {id(self)} (repr: {self.__str__()}, " \
               f"value: {self.value}, " \
               f"state: {self.state}, " \
               f"activator: {self.activator.__repr__()})"