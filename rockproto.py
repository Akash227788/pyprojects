import random
play=("rock" , "paper" , "scissor" )
game=random.choice( play )
print(game)

user= input(" enter rock , paper , or scissor " )
#while :
if (game==user) :
   print ("tie")
while (user!=game) :
    if (user=="rock") :
      if game=="paper" :
        print (" the computer wins the game " )
        break
      else :
        print ("you have won the game" )
        break
    if (user=="paper" ) :
     if (game=="rock") :
       print (" you won the game " )
       break
     else :
       print ("computer won the game " )
       break
    if ( user=="scissor") :
     if (game=="rock") :
        print ( "the computer won the game " )
        break
     else :
        print ("you won the game " )
        break
      
        

    
