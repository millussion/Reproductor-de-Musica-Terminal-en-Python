import pygame

pygame.mixer.init()
bien = input("Bienvenido al reproducto de música via Terminal. ¿Continuar? Y/N ")

if bien.lower() == "y":
    
    while True :
        print("Selecciona la canción\n 1.Folded x Miss Independent\n 2.Follow You\n 3.Kulosa\n 4.Boyfriend\n 5.Salir del Reproductor")

        opcion = input("Selección: ").strip()

        if opcion == "1" :
            pygame.mixer.music.load('canciones/Folded x Miss Independent.mp3')
        elif opcion == "2" :
            pygame.mixer.music.load('canciones/Follow You.mp3')
        elif opcion == "3" :
            pygame.mixer.music.load('canciones/Kulosa.mp3')
        elif opcion == "4" :
            pygame.mixer.music.load('canciones/Boyfriend.mp3')
        elif opcion == "5":
            print("Cerrando reproductor...")
            break
        else:
            print("Opción no válida")
            continue

        pygame.mixer.music.play()
        print("▶ Reproduciendo...")


        while True:
            print("Elige una opción: \n1.Pausar \n2.Reanudar \n3.Detener y salir ")
            coman = input("Opción: ").strip()

            if coman == "1" :
                pygame.mixer.music.pause()
                print("Musica en pausa")
            elif coman == "2" :
                pygame.mixer.music.unpause()
                print("Musica reanudada")
            elif coman == "3" :
                pygame.mixer.music.stop()
                break
            else:
                print("Opción no válida")

else :
    print("Hasta luego.")
