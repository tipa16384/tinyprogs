from dice import roll_dice

luck_influence = [
    "Harsh winter: All attack rolls",
    "The bull: Melee attack rolls",
    "Fortunate date: Missile fire attack rolls",
    "Raised by wolves: Unarmed attack rolls",
    "Conceived on horseback: Mounted attack rolls",
    "Born on the battlefield: Damage rolls",
    "Path of the bear: Melee damage rolls",
    "Hawkeye: Missile fire damage rolls",
    "Pack hunter: Attack and damage rolls for 0-level starting weapons",
    "Born under the loom: Skill checks (including thief skills)",
    "Fox's cunning: Find/disable traps",
    "Four-leafed clover: Reflex saving throws",
    "Seventh son: Spell checks",
    "The raging storm: Spell damage",
    "Righteous heart: Turn unholy checks",
    "Survived the plague: Magical healing",
    "Lucky sign: Saving throws",
    "Guardian angel: Savings throws to escape traps",
    "Survived a spider bite: Saving throws against poison",
    "Struck by lightning: Reflex saving throws",
    "Lived through famine: Fortitude saving throws",
    "Resisted temptation: Willpower saving throws",
    "Charmed house: Armor Class",
    "Speed of the cobra: Initiative",
    "Bountiful harvest: Hit points (applies at each level)",
    "Warrior's arm: Critical hit tables",
    "Unholy house: Corruption rolls",
    "The Broken Star: Fumbles",
    "Birdsong: Number of languages",
    "Wild child: Speed"
]

def get_luck_influence():
    return luck_influence[roll_dice(30) - 1]
