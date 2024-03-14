import pygame
import pygame_gui
from bidict import bidict

# Start PyGame
pygame.init()
screen_x, screen_y = 800, 700
SCREEN = pygame.display.set_mode((screen_x, screen_y))
MANAGER = pygame_gui.ui_manager.UIManager((screen_x, screen_y), 'resources/defaults.json', enable_live_theme_updates=False)

MANAGER.get_theme().load_theme('resources/defaults.json')
MANAGER.get_theme().load_theme('resources/buttons.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')


import scripts.cat.cats

CREATED_CAT = scripts.cat.cats.Cat()


def sort_bidict(d: bidict, first_element=None):
    """Sorts Dictionary alphbetically. If None if in the dictionary, always have that first. """

    temp = bidict({})
    if first_element in d:
        temp[first_element] = d[first_element]
        del d[first_element]

    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    temp.update(sorted_dict)
    return temp


pelt_options = bidict({"SingleColour": "Plain",  "Smoke": "Smoke", 'Singlestripe': "Single Stripe", 'Tabby': "Tabby",
                       'Ticked': "Ticked Tabby", 'Mackerel': "Mackerel Tabby", 'Classic': "Classic Tabby",
                       'Sokoke': "Sokoke", 'Agouti': "Agouti", "Speckled": "Speckled Tabby", "Rosette": "Rosette",
                       "Bengal": "Bengal", "Marbled": "Marbled Tabby", 'Abyssinian': "Abyssinian", 'Brindle': "Brindle",
                       'Braided': "Braided", 'Splotch': "Splotch", 'Saber': "Saber", 'Faded': "Faded", 'Masked': "Masked"})
pelt_options = sort_bidict(pelt_options)

tortie_patches_patterns = bidict({"single": "Plain", "tabby": "Tabby", "bengal": "Bengal", "marbled": "Marbled Tabby",
                                  "ticked": "Ticked Tabby", "rosette": "Rosette", "smoke": "Smoke",
                                  "speckled": "Speckled Tabby", "agouti": "Agouti", "classic": "Classic Tabby",
                                  "mackerel": "Mackerel Tabby", "sokoke": "Sokoke", "abyssinian": "Abyssinian",
                                  "brindle": "Brindle", "braided": "Braided", "splotch": "Splotch", "saber": "Saber",
                                  "faded": "Faded", 'Masked': "Masked"})
tortie_patches_patterns = sort_bidict(tortie_patches_patterns)

tortie_patches_shapes = bidict({"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four",  'REDTAIL': "Redtail",
                                'DELILAH': "Delilah", 'MINIMALONE': "Minimal 1", 'MINIMALTWO': "Minimal 2",
                                'MINIMALTHREE': "Minimal 3", 'MINIMALFOUR': "Minimal 4", 'OREO': "Oreo", 'SWOOP': "Swoop",
                                'MOTTLED': "Mottled", 'SIDEMASK': "Sidemask", 'EYEDOT': "Eye dot",
                                'BANDANA': "Bandana", 'PACMAN': "Pacman", 'STREAMSTRIKE': "Streamstrike",
                                'ORIOLE': "Oriole", 'ROBIN': "Robin", 'BRINDLE': "Brindle", 'PAIGE': "Paige", 
                                "ROSETAIL": "Rosetail", "SAFI": "Safi", "HALF": "Half", "CHIMERA": "Chimera", 
                                "SMUDGED": "Smudged", "DAUB": "Daub", "DAPPLENIGHT": "Dapplenight", "STREAK": "Streak", 
                                "MASK": "Mask", "CHEST": "Chest", "ARMTAIL": "Armtail", "EMBER": "Ember", 'BRIE': "Brie",
                                'BLANKET': "Blanket", 'BELOVED': "Beloved", 'VIPER': "Viper", 'SKULL': "Skull",
                                'POINTS': "Points", 'DITTO': "Ditto", 'BODY': "Body", 'SHILOH': "Shiloh", 'SPECKLED': "Speckled",
                                'BENGAL': "Bengal", 'CLASSIC': "Classic", 'MACKEREL': "Mackerel", 'MARBLED': "Marbled"})
tortie_patches_shapes = sort_bidict(tortie_patches_shapes)

eye_colors = bidict({'YELLOW': "Yellow", 'AMBER': "Amber", 'HAZEL': "Hazel", 'PALE GREEN': "Pale Green", 'GREEN': "Green",
                      'BLUE': "Blue", 'DARK BLUE': "Dark Blue", 'GREY': "Gray", 'CYAN': "Cyan", 'EMERALD': "Emerald",
                      'HEATHER BLUE': "Heather Blue", 'SUN-LIT ICE': "Sun lit Ice", 'COPPER': "Copper", 'SAGE': "Sage",
                      'BRIGHT BLUE': "Bright Blue", 'PALE BLUE': "Pale Blue", 'LAVENDER': "Lavender", 'DARK GREY': "Dark Gray",
                      'PALE YELLOW': "Pale Yellow", 'GOLD': "Gold", 'LIME': "Lime", 'HAZELNUT': "Hazelnut",
                      'DARK AMBER': "Dark Amber", 'SLATE': "Slate", 'RUBY': "Ruby", 'LILAC': "Lilac",
                      'LIGHT GREY': "Light Gray", 'PINK': "Pink", 'DARK HAZEL': "Dark Hazel", 'CHOCOLATE': "Chocolate"})
eye_colors = sort_bidict(eye_colors)
eye_patterns = bidict( {None: 'None', 'TRUE': "True", 'CENTRAL': "Central", 'QUARTER': "Quarter", 'SLIVER': "Sliver",
                        'SPECKLES': "Speckles", 'FROSTED': "Frosted", 'RING': "Ring", 'HALFCENTRAL': "Half Central",
                        'HALFRING': "Halfring", 'BUBBLE': "Bubble", 'OUTRING': "Outring", 'SWAP': "Swap"})
eye_patterns = sort_bidict(eye_patterns, None)

white_patches_tint = bidict({"none": "None", "darkcream": "Dark Cream", "cream": "Cream", "offwhite": "Off White",
                             "gray": "Gray", "pink": "Pink", "black": "Black", "birch": "Birch", "gold": "Gold",
                             "fire": "Fire", "ginger": "Ginger", "blue": "Blue", "lilac": "Lilac",
                             "darklilac": "Dark Lilac"})

skin_colors = bidict({'BLACK': "Black", 'RED': "Red", 'PINK': "Pink", 'DARKBROWN': "Dark Brown", 'BROWN': "Brown",
                      'LIGHTBROWN': "Light Brown", 'DARK': "Dark", 'DARKGREY': "Dark Gray", 'GREY': "Gray",
                      'DARKSALMON': "Dark Salmon", 'SALMON': 'Salmon', 'PEACH': 'Peach', 'DARKMARBLED': 'Dark Marbled',
                      'MARBLED': 'Marbled', 'LIGHTMARBLED': 'Light Marbled', 'DARKBLUE': 'Dark Blue', 'BLUE': 'Blue',
                      'LIGHTBLUE': 'Light Blue'})
skin_colors = sort_bidict(skin_colors)

colors = bidict({'WHITE': "White", 'SNOW WHITE': "Snow White", 'GRAY': "Gray", 'SLATE': "Slate", 'DARK GRAY': "Dark Gray",
                 'DARK SLATE': "Dark Slate", 'PALE BLUE': "Pale Blue", 'BLUE': "Blue", 'PALE LILAC': "Pale Lilac",
                 'LILAC': "Lilac", 'SILVER': "Silver", 'BLACK': "Black", 'SOOT BLACK': "Soot Black",
                 'OBSIDIAN': "Obsidian", 'GHOST': "Ghost", 'PALE BROWN': "Pale Brown", 'ALMOND': "Almond", 'ACORN': "Acorn",
                 'LIGHT BROWN': "Light Brown", 'BROWN': "Brown", 'DARK BROWN': "Dark Brown",
                 'PALE CINNAMON': "Pale Cinnamon", 'CINNAMON': "Cinnamon", 'SABLE': "Sable", 'DARK SABLE': "Dark Sable",
                 'BIRCH': "Birch", 'PALE LAVENDER': "Pale Lavender", 'LAVENDER': "Lavender",
                 'DARK LAVENDER': "Dark Lavender", 'DARK ORANGE': "Dark Orange", 'PALE FIRE': "Pale Fire", 'FIRE': "Fire",
                 'DARK FIRE': "Dark Fire", 'PALE GINGER': "Pale Ginger", 'GINGER': "Ginger", 'DARK GINGER': "Dark Ginger",
                 'PALE GOLD': "Pale Gold", 'YELLOW': "Yellow", 'GOLD': "Gold", 'BRONZE': "Bronze", 'ROSE': "Rose",
                 'LIGHT CREAM': "Light Cream", 'CREAM': "Cream", 'DARK CREAM': "Dark Cream", 'DARK GOLD': "Dark Gold"
                 })
colors = sort_bidict(colors)

white_patches = bidict({None: 'None', 'MAO': 'Mao', 'LUNA': 'Luna', 'CHESTSPECK': 'Chest Speck', 'WINGS': 'Wings',
                        'PAINTED': 'Painted', 'BLACKSTAR': 'Blackstar', 'LITTLE': 'Little', 'TUXEDO': 'Tuxedo',
                        'LIGHTTUXEDO': 'Light Tuxedo', 'BUZZARDFANG': 'Buzzardfang', 'TIP': 'Tip', 'BLAZE': 'Blaze',
                        'BIB': 'Bib', 'VEE': 'Vee', 'PAWS': 'Paws', 'BELLY': 'Belly', 'TAILTIP': 'Tail Tip',
                        'TOES': 'Toes', 'BROKENBLAZE': 'Broken Blaze', 'LILTWO': 'Lil Two', 'SCOURGE': 'Scourge',
                        'TOESTAIL': 'Toes Tail', 'RAVENPAW': 'Ravenpaw', 'HONEY': 'Honey', 'FANCY': 'Fancy',
                        'UNDERS': 'Unders', 'DAMIEN': 'Damien', 'SKUNK': 'Skunk', 'MITAINE': 'Mitaine',
                        'SQUEAKS': 'Squeaks', 'STAR': 'Star', 'ANY': 'Any', 'ANYTWO': 'Any Two', 'BROKEN': 'Broken',
                        'FRECKLES': 'Freckles', 'RINGTAIL': 'Ringtail', 'HALFFACE': 'Half Face', 'PANTSTWO': 'Pants 2',
                        'GOATEE': 'Goatee', 'PRINCE': 'Prince', 'FAROFA': 'Farofa', 'MISTER': 'Mister',
                        'PANTS': 'Pants', 'REVERSEPANTS': 'Reverse Pants', 'HALFWHITE': 'Half White',
                        'APPALOOSA': 'Appaloosa', 'PIEBALD': 'Piebald', 'CURVED': 'Curved', 'GLASS': 'Glass',
                        'MASKMANTLE': 'Mask Mantle', 'VAN': 'Van', 'ONEEAR': 'One Ear', 'LIGHTSONG': 'Lightsong',
                        'TAIL': 'Tail', 'HEART': 'Heart', 'HEARTTWO': 'Heart 2', 'MOORISH': 'Moorish', 'APRON': 'Apron',
                        'CAPSADDLE': 'Cap Saddle', 'FULLWHITE': 'Full White', "EXTRA": "Extra", 'PETAL': 'Petal',
                        "DIVA": "Diva", "SAVANNAH": "Savannah", "FADESPOTS": "Fadespots", "SHIBAINU": "Shiba Inu", 
                        "TOPCOVER": "Top Cover", "DAPPLEPAW": "Dapplepaw", "BEARD": "Beard", "PEBBLESHINE": "Pebbleshine", 
                        "OWL": "Owl", "WOODPECKER": "Woodpecker", "MISS": "Miss", "BOOTS": "Boots", "COW": "Cow", 
                        "COWTWO": "Cow 2", "BUB": "Bub",
                        'BOWTIE': "Bow Tie", 'MUSTACHE': "Mustache", 'REVERSEHEART': "Reverse Heart", 'SPARROW': "Sparrow",
                        'VEST': "Vest", 'LOVEBUG': "Love Bug", 'TRIXIE': "Trixie", 'SAMMY': "Sammy", 'SPARKLE': "Sparkle",
                        'CHANCE': "Chance", 'MOSSY': "Mossy", 'MOTH': "Moth", 'NIGHTMIST': "Nightmist", 'FALCON': "Falcon",
                        'VENUS': "Venus", 'RETSUKO': "Retsuko", 'TIDAL': "Tidal", 'DIAMOND': "Diamond", "ECLIPSE": "Eclipse",
                        'SNOWSTORM': "Snow Storm", 'PEPPER': "Pepper", 'COWTHREE': "Cow Three", 'COWFOUR': "Cow Four",
                        'COWFIVE': "Cow Five", 'COWSIX': "Cow Six", 'COWSEVEN': "Cow Seven", 'COWEIGHT': "Cow Eight",
                        'COWNINE': "Cow Nine", 'COWTEN': "Cow Ten", 'COWELEVEN': "Cow Eleven", 'FRECKLEMASK': "Frecklemask",
                        'SPLAT': "Splat", 'BATWING': "Batwing"})
white_patches = sort_bidict(white_patches, None)

points = bidict({None: 'None', 'COLOURPOINT': 'Colorpoint', 'RAGDOLL': 'Ragdoll', 'SEPIAPOINT': 'Sepiapoint', 'MINKPOINT': 'Minkpoint',
                 'SEALPOINT': 'Sealpoint',})
points = sort_bidict(points, None)

vit = bidict({None: 'None', 'VITILIGO': 'Vitiligo 1', 'VITILIGOTWO': 'Vitiligo 2', 'KARPATI': 'Karpati',
              'MOON': 'Moon', 'PHANTOM': 'Phantom', 'POWDER': 'Powder', 'BLEACHED': 'Bleached', 'SPLAT': "Splat", 'SMOKEY': "Smokey"})
vit = sort_bidict(vit, None)

scars = bidict({None: "None", "ONE": "Chest", "TWO": "Shoulder", "THREE": "Over Eye", "TAILSCAR": "Tail",
                "SNOUT": "Snout", "CHEEK": "Cheek",
                "SIDE": "Side", "THROAT": "Throat", "TAILBASE": "Tail Base", "BELLY": "Belly", "LEGBITE": "Bite: Leg",
                "NECKBITE": "Bite: Neck", "FACE": "Face", "MANLEG": "Mangled Leg", "BRIGHTHEART": "Mangled Face",
                "MANTAIL": "Mangled Tail", "BRIDGE": "Bridge", "RIGHTBLIND": "Right Eye Blind",
                "LEFTBLIND": "Left Eye Blind", "BOTHBLIND": "Both Eyes Blind", "BEAKCHEEK": "Beak: Cheek",
                "BEAKLOWER": "Beak: Lower", "CATBITE": "Cat Bite", "RATBITE": "Rat Bite", "QUILLCHUNK": "Quill Chunk",
                "QUILLSCRATCH": "Quill Scratch", "LEFTEAR": "Left Ear Notch", "RIGHTEAR": "Right Ear Notch",
                "NOLEFTEAR": "No Left Ear", "NORIGHTEAR": "No Right Ear", "NOEAR": "No Ears", "NOTAIL": "No Tail",
                "HALFTAIL": "Half Tail", "NOPAW": "Missing Leg",
                "SNAKE": "Bite: Snake", "TOETRAP": "Toe Trap", "BURNPAWS": "Burnt Paws", "BURNTAIL": "Burnt Tail",
                "BURNBELLY": "Burnt Belly", "BURNRUMP": "Burnt Rump", "FROSTFACE": "Frostbitten Face",
                "FROSTTAIL": "Frostbitten Tail", "FROSTMITT": "Frostbitten Paw1", "FROSTSOCK": "Frostbitten Paw2"})
scars = sort_bidict(scars, None)

accessories = bidict({None: "None", "MAPLE LEAF": "Maple Leaf", "HOLLY": "Holly", "BLUE BERRIES": "Blue Berries",
                      "FORGET ME NOTS": "Forget-me-nots", "RYE STALK": "Rye Stalk", "LAUREL": "Laurel",
                      "BLUEBELLS": "Bluebells", "NETTLE": "Nettle", "POPPY": "Poppy", "LAVENDER": "Lavender",
                      "HERBS": "Herbs", "PETALS": "Petals", "DRY HERBS": "Dry Herbs", "OAK LEAVES": "Oak Leaves",
                      "CATMINT": "Catmint", "MAPLE SEED": "Maple Seed", "JUNIPER": "Juniper",
                      "RED FEATHERS": "Red Feathers", "BLUE FEATHERS": "Blue Feathers", "JAY FEATHERS": "Jay Feathers",
                      "MOTH WINGS": "Moth Wings", "CICADA WINGS": "Cicada Wings", "CRIMSON": "Crimson Collar",
                      "BLUE": "Blue Collar", "YELLOW": "Yellow Collar", "CYAN": "Cyan Collar", "RED": "Red Collar",
                      "LIME": "Lime Collar", "GREEN": "Green Collar", "RAINBOW": "Rainbow Collar",
                      "BLACK": "Black Collar", "SPIKES": "Spiked Collar", "PINK": "Pink Collar",
                      "PURPLE": "Purple Collar", "MULTI": "Mulicolored Collar", "CRIMSONBELL": "Crimson Bell Collar",
                      "BLUEBELL": "Blue Bell Collar", "YELLOWBELL": "Yellow Bell Collar",
                      "CYANBELL": "Cyan Bell Collar", "REDBELL": "Red Bell Collar", "LIMEBELL": "Lime Bell Collar",
                      "GREENBELL": "Green Bell Collar", "RAINBOWBELL": "Rainbow Bell Color",
                      "BLACKBELL": "Black Bell Collar", "SPIKESBELL": "Spiked Bell Collar",
                      "PINKBELL": "Pine Bell Collar", "PURPLEBELL": "Purple Bell Collar",
                      "MULTIBELL": "Mulitcolored Bell Color", "CRIMSONBOW": "Crimson Bow", "BLUEBOW": "Blue Bow",
                      "YELLOWBOW": "Yellow Bow", "CYANBOW": "Cyan Bow", "REDBOW": "Red Bow", "LIMEBOW": "Lime Bow",
                      "GREENBOW": "Green Bow", "RAINBOWBOW": "Rainbow Bow", "BLACKBOW": "Black Bow",
                      "SPIKESBOW": "Spiked Bow", "PINKBOW": "Pink Bow", "PURPLEBOW": "Purple Bow",
                      "MULTIBOW": "Multicolored Bow", "WHITEBOW": "White Bow", "INDIGOBOW": "Indigo Bow",
                      "INDIGO": "Indigo Collar", "WHITE": "White Collar", "WHITEBELL": "White Bell Collar",
                      "INDIGOBELL": "Indigo Bell Collar", "CRIMSONNYLON": "Crimson Nylon Collar",
                      "BLUENYLON": "Blue Nylon Collar", "YELLOWNYLON": "Yellow Nylon Collar",
                      "CYANNYLON": "Cyan Nylon Collar", "REDNYLON": "Red Nylon Collar",
                      "LIMENYLON": "Line Nylon Collar", "GREENNYLON": "Green Nylon Collar",
                      "RAINBOWNYLON": "Rainbow Nylon Collar", "BLACKNYLON": "Black Nylon Collar",
                      "SPIKESNYLON": "Spiked Nylon Collar", "WHITENYLON": "White Nylon Collar",
                      "PINKNYLON": "Pink Nylon Collar", "PURPLENYLON": "Purple Nylon Collar",
                      "MULTINYLON": "Mulicolored Nylon Collar", "INDIGONYLON": "Indigo Nylon Collar",
                      "LUNA MOTH": "Luna Moth", "ATLAS MOTH": "Atlas Moth", "BIRD SKULL": "Bird Skull",
                      "IVY": "Ivy", "DAISY": "Daisy", "BUTTERFLIES": "Butterflies", "CLOVER": "Clover",
                      "ANTLERS": "Stick Antlers", "STICK": "Odd Stick", "FIREFLIES": "Fireflies", "WREATH": "Wreath",
                      "FLOWER WREATH": "Flower Wreath", "SPROUT": "Sprout", "MUSHROOM": "Mushrooms", "LILAC": "Lilac",
                      "SEAWEED": "Seaweed", "LILY PAD": "Lily Pads", "MONSTERA": "Monstera Leaf",
                      "WILD FLOWERS": "Wild Flowers", "TWIGS": "Twigs", "SHELL": "Shell", "CRYSTAL": "Crystal",
                      "SERPENT": "Snake Bones", "MOSS BALL": "Moss Ball", "CRIMSONFANG": "Crimson Fang", "BLUEFANG": "Blue Fang",
                      "YELLOWFANG": "Yellow Fang", "CYANFANG": "Cyan Fang", "REDFANG": "Red Fang", "LIMEFANG": "Lime Fang",
                      "GREENFANG": "Green Fang", "RAINBOWFANG": "Rainbow Fang", "BLACKFANG": "Black Fang", "SPIKESFANG": "Spikes Fang",
                      "WHITEFANG": "White Fang", "PINKFANG": "Pink Fang", "PURPLEFANG": "Purple Fang", 
                      "MULTIFANG": "Multi Fang", "INDIGOFANG": "Indigo Fang"})


accessories = sort_bidict(accessories, None)

platforms = {"None": None,
             "Greenleaf Plains - Day": "resources/images/platforms/plains/greenleaf_light.png",
             "Leaf-fall Plains - Day": "resources/images/platforms/plains/leaffall_light.png",
             "Leaf-bare Plains - Day": "resources/images/platforms/plains/leafbare_light.png",
             "Newleaf Plains - Day": "resources/images/platforms/plains/newleaf_light.png",
             "Greenleaf Plains - Night": "resources/images/platforms/plains/greenleaf_dark.png",
             "Leaf-fall Plains - Night": "resources/images/platforms/plains/leaffall_dark.png",
             "Leaf-bare Plains - Night": "resources/images/platforms/plains/leafbare_dark.png",
             "Newleaf Plains - Night": "resources/images/platforms/plains/newleaf_dark.png",
             "Greenleaf Forest - Day": "resources/images/platforms/forest/greenleaf_light.png",
             "Leaf-fall Forest - Day": "resources/images/platforms/forest/leaffall_light.png",
             "Leaf-bare Forest - Day": "resources/images/platforms/forest/leafbare_light.png",
             "Newleaf Forest - Day": "resources/images/platforms/forest/newleaf_light.png",
             "Greenleaf Forest - Night": "resources/images/platforms/forest/greenleaf_dark.png",
             "Leaf-fall Forest - Night": "resources/images/platforms/forest/leaffall_dark.png",
             "Leaf-bare Forest - Night": "resources/images/platforms/forest/leafbare_dark.png",
             "Newleaf Forest - Night": "resources/images/platforms/forest/newleaf_dark.png",
             "Greenleaf Mountains - Day": "resources/images/platforms/mountainous/greenleaf_light.png",
             "Leaf-fall Mountains - Day": "resources/images/platforms/mountainous/leaffall_light.png",
             "Leaf-bare Mountains - Day": "resources/images/platforms/mountainous/leafbare_light.png",
             "Newleaf Mountains - Day": "resources/images/platforms/mountainous/newleaf_light.png",
             "Greenleaf Mountains - Night": "resources/images/platforms/mountainous/greenleaf_dark.png",
             "Leaf-fall Mountains - Night": "resources/images/platforms/mountainous/leaffall_dark.png",
             "Leaf-bare Mountains - Night": "resources/images/platforms/mountainous/leafbare_dark.png",
             "Newleaf Mountains - Night": "resources/images/platforms/mountainous/newleaf_dark.png",
             "Greenleaf Beach - Day": "resources/images/platforms/beach/greenleaf_light.png",
             "Leaf-fall Beach - Day": "resources/images/platforms/beach/leaffall_light.png",
             "Leaf-bare Beach - Day": "resources/images/platforms/beach/leafbare_light.png",
             "Newleaf Beach - Day": "resources/images/platforms/beach/newleaf_light.png",
             "Greenleaf Beach - Night": "resources/images/platforms/beach/greenleaf_dark.png",
             "Leaf-fall Beach - Night": "resources/images/platforms/beach/leaffall_dark.png",
             "Leaf-bare Beach - Night": "resources/images/platforms/beach/leafbare_dark.png",
             "Newleaf Beach - Night": "resources/images/platforms/beach/newleaf_dark.png",
             "Dark Forest - Light": "resources/images/platforms/darkforestplatform_light.png",
             "Dark Forest - Dark": "resources/images/platforms/darkforestplatform_dark.png",
             "StarClan": "resources/images/platforms/starclanplatform_dark.png"}

lineart = ["Normal", "StarClan", "Dark Forest"]

poses = {
    "short": {
        "newborn": {
            "1": 38,
            "2": 38,
            "3": 38,
            "4": 38,
            "5": 38,
            "6": 38
        },
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 0,
            "5": 1,
            "6": 2
        },
        "adolescent": {
            "1": 6,
            "2": 7,
            "3": 8,
            "4": 6,
            "5": 7,
            "6": 8
        },
        "adult": {
            "1": 12,
            "2": 13,
            "3": 14,
            "4": 15,
            "5": 16,
            "6": 17
        },
        "senior": {
            "1": 24,
            "2": 25,
            "3": 26,
            "4": 24,
            "5": 25,
            "6": 26
        }
    },
    "long": {
        "newborn": {
            "1": 38,
            "2": 38,
            "3": 38,
            "4": 38,
            "5": 38,
            "6": 38
        },
        "kitten": {
            "1": 3,
            "2": 4,
            "3": 5,
            "4": 3,
            "5": 4,
            "6": 5
        },
        "adolescent": {
            "1": 9,
            "2": 10,
            "3": 11,
            "4": 9,
            "5": 10,
            "6": 11
        },
        "adult": {
            "1": 18,
            "2": 19,
            "3": 20,
            "4": 21,
            "5": 22,
            "6": 23
        },
        "senior": {
            "1": 27,
            "2": 28,
            "3": 29,
            "4": 27,
            "5": 28,
            "6": 29
        }
    }
}