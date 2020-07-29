#Kevin and Stuart want to play the 'The Minion Game'
def minion_game(string):
      k=["A","E","I","O","U"]
      A=0
      B=0
      for i in range(0,len(string)):
          if string[i] in k:
             B+=len(string)-i
          else:
             A+=len(string)-i
      if A<B:
         print("Kevin" ,B)
      elif B<A:
         print("Stuart" ,A)
      elif A==B:
         print("Draw")
