COLOURS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black"]

def w_to_json(filename, formula):
    file = open(filename, "w")
    for line in formula:
        file.write(line)
        file.write("\n")
    file.close()

def slab_blockstate_formula(colour, block):
    return ["{","  \"variants\": {","    \"type=bottom\": {",f"      \"model\": \"moreterracotta:block/{colour}_{block}_slab\"","    },","    \"type=double\": {",f"      \"model\": \"minecraft:block/{colour}_{block}\"","    },","    \"type=top\": {",f"      \"model\": \"moreterracotta:block/{colour}_{block}_slab_top\"","    }","  }","}"]

def slab_formula(top, colour, block):
    return ["{",f"  \"parent\": \"minecraft:block/slab{top}\",","  \"textures\": {",f"    \"bottom\": \"minecraft:block/{colour}_{block}\",",f"    \"top\": \"minecraft:block/{colour}_{block}\",",f"    \"side\": \"minecraft:block/{colour}_{block}\"","  }","}"]

def slab_crafting_table_recipe_formula(colour, block):
    return ["{","  \"type\": \"minecraft:crafting_shaped\",","  \"pattern\": [","    \"###\"","  ],","  \"key\": {","    \"#\": {",f"      \"item\": \"minecraft:{colour}_{block}\"","    }","  },","  \"result\": {",f"    \"item\": \"moreterracotta:{colour}_{block}_slab\",","    \"count\": 6","  }","}"]

def slab_stonecutting_recipe_formula(colour, block):
    return ["{","  \"type\": \"minecraft:stonecutting\",","  \"ingredient\": {",f"    \"item\": \"minecraft:{colour}_{block}\"","  },",f"  \"result\": \"moreterracotta:{colour}_{block}_slab\",","  \"count\": 2","}"]

def stair_blockstate_formula(colour, block):
    blockstate_template = open('stairBlockstate.json', 'r')
    blockstate_lines = blockstate_template.readlines()

    output = []
    for line in blockstate_lines:
        newLine = ''
        for char in line:


            if char == "'":
                newLine += colour
            elif char == "3":
                newLine += block
            elif char == "\n":
                pass
            else:
                newLine += char

        output.append(newLine)

    blockstate_template.close()
    return output

def stair_block_formula(colour, block):
    return ["{","  \"parent\": \"minecraft:block/stairs\",","  \"textures\": {",f"    \"bottom\": \"minecraft:block/{colour}_{block}\",",f"    \"top\": \"minecraft:block/{colour}_{block}\",",f"    \"side\": \"minecraft:block/{colour}_{block}\"","  }","}"]

def inner_stair_block_formula(colour, block):
    return ["{","  \"parent\": \"minecraft:block/inner_stairs\",","  \"textures\": {",f"    \"bottom\": \"minecraft:block/{colour}_{block}\",",f"    \"top\": \"minecraft:block/{colour}_{block}\",",f"    \"side\": \"minecraft:block/{colour}_{block}\"","  }","}"]

def outer_stair_block_formula(colour, block):
    return ["{","  \"parent\": \"minecraft:block/outer_stairs\",","  \"textures\": {",f"    \"bottom\": \"minecraft:block/{colour}_{block}\",",f"    \"top\": \"minecraft:block/{colour}_{block}\",",f"    \"side\": \"minecraft:block/{colour}_{block}\"","  }","}"]

def stair_crafting_table_recipe_formula(colour,block):
    return ["{","  \"type\": \"minecraft:crafting_shaped\",","  \"pattern\": [","    \"#  \",","    \"## \",","    \"###\"","  ],","  \"key\": {","    \"#\": {",f"      \"item\": \"minecraft:{colour}_{block}\"","    }","  },","  \"result\": {",f"    \"item\": \"moreterracotta:{colour}_{block}_stairs\",","    \"count\": 4","  }","}"]

def wall_crafting_table_recipe_formula(colour,block):
    return ["{","  \"type\": \"minecraft:crafting_shaped\",","  \"pattern\": [","    \"###\",","    \"###\"","  ],","  \"key\": {","    \"#\": {",f"      \"item\": \"minecraft:{colour}_{block}\"","    }","  },","  \"result\": {",f"    \"item\": \"moreterracotta:{colour}_{block}_wall\",","    \"count\": 6","  }","}"]

def stair_stonecutting_recipe_formula(colour, block):
    return ["{","  \"type\": \"minecraft:stonecutting\",","  \"ingredient\": {",f"    \"item\": \"minecraft:{colour}_{block}\"","  },",f"  \"result\": \"moreterracotta:{colour}_{block}_stairs\",","  \"count\": 1","}"]

def stonecutting_recipe_formula(colour, block, parent):
    return ["{","  \"type\": \"minecraft:stonecutting\",","  \"ingredient\": {",f"    \"item\": \"minecraft:{colour}_{block}\"","  },",f"  \"result\": \"moreterracotta:{colour}_{block}_{parent}\",","  \"count\": 1","}"]

def look_tables_formula(colour,block,stair):
    return ["{","  \"type\": \"minecraft:block\",","  \"pools\": [","    {","      \"rolls\": 1,","      \"entries\": [","        {","          \"type\": \"minecraft:item\",",f"          \"name\": \"moreterracotta:{colour}_{block}_{stair}\"","        }","      ],","      \"conditions\": [","        {","          \"condition\": \"minecraft:survives_explosion\"","        }","      ]","    }","  ]","}"]

def wall_blockstate_formula(colour, block):

    blockstate_template = open('wallBlockstate.json', 'r')
    blockstate_lines = blockstate_template.readlines()

    output = []
    for line in blockstate_lines:
        newLine = ''
        for char in line:

            if char == "3":
                newLine += f"{colour}_{block}"
            elif char == "\n":
                pass
            else:
                newLine += char

        output.append(newLine)

    blockstate_template.close()
    return output

def wall_block_formula(colour, block, parent, template):
    return ["{",f"  \"parent\": \"minecraft:block/{template}wall_{parent}\",","  \"textures\": {",f"    \"wall\": \"minecraft:block/{colour}_{block}\"","  }","}"]

def item_formula(colour, block, parent):
    return ["{",f"  \"parent\": \"moreterracotta:block/{colour}_{block}_{parent}\"","}"]

lang_file = open(f"lang/en_gb.json", "w")
lang_file.write("{\n")

for colour in COLOURS:
    for block in ["terracotta", "concrete"]:
        
        print(f"\"moreterracotta:{colour}_{block}_wall\",")

        w_to_json(f"blockstates/{colour}_{block}_slab.json", slab_blockstate_formula(colour, block))                            #Generate blockstate JSON Files for Slabs
        w_to_json(f"blockstates/{colour}_{block}_stairs.json",stair_blockstate_formula(colour, block))                          #Generate blockstate JSON Files for Stairs  
        w_to_json(f"blockstates/{colour}_{block}_wall.json", wall_blockstate_formula(colour, block))                            #Generate blockstate JSON Files for Walls  
        w_to_json(f"slabtops/{colour}_{block}_slab_top.json", slab_formula("_top", colour, block))                              #Generate model JSON Files for Slab Tops
        w_to_json(f"slabs/{colour}_{block}_slab.json",slab_formula("", colour, block))                                          #Generate model JSON Files for Slabs
        w_to_json(f"stairs/{colour}_{block}_stairs.json",stair_block_formula(colour, block))                                    #Generate model JSON Files for Stairs
        w_to_json(f"stairs/{colour}_{block}_stairs_outer.json", outer_stair_block_formula(colour, block))                       #Generate model JSON Files for Outer Stairs
        w_to_json(f"stairs/{colour}_{block}_stairs_inner.json",inner_stair_block_formula(colour, block))                        #Generate model JSON Files for Inner Stairs
        w_to_json(f"walls/{colour}_{block}_wall_inventory.json", wall_block_formula(colour, block, "inventory", ""))            #Generate model JSON Files for Wall inventory
        w_to_json(f"walls/{colour}_{block}_wall_post.json", wall_block_formula(colour, block, "post", "template_"))             #Generate model JSON Files for Wall post
        w_to_json(f"walls/{colour}_{block}_wall_side.json", wall_block_formula(colour, block,"side", "template_"))              #Generate model JSON Files for Wall side
        w_to_json(f"walls/{colour}_{block}_wall_side_tall.json", wall_block_formula(colour, block, "side_tall", "template_"))   #Generate model JSON Files for Wall side tall
        w_to_json(f"items/{colour}_{block}_slab.json", item_formula(colour, block, "slab"))                                     #Generate item JSON Files for Slabs
        w_to_json(f"items/{colour}_{block}_stairs.json", item_formula(colour, block,"stairs"))                                  #Generate item JSON Files for Stairs
        w_to_json(f"items/{colour}_{block}_wall.json", item_formula(colour, block, "wall_inventory"))                           #Generate item JSON Files for Wall
        w_to_json(f"recipes/{colour}_{block}_slab.json", slab_crafting_table_recipe_formula(colour, block))                     #Generate crafting table recipe JSON Files for Slabs
        w_to_json(f"recipes/{colour}_{block}_stairs.json", stair_crafting_table_recipe_formula(colour, block))                  #Generate crafting table recipe JSON Files for Stairs
        w_to_json(f"recipes/{colour}_{block}_wall.json", wall_crafting_table_recipe_formula(colour, block))                     #Generate crafting table recipe JSON Files for Wall
        w_to_json(f"recipes/{colour}_{block}_slab_stonecutting.json", stonecutting_recipe_formula(colour, block, "slab"))       #Generate stonecutting JSON Files for Slabs
        w_to_json(f"recipes/{colour}_{block}_stairs_stonecutting.json", stonecutting_recipe_formula(colour, block, "stairs"))   #Generate stonecutting JSON Files for Stairs
        w_to_json(f"recipes/{colour}_{block}_wall_stonecutting.json", stonecutting_recipe_formula(colour, block, "wall"))       #Generate stonecutting JSON Files for Wall
        w_to_json(f"loot_tables/{colour}_{block}_slab.json", look_tables_formula(colour,block,"slab"))                          #Generate loottables for Slabs
        w_to_json(f"loot_tables/{colour}_{block}_stairs.json", look_tables_formula(colour,block,"stairs"))                      #Generate loottables for Stairs
        w_to_json(f"loot_tables/{colour}_{block}_wall.json", look_tables_formula(colour,block,"wall"))                          #Generate loottables for Wall


        lang_colour = " ".join([i.capitalize() for i in colour.split("_")])                                                     #Remove the _ from colour names and capitalise each word
        lang_file.write(f"  \"block.moreterracotta.{colour}_{block}_slab\": \"{lang_colour} {block.capitalize()} Slab\",")      #Add languages for Slabs
        lang_file.write("\n")

        lang_file.write(f"  \"block.moreterracotta.{colour}_{block}_stairs\": \"{lang_colour} {block.capitalize()} Stairs\",")  #Add languages for Stairs
        lang_file.write("\n")

        lang_file.write(f"  \"block.moreterracotta.{colour}_{block}_wall\": \"{lang_colour} {block.capitalize()} Wall\",")    #Add languages for Wall
        lang_file.write("\n")

lang_file.write("\n")
for line in [
    "  \"block.moreterracotta.terracotta_slab\": \"Terracotta Slab\",",
    "  \"block.moreterracotta.terracotta_stairs\": \"Terracotta Stairs\",",
    "  \"block.moreterracotta.terracotta_wall\": \"Terracotta Wall\",",
    "",
    "  \"itemGroup.moreterracotta.terracotta_group\": \"More Terracotta\",",
    "  \"itemGroup.moreterracotta.concrete_group\": \"More Concrete\""
]:
    lang_file.write(line)
    lang_file.write("\n")

lang_file.write("}")
lang_file.close()