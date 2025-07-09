import json
import statistics


class Flowers:
    def __init__(self, filename):
        self.file_name = filename
        self.data = self.read_file()
        self.name = self.data['name']
        self.color = self.data['color']
        self.price = self.data['price']
        self.stem_length_cm = self.data['stem_length_cm']
        self.avg_life_time = self.data['avg_life_time']
        self.freshness_days = self.data['freshness_days']

    def read_file(self):
        with open(self.file_name) as file_data:
            data = json.load(file_data)
        return data

    def __repr__(self):
        return self.name


class Rose(Flowers):
    def __init__(self, filename):
        super().__init__(filename)


class Lily(Flowers):
    def __init__(self, filename):
        super().__init__(filename)


class Pione(Flowers):
    def __init__(self, filename):
        super().__init__(filename)


class Bouquet:
    def __init__(self):
        self.flowers_in_bouquet = []

    def add_flower(self, flower, flowers_count):
        for _ in range(flowers_count):
            self.flowers_in_bouquet.append(flower)

    def avg_life_times(self):
        return statistics.mean(f.avg_life_time for f in self.flowers_in_bouquet)

    def total_price(self):
        return sum(f.price for f in self.flowers_in_bouquet)

    def sort_by(self, attr_name, reverse=False):
        self.flowers_in_bouquet.sort(
            key=lambda flower: getattr(flower, attr_name),
            reverse=reverse
        )
        return self.flowers_in_bouquet

    def find_by(self, attr_name, value):
        return [flower for flower in self.flowers_in_bouquet
                if getattr(flower, attr_name, None) == value]


rose = Rose("Rose.txt")
lily = Lily("Lily.txt")
pione = Pione("Pione.txt")

bouqet = Bouquet()
bouqet.add_flower(rose, 1)
bouqet.add_flower(lily, 2)
bouqet.add_flower(pione, 1)

print(bouqet.total_price())
print(bouqet.avg_life_times())
print(bouqet.sort_by('freshness_days', reverse=False))
print(bouqet.sort_by('stem_length_cm', reverse=False))
print(bouqet.sort_by('price', reverse=True))
print(bouqet.find_by('avg_life_time', 8))
