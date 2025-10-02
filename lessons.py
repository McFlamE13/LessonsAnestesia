def welcome():
    username = input("Введите ваше игровое имя: ")
    msg =  f"{username} welcome to the Magic World of dragons and warriors!"
    print(msg)

location = ["forest","castle", "village"]
def print_location(locs):
    count = 1
    for l in locs:
        print(f"Location #{count} {l}")
        count += 1


print_location(location)

inventory = {
  "coins": 15,
  "regenerator": 2,
  "apple": 1,
  "basilisk_tooth": 1
}
item = "apple"
def add_to_inventory(item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

add_to_inventory(item)
print(inventory)

recipe = {
  "fire_flower": 2,
  "toad_eye": 1,
  "basilisk_tooth": 1,
  "griffin_feather": 3
}

def potion(recipe, inventory):
    for ingridient, amount in recipe.items():
        if inventory.get(ingridient, 0) < amount:
            return False
    return True

if potion(recipe, inventory):
    print("We can")
else:
    print("We haves lapkis")


paths = [
    ("mountain_pass", 8),          
    ("forest_trail", 3),           
    ("river", 7),         
    ("desert", 9),           
    ("canyon", 6),           
    ("plain", 2),             
    ("swamp", 5)              
]
def not_danger(our_paths):
    path_not_danger = our_paths[0][0]
    min_danger = our_paths[0][1]
    for paths in our_paths:
        if paths[1] < min_danger:
            min_danger = paths[1]
            path_not_danger = paths[0]
    return path_not_danger
our_path = not_danger(paths)
print(f"Not danger path - {our_path}")

character = {
    "name": "",
    "head": None,
    "right hand": None,
    "left hand": None
    }
character["name"] = input("Please enter name your character: ")
def equip_character(slot, item):
    if slot not in character:
        print(f"Mistake! Slot {slot} off")
        return
    if character[slot] is not None:
        print(f"Mistake! Slot {slot} already use")
    else:
        character[slot] = item
        print(f"Slot {slot} equipment {item}")

equip_character("right hand", "steel sword")









    