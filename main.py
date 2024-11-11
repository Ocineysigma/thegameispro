import os
import time
import random
audio = True
#Funções:
def gameover(npc,message):
    time.sleep(0.5)
    print("------------------<<Lá ELE ZADO>>------------------")
    print(f"você morreu para {npc},{message} sua experiência foi {experience}")
    time.sleep(5)
    print("esse jeito de morrer foi sus")
def Win(npc,xpEarned):
    global experience
    experience += xpEarned
    time.sleep(0.5)
    print("------------------<<!VITÓRIA!>>------------------")
    print(f"você derrotou {npc} e ganhou {xpEarned} de experiência")
    print(f"sua experiência atual é {experience}")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()
#Jogo:
nome = input("Qual seu Nome?: ")
invalidage = False
idadeprompt = ""
while invalidage == False:
    idade = int(input("Legal! Qual sua idade: "))
    if idade < 3:
        print("Idade inválida. A idade não pode ser menor que 3.")
    elif idade > 60:
        print("Idade inválida. A idade não pode ser maior que 60.")
    else:
        if 3 <= idade <= 12:
            invalidage = True
            idadeprompt = "Criança"
            print("Modo Criança")
        elif idade == 13:
            invalidage = True
            idadeprompt = "Pré-adolescente"
            print("Modo pré-adolescente")
        elif 14 <= idade <= 19:
            invalidage = True
            idadeprompt = "Adolescente"
            print("Modo adolescente")
        elif 20 <= idade <= 40:
            invalidage = True
            idadeprompt = "Boomer"
            print("Modo boomer")
        else:
            invalidage = True
            idadeprompt = "old as shit"
            print("Modo Velho")
print("lá ele, amostradinho quer te dar a bomba")
experience = 0
time.sleep(1)
FirstinputCheck = False
while FirstinputCheck == False:
    primeiroinput = input("Decide Tomar? S/N:")
    if primeiroinput == "S":
        FirstinputCheck = True
        print("FAKE NATTY!")
        time.sleep(0.1)
        print("Oh não! Rodrigo goés pegou você no flagra tomando bomba")
        time.sleep(6)
        cls()
        print("{System}:Você entrou em uma batalha*")
        time.sleep(1)
        print("Ataques:")
        print("Correr")
        print("Soco")

        inputbattle1 = input("Escolha!:")
        input1battlecheck = False
        while input1battlecheck == False:
            if inputbattle1 == "Correr":
                input1battlecheck = True
                print("você escolheu correr!")
                time.sleep(1)
                print("Rodrigo goés te alcançou e te bateu com o baseballbat")
                gameover("Rodrigo goés","você não deveria tomado a bomba")
            elif inputbattle1 == "Soco":
                input1battlecheck = True
                Socorand = random.randint(0,10)
                print(f'seu soco deu {Socorand} de dano')
                time.sleep(1)
                if Socorand >=4:
                   Win(npc="Rodrigo goés",xpEarned=10)
                elif Socorand <= 4:
                    print("Rodrigo goés caiu de gargalhada e te bateu com o baseballbat")
                elif Socorand == 0:
                    print("Você rebolou lentinho para Rodrigo Góes")   
            else:
                print("Escolha algum ataque que vocẽ tenha!")
    elif primeiroinput == "N":
            print("eu gosto assim...")
            time.sleep(1)
            print("AMOSTRADINHO")
            time.sleep(2)
            print("{System}:Você entrou em uma batalha*")
            time.sleep(1)
            print("Ataques:")
            print("Correr")
            print("Soco")
            inputdeahthamostrado1 = input("Escolha!:")
            if inputdeahthamostrado1 == "Correr":
                cls()
                time.sleep(3)
                print(".")
                time.sleep(1)
                cls()
                print(". .")
                time.sleep(1)
                cls()
                print(". . .")
                time.sleep(1)
                cls()
                time.sleep(4)
                print("acha que consegue me deter?")
                time.sleep(5)
                cls()
                time.sleep(5)
                print("errado.")
                time.sleep(1)
                cls()
                print("errado..")
                time.sleep(1)
                cls()
                print("errado...")
                time.sleep(1)
                cls()
                time.sleep(1)
                print("Amostradinho te deu backshots😶‍🌫")
                gameover("Amostradinho","Recusaste a bomba?")
            elif inputdeahthamostrado1 == "Soco":
                Socorand = random.randint(1,50)
                if Socorand >=30:
                    print(f'seu soco deu {Socorand} de dano')
                    Win(npc="Amostradinho",xpEarned=4925843)
                    time.sleep(5)
                    print("Não é possivel")
                    time.sleep(1)
                    print(f"{nome}: Você acabou de perder para um humano que tem {experience}😜")
                    print(f"{nome}: EZZZZZZZZ😜")
                    print(f"{nome}: EZZZZZZZZ😜")
                    print(f"{nome}: EZZZZZZZZ😜")
                    print(f"{nome}: EZZZZZZZZ😜")
                    print(f"{nome}: EZZZZZZZZ😜")
                    time.sleep(5)
                    cls()
                    print("Amostradinho: Nãooooooo!")
                    time.sleep(2)
                    print(f"{nome}:vira de costas, agora.")
                    time.sleep(2)
                    print(f"você derrotou Amostradinho e ganhou {492}... quem liga man")
                    print("você fez amostradinho rebolar pros crias(você)! e você se tornou desumilde.")
                    print("obrigado por jogar!")
                    
                elif Socorand <=30:
                    print("achou que podia me derrotar?")
                    time.sleep(3)
                    print("Amostradinho te deu backshots😶‍🌫")
                    gameover("Amostradinho","seu soco foi horrível") 
    else:
        print("cara n to zuando")
