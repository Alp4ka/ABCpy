from models import Plants

MAX_CONTAINER_SIZE = 10000

class Container:
    def __init__(self):
        self.c = list()

    def length(self):
        return len(self.c)

    @staticmethod
    def from_list(arr):
        result = Container()
        for i in range(len(arr)):
            result.add(arr[i])
        return result

    def write_file(self, output_file):
        with open(output_file, 'w') as f:
            f.write(str(len(self.c)) + '\n')
            for plant in self.c:
                f.write(str(plant) + '\n')

    def add(self, item):
        if len(self.c) < MAX_CONTAINER_SIZE:
            self.c.append(item)
            return True
        else:
            return False

    def remove_at(self, index):
        del self.c[index]

    def __getitem__(self, index):
        return self.c[index]

    def __setitem__(self, index, item):
        self.c[index] = item

    def __iter__(self):
        for elem in self.c:
            yield elem

    @staticmethod
    def from_file(file_name):
        container = Container()
        with open(file_name, 'r') as input_file:
            number_of_elements = input_file.readline()
            if not number_of_elements:
                return container
            number_of_elements = int(number_of_elements)
            for i in range(number_of_elements):
                container.add(Plants.Plant.parse(input_file))
        return container
