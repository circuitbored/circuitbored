import os

num = 1
while(1):
  num = num+1
  F_Name = ("epic_folder" + num)
  os.makedirs(F_Name, exist_ok=True)
  print(num)