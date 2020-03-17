from random import choice, choices


class Verse:

    def __init__(self):
        self.factions = {}
        self.tone = {}
        self.the_self = {}
        self.init_factions()
        self.init_tone()

    def __str__(self):
        string = ""
        for d in [self.factions, self.tone]:
            for k, v in d.items():
                string += f"{k.title()}: {v.title()}\n"

        return string

    def init_factions(self):
        agencies = ['aegis', 'strike']
        strength = ['weak', 'average', 'strong']
        for agency in agencies:
            self.factions[agency] = choice(strength)

        self.factions['independent'] = choices(strength, [4, 4, 2], k=1)[0]

    def init_tone(self):
        self.tone['outlook'] = choice(['light', 'dark', 'neutral'])
        self.tone['government'] = choice([
            'totalitarian',
            'libertarian',
            'egalitarian',
            'anarchy',
            'moderate'
        ])
        self.tone['tech'] = (
            choices([
                'far below',
                'below',
                'similar',
                'higher',
                'far higher',
                'indistinguishable from magic',
            ],
                weights=[
                    15,
                    10,
                    25,
                    25,
                    25,
                    0.1
                ], k=1)[0])


    def print_self(self):
        print(self.factions)
        print(self.tone)
        print(self.the_self)


class Character:


    def __init__(self):
        colors = [
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'purple',
            'pink',
            'white',
            'black',
            'silver',
            'gold'
        ]
        self.the_self = {
            'gender': choices(['same', 'different'], [2, 1], k=1)[0],
            'personality': choices([
                'very different',
                'moderately different',
                'slightly different',
                'similar',
                'very similar'],
                k=1
            )[0],
            'color scheme': choice(colors)
        }

    def __str__(self):
        string = ""
        for k, v in self.the_self.items():
            string += f"{k.title()}: {v.title()}\n"

        return string.strip()


if __name__ == "__main__":
    #verse = Verse()
    #verse.print_self()
    char = Character()
    print(str(char))
