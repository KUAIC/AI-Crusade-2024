"""Color mappings"""

from typing import List

TRIVIA = {
    "#B47878": "building;edifice",
    "#06E6E6": "sky",
    "#04C803": "tree",
    "#8C8C8C": "road;route",
    "#04FA07": "grass",
    "#96053D": "person;individual;someone;somebody;mortal;soul",
    "#CCFF04": "plant;flora;plant;life",
    "#787846": "earth;ground",
    "#FF09E0": "house",
    "#0066C8": "car;auto;automobile;machine;motorcar",
    "#3DE6FA": "water",
    "#FF3D06": "railing;rail",
    "#FF5C00": "arcade;machine",
    "#FFE000": "stairs;steps",
    "#00F5FF": "fan",
    "#FF008F": "step;stair",
    "#1F00FF": "stairway;staircase",
    "#FFD600": "radiator",
}

OBJECTS = {
    "#CC05FF": "bed",
    "#FF0633": "painting;picture",
    "#DCDCDC": "mirror",
    "#00FF14": "box",
    "#FF0000": "flower",
    "#FFA300": "book",
    "#00FFC2": "television;television;receiver;television;set;tv;tv;set;idiot;box;boob;tube;telly;goggle;box",
    "#F500FF": "pot;flowerpot",
    "#00FFCC": "vase",
    "#29FF00": "tray",
    "#8FFF00": "poster;posting;placard;notice;bill;card",
    "#5CFF00": "basket;handbasket",
    "#00ADFF": "screen;door;screen",
}


SITTING = {
    "#0B66FF": "sofa;couch;lounge",
    "#CC4603": "chair",
    "#07FFE0": "seat",
    "#08FFD6": "armchair",
    "#FFC207": "cushion",
    "#00EBFF": "pillow",
    "#00D6FF": "stool",
    "#1400FF": "blanket;cover",
    "#0A00FF": "swivel;chair",
    "#FF9900": "ottoman;pouf;pouffe;puff;hassock",
}

LIGHTING = {
    "#E0FF08": "lamp",
    "#FFAD00": "light;light;source",
    "#001FFF": "chandelier;pendant;pendent",
}

TABLES = {
    "#FF0652": "table",
    "#0AFF47": "desk",
}

CLOSETS = {
    "#E005FF": "cabinet",
    "#FF0747": "shelf",
    "#07FFFF": "wardrobe;closet;press",
    "#0633FF": "chest;of;drawers;chest;bureau;dresser",
    "#0000FF": "case;display;case;showcase;vitrine",
}


BATHROOM = {
    "#6608FF": "bathtub;bathing;tub;bath;tub",
    "#00FF85": "toilet;can;commode;crapper;pot;potty;stool;throne",
    "#0085FF": "shower",
    "#FF0066": "towel",
}

WINDOWS = {
    "#FF3307": "curtain;drape;drapery;mantle;pall",
    "#E6E6E6": "windowpane;window",
    "#00FF3D": "awning;sunshade;sunblind",
    "#003DFF": "blind;screen",
}

FLOOR = {
    "#FF095C": "rug;carpet;carpeting",
    "#503232": "floor;flooring",
}

INTERIOR = {
    "#787878": "wall",
    "#787850": "ceiling",
    "#08FF33": "door;double;door",
}

KITCHEN = {
    "#00FF29": "kitchen;island",
    "#14FF00": "refrigerator;icebox",
    "#00A3FF": "sink",
    "#EB0CFF": "counter",
    "#D6FF00": "dishwasher;dish;washer;dishwashing;machine",
    "#FF00EB": "microwave;microwave;oven",
    "#47FF00": "oven",
    "#66FF00": "clock",
    "#00FFB8": "plate",
    "#19C2C2": "glass;drinking;glass",
    "#00FF99": "bar",
    "#00FF0A": "bottle",
    "#FF7000": "buffet;counter;sideboard",
    "#B800FF": "washer;automatic;washer;washing;machine",
    "#00FF70": "coffee;table;cocktail;table",
    "#008FFF": "countertop",
    "#33FF00": "stove;kitchen;stove;range;kitchen;range;cooking;stove",
}

LIVINGROOM = {
    "#FA0A0F": "fireplace;hearth;open;fireplace",
    "#FF4700": "pool;table;billiard;table;snooker;table",
}

OFFICE = {
    "#00FFAD": "computer;computing;machine;computing;device;data;processor;electronic;computer;information;processing;system",
    "#00FFF5": "bookcase",
    "#0633FF": "chest;of;drawers;chest;bureau;dresser",
    "#005CFF": "monitor;monitoring;device",
}


COLOR_MAPPING_CATEGORY_ = {
    "keep background": {"#FFFFFF": "background"},
    "trivia": TRIVIA,
    "objects": OBJECTS,
    "sitting": SITTING,
    "lighting": LIGHTING,
    "tables": TABLES,
    "closets": CLOSETS,
    "bathroom": BATHROOM,
    "windows": WINDOWS,
    "floor": FLOOR,
    "interior": INTERIOR,
    "kitchen": KITCHEN,
    "livingroom": LIVINGROOM,
    "office": OFFICE,
}


COLOR_MAPPING_ = {
    "#FFFFFF": "background",
    "#787878": "wall",
    "#B47878": "building;edifice",
    "#06E6E6": "sky",
    "#503232": "floor;flooring",
    "#04C803": "tree",
    "#787850": "ceiling",
    "#8C8C8C": "road;route",
    "#CC05FF": "bed",
    "#E6E6E6": "windowpane;window",
    "#04FA07": "grass",
    "#E005FF": "cabinet",
    "#EBFF07": "sidewalk;pavement",
    "#96053D": "person;individual;someone;somebody;mortal;soul",
    "#787846": "earth;ground",
    "#08FF33": "door;double;door",
    "#FF0652": "table",
    "#8FFF8C": "mountain;mount",
    "#CCFF04": "plant;flora;plant;life",
    "#FF3307": "curtain;drape;drapery;mantle;pall",
    "#CC4603": "chair",
    "#0066C8": "car;auto;automobile;machine;motorcar",
    "#3DE6FA": "water",
    "#FF0633": "painting;picture",
    "#0B66FF": "sofa;couch;lounge",
    "#FF0747": "shelf",
    "#FF09E0": "house",
    "#0907E6": "sea",
    "#DCDCDC": "mirror",
    "#FF095C": "rug;carpet;carpeting",
    "#7009FF": "field",
    "#08FFD6": "armchair",
    "#07FFE0": "seat",
    "#FFB806": "fence;fencing",
    "#0AFF47": "desk",
    "#FF290A": "rock;stone",
    "#07FFFF": "wardrobe;closet;press",
    "#E0FF08": "lamp",
    "#6608FF": "bathtub;bathing;tub;bath;tub",
    "#FF3D06": "railing;rail",
    "#FFC207": "cushion",
    "#FF7A08": "base;pedestal;stand",
    "#00FF14": "box",
    "#FF0829": "column;pillar",
    "#FF0599": "signboard;sign",
    "#0633FF": "chest;of;drawers;chest;bureau;dresser",
    "#EB0CFF": "counter",
    "#A09614": "sand",
    "#00A3FF": "sink",
    "#8C8C8C": "skyscraper",
    "#FA0A0F": "fireplace;hearth;open;fireplace",
    "#14FF00": "refrigerator;icebox",
    "#1FFF00": "grandstand;covered;stand",
    "#FF1F00": "path",
    "#FFE000": "stairs;steps",
    "#99FF00": "runway",
    "#0000FF": "case;display;case;showcase;vitrine",
    "#FF4700": "pool;table;billiard;table;snooker;table",
    "#00EBFF": "pillow",
    "#00ADFF": "screen;door;screen",
    "#1F00FF": "stairway;staircase",
    "#0BC8C8": "river",
    "#FF5200": "bridge;span",
    "#00FFF5": "bookcase",
    "#003DFF": "blind;screen",
    "#00FF70": "coffee;table;cocktail;table",
    "#00FF85": "toilet;can;commode;crapper;pot;potty;stool;throne",
    "#FF0000": "flower",
    "#FFA300": "book",
    "#FF6600": "hill",
    "#C2FF00": "bench",
    "#008FFF": "countertop",
    "#33FF00": "stove;kitchen;stove;range;kitchen;range;cooking;stove",
    "#0052FF": "palm;palm;tree",
    "#00FF29": "kitchen;island",
    "#00FFAD": "computer;computing;machine;computing;device;data;processor;electronic;computer;information;processing;system",
    "#0A00FF": "swivel;chair",
    "#ADFF00": "boat",
    "#00FF99": "bar",
    "#FF5C00": "arcade;machine",
    "#FF00FF": "hovel;hut;hutch;shack;shanty",
    "#FF00F5": "bus;autobus;coach;charabanc;double-decker;jitney;motorbus;motorcoach;omnibus;passenger;vehicle",
    "#FF0066": "towel",
    "#FFAD00": "light;light;source",
    "#FF0014": "truck;motortruck",
    "#FFB8B8": "tower",
    "#001FFF": "chandelier;pendant;pendent",
    "#00FF3D": "awning;sunshade;sunblind",
    "#0047FF": "streetlight;street;lamp",
    "#FF00CC": "booth;cubicle;stall;kiosk",
    "#00FFC2": "television;television;receiver;television;set;tv;tv;set;idiot;box;boob;tube;telly;goggle;box",
    "#00FF52": "airplane;aeroplane;plane",
    "#000AFF": "dirt;track",
    "#0070FF": "apparel;wearing;apparel;dress;clothes",
    "#3300FF": "pole",
    "#00C2FF": "land;ground;soil",
    "#007AFF": "bannister;banister;balustrade;balusters;handrail",
    "#00FFA3": "escalator;moving;staircase;moving;stairway",
    "#FF9900": "ottoman;pouf;pouffe;puff;hassock",
    "#00FF0A": "bottle",
    "#FF7000": "buffet;counter;sideboard",
    "#8FFF00": "poster;posting;placard;notice;bill;card",
    "#5200FF": "stage",
    "#A3FF00": "van",
    "#FFEB00": "ship",
    "#08B8AA": "fountain",
    "#8500FF": "conveyer;belt;conveyor;belt;conveyer;conveyor;transporter",
    "#00FF5C": "canopy",
    "#B800FF": "washer;automatic;washer;washing;machine",
    "#FF001F": "plaything;toy",
    "#00B8FF": "swimming;pool;swimming;bath;natatorium",
    "#00D6FF": "stool",
    "#FF0070": "barrel;cask",
    "#5CFF00": "basket;handbasket",
    "#00E0FF": "waterfall;falls",
    "#70E0FF": "tent;collapsible;shelter",
    "#46B8A0": "bag",
    "#A300FF": "minibike;motorbike",
    "#9900FF": "cradle",
    "#47FF00": "oven",
    "#FF00A3": "ball",
    "#FFCC00": "food;solid;food",
    "#FF008F": "step;stair",
    "#00FFEB": "tank;storage;tank",
    "#85FF00": "trade;name;brand;name;brand;marque",
    "#FF00EB": "microwave;microwave;oven",
    "#F500FF": "pot;flowerpot",
    "#FF007A": "animal;animate;being;beast;brute;creature;fauna",
    "#FFF500": "bicycle;bike;wheel;cycle",
    "#0ABED4": "lake",
    "#D6FF00": "dishwasher;dish;washer;dishwashing;machine",
    "#00CCFF": "screen;silver;screen;projection;screen",
    "#1400FF": "blanket;cover",
    "#FFFF00": "sculpture",
    "#0099FF": "hood;exhaust;hood",
    "#0029FF": "sconce",
    "#00FFCC": "vase",
    "#2900FF": "traffic;light;traffic;signal;stoplight",
    "#29FF00": "tray",
    "#AD00FF": "ashcan;trash;can;garbage;can;wastebin;ash;bin;ash-bin;ashbin;dustbin;trash;barrel;trash;bin",
    "#00F5FF": "fan",
    "#4700FF": "pier;wharf;wharfage;dock",
    "#7A00FF": "crt;screen",
    "#00FFB8": "plate",
    "#005CFF": "monitor;monitoring;device",
    "#B8FF00": "bulletin;board;notice;board",
    "#0085FF": "shower",
    "#FFD600": "radiator",
    "#19C2C2": "glass;drinking;glass",
    "#66FF00": "clock",
    "#5C00FF": "flag",
}


def ade_palette() -> List[List[int]]:
    """ADE20K palette that maps each class to RGB values."""
    return [
        [120, 120, 120],
        [180, 120, 120],
        [6, 230, 230],
        [80, 50, 50],
        [4, 200, 3],
        [120, 120, 80],
        [140, 140, 140],
        [204, 5, 255],
        [230, 230, 230],
        [4, 250, 7],
        [224, 5, 255],
        [235, 255, 7],
        [150, 5, 61],
        [120, 120, 70],
        [8, 255, 51],
        [255, 6, 82],
        [143, 255, 140],
        [204, 255, 4],
        [255, 51, 7],
        [204, 70, 3],
        [0, 102, 200],
        [61, 230, 250],
        [255, 6, 51],
        [11, 102, 255],
        [255, 7, 71],
        [255, 9, 224],
        [9, 7, 230],
        [220, 220, 220],
        [255, 9, 92],
        [112, 9, 255],
        [8, 255, 214],
        [7, 255, 224],
        [255, 184, 6],
        [10, 255, 71],
        [255, 41, 10],
        [7, 255, 255],
        [224, 255, 8],
        [102, 8, 255],
        [255, 61, 6],
        [255, 194, 7],
        [255, 122, 8],
        [0, 255, 20],
        [255, 8, 41],
        [255, 5, 153],
        [6, 51, 255],
        [235, 12, 255],
        [160, 150, 20],
        [0, 163, 255],
        [140, 140, 140],
        [250, 10, 15],
        [20, 255, 0],
        [31, 255, 0],
        [255, 31, 0],
        [255, 224, 0],
        [153, 255, 0],
        [0, 0, 255],
        [255, 71, 0],
        [0, 235, 255],
        [0, 173, 255],
        [31, 0, 255],
        [11, 200, 200],
        [255, 82, 0],
        [0, 255, 245],
        [0, 61, 255],
        [0, 255, 112],
        [0, 255, 133],
        [255, 0, 0],
        [255, 163, 0],
        [255, 102, 0],
        [194, 255, 0],
        [0, 143, 255],
        [51, 255, 0],
        [0, 82, 255],
        [0, 255, 41],
        [0, 255, 173],
        [10, 0, 255],
        [173, 255, 0],
        [0, 255, 153],
        [255, 92, 0],
        [255, 0, 255],
        [255, 0, 245],
        [255, 0, 102],
        [255, 173, 0],
        [255, 0, 20],
        [255, 184, 184],
        [0, 31, 255],
        [0, 255, 61],
        [0, 71, 255],
        [255, 0, 204],
        [0, 255, 194],
        [0, 255, 82],
        [0, 10, 255],
        [0, 112, 255],
        [51, 0, 255],
        [0, 194, 255],
        [0, 122, 255],
        [0, 255, 163],
        [255, 153, 0],
        [0, 255, 10],
        [255, 112, 0],
        [143, 255, 0],
        [82, 0, 255],
        [163, 255, 0],
        [255, 235, 0],
        [8, 184, 170],
        [133, 0, 255],
        [0, 255, 92],
        [184, 0, 255],
        [255, 0, 31],
        [0, 184, 255],
        [0, 214, 255],
        [255, 0, 112],
        [92, 255, 0],
        [0, 224, 255],
        [112, 224, 255],
        [70, 184, 160],
        [163, 0, 255],
        [153, 0, 255],
        [71, 255, 0],
        [255, 0, 163],
        [255, 204, 0],
        [255, 0, 143],
        [0, 255, 235],
        [133, 255, 0],
        [255, 0, 235],
        [245, 0, 255],
        [255, 0, 122],
        [255, 245, 0],
        [10, 190, 212],
        [214, 255, 0],
        [0, 204, 255],
        [20, 0, 255],
        [255, 255, 0],
        [0, 153, 255],
        [0, 41, 255],
        [0, 255, 204],
        [41, 0, 255],
        [41, 255, 0],
        [173, 0, 255],
        [0, 245, 255],
        [71, 0, 255],
        [122, 0, 255],
        [0, 255, 184],
        [0, 92, 255],
        [184, 255, 0],
        [0, 133, 255],
        [255, 214, 0],
        [25, 194, 194],
        [102, 255, 0],
        [92, 0, 255],
    ]
