"""
harvesting.py
Comprehensive harvesting database for RPG / Survival / MMO games.
"""

class Harvesting:

    FISH = {
        "anchovy":"Anchovy","sardine":"Sardine","trout":"Trout","salmon":"Salmon",
        "tuna":"Tuna","cod":"Cod","mackerel":"Mackerel","halibut":"Halibut",
        "catfish":"Catfish","eel":"Eel","lobster":"Lobster","crab":"Crab",
        "shrimp":"Shrimp","octopus":"Octopus","squid":"Squid","shark":"Shark",
        "swordfish":"Swordfish","marlin":"Marlin","sturgeon":"Sturgeon"
    }

    ORES = {
        "iron":"Iron Ore","coal":"Coal","gold":"Gold Ore","silver":"Silver Ore",
        "copper":"Copper Ore","tin":"Tin Ore","lead":"Lead Ore","zinc":"Zinc Ore",
        "nickel":"Nickel Ore","aluminum":"Aluminum Ore","cobalt":"Cobalt Ore",
        "titanium":"Titanium Ore","manganese":"Manganese Ore",
        "chromium":"Chromium Ore","vanadium":"Vanadium Ore",
        "lithium":"Lithium Ore","uranium":"Uranium Ore",
        "platinum":"Platinum Ore","palladium":"Palladium Ore",
        "rhodium":"Rhodium Ore","iridium":"Iridium Ore",
        "osmium":"Osmium Ore","ruthenium":"Ruthenium Ore",
        "tungsten":"Tungsten Ore","molybdenum":"Molybdenum Ore",
        "tantalum":"Tantalum Ore","cadmium":"Cadmium Ore",
        "bismuth":"Bismuth Ore","antimony":"Antimony Ore"
    }

    GEMS = {
        "diamond":"Diamond","emerald":"Emerald","ruby":"Ruby",
        "sapphire":"Sapphire","amethyst":"Amethyst","topaz":"Topaz",
        "opal":"Opal","turquoise":"Turquoise","onyx":"Onyx",
        "peridot":"Peridot","zircon":"Zircon","aquamarine":"Aquamarine",
        "garnet":"Garnet","citrine":"Citrine","tanzanite":"Tanzanite",
        "alexandrite":"Alexandrite","moonstone":"Moonstone","jade":"Jade"
    }

    MINERALS = {
        "quartz":"Quartz","graphite":"Graphite","gypsum":"Gypsum","apatite":"Apatite","kaolinite":"Kaolinite",
        "olivine":"Olivine","selenium":"Selenium","tellurium":"Tellurium","arsenic":"Arsenic","phosphorus":"Phosphorus",
        "calcite":"Calcite","fluorite":"Fluorite","halite":"Halite","mica":"Mica","feldspar":"Feldspar",
        "talc":"Talc","barite":"Barite","celestine":"Celestine","corundum":"Corundum","beryl":"Beryl",
        "tourmaline":"Tourmaline","spodumene":"Spodumene","cassiterite":"Cassiterite","wolframite":"Wolframite",
        "chromite":"Chromite","malachite":"Malachite","azurite":"Azurite","galena":"Galena","hematite":"Hematite",
        "magnetite":"Magnetite","pyrite":"Pyrite","chalcopyrite":"Chalcopyrite","bornite":"Bornite",
        "sphalerite":"Sphalerite","cinnabar":"Cinnabar","rutile":"Rutile","ilmenite":"Ilmenite",
        "garnierite":"Garnierite","monazite":"Monazite","bastnasite":"Bastnasite"
    }

    STONES = {
        "granite":"Granite","basalt":"Basalt","marble":"Marble","limestone":"Limestone","slate":"Slate",
        "sandstone":"Sandstone","shale":"Shale","obsidian":"Obsidian","andesite":"Andesite","diorite":"Diorite",
        "gneiss":"Gneiss","schist":"Schist","rhyolite":"Rhyolite","dolomite":"Dolomite","travertine":"Travertine",
        "quartzite":"Quartzite","conglomerate":"Conglomerate","breccia":"Breccia","chalk":"Chalk","flint":"Flint",
        "soapstone":"Soapstone","pumice":"Pumice","scoria":"Scoria","tuff":"Tuff","pegmatite":"Pegmatite",
        "mudstone":"Mudstone","siltstone":"Siltstone","arkose":"Arkose","laterite":"Laterite","serpentinite":"Serpentinite"
    }

    WOODS = {
        "oak":"Oak Log","pine":"Pine Log","birch":"Birch Log",
        "spruce":"Spruce Log","cedar":"Cedar Log","maple":"Maple Log",
        "ash":"Ash Log","willow":"Willow Log","mahogany":"Mahogany Log",
        "teak":"Teak Log","ebony":"Ebony Log","rosewood":"Rosewood Log",
        "yew":"Yew Log","redwood":"Redwood Log","ironwood":"Ironwood Log",
        "blackwood":"Blackwood Log","sandalwood":"Sandalwood Log",
        "bloodwood":"Bloodwood Log","dragonwood":"Dragonwood Log",
        "crystalwood":"Crystalwood Log","world_tree":"World Tree Log"
    }

    HERBS = {
        "mint":"Mint","sage":"Sage","rosemary":"Rosemary","lavender":"Lavender","ginseng":"Ginseng",
        "aloe":"Aloe","chamomile":"Chamomile","thyme":"Thyme","basil":"Basil","nettle":"Nettle",
        "mandrake":"Mandrake","nightshade":"Nightshade","oregano":"Oregano","parsley":"Parsley",
        "cilantro":"Cilantro","dill":"Dill","fennel":"Fennel","lemongrass":"Lemongrass","catnip":"Catnip",
        "echinacea":"Echinacea","valerian":"Valerian","yarrow":"Yarrow","wormwood":"Wormwood",
        "comfrey":"Comfrey","mugwort":"Mugwort","plantain":"Plantain Herb","bay_leaf":"Bay Leaf",
        "marjoram":"Marjoram","tarragon":"Tarragon","saffron":"Saffron"
    }

    MUSHROOMS = {
        "button":"Button Mushroom","shiitake":"Shiitake","oyster":"Oyster Mushroom","chanterelle":"Chanterelle",
        "morel":"Morel","truffle":"Black Truffle","glowcap":"Glowcap Mushroom","shadowcap":"Shadowcap Mushroom",
        "portobello":"Portobello","enoki":"Enoki","porcini":"Porcini","lion_mane":"Lion's Mane",
        "wood_ear":"Wood Ear","reishi":"Reishi","turkey_tail":"Turkey Tail","death_cap":"Death Cap",
        "fly_agaric":"Fly Agaric","blewit":"Blewit","hedgehog":"Hedgehog Mushroom","puffball":"Puffball"
    }

    CROPS = {
        "wheat":"Wheat","barley":"Barley","oats":"Oats","corn":"Corn","rice":"Rice","soybean":"Soybean",
        "sugarcane":"Sugarcane","cotton":"Cotton","coffee":"Coffee Beans","cocoa":"Cocoa Beans",
        "rye":"Rye","millet":"Millet","sorghum":"Sorghum","quinoa":"Quinoa","buckwheat":"Buckwheat",
        "sunflower":"Sunflower","canola":"Canola","peanut":"Peanut","sesame":"Sesame","flax":"Flax",
        "tea":"Tea Leaf","tobacco":"Tobacco","lentil":"Lentil","chickpea":"Chickpea","bean":"Bean"
    }

    FRUITS = {
        "apple":"Apple","banana":"Banana","orange":"Orange","mango":"Mango","grape":"Grape",
        "pear":"Pear","peach":"Peach","pineapple":"Pineapple","watermelon":"Watermelon","dragonfruit":"Dragon Fruit",
        "papaya":"Papaya","guava":"Guava","lychee":"Lychee","rambutan":"Rambutan","durian":"Durian",
        "jackfruit":"Jackfruit","coconut":"Coconut","lemon":"Lemon","lime":"Lime","cherry":"Cherry",
        "plum":"Plum","apricot":"Apricot","fig":"Fig","pomegranate":"Pomegranate","kiwi":"Kiwi"
    }

    VEGETABLES = {
        "carrot":"Carrot","potato":"Potato","tomato":"Tomato","onion":"Onion","cabbage":"Cabbage",
        "lettuce":"Lettuce","broccoli":"Broccoli","cucumber":"Cucumber","pumpkin":"Pumpkin","spinach":"Spinach",
        "kale":"Kale","cauliflower":"Cauliflower","beetroot":"Beetroot","radish":"Radish","turnip":"Turnip",
        "eggplant":"Eggplant","zucchini":"Zucchini","bell_pepper":"Bell Pepper","chili":"Chili Pepper",
        "garlic":"Garlic","leek":"Leek","celery":"Celery","okra":"Okra","peas":"Peas","yam":"Yam"
    }

    LIVESTOCK = {
        "milk":"Milk","egg":"Egg","wool":"Wool","feather":"Feather","leather":"Leather",
        "fur":"Fur","horn":"Horn","goat_milk":"Goat Milk","duck_egg":"Duck Egg","goose_feather":"Goose Feather",
        "alpaca_wool":"Alpaca Wool","yak_milk":"Yak Milk","bee_wax":"Bee Wax","royal_jelly":"Royal Jelly",
        "silkworm_cocoon":"Silkworm Cocoon"
    }

    MONSTER_DROPS = {
        "slime_gel":"Slime Gel","goblin_ear":"Goblin Ear","wolf_fang":"Wolf Fang","spider_silk":"Spider Silk",
        "dragon_scale":"Dragon Scale","dragon_claw":"Dragon Claw","phoenix_feather":"Phoenix Feather",
        "wyvern_tooth":"Wyvern Tooth","troll_hide":"Troll Hide","orc_tusk":"Orc Tusk",
        "skeleton_bone":"Skeleton Bone","zombie_flesh":"Zombie Flesh","demon_horn":"Demon Horn",
        "ghost_essence":"Ghost Essence","kraken_ink":"Kraken Ink","basilisk_eye":"Basilisk Eye",
        "griffin_feather":"Griffin Feather","minotaur_horn":"Minotaur Horn","hydra_scale":"Hydra Scale",
        "vampire_fang":"Vampire Fang","werewolf_pelt":"Werewolf Pelt","lich_dust":"Lich Dust",
        "golem_core":"Golem Core","elemental_shard":"Elemental Shard","fairy_dust":"Fairy Dust"
    }

    FOSSILS = {
        "ammonite":"Ammonite Fossil","trilobite":"Trilobite Fossil","dinosaur_bone":"Dinosaur Bone",
        "ancient_skull":"Ancient Skull","mammoth_tusk":"Mammoth Tusk","fossil_leaf":"Fossil Leaf",
        "fossil_fish":"Fossil Fish","amber_insect":"Amber Insect","raptor_claw":"Raptor Claw Fossil",
        "ancient_shell":"Ancient Shell Fossil"
    }

    ARTIFACTS = {
        "ancient_coin":"Ancient Coin","relic_tablet":"Relic Tablet","lost_compass":"Lost Compass",
        "golden_idol":"Golden Idol","crystal_skull":"Crystal Skull","sun_relic":"Sun Relic",
        "moon_relic":"Moon Relic","forgotten_crown":"Forgotten Crown","royal_seal":"Royal Seal",
        "ancient_map":"Ancient Map","runic_stone":"Runic Stone","timepiece":"Ancient Timepiece"
    }

    ALCHEMY = {
        "mana_flower":"Mana Flower","fire_blossom":"Fire Blossom","frost_leaf":"Frost Leaf",
        "shadow_essence":"Shadow Essence","light_essence":"Light Essence","arcane_dust":"Arcane Dust",
        "void_bloom":"Void Bloom","storm_petal":"Storm Petal","earth_root":"Earth Root",
        "water_orb":"Water Orb","phoenix_ash":"Phoenix Ash","dragon_blood":"Dragon Blood",
        "moon_dew":"Moon Dew","sun_sap":"Sun Sap","astral_pollen":"Astral Pollen"
    }

    BIOME_RESOURCES = {
        "cactus":"Cactus",
        "volcanic_ash":"Volcanic Ash",
        "glacier_crystal":"Glacier Crystal",
        "swamp_moss":"Swamp Moss",
        "jungle_vine":"Jungle Vine"
    }

    GATHERABLES = {
        "clay":"Clay","sand":"Sand","water":"Water","oil":"Oil","resin":"Resin","sap":"Sap",
        "charcoal":"Charcoal","peat":"Peat","seaweed":"Seaweed","bamboo":"Bamboo","honey":"Honey",
        "wax":"Beeswax","crystal":"Crystal","vine":"Vine","reed":"Reed","driftwood":"Driftwood",
        "cactus":"Cactus","coconut_fiber":"Coconut Fiber","seashell":"Seashell","coral":"Coral",
        "volcanic_ash":"Volcanic Ash","swamp_moss":"Swamp Moss","glacier_ice":"Glacier Ice",
        "jungle_vine":"Jungle Vine","cotton_fiber":"Cotton Fiber"
    }

    def mine(self, resource):
        resource = resource.lower()
        return (
            self.ORES.get(resource)
            or self.GEMS.get(resource)
            or self.MINERALS.get(resource)
            or self.STONES.get(resource)
        )

    def chop(self, wood):
        return self.WOODS.get(wood.lower())

    def fish(self, fish):
        return self.FISH.get(fish.lower())

    def gather_herb(self, herb):
        return self.HERBS.get(herb.lower())

    def gather_mushroom(self, mushroom):
        return self.MUSHROOMS.get(mushroom.lower())

    def harvest_crop(self, crop):
        return self.CROPS.get(crop.lower())

    def harvest_fruit(self, fruit):
        return self.FRUITS.get(fruit.lower())

    def harvest_vegetable(self, vegetable):
        return self.VEGETABLES.get(vegetable.lower())

    def gather(self, resource):
        resource = resource.lower()
        return (
            self.GATHERABLES.get(resource)
            or self.LIVESTOCK.get(resource)
            or self.MONSTER_DROPS.get(resource)
            or self.FOSSILS.get(resource)
            or self.ARTIFACTS.get(resource)
            or self.ALCHEMY.get(resource)
            or self.BIOME_RESOURCES.get(resource)
        )
