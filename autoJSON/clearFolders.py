import os, re, os.path

def clear_folder(mypath):
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))

clear_folder('blockstates')
clear_folder('items')
clear_folder('lang')
clear_folder('loot_tables')
clear_folder('recipes')
clear_folder('slabs')
clear_folder('slabtops')
clear_folder('stairs')
clear_folder('walls')