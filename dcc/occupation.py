from dice import roll_dice
from random import choice

occupations = [
    (1, 'Alchemist', 'Staff', 'Staff', 'Oil, 1 flask'),
    (2, 'Animal Trainer', 'Club', 'Club', 'Pony'),
    (3, 'Armorer', 'Hammer', 'Club', 'Iron helmet'),
    (4, 'Astrologer', 'Dagger', 'Dagger', 'Spyglass'),
    (5, 'Barber', 'Razor', 'Dagger', 'Scissors'),
    (6, 'Beadle', 'Staff', 'Staff', 'Holy symbol'),
    (7, 'Beekeeper', 'Staff', 'Staff', 'Jar of honey'),
    (8, 'Blacksmith', 'Hammer', 'Club', 'Steel tongs'),
    (9, 'Butcher', 'Cleaver', 'Axe', 'Side of beef'),
    (10, 'Caravan Guard', 'Short sword', 'Short sword', 'Linen, 1 yard'),
    (11, 'Cheesemaker', 'Cudgel', 'Staff', 'Stinky cheese'),
    (12, 'Cobbler', 'Awl', 'Dagger', 'Shoehorn'),
    (13, 'Confidence Artist', 'Dagger', 'Dagger', 'Quality cloak'),
    (14, 'Cooper', 'Crowbar', 'Club', 'Barrel'),
    (15, 'Costermonger', 'Knife', 'Dagger', 'Fruit'),
    (16, 'Cutpurse', 'Dagger', 'Dagger', 'Small chest'),
    (17, 'Ditch Digger', 'Shovel', 'Staff', 'Fine dirt, 1 lb.'),
    (18, 'Dock worker', 'Shovel', 'Staff', '1 late RPG book'),
    (19, 'Dwarven Apothecarist', 'Cudgel', 'Staff', 'Steel vial'),
    (20, 'Dwarven Blacksmith', 'Hammer', 'Club', 'Mithril, 1 oz.'),
    (21, 'Dwarven Chest Maker', 'Chisel', 'Dagger', 'Wood, 10 lbs.'),
    (22, 'Dwarven Herder', 'Staff', 'Staff', 'Sow'),
    (23, 'Dwarven Miner', 'Pick', 'Club', 'Lantern'),
    (25, 'Dwarven Mushroom Farmer', 'Shovel', 'Staff', 'Sack'),
    (26, 'Dwarven Ratcatcher', 'Club', 'Club', 'Net'),
    (27, 'Dwarven Stonemason', 'Hammer', 'Club', 'Fine stone, 10 lbs.'),
    (29, 'Elven Artisan', 'Staff', 'Staff', 'Clay, 1 lb.'),
    (30, 'Elven Barrister', 'Quill', 'Dart', 'Book'),
    (31, 'Elven Chandler', 'Scissors', 'Dagger', 'Candles, 20'),
    (32, 'Elven Falconer', 'Dagger', 'Dagger', 'Falcon'),
    (33, 'Elven Forester', 'Staff', 'Staff', 'Herbs, 1 lb.'),
    (35, 'Elven Glassblower', 'Hammer', 'Club', 'Glass beads'),
    (36, 'Elven Navigator', 'Shortbow', 'Shortbow', 'Spyglass'),
    (37, 'Elven Sage', 'Dagger', 'Dagger', 'Parchment and quill pen'),
    (39, 'Farmer', 'Pitchfork', 'Spear', 'Hen'),
    (48, 'Fortune Teller', 'Dagger', 'Dagger', 'Tarot deck'),
    (49, 'Gambler', 'Club', 'Club', 'Dice'),
    (50, 'Gongfarmer', 'Trowel', 'Dagger', 'Sack of night soil'),
    (51, 'Grave Digger', 'Shovel', 'Staff', 'Trowel'),
    (53, 'Guild Beggar', 'Sling', 'Sling', 'Crutches'),
    (55, 'Halfling Chicken Butcher', 'Handaxe', 'Handaxe', 'Chicken meat, 5 lbs.'),
    (56, 'Halfling Dyer', 'Staff', 'Staff', 'Fabric, 3 yards'),
    (58, 'Halfling Glovemaker', 'Awl', 'Dagger', 'Gloves, 4 pairs'),
    (59, 'Halfling Wanderer', 'Sling', 'Sling', 'Hex doll'),
    (60, 'Halfling Haberdasher', 'Scissors', 'Dagger', 'Fine suits, 3 sets'),
    (61, 'Halfling Mariner', 'Knife', 'Dagger', 'Sailcloth, 2 yards'),
    (62, 'Halfling Moneylender', 'Short sword', 'Short sword', '5 gp, 10 sp, 200 cp'),
    (63, 'Halfling Trader', 'Short sword', 'Short sword', '20 sp'),
    (64, 'Halfling vagrant', 'Club', 'Club', 'Begging bowl'),
    (65, 'Healer', 'Club', 'Club', 'Holy water, 1 vial'),
    (66, 'Herbalist', 'Club', 'Club', 'Herbs, 1 lb.'),
    (67, 'Herder', 'Staff', 'Staff', 'Herding dog'),
    (68, 'Hunter', 'Shortbow', 'Shortbow', 'Deer pelt'),
    (70, 'Indentured Servant', 'Staff', 'Staff', 'Locket'),
    (71, 'Jester', 'Dart', 'Dart', 'Silk clothes'),
    (72, 'Jeweler', 'Dagger', 'Dagger', 'Gem worth 20 gp'),
    (73, 'Locksmith', 'Dagger', 'Dagger', 'Fine tools'),
    (74, 'Mendicant', 'Club', 'Club', 'Cheese dip'),
    (75, 'Mercenary', 'Longsword', 'Longsword', 'Hide armor'),
    (76, 'Merchant', 'Dagger', 'Dagger', '4 gp, 14 sp, 27 cp'),
    (77, 'Miller/Baker', 'Club', 'Club', 'Flour, 1 lb.'),
    (78, 'Minstrel', 'Dagger', 'Dagger', 'Ukulele'),
    (79, 'Noble', 'Longsword', 'Longsword', 'Gold ring worth 10 gp'),
    (80, 'Orphan', 'Club', 'Club', 'Rag doll'),
    (81, 'Ostler', 'Staff', 'Staff', 'Bridle'),
    (82, 'Outlaw', 'Short sword', 'Short sword', 'Leather armor'),
    (83, 'Rope Maker', 'Knife', 'Dagger', 'Rope, 100 feet'),
    (84, 'Scribe', 'Dart', 'Dart', 'Parchment, 10 sheets'),
    (85, 'Shaman', 'Mace', 'Mace', 'Herbs, 1 lb.'),
    (86, 'Slave', 'Club', 'Club', 'Strange-looking rock'),
    (87, 'Smuggler', 'Sling', 'Sling', 'Waterproof sack'),
    (88, 'Soldier', 'Spear', 'Spear', 'Shield'),
    (89, 'Squire', 'Longsword', 'Longsword', 'Steel helmet'),
    (91, 'Tax Collector', 'Longsword', 'Longsword', '100 cp'),
    (92, 'Trapper', 'Sling', 'Sling', 'Badger pelt'),
    (94, 'Urchin', 'Stick', 'Club', 'Begging bowl'),
    (95, 'Wainwright', 'Club', 'Club', 'Pushcart'),
    (96, 'Weaver', 'Dagger', 'Dagger', 'Fine suit of clothes'),
    (97, 'Wizard\'s Apprentice', 'Dagger', 'Dagger', 'Black grimoire'),
    (98, 'Woodcutter', 'Handaxe', 'Handaxe', 'Bundle of wood')
]

farmer_type = [ 'Potato', 'Wheat', 'Turnip', 'Corn', 'Rice', 'Parsnip', 'Radish', 'Rutabaga']

animal_type = ['Hen', 'Sheep', 'Duck', 'Goose', 'Cow', 'Mule']

cart_contents = ['tomatoes', 'nothing', 'straw', 'your dead', 'dirt', 'rocks']

def get_occupation():
    index = roll_dice(100)
    occ = None

    # if tuple with first element with that index exists, return it
    for occupation in occupations:
        if occupation[0] == index:
            occ = occupation
            break

    if not occ:
        # if tuple with first element > than index, return the previous tuple
        for i in range(len(occupations)):
            if occupations[i][0] > index:
                occ = occupations[i-1]
                break

    if not occ:
        # if no tuple with first element > than index, return the last tuple
        occ = occupations[-1]

    if occ[1] == 'Farmer':
        farmer = choice(farmer_type) + ' Farmer'
        occ = (occ[0], farmer, occ[2], occ[3], choice(animal_type))
    
    if occ[4] == 'Pushcart':
        occ = (occ[0], occ[1], occ[2], occ[3], 'Pushcart containing ' + choice(cart_contents))
    
    if occ[2] != occ[3]:
        occ = (occ[0], occ[1], occ[2] + ' ('+occ[3]+')', occ[3], occ[4])

    return occ

