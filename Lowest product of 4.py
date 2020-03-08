class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):
        new_color = []
        ratio1 = self.volume / (self.volume + other.volume)
        ratio2 = other.volume / (self.volume + other.volume)
        c = 0
        for color in self.color:
            color_1 = (color * ratio1 + other.color[c] * ratio2) / (ratio1 + ratio2)
            self.color[c] = color_1
            c += 1
        self.volume += other.volume



potions = [
    Potion((153, 210, 199), 32),
    Potion((135, 34, 0), 17),
    Potion((18, 19, 20), 25),
    Potion((174, 211, 13), 4),
    Potion((255, 23, 148), 19),
    Potion((51, 102, 51), 6)
]
a = potions[0].mix(potions[1])
# b = potions[0].mix(potions[2]).mix(potions[4])
# c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
# d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
# e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])

print(a)
