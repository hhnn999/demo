import random

print("Chào mừng bạn đến với trò chơi 'Tìm kho báu'!")
print("Lâu đài có 3 cánh cửa. Bạn hãy chọn một cánh cửa từ 1 đến 3.")

# Randomly assign the locations of treasure, monster, and dragon
treasure_location = random.randint(1, 3)
monster_location = random.randint(1, 3)
while monster_location == treasure_location:
    monster_location = random.randint(1, 3)

door_chosen = int(input("Chọn một cánh cửa (1-3): "))

# Validate user input
while door_chosen not in [1, 2, 3]:
    print("Vui lòng chọn một cánh cửa từ 1 đến 3.")
    door_chosen = int(input("Chọn một cánh cửa (1-3): "))

# Open the chosen door and reveal the result
print("Bạn đã chọn cánh cửa", door_chosen)

if door_chosen == treasure_location:
    print("Xin chúc mừng! Bạn đã tìm thấy kho báu!")
elif door_chosen == monster_location:
    print("Oops! Bạn đã gặp phải quái vật! Bạn đã thua.")
else:
    print("Oops! Bạn đã vào phòng của con rồng! Bạn đã chết.")

print("Cám ơn bạn đã chơi!")