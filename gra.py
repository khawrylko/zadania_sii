import random
print ("To jest gra w papier, kamień i nożyce.")
while True:
    print ("Podaj cyfrę od 1 do 3. Jeżeli chcesz rzucić papier: 1, kamień: 2, nożyce: 3")
    player_choice = 0

    choice ={
        1: "papier",
        2: "kamień",
        3: "nożyce"
    }
    while True:
        try:
            player_choice = int(input())
            if 1 <= player_choice <= 3:
                print ("Wybrałeś: " + choice.get(player_choice))
                break
            else:
                raise ValueError()
        except:
            print ("Nieprawidłowy wybór. Wybierz 1, 2 lub 3.")

    opponent_choice =  random.randrange(1,3)
    print ("Twój przeciwnik wybrał: " + choice.get(opponent_choice))
    if player_choice  == opponent_choice:
        print ("remis")
    elif (player_choice == 1 and opponent_choice == 2) or (player_choice == 2 and opponent_choice == 3) or (player_choice == 3 and opponent_choice == 1):
        print ("Zwycięstwo!")
    else:
        print ("przegrana :(")



