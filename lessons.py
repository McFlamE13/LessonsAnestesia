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




    