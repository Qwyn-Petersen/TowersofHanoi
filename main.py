#NAME(s): 
#Assignment Towers of Hanoi (you may work alone or in a pair) 
#NOTE: FPT.so and Gkit.py files are included, but are ONLY needed if you intend to add graphics 


########## display towers
def display_towers(towers) :
  print()
  k = len(towers[0])-1
  while(k >= 0) :
    if(towers[0][k] != -1) :
      print(towers[0][k]+1 , end= "  ")
    else :
      print("+" , end= "  ")

    if(towers[1][k] != -1) :
      print(towers[1][k]+1 , end= "  ")
    else :
      print("+" , end= "  ")

    if(towers[2][k] != -1) :
      print(towers[2][k]+1 , end= "  ")
    else :
      print("+" , end= "  ")

    print()
    k = k - 1
  print("_______")


#########  main
# Example using a 5-ring tower
towers = [-1,-1,-1]
towers[0] = [4,3,2,1,0]  # tower 0
towers[1] = [-1,-1,-1,-1,-1]  # tower 1
towers[2] = [-1,-1,-1,-1,-1]  # tower 2
sp = [4,-1,-1]  # stack pointers for each tower
display_towers(towers)
print("Hit -enter- key to continue")
