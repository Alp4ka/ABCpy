from enum import Enum
from logger import Logger
from random import randint
import typing
from abc import abstractmethod
from utils import functions

MIN_NAME_LENGTH = 6
MAX_NAME_LENGTH = 14


#  Hardcoded a little.
REALISTIC_RELATION = {
    'a': 'hmscukrrtcbzpscndssctracnnbcdferdtdttntndnbskbscnceplcqtcezlcpstfscbsricshtebhrpzonfbowynwzswkueknccrdjnlcbcsccrdcttcldccqcgatprctlmsssnttc',
    'b': 'unuaciaudeearoauuearlsjurtlenirinjerosybiznyowsaeejalsauss',
    'c': 'ecaueakkaikyetaitokkkoaaiaiouikaaiaikokhakaekkkkelkueaoikkiizkiykyiaoioaeskekakukaekoankeaaikykeaohkkaeiuakqu',
    'd': 'iuiieuaeaaiieeuiiieeiauuiauiide',
    'e': 'hvacmlmvadomdvdatvvvbulaabvkdtoktfvawmunvcnmwqrtcvoanlwqlslhwwhtwtvmuwrzivcwccvgklvuvtttvpbtqwbvouvvvnandtlrvstpkqnedvjfveuevvqsznqxvvqcruxvqmevhtetkbhnvlchyn',
    'f': 'olceluoaileiuiilailuaiuaio',
    'g': 'aaeeroiageraeea',
    'h': 'eeettaaaiiioollanitooiielniioi',
    'i': 'clnonnnnnnennonnoannncecnalehenenlnnnaloenncennabebnnnanonbnnoeeonecannacbenonanoananeenelnneqneonnnnnneenllnncclhbaoabneoeconneon',
    'j': 'oooeeiiaaaoiiooo',
    'k': 'iilloooaaaeeieekeaeaeioeaoileoaoiaiaileil',
    'l': 'eeessiiioooaaeleoaiaoeaeaiisseaaaaaaaaaelaeeooieeo',
    'm': 'euuuooonnaaaaiiisemmmoaaoiia',
    'n': 'neeeuuuuiiieeininuinuiiieieiueeueueeeeunuiiiienieueieeeueeieeeeniueeiuiueu',
    'o': 'ccrrrriikctrrwrlcukqchhumulbuhrrrirpsllrbhyoulkkpwtshrarqbwrlrweyrrrprrwucrkbcckrrurywrwprpklkhrcrbhszpqa',
    'p': 'ooooaaaaiiirrroooairroooaiiiaiioii',
    'q': 'euuuuuiirtaaeeiuiu',
    'r': 'nnoonooooooaaeeeeeiiiioaaaauuuqkiiccnnsuussnnniuiiuoiioeuiasuuunuiaaueeoeaoua',
    's': 'uuuiiiaappuuuuyyyuuuyyuauuauuyaauauuuiuiuuuuuipuuuuuuuyyuuya',
    't': 'ttuuiiooaaeeeueeeeuueeiaeaaeueeiueaoeueeaeii',
    'u': 'cccccceeeecccaaaattnpzzssspeaaacscacacpsecpzzcecntccasaeecesssepaapeeaecanzsczpcnescaptceesccscscaapccnsacccccatescsaztccacscteaeaes',
    'v': 'iiiuuuiiiiuiiiuuuuuiiiuiiiuiiiiuuiuuiiu',
    'w': 'eeaaoooooouuiooaoooooooeaoooo',
    'x': 'yyyyceiiiyyeeeaaaaaeqy',
    'y': 'eeeuuuttrbbruuueuuuueuuuuueu',
    'z': 'aaeeiiuuuuaaeueaeauuaeauaueauuee'
}

ENDINGS = ["vin", "tus", "tas", "win", "lis"]

ALLOWED_SYMBOLS = "QWERTYUIOPASDFGHJKLZXCVBNM-qwertyuiopasdfghjklzxcvbnm"


class FlowerType(Enum):
    DOMESTIC = 0
    GARDEN = 1
    WILD = 2


class PlantType(Enum):
    FLOWER = 0
    SHRUB = 1
    TREE = 2


class BlossomTime(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Plant:
    def __init__(self, name: str):
        self.name = name

    def relation(self) -> float:
        """
            Counts relation of vowels and amount of symbols summary in name of a plant.

            Return:
                float
        """
        return functions.count_relation(self.name)

    def __str__(self):
        return f"Name: {self.name}; Relation: {self.relation()}."

    @staticmethod
    def generate_plant():
        """
            Generate random plant.

            Return:
                Plant child with random fields.
        """
        random_plant_type = PlantType(randint(0, len(PlantType) - 1))
        if random_plant_type == PlantType.FLOWER:
            return Flower.generate_plant()
        elif random_plant_type == PlantType.SHRUB:
            return Shrub.generate_plant()
        elif random_plant_type == PlantType.TREE:
            return Tree.generate_plant()
        else:
            return None

    @abstractmethod
    def get_file_representation(self):
        """
            Get plant file representation.
        """
        pass

    @staticmethod
    def generate_name_realistic(length: int) -> str:
        """
            Realistic name generation.

            Args:
                length: length of name.

            Return:
                str, random name
        """
        global REALISTIC_RELATION
        result = ""
        random_ending = ENDINGS[randint(0, len(ENDINGS) - 1)]
        current_sym = list(REALISTIC_RELATION.keys())[randint(0, len(REALISTIC_RELATION.keys()) - 1)]
        for i in range(length - len(random_ending)):
            result += current_sym
            current_sym = REALISTIC_RELATION[current_sym][randint(0, len(REALISTIC_RELATION[current_sym]) - 1)]
        result = result[0].upper() + result[1:] + random_ending
        return result

    @staticmethod
    def generate_name(length: int):
        """
            Standard name generation.

            Args:
                length: length of name.

            Return:
                str, random name
        """
        global ALLOWED_SYMBOLS
        result = ""
        for i in range(length):
            result += ALLOWED_SYMBOLS[randint(0, len(ALLOWED_SYMBOLS) - 1)]
        result = result[0].upper() + result[1:]
        return result

    @staticmethod
    def parse(input_file) -> typing.Optional['Plant']:
        """
            Parse plant from file.

            Args:
                input_file: input file to read data from.

            Return:
                Plant child or None.
        """
        try:
            line = input_file.readline()
            plant_type_int = int(line)
            plant_type = PlantType(plant_type_int)
            if plant_type == PlantType.FLOWER:
                return Flower.parse(input_file)
            elif plant_type == PlantType.SHRUB:
                return Shrub.parse(input_file)
            elif plant_type == PlantType.TREE:
                return Tree.parse(input_file)
            else:
                Logger.log("Oops! Looks like there is no such a plant type!", Logger.LogType.ERROR)
                return None
        except Exception as ex:
            Logger.log(f"Error while reading plant! {ex.__str__()}", Logger.LogType.ERROR)
            return None


class Flower(Plant):
    def __init__(self, name: str, flower_type):
        super().__init__(name)
        self.flower_type = flower_type

    def __str__(self):
        return f">FLOWER: Type: {self.flower_type.name}; " + super().__str__() + "<"

    @staticmethod
    def generate_plant() -> 'Flower':
        name = Plant.generate_name_realistic(randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH))
        flower_type = FlowerType(randint(0, len(FlowerType) - 1))
        return Flower(name, flower_type)

    def get_file_representation(self):
        return f"{PlantType.FLOWER.value}\n" \
               f"{self.name} {self.flower_type.value}"

    @staticmethod
    def parse(input_file):
        try:
            line = input_file.readline()
            splitted = line.split()
            if len(splitted) != 2:
                Logger.log(f"Wrong amount amount of arguments for Flower. Need: 2. Found: {len(splitted)}!",
                           Logger.LogType.ERROR)
                raise Exception()
            name = splitted[0]
            flower_type = FlowerType(int(splitted[1]))
            return Flower(name, flower_type)
        except:
            Logger.log("Error while reading Flower!", Logger.LogType.ERROR)
            return None


class Shrub(Plant):
    def __init__(self, name: str, blossom_time):
        super().__init__(name)
        self.blossom_time = blossom_time

    def __str__(self):
        return f">SHRUB: Blossom time: {self.blossom_time.name}; " + super().__str__() + "<"

    @staticmethod
    def generate_plant() -> 'Shrub':
        name = Plant.generate_name_realistic(randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH))
        blossom_time = BlossomTime(randint(1, len(BlossomTime)))
        return Shrub(name, blossom_time)

    def get_file_representation(self):
        return f"{PlantType.SHRUB.value}\n" \
               f"{self.name} {self.blossom_time.value}"

    @staticmethod
    def parse(input_file):
        try:
            line = input_file.readline()
            splitted = line.split()
            if len(splitted) != 2:
                Logger.log(f"Wrong amount amount of arguments for Shrub. Need: 2. Found: {len(splitted)}!",
                           Logger.LogType.ERROR)
                raise Exception()
            name = splitted[0]
            blossom_time = BlossomTime(int(splitted[1]))
            return Shrub(name, blossom_time)
        except:
            Logger.log("Error while reading Shrub!", Logger.LogType.ERROR)
            return None


class Tree(Plant):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f">TREE: Age: {self.age}; " + super().__str__() + "<"

    @staticmethod
    def generate_plant() -> 'Tree':
        name = Plant.generate_name_realistic(randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH))
        age = randint(1, 1000)
        return Tree(name, age)

    def get_file_representation(self):
        return f"{PlantType.TREE.value}\n" \
               f"{self.name} {self.age}"

    @staticmethod
    def parse(input_file):
        try:
            line = input_file.readline()
            splitted = line.split()
            if len(splitted) != 2:
                Logger.log(f"Wrong amount amount of arguments for Tree. Need: 2. Found: {len(splitted)}!",
                           Logger.LogType.ERROR)
                raise Exception()
            name = splitted[0]
            age = int(splitted[1])
            return Tree(name, age)
        except:
            Logger.log("Error while reading Flower!", Logger.LogType.ERROR)
            return None
