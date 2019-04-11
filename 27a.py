print ("Задание 27, вариант а")
end = ""
while end != "q": 
    #Input module
    i = 2
    set1 = ""
    set2 = ""
    while i > 0:
        i = i - 1
        print ("Enter ", i, "pair of numbers")
        temp1 = input ("Enter number #1 and press Enter ")
        if temp1.isdigit():
            set1 = (set1 + temp1)
            set1 = (set1 + ", ") #debug feature
            print ("Your Set 1 is:", set1) 
        else:
            print ("#1 is Not a number! Try another one!")
        temp2 = input ("Enter number #2 and press Enter ")
        if temp2.isdigit():
            set2 = (set2 + temp2)
            set2 = (set2 + ", ") #debug feature
            print ("Your Set 2 is:", set2)
        else:
            print ("#2 Is Not a number! Please, use 0-9 digits!")
    #Razbor Stroky
    raz1 = ""

    #Calculation module
    answer = 0
    print ("Answer is... ", answer)
    end = input ("Press Q to finish or Enter to play again ")
    if end == "Q":
        end = "q"
else:
    print ("Bye")

    

    
    
        
