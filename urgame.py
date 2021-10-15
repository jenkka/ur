#Importar bibliotecas
import pygame
import random
import sys

#Inicializar libreria pygame
pygame.init()

#Importar media
fight = pygame.mixer.Sound("fight.wav")
out = pygame.mixer.Sound("out.wav")
pygame.mixer.music.load("musicGame.mp3")

#Resolucion de la ventana
displayWidth = 1580
displayHeight = 900

#Variable para el color blanco RGB
white  = (255,255,255)

#Variables para las dimensiones de los espacios
characterx = 168
charactery = 168

#Variable para aplicar el tamaño de la pantalla
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
#Titulo de la ventana
pygame.display.set_caption('Royal Game: Ur')
#Variable para los fps
clock = pygame.time.Clock()

#Importar imagenes (Una variable para cada una)
backgroundImg = pygame.image.load('urgame.jpg')
mainImg = pygame.image.load('urmain.jpg')

p1Wins = pygame.image.load('p1wins.jpg')
p2Wins = pygame.image.load('p2wins.jpg')
player1Img1 = pygame.image.load('king1.png')
player1Img2 = pygame.image.load('king2.png')
player1Img3 = pygame.image.load('king3.png')
player1Img4 = pygame.image.load('king4.png')
player1Img5 = pygame.image.load('king5.png')
player1Img6 = pygame.image.load('king6.png')
player1Img7 = pygame.image.load('king7.png')
player1Images = [player1Img1, player1Img2, player1Img3, player1Img4, player1Img5, player1Img6, player1Img7]

player2Img1 = pygame.image.load('ghoul1.png')
player2Img2 = pygame.image.load('ghoul2.png')
player2Img3 = pygame.image.load('ghoul3.png')
player2Img4 = pygame.image.load('ghoul4.png')
player2Img5 = pygame.image.load('ghoul5.png')
player2Img6 = pygame.image.load('ghoul6.png')
player2Img7 = pygame.image.load('ghoul7.png')
player2Images = [player2Img1, player2Img2, player2Img3, player2Img4, player2Img5, player2Img6, player2Img7]

#Variables para acomnodar las fichas en su lugar
x = (displayWidth * 0.00001)
y = (displayHeight * 0.000001)

#Array para saber si las fichas estan activas y si los espacios del tablero estan ocupados
zone1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
zone2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tokens1 = [0,0,0,0,0,0,0]
tokens2 = [0,0,0,0,0,0,0]

#Variable para definir el largo de los espacios
spaceLenght = 162

#Variable para el numero de espacios que vamos a avanzar
moving = 0

#Define de que jugador es turno
player1Turn = True

#Variable para acabar el juego
end = False

#Funcion "principal", aqui esta la mayoria del codigo. Tira el dado, acomoda la ficha en el tablero, etc.
def turn():

    #Tira el dado
    plus = random.randint(0,4)

    #Turno del jugador 1
    if player1Turn:
        print("-------------------------------------------------------------\nJugador 1: Tiraste un", plus)
        if plus != 0:
            goodAnswer = False

            #Verifica el lugar al que se movera la ficha seleccionada
            moving = ask()
            while not goodAnswer:   
                if moving < 0 or moving > 6:
                    print("Esa ficha no esta dentro del rango (1-7).")
                    moving = ask()
                
                elif tokens1[moving] == 99:
                    print("Esa ficha ya esta fuera del juego.")
                    moving = ask()
                    
                elif (tokens1[moving] + plus in tokens1) or (tokens1[moving] + plus == 8 and zone2[7] == 1):
                    print("Esa posicion ya esta ocupada.")
                    moving = ask()
                else:
                    goodAnswer = True

            #Suma el numero del dado a la posicion de la ficha o elimina la ficha del juego si llega al final
            if (tokens1[moving] + plus) <= 14:
                tokens1[moving] = tokens1[moving] + plus
            else:
                if tokens1[moving] > 12:
                    gameDisplay.blit(backgroundImg, ((tokens1[moving] - 13)* spaceLenght + 150, 190), pygame.Rect((tokens1[moving] - 13)* spaceLenght + 150, 190, characterx, charactery))

                else:
                    gameDisplay.blit(backgroundImg, ((1450  - (tokens1[moving]  - 4) * (spaceLenght)), 350), pygame.Rect((1450  - (tokens1[moving]  - 4) * (spaceLenght)), 350, characterx, charactery))

                pygame.mixer.Sound.play(out)
                zone1[tokens1[moving] - 1] = 0
                tokens1[moving] = 99
                
            
            #Borra la imagen anterior del tablero e imprime la nueva posicion de la ficha
            if tokens1[moving] != 0 and tokens1[moving] != 99:
                if tokens1[moving] - plus > 12:
                    gameDisplay.blit(backgroundImg, ((tokens1[moving] - plus - 13)* spaceLenght + 150, 190), pygame.Rect((tokens1[moving] - plus - 13)* spaceLenght + 150, 190, characterx, charactery))
                    
                elif tokens1[moving] - plus < 5:
                    gameDisplay.blit(backgroundImg, ((tokens1[moving] - plus - 1) * spaceLenght + 800, 190), pygame.Rect((tokens1[moving] - plus - 1) * spaceLenght + 800, 190, characterx, charactery))
                    
                else:
                    gameDisplay.blit(backgroundImg, ((1450  - (tokens1[moving]  - plus - 4) * (spaceLenght)), 350), pygame.Rect((1450  - (tokens1[moving]  - plus - 4) * (spaceLenght)), 350, characterx, charactery))
                    
                
                if tokens1[moving] > 12:
                    gameDisplay.blit(backgroundImg, ((tokens1[moving] - 13)* spaceLenght + 150, 190), pygame.Rect((tokens1[moving] - 13)* spaceLenght + 150, 190, characterx, charactery))
                    gameDisplay.blit(player1Images[moving],((tokens1[moving] - 13)* spaceLenght + 150, 190))
                    
                elif tokens1[moving] < 5:
                    gameDisplay.blit(backgroundImg, ((tokens1[moving] - 1) * spaceLenght + 800, 190), pygame.Rect((tokens1[moving] - 1) * spaceLenght + 800, 190, characterx, charactery))
                    gameDisplay.blit(player1Images[moving],((tokens1[moving] - 1) * spaceLenght + 800, 190))
                    
                else:
                    gameDisplay.blit(backgroundImg, ((1450  - (tokens1[moving]  - 4) * (spaceLenght)), 350), pygame.Rect((1450  - (tokens1[moving]  - 4) * (spaceLenght)), 350, characterx, charactery))
                    gameDisplay.blit(player1Images[moving],(1450  - (tokens1[moving] - 4) * (spaceLenght), 350))

                #Sobreescribe la posicion en el arrray
                zone1[tokens1[moving] - plus - 1] = 0
                zone1[tokens1[moving]-1] = 1
                check()

            #Si el jugador cae en alguna de las posiciones especiales, vuelve a tirar, si no, cambia de turno
            if tokens1[moving] != 4 and tokens1[moving] != 8 and tokens1[moving] != 14:
                turnSwitch()
            else:
                print("Jugador 1 mueve de nuevo.")
        else:
            turnSwitch()

    #Turno del jugador 2 (La lógica es igual que en la del jugador 1)
    else:
        print("-------------------------------------------------------------\nJugador 2: Tiraste un", plus)
        if plus != 0:
            goodAnswer = False
            moving = ask()
            
            while not goodAnswer:   
                if moving < 0 or moving > 6:
                    print("Esa ficha no esta dentro del rango (1-7).")
                    moving = ask()
                
                elif tokens2[moving] == 99:
                    print("Esa ficha ya esta fuera del juego.")
                    moving = ask()
                    
                elif (tokens2[moving] + plus in tokens2) or (tokens2[moving] + plus == 8 and zone1[7] == 1):
                    print("Esa posicion ya esta ocupada.")
                    moving = ask()
                else:
                    goodAnswer = True
                    
            
            if (tokens2[moving] + plus) <= 14:
                tokens2[moving] = tokens2[moving] + plus
            else:
                if tokens2[moving] > 12:
                    gameDisplay.blit(backgroundImg, ((tokens2[moving] - 13)* spaceLenght + 150, 510), pygame.Rect((tokens2[moving] - 13)* spaceLenght + 150, 510, characterx, charactery))

                else:
                    gameDisplay.blit(backgroundImg, ((1450  - (tokens2[moving]  - 4) * (spaceLenght)), 350), pygame.Rect((1450  - (tokens2[moving]  - 4) * (spaceLenght)), 350, characterx, charactery))

                pygame.mixer.Sound.play(out)
                zone2[tokens2[moving] - 1] = 0
                tokens2[moving] = 99
                
                
                
            if tokens2[moving] != 0 and tokens2[moving] != 99:
                if tokens2[moving] - plus > 12:
                    gameDisplay.blit(backgroundImg, ((tokens2[moving] - plus - 13)* spaceLenght + 150, 510), pygame.Rect((tokens2[moving] - plus - 13)* spaceLenght + 150, 510, characterx, charactery))
                    
                elif tokens2[moving] - plus < 5:
                    gameDisplay.blit(backgroundImg, ((tokens2[moving] - plus - 1) * spaceLenght + 800, 510), pygame.Rect((tokens2[moving] - plus - 1) * spaceLenght + 800, 510, characterx, charactery))
                    
                else:
                    gameDisplay.blit(backgroundImg, ((1450  - (tokens2[moving]  - plus - 4) * (spaceLenght)), 350), pygame.Rect((1450  - (tokens2[moving]  - plus - 4) * (spaceLenght)), 350, characterx, charactery))
                    

            
                if tokens2[moving] > 12:
                    gameDisplay.blit(backgroundImg, ((tokens2[moving] - 13)* spaceLenght + 150, 510), pygame.Rect((tokens2[moving] - 13)* spaceLenght + 150, 510, characterx, charactery))
                    gameDisplay.blit(player2Images[moving],((tokens2[moving] - 13)* spaceLenght + 150, 510))
                    
                elif tokens2[moving] < 5:
                    gameDisplay.blit(backgroundImg, ((tokens2[moving] - 1) * spaceLenght + 800, 510), pygame.Rect((tokens2[moving] - 1) * spaceLenght + 800, 510, characterx, charactery))
                    gameDisplay.blit(player2Images[moving],((tokens2[moving] - 1) * spaceLenght + 800, 510))
                    
                else:
                    gameDisplay.blit(backgroundImg, ((1450  - (tokens2[moving]  - 4) * (spaceLenght)), 350), pygame.Rect((1450  - (tokens2[moving]  - 4) * (spaceLenght)), 350, characterx, charactery))
                    gameDisplay.blit(player2Images[moving],(1450  - (tokens2[moving] - 4) * (spaceLenght), 350))

                zone2[tokens2[moving] - plus - 1] = 0
                zone2[tokens2[moving]-1] = 1
                check()
                
            if tokens2[moving] != 4 and tokens2[moving] != 8 and tokens2[moving] != 14:
                turnSwitch()
            else:
                print("Jugador 2 mueve de nuevo.")
        else:
            turnSwitch()
                
#Try catch para preguntar la ficha que se va a mover. Verifica que el dato ingresado sea aceptable.
def ask():
    while True:
        try:
            question = int(input("Elige el numero de la ficha que deseas mover(1-7): ")) - 1
        except ValueError:
            print("Valor incorrecto.")
            
        else:
            break
    return question


#Funcion para comer fichas
def check():
    for i in range(4,12):
        if (zone1[i] == 1) and (zone2[i] == 1):
            pygame.mixer.Sound.play(fight)
            if player1Turn:
                zone2[i] = 0
                tokens2[tokens2.index(i+1)] = 0
            else:
                zone1[i] = 0
                tokens1[tokens1.index(i+1)] = 0
        
#Verifica si alguien ganó el juego y hace display a la pantalla final
def winCheck():
    
    counterP1 = 0
    counterP2 = 0

    #Cuenta cada ficha que esté fuera del juego, si llega a 7 el contador, gana el jugador
    for i in range(7):
        if tokens1[i] == 99:
            counterP1+=1
        if tokens2[i] == 99:
            counterP2 +=1

    #Panalla final para jugador 1        
    if counterP1 >= 7:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("musicWin.mp3")
        pygame.mixer.music.play(-1)
        gameDisplay.blit(p1Wins,(x,y))
        pygame.display.update()
        input("Presiona Enter para finalizar.")
        sys.exit()    

    #Panalla final para jugador 2           
    elif counterP2 >= 7:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("musicWin.mp3")
        pygame.mixer.music.play(-1)
        gameDisplay.blit(p2Wins,(x,y))
        pygame.display.update()
        input("Presiona Enter para finalizar.")
        sys.exit()    
            
#Alterna entre el turno de los jugadores
def turnSwitch():
    
    global player1Turn
    
    if player1Turn:
        player1Turn = False
    else:
        player1Turn = True

#Main
while not end:
    
    for event in pygame.event.get():
        #Pantalla de inicio
        gameDisplay.blit(mainImg,(x,y))
        clock.tick(60)
        pygame.display.update()
        pygame.mixer.music.play(-1)
        input("Presiona Enter para comenzar a jugar.")
        #Pantalla del tablero
        gameDisplay.fill(white)    
        gameDisplay.blit(backgroundImg,(x,y))
        pygame.display.update()
            
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            #Utilizamos funciones esenciales (Correr el turno, verificar si alguien ganó, inicializar la funcion de fps e imprimir la imagen cada frame)
            turn()
            winCheck()   
            clock.tick(60)
            pygame.display.update()

#Terminar juego
pygame.quit()
quit()
