from dice import roll_dice_n_times_and_sum, roll_dice
from luck import get_luck_influence
from occupation import get_occupation
from random import choice

characteristics = ['STR', 'AGI', 'STA', 'PER', 'INT', 'LCK']

mods = [-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]

gender = ['Male', 'Female']

equipment = [
    'Backpack',
    'Candle',
    'Chain, 10 feet',
    'Chalk, 1 piece',
    'Chest, empty',
    'Crowbar',
    'Flask, empty',
    'Flint & steel',
    'Grappling hook',
    'Hammer, small',
    'Holy symbol',
    'Holy water, 1 vial',
    'Iron spikes, dozen',
    'Lantern',
    'Mirror, hand-sized',
    'Oil, 1 flask',
    'Pole, 10-foot',
    'Rations',
    'Rope, 50-foot',
    'Sack, large',
    'Sack, small',
    'Thieves\' tools',
    'Torch',
    'Waterskin'
]

def plural(n: int, s: str) -> str:
    return str(n) + ' ' + (s + 's' if n != 1 else s)

class Character:
    def __init__(self, name: str):
        self.name = name
        self.characteristics = {c: 0 for c in characteristics}
        self.luck_influence = get_luck_influence()
        self.skills = {}
        self.health = 0
        self.magic = 0
        self.wealth = 0
        self.ammo = None
        self.equipment = []
        self.spells = []
        self.languages = []
        self.race = 'Human'
        self.occupation = None
        self.trade_goods = []
        self.gender = choice(gender)
        
    def __str__(self) -> str:
        special = []
        if self.characteristics['STR'] <= 5:
            special.append('Can wield a weapon or a shield, but not both')
        if self.characteristics['STA'] <= 5:
            special.append('Double damage from poisons and disease')
        if self.characteristics['INT'] <= 7:
            special.append('Can only speak Common')
        if self.characteristics['INT'] <= 5:
            special.append('Cannot read or write')
        return f'{self.name}:\n' + \
               f'Occupation: {self.occupation[1]}\n' + \
               f'Race: {self.race}\n' + \
               f'Characteristics: {self.characteristics}\n' + \
               f'Luck Influence: {self.luck_influence}\n' + \
               f'Health: {self.health}\n' + \
               f'Wealth: {self.wealth} copper pieces\n' + \
               f'Equipment: {self.equipment}\n' + \
               f'Languages: {self.languages}\n' + \
               f'Trade Goods: {self.trade_goods}'
    
    def prompt(self) -> str:
        luck_influence = self.luck_influence.split(': ')
        # return a prompt that could be fed into ChatGPT in order to provide a background for the character
        return f'Please provide a short background for a RPG character who is a {self.occupation[1]}, a {self.gender} {self.race}. They can speak {", ".join(self.languages)} ' + \
             f' and have the following characteristics: {", ".join([f"{c}: {self.characteristics[c]}" for c in self.characteristics])}. ' + \
             f'They have {self.health} health, and {self.wealth} copper pieces. They have the following equipment: {", ".join(self.equipment)}. ' + \
             f'They have the following trade goods: {", ".join(self.trade_goods)}. ' + \
             f'Their luck influence is {luck_influence[0].lower()} that modifies their {luck_influence[1].lower()}.' + \
             '  Please write only a single paragraph for their background, please do not recap the input.'

    def roll_characteristics(self) -> None:
        for c in self.characteristics:
            self.characteristics[c] = roll_dice_n_times_and_sum(6, 3)
        self.health =  max(1,roll_dice(4) + mods[self.characteristics['STA']-3])
        self.magic = self.characteristics['INT']
        self.wealth = roll_dice_n_times_and_sum(12, 5)
        self.languages = ['Common']
        background = get_occupation()
        title = background[1]
        if title.startswith('Dwarven'):
            self.race = 'Dwarf'
        elif title.startswith('Elven'):
            self.race = 'Elf'
            self.gender = 'Ambiguously gendered'
        elif title.startswith('Halfling'):
            self.race = 'Halfling'
        match background[3]:
            case 'Sling': self.ammo = 'stone'
            case 'Shortbow': self.ammo = 'arrow'
            case 'Dart': self.ammo = 'dart'
            case _: self.ammo = None
        if self.characteristics['INT'] >= 8:
            if title.startswith('Dwarven'):
                self.languages.append('Dwarven')
            elif title.startswith('Elven'):
                self.languages.append('Elven')
            elif title.startswith('Halfling'):
                self.languages.append('Halfling')
        self.occupation = background
        self.equipment.append(background[2])
        if self.ammo:
            amount = roll_dice(6)
            self.equipment.append(plural(amount, self.ammo))
        self.equipment.append(choice(equipment))
        self.trade_goods.append(background[4])
