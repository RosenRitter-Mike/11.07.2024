start: int = int(input("please enter the start point?"));
end: int =  int(input("please enter the end point?"));
gap: int = int(input("please enter the gap?"));

for x in range(start, end+1, gap):
  print(x);
else:
  print("For loop finally finished!");