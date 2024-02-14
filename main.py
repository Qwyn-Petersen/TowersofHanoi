#NAME(s): 
#Assignment Towers of Hanoi (you may work alone or in a pair) 
#NOTE: FPT.so and Gkit.py files are included, but are ONLY needed if you intend to add graphics 

def pop(tower,sp) :
  if(tower[sp] == -1) :
    print("Error: Tower is empty")
    return 0 
  ring = tower[sp]
  tower[sp] = -1
  sp = sp -1
  return ring

def push(tower,sp,ring) :
  if(sp == 4) :
    print("Error: Tower is full!")
  else:
    sp = sp + 1
    if(tower[sp] == -1) :
      tower[sp] = ring
    else:
      print("Whoops!! Somethings already here!")
      return 0


def towers_of_hanoi() :
  towers = [-1,-1,-1]
  towers[0] = [4,3,2,1,0]  # tower 0
  towers[1] = [-1,-1,-1,-1,-1]  # tower 1
  towers[2] = [-1,-1,-1,-1,-1]  # tower 2
  sp = [4,-1,-1]  # stack pointers for each tower
  return towers


  

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

def main() : 

  towers = towers_of_hanoi()
  display_towers(towers) # display function
  print("Hit -enter- key to continue") # Need to display again after this


if __name__ == "__main__":
  main()