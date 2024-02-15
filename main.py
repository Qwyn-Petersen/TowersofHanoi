#NAME(s): 
#Assignment Towers of Hanoi (you may work alone or in a pair) 
#NOTE: FPT.so and Gkit.py files are included, but are ONLY needed if you intend to add graphics 

def pop(tower_passed) :
  this_tower = tower_passed[0]
  this_pointer = tower_passed[1]
  
  if(this_pointer == -1) :
    print("Error: Tower is empty")
    return None
    
  ring = this_tower[this_pointer]
  this_tower[this_pointer] = -1
  tower_passed[1] = this_pointer - 1
  return ring

def push(tower_passed,ring) :
  this_pointer = tower_passed[1]
  this_tower = tower_passed[0]
  
  if(this_pointer == 4) :
    print("Error: Tower is full!")
  else:
    tower_passed[1] += 1 
    this_pointer += 1
    this_tower[this_pointer] = ring
    print("Ring", ring, "pushed onto tower.")

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

def play_game(towers,n,origin,aux,dest) :
  if n == 1 : 
    ring = pop(origin)
    push(dest,ring)
    display_towers(towers) 
    return 

  # reverse order of towers, aux - dest
  play_game(towers,n-1,origin,dest,aux)

  ring = pop(origin)
  push(dest,ring)
  display_towers(towers) 

  play_game(towers,n-1,aux,origin,dest)

#########  main
def main() : 

  # Example using a 5-ring tower
  towers = [-1,-1,-1]
  towers[0] = [4,3,2,1,0]  # tower 0
  towers[1] = [-1,-1,-1,-1,-1]  # tower 1
  towers[2] = [-1,-1,-1,-1,-1]  # tower 2
  sp = [4,-1,-1]  # stack pointers for each tower

  n = len(towers[0])
  origin = [towers[0],sp[0]]
  aux = [towers[1],sp[1]]
  dest = [towers[2],sp[2]]

  display_towers(towers)
  play_game(towers,n,origin,aux,dest)
  display_towers(towers) # display function
  print("We are done! Yay!") # Need to display again after this

if __name__ == "__main__":
  main()