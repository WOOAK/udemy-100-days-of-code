# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position_char = list(position)
#print(position_char)
col_pos = int(position_char[0]) - 1
row_pos = int(position_char[1]) - 1
if row_pos == 0:
  row1[col_pos] = "X"
elif row_pos == 1:
  row2[col_pos] = "X"
elif row_pos == 2:
  row3[col_pos] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")