from random import choice
from scripts.cat.sprites import Sprites
import random
from re import sub
from scripts.game_structure.game_essentials import game
import scripts.global_vars as global_vars


    

class Pelt():
    
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'Tabby': 'tabby',
        'Marbled': 'marbled',
        'Rosette': 'rosette',
        'Smoke': 'smoke',
        'Ticked': 'ticked',
        'Speckled': 'speckled',
        'Bengal': 'bengal',
        'Mackerel': 'mackerel',
        'Classic': 'classic',
        'Sokoke': 'sokoke',
        'Agouti': 'agouti',
        'Singlestripe': 'singlestripe',
        'Abyssinian': 'abyssinian',
        'Brindle': 'brindle',
        'Braided': 'braided',
        'Splotch': 'splotch',
        'Saber': 'saber',
        'Faded': 'faded',
        'Masked': 'masked',
        'Tortie': None,
        'Calico': None
    }

    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'WHITE', 'SNOW WHITE', 'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE',
        'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'SILVER',
        'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST',
        'PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER',
        'PALE GOLD', 'YELLOW', 'GOLD', 'BRONZE', 'ROSE',
        'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD',
        'PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN',
        'PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE', 'BIRCH',
        'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'
    ]
    pelt_c_no_white = [
        'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE',
        'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'SILVER',
        'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST',
        'PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER',
        'PALE GOLD', 'YELLOW', 'GOLD', 'BRONZE', 'ROSE',
        'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD',
        'PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN',
        'PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE', 'BIRCH',
        'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'
    ]
    pelt_c_no_bw = [
        'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE',
        'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'SILVER',
        'PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER',
        'PALE GOLD', 'YELLOW', 'GOLD', 'BRONZE', 'ROSE',
        'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD',
        'PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN',
        'PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE', 'BIRCH',
        'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'
    ]


    tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'HALF', 'STREAK', 'MASK', 'SMOKE',
                      'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP', 'CHIMERA', 'CHEST', 'ARMTAIL', 'GRUMPYFACE',
                      'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'SMUDGED', 'DAUB', 'EMBER', 'BRIE',
                      'ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'DAPPLENIGHT', 'BLANKET', 'BELOVED',
                      'VIPER', 'SKULL', 'POINTS', 'DITTO', 'BODY', 'SHILOH', 'TABBY', 'SPECKLED', 'BENGAL', 'CLASSIC', 'MACKEREL', 'MARBLED',
                      'SABER', 'ROSETTE', 'MASKED', 'DUST']

    tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
                   'classic', 'sokoke', 'agouti', 'singlestripe', 'abyssinian', 'brindle', 'braided', 'splotch',
                   'saber', 'faded', 'masked']


    pelt_length = ["short", "medium", "long"]
    eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALE GREEN', 'GREEN', 'BLUE',
               'DARK BLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHER BLUE', 'SUN-LIT ICE',
               'COPPER', 'SAGE', 'BRIGHT BLUE', 'PALE BLUE', 'LAVENDER', 'DARK GREY',
               'PALE YELLOW', 'GOLD', 'LIME', 'HAZELNUT', 'DARK AMBER', 'SLATE',
               'RUBY', 'LILAC', 'LIGHT GREY', 'PINK', 'DARK HAZEL', 'CHOCOLATE']
    yellow_eyes = ['YELLOW', 'PALE YELLOW', 'GOLD']
    blue_eyes = ['BLUE', 'DARK BLUE', 'CYAN', 'SUN-LIT ICE', 'BRIGHT BLUE', 'PALE BLUE']
    green_eyes = ['HAZEL', 'PALE GREEN', 'GREEN', 'EMERALD', 'SAGE', 'LIME', 'DARK HAZEL']
    red_eyes = ['AMBER', 'COPPER', 'HAZELNUT', 'DARK AMBER', 'RUBY', 'CHOCOLATE']
    grey_eyes = ['GREY', 'DARK GREY', 'SLATE', 'LIGHT GREY']
    purple_eyes = ['HEATHER BLUE', 'LAVENDER', 'LILAC', 'PINK']
    # scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
    # bite scars by @wood pank on discord
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
            "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH", "HINDLEG",
            "BACK", "QUILLSIDE", "SCRATCHSIDE", "BEAKSIDE", "CATBITETWO", "FOUR"]
    scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
            "FROSTSOCK", "TOE", "SNAKETWO"]

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                        "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                        "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                        ]
    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                        ]
    tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
    living_accessories = ["LUNA MOTH", "ATLAS MOTH", "BUTTERFLIES", "FIREFLIES"]
    plant2_accessories = ["DAISY", "IVY", "CLOVER", "WREATH", "FLOWER WREATH", "WILD FLOWERS", "LILAC", "MONSTERA"]
    wild2_accessories = ["BIRD SKULL", "ANTLERS", "TWIGS", "SERPENT"]
    beach_accessories = ["SEAWEED", "SHELL"]
    mountain_accessories = ["CRYSTAL"]
    plains_accessories = ["SPROUT"]
    forest_accessories = ["MUSHROOM"]
    special_accessories = ["STICK", "MOSS BALL", "LILY PAD"]
    collars = [
        "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
        "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
        "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
        "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
        "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
        "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
        "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
        "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
        "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
    ]
    dog_collars = ["CRIMSONFANG", "BLUEFANG", "YELLOWFANG", "CYANFANG", "REDFANG", "LIMEFANG", "GREENFANG", "RAINBOWFANG",
        "BLACKFANG", "SPIKESFANG", "WHITEFANG", "PINKFANG", "PURPLEFANG", "MULTIFANG", "INDIGOFANG"]

    points = ["Ticked", "Agouti", "Smoke"]
    spots = ["Speckled", "Rosette", "Bengal"]
    swirls = ["Tabby", "Classic", "Sokoke", "Marbled"]
    flats = ["SingleColour", "TwoColour", "Singlestripe", "Abyssinian"]
    stripes = ["Mackerel", "Braided", "Brindle"]
    splotches = ["Splotch", "Masked"]
    exotic = ["Saber", "Faded"]
    torties = ["Tortie", "Calico"]
    pelt_categories = [points, spots, swirls, flats, stripes, splotches, exotic, torties]

    # SPRITE NAMES
    single_colours = [
        'WHITE', 'SNOW WHITE', 'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE', 'SILVER',
        'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST', 'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'PALE GOLD', 'PALE GINGER', 'ROSE',
        'YELLOW', 'GOLD', 'BRONZE', 'DARK GOLD', 'PALE FIRE', 'FIRE', 'DARK FIRE', 'GINGER', 'DARK GINGER', 'DARK ORANGE',
        'PALE BROWN', 'ALMOND', 'BIRCH', 'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'PALE CINNAMON', 'CINNAMON', 'SABLE',
        'DARK SABLE', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN'
    ]
    white_colours = ['WHITE', 'SNOW WHITE']
    blue_colours = ['PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC']
    gray_colours = ['GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE', 'SILVER']
    black_colours = ['BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST']
    cream_colours = ['LIGHT CREAM', 'CREAM', 'DARK CREAM', 'PALE GOLD', 'PALE GINGER', 'ROSE']
    gold_colours = ['YELLOW', 'GOLD', 'BRONZE', 'DARK GOLD']
    fire_colours = ['PALE FIRE', 'FIRE', 'DARK FIRE']
    ginger_colours = ['GINGER', 'DARK GINGER', 'DARK ORANGE']
    coolbrown_colours = ['PALE BROWN', 'ALMOND', 'BIRCH']
    lavender_colours = ['PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER']
    warmbrown_colours = ['PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE']
    brown_colours = ['ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN']
    colour_categories = [white_colours, blue_colours, gray_colours, black_colours, cream_colours, gold_colours,
                     fire_colours, ginger_colours, coolbrown_colours, lavender_colours, warmbrown_colours,
                     brown_colours]
    eye_sprites = [
        'YELLOW', 'AMBER', 'HAZEL', 'PALE GREEN', 'GREEN', 'BLUE', 'DARK BLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHER BLUE',
        'SUN-LIT ICE', 'COPPER', 'SAGE', 'BRIGHT BLUE', 'PALE BLUE', 'LAVENDER', 'DARK GREY', 'PALE YELLOW', 'GOLD', 'LIME',
        'HAZELNUT', 'DARK AMBER', 'SLATE', 'RUBY', 'LILAC', 'LIGHT GREY', 'PINK', 'DARK HAZEL', 'CHOCOLATE'
    ]
    eye_patterns = ['TRUE', 'CENTRAL', 'QUARTER', 'SLIVER', 'SPECKLES', 'FROSTED', 'RING', 'HALFCENTRAL', 'HALFRING', 'BUBBLE', 'OUTRING', 'SWAP']
    little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
                    'LUNA', 'EXTRA', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'REVERSEEYE', 'BACKSPOT',
                    'EYEBAGS', 'LOCKET', 'BLAZEMASK', 'TEARS']
    mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
                 'WINGS', 'MOSSY', 'CHANCE', 'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER', 'WOODPECKER', 'MISS', 'VENUS',
                 'BOWTIE', 'VEST', 'FADEBELLY', 'DIGIT', 'FCTWO', 'FCONE', 'MIA', 'ROSINA', 'PRINCESS', 'DOUGIE']
    high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
                  'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
                  'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'NIGHTMIST', 'FALCON', 'RETSUKO', 'SHIBAINU',
                  'SNOWSTORM', 'PEPPER', 'OWL', 'BUB', 'SPARROW', 'TRIXIE',
                  'SAMMY', 'FRONT', 'BLOSSOMSTEP', 'BULLSEYE', 'COWTWO', 'COWFOUR', 'COWSIX', 'COWEIGHT', 'COWELEVEN',
                  'FINN', 'SCAR', 'BUSTER', 'HAWKBLAZE', 'CAKE']
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO', 'MOTH', 'FRECKLEMASK', 'COW', 'TIDAL',
                    'DIAMOND', 'ECLIPSE', 'PEBBLESHINE', 'BOOTS', 'COWTHREE', 'COWFIVE', 'COWSEVEN', 'COWNINE', 'COWTEN',
                    'LOVEBUG', 'SHOOTINGSTAR', 'EYESPOT', 'PEBBLE', 'TAILTWO', 'BUDDY', 'BATWING', 'KROPKA']
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER', 'SPLAT', 'BLEACHED', 'SMOKEY']
    white_sprites = [
            little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

    skin_sprites = ['BLACK',  'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                    'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'RED']

    """Holds all appearence information for a cat. """
    def __init__(self,
                 name:str="SingleColour",
                 length:str="short",
                 colour:str="WHITE",
                 white_patches:str=None,
                 eye_color:str="BLUE",
                 eye_colour2:str=None,
                 eye_patterns:str=None,
                 tortiebase:str=None,
                 tortiecolour:str="GINGER",
                 pattern:str="ONE",
                 tortiepattern:str="single",
                 vitiligo:str=None,
                 points:str=None,
                 accessory:str=None,
                 paralyzed:bool=False,
                 opacity:int=100,
                 scars:list=None,
                 tint:str="none",
                 skin:str="BLACK",
                 white_patches_tint:str="none",
                 kitten_sprite:int=None,
                 adol_sprite:int=None,
                 adult_sprite:int=None,
                 senior_sprite:int=None,
                 para_adult_sprite:int=None,
                 reverse:bool=False,
                 ) -> None:
        self.name = name
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.eye_patterns = eye_patterns
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length=length
        self.points = points
        self.accessory = accessory
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scar_slot_list = [
            None,
            None,
            None,
            None
        ]
        self.tint = "none"
        self.white_patches_tint = white_patches_tint
        self.cat_sprites =  {
            "kitten": kitten_sprite if kitten_sprite is not None else 0,
            "adolescent": adol_sprite if adol_sprite is not None else 0,
            "young adult": adult_sprite if adult_sprite is not None else 0,
            "adult": adult_sprite if adult_sprite is not None else 0,
            "senior adult": adult_sprite if adult_sprite is not None else 0,
            "senior": senior_sprite if senior_sprite is not None else 0,
            "para_adult": para_adult_sprite if para_adult_sprite is not None else 0,
        }        
        self.cat_sprites['newborn'] = 38
        self.cat_sprites['para_young'] = 32
        self.cat_sprites["sick_adult"] = 36
        self.cat_sprites["sick_young"] = 37
        
        
        self.current_poses = {
            "newborn": "1",
            "kitten": "1",
            "adolescent": "1",
            "adult": "1",
            "senior": "1",
        }
        self.not_working = False
        self.stored_eye_color_2 = "BLUE"
        
        self.reverse = reverse
        self.skin = skin

    def randomize_pelt(self):
        
        self.init_pattern_color()
        self.init_white_patches()
        self.init_pose()
        self.init_scars()
        self.init_accessories()
        self.init_eyes()
        self.init_pattern()
        self.init_tint()
        
        self.paralyzed = choice([True, False])
        self.not_working = choice([True, False])
    
    #-------------------------------------------------------------------------------------------------#
    #                               Setter Functions                                                  #
    #-------------------------------------------------------------------------------------------------#
    
    def set_pose(self, age, pose):
        """Sets the pose, updating cat_sprites """
        if not pose:
            return
           
        if age in ["young adult", "adult", "senior adult"]:
            for inter_age in ["young adult", "adult", "senior adult"]:
                self.cat_sprites[inter_age] = global_vars.poses[
                self.length]["adult"][pose]

                # Adjust tracked poses.
            self.current_poses["adult"] = pose
        else:
            # Change the sprite number.
            self.cat_sprites[age] = global_vars.poses[
                self.length][age][pose]

            # Adjust tracked poses.
            self.current_poses[age] = pose
    
    def set_pelt_length(self, fur_length):
        if fur_length not in ["short", "long"]:
            return
        
        self.length = fur_length

        # Update the sprite numbers:
        for age in self.current_poses:
            self.set_pose(age, self.current_poses[age])

    #-------------------------------------------------------------------------------------------------#
    #                               Randomize Functions                                                  #
    #-------------------------------------------------------------------------------------------------#

    def init_eyes(self):
        
        self.eye_colour = choice(list(global_vars.eye_colors.keys()))
        
        if not random.randint(0, 4):
            self.eye_colour2 = choice(list(global_vars.eye_colors.keys()))
            valid_eye_patterns = [pattern for pattern in global_vars.eye_patterns.keys() if pattern is not None]
            self.eye_patterns = random.choice(valid_eye_patterns)
        else:
            self.eye_colour2 = None
            self.eye_patterns = None



    def init_pattern_color(self) -> bool:
        """Inits self.name, self.colour, self.length, 
            self.tortiebase """
        
        self.name = random.choice(list(global_vars.pelt_options.keys()) + ["Tortie"])
        self.tortiebase = random.choice(list(global_vars.tortie_patches_patterns.keys()))
        self.colour = random.choice(list(global_vars.colors.keys()))
        self.length = random.choice(["short", "long"])
        self.skin = choice(list(global_vars.skin_colors.keys()))
        
    def init_pose(self):

        poses = ["1", "2", "3", "4", "5", "6"]
        for age in self.current_poses:
            self.set_pose(age, random.choice(poses))
        
        self.reverse = choice([True, False])

    def init_scars(self):
        self.scar_slot_list = [
            None,
            None,
            None,
            None
        ]
        
        for i in range(0, len(self.scar_slot_list)):
            if random.randint(0, 1):
                self.scar_slot_list[i] = random.choice(list(global_vars.scars.keys()))
        
    def init_accessories(self):
        
        self.accessory = random.choice(list(global_vars.accessories.keys()))

    def init_pattern(self):
        
        self.pattern = random.choice(list(global_vars.tortie_patches_shapes.keys()))
        self.tortiecolour = random.choice(list(global_vars.colors.keys()))
        self.tortiepattern = random.choice(list(global_vars.tortie_patches_patterns.keys()))

    def init_white_patches(self):
         
        self.white_patches = choice(list(global_vars.white_patches.keys()))
        
        if random.random() > 0.5:
            self.points = choice(list(global_vars.points.keys()))
        else:
            self.points = None
        
        if random.random() > 0.9:
            self.vitiligo = choice(list(global_vars.vit.keys()))
        else:
            self.vitiligo = None
        
        
    def init_tint(self):
        """Sets tint for pelt and white patches"""

        self.tint = "none"
        self.white_patches_tint = choice(list(global_vars.white_patches_tint.keys()))

    @property
    def white(self):
        return self.white_patches or self.points
    
    @white.setter
    def white(self, val):
        print("Can't set pelt.white")
        return    

    @staticmethod
    def describe_appearance(cat, short=False):
        
        # Define look-up dictionaries
        if short:
            renamed_colors = {
                "white": "white",
                "snow white": "white",
                "gray": "gray",
                "slate": "gray",
                "dark gray": "gray",
                "dark slate": "gray",
                "pale blue": "blue",
                "blue": "blue",
                "lilac": "lilac",
                "pale lilac": "lilac",
                "silver": "silver",
                "black": "black",
                "soot black": "black",
                "obsidian": "black",
                "ghost": "black",
                "pale brown": "brown",
                "almond": "brown",
                "acorn": "brown",
                "light brown": "brown",
                "brown": "brown",
                "dark brown": "brown",
                "pale cinnamon": "ginger",
                "cinnamon": "ginger",
                "sable": "brown",
                "dark sable": "brown",
                "birch": "cream",
                "pale lavender": "lilac",
                "lavender": "lilac",
                "dark lavender": "lilac",
                "dark orange": "ginger",
                "pale fire": "ginger",
                "fire": "ginger",
                "dark fire": "ginger",
                "pale ginger": "ginger",
                "ginger": "ginger",
                "dark ginger": "ginger",
                "pale gold": "cream",
                "yellow": "cream",
                "gold": "gold",
                "bronze": "ginger",
                "rose": "ginger",
                "light cream": "cream",
                "cream": "cream",
                "dark cream": "cream",
                "dark gold": "gold"
            }
        else:
            renamed_colors = {
                "white": "white",
                "snow white": "snow white",
                "gray": "gray",
                "slate": "slate",
                "dark gray": "dark gray",
                "dark slate": "dark slate",
                "pale blue": "pale blue",
                "blue": "blue",
                "lilac": "lilac",
                "pale lilac": "pale lilac",
                "silver": "silver",
                "black": "black",
                "soot black": "soot black",
                "obsidian": "obsidian",
                "ghost": "ghost",
                "pale brown": "pale brown",
                "almond": "almond",
                "acorn": "acorn",
                "light brown": "light brown",
                "brown": "brown",
                "dark brown": "dark brown",
                "pale cinnamon": "pale cinnamon",
                "cinnamon": "cinnamon",
                "sable": "sable",
                "dark sable": "dark sable",
                "birch": "birch",
                "pale lavender": "pale lavender",
                "lavender": "lavender",
                "dark lavender": "dark lavender",
                "dark orange": "dark orange",
                "pale fire": "pale fire-red",
                "fire": "fire-red",
                "dark fire": "dark fire-red",
                "pale ginger": "pale ginger",
                "ginger": "ginger",
                "dark ginger": "dark ginger",
                "pale gold": "pale gold",
                "yellow": "yellow",
                "gold": "gold",
                "bronze": "bronze",
                "rose": "rose",
                "light cream": "light cream",
                "cream": "cream",
                "dark cream": "dark cream",
                "dark gold": "dark gold"
            }

        pattern_des = {
            "Tabby": "c_n tabby",
            "Speckled": "speckled c_n",
            "Bengal": "unusually dappled c_n",
            "Marbled": "c_n marbled tabby",
            "Ticked": "c_n ticked tabby",
            "Smoke": "c_n smoke",
            "Mackerel": "c_n mackerel tabby",
            "Classic": "c_n classic tabby",
            "Agouti": "c_n agouti tabby",
            "Singlestripe": "dorsal-striped c_n",
            "Rosette": "rosetted c_n",
            "Sokoke": "c_n sokoke tabby",
            "Abyssinian": "c_n abyssinian",
            "Brindle": "c_n brindle",
            "Braided": "c_n braided tabby",
            "Splotch": "unusually splotched c_n",
            "Saber": "c_n wild tabby",
            "Faded": "c_n faded tabby",
            "Masked": "c_n masked tabby"
        }

        # Start with determining the base color name. 
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]
        
        # Replace "white" with "pale" if the cat is 
        if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
            color_name = "pale"

        # Time to descibe the pattern and any additional colors. 
        if cat.pelt.name in pattern_des:
            color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
        elif cat.pelt.name in Pelt.torties:
            # Calicos and Torties need their own desciptions. 
            if short:
                # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                    color_name = "mottled"
                else:
                    color_name = cat.pelt.name.lower()
            else:
                base = cat.pelt.tortiebase.lower()
                if base in Pelt.tabbies + ['bengal', 'rosette', 'speckled']:
                    base = 'tabby'
                else:
                    base = ''

                patches_color = cat.pelt.tortiecolour.lower()
                if patches_color in renamed_colors:
                    patches_color = renamed_colors[patches_color]
                color_name = f"{color_name}/{patches_color}"
                
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                        color_name = f"{color_name} mottled"
                else:
                    color_name = f"{color_name} {cat.pelt.name.lower()}"

        if cat.pelt.white_patches:
            if cat.pelt.white_patches == "FULLWHITE":
                # If the cat is fullwhite, discard all other information. They are just white. 
                color_name = "white"
            if cat.pelt.white_patches in Pelt.mostly_white and cat.pelt.name != "Calico":
                color_name = f"white and {color_name}"
            elif cat.pelt.name != "Calico":
                color_name = f"{color_name} and white"
        
        if cat.pelt.points:
            color_name = f"{color_name} point"
            if "ginger point" in color_name:
                color_name.replace("ginger point", "flame point")

        if "white and white" in color_name:
            color_name = color_name.replace("white and white", "white")

        # Now it's time for gender
        if cat.genderalign in ["female", "trans female"]:
            color_name = f"{color_name} she-cat"
        elif cat.genderalign in ["male", "trans male"]:
            color_name = f"{color_name} tom"
        else:
            color_name = f"{color_name} cat"

        # Here is the place where we can add some additional details about the cat, for the full non-short one. 
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
        if not short:
            
            scar_details = {
                "NOTAIL": "no tail", 
                "HALFTAIL": "half a tail", 
                "NOPAW": "three legs", 
                "NOLEFTEAR": "a missing ear", 
                "NORIGHTEAR": "a missing ear",
                "NOEAR": "no ears"
            }

            additional_details = []
            if cat.pelt.vitiligo:
                additional_details.append("vitiligo")
            for scar in cat.pelt.scars:
                if scar in scar_details and scar_details[scar] not in additional_details:
                    additional_details.append(scar_details[scar])
            
            if len(additional_details) > 1:
                color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
            elif additional_details:
                color_name = f"{color_name} with {additional_details[0]}"
        
        
            if len(cat.pelt.scars) >= 3:
                color_name = f"scarred {color_name}"
            if cat.pelt.length == "long":
                color_name = f"long-furred {color_name}"

        return color_name
    
    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
