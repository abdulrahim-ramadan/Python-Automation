'''''''''
       Geme :
           -welcome message ,games as options
           -enter game  number
           -option to exit
           -after playing , ask play again
           -games :
                 - sentence no duplicate
                 - from-to multiplication table
'''''''''                 
class Game :

    def __init__(self):
         while True:
            print(""" welcome to our game , enter game number
            1 : sentence no duplicate
            2 : from-to multiplication table
            3 : to exit \n""")
            user_choice = int (input("Enter Game Number : "))

            if user_choice == 1:
                s = input("Enter Sentence :")
                self.sentence_no_duplicate(s)


            elif user_choice == 2:
                start =int(input("Enter Start Number : "))
                end = int(input("Enter End Number :"))
                self.from_to_multiplication_table(start,end)



            elif user_choice ==3:
                print("godbye...")
                break



            play_again = input('Press any char to play agin , n to exit')
            if play_again == 'n':
                break


    def sentence_no_duplicate(self,sentence):
        words = sentence.split()
        main_words = []

        for w in words :
            if w in main_words :
                continue
            else:
                main_words.append(w)
        print(' '.join(main_words))

    def from_to_multiplication_table(self,start,end):
         for x in range(start,end+1):
            for y in range(1,11):
                print(f'{x} X {y} ={x*y}')

            print('---------------------')






g1 = Game()       

#sentence no duplicate

# def sentence_no_duplicate(self,sentence):
#          words = sentence.split()
#          main_words = []

#          for w in words :
#             if w in main_words :
#                 continue
#             else:
#                 main_words.append(w)
#          print(' '.join(main_words))

   

s = "Abdulrahim is a great is great ist developer"

#sentence_no_duplicate(s)






# #from-to multiplication table
# def from_to_multiplication_table(start,end):
#          for x in range(start,end+1):
#              for y in range(1,13):
#                  print(f'{x} X {Y} ={x*Y}')

#              print('---------------------')






















#from_to_multiplication_table(4,7)        
               
