import pygame
import random
import math
from pygame import mixer
import io

# Para inicializar pygame
pygame.init()

# Establecer el tamaño de nuestra pantalla y mostrarla
pantalla = pygame.display.set_mode((800, 600))


# def fuente_bytes(fuente):
#     # Abre el archivo TTF en modo lectura binaria
#     with open(fuente, 'rb') as f:
#         # Lee todos los bytes del archivo y los almacena en una variable
#         ttf_bytes = f.read()
#     # Crea un objeto BytesIO a partir de los bytes del archivo TTF
#     return io.BytesIO(ttf_bytes)


# Cambiar Título, Icono y Color
pygame.display.set_caption("Invasión espacial - 24.7")
icono = pygame.image.load("images\\ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("images\\Fondo.jpg")

# Agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.5)
# -1 para que cuando termine la musica vuelva a empezar
mixer.music.play(-1)

# Creamos al personaje principal del juego y sus variables
img_jugador = pygame.image.load("images\\cohete.png")
# 368 es la posicion exacta para que se ubique justo al medio de la pantalla
jugador_x = 368
# 500 pixeles para que el jugador se ubique justo en la parte inferior de la pantalla
jugador_y = 500
jugador_x_cambio = 0

# Creamos al enemigo del juego y sus variables
# Duplicamos todas las variables que teniamos de enemigos y en un lista vacia
# y creamos un loop for que vaya completando cada una de las listas en 8 registros de enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 6

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("images\\enemigo.png"))
    # Usamos random para darle una ubicacion en el eje x aleatoria al enemigo 736 es la resta de 800 - 64px de la img
    enemigo_x.append(random.randint(0, 736))
    # Usamos random para darle una posicion de altura en el eje y aleatoria al enemigo
    enemigo_y.append(random.randint(0, 200))
    # Lo fijamos en 0.5 para que cuando la posicion del enemigo llegue a los bordes no se detenga,
    # si no que cambie de direccion, lo mismo con el eje x 50 para que el enemigo vaya bajando
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# Creamos las variables de las balas que dispara el jugador
balas = []
img_bala = pygame.image.load("images\\bala.png")
bala_x = 0
# Usamos la misma ubicacion inicial que tiene la nave
bala_y = 500
# eje y
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# Variable para la puntuacion del jugador
puntacion = 0
# fuente_como_bytes = fuente_bytes("RuthlessWreckin2.ttf")
fuente = pygame.font.Font("RuthlessWreckin2.ttf", 32)
# Coordenadas de donde debe aparecer el puntaje
texto_x = 10
texto_y = 10

# Variable para el texto del fin del juego
fuente_final = pygame.font.Font("RuthlessWreckin2.ttf", 40)


def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER LOOSER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (190, 250))


# Funcion mostrar puntaje
def motrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntacion}", True, (252, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion para construir la posicion del personaje
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion para construir la posicion del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Funcion para disparar la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    # Para que la bala aparezca justo al medio de la nave le sumamos los valores
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion para calcular colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    # Formula para calcular la distancia entre la nave y el enemigo
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Cambiamos el color del fondo de la pantalla con RGB / Fondo que elegimos al final
    # pantalla.fill((90, 220, 200))
    pantalla.blit(fondo, (0, 0))
    # Darle movimiento al jugador en el eje x / eje y (DEMOSTRACION)
    # jugador_x -= 0.1
    # jugador_y -= 0.1

    # Iterar eventos
    for evento in pygame.event.get():

        # Evento para cerrar el juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            # print("una tecla fue presionada")
            # VERIFICAMOS SI SE ACTIVA EL EVENTO CUANDO PRESIONAS LA FLECHA A LA IZQUIERDA / DERECHA
            if evento.key == pygame.K_LEFT:
                # print('flecha izq presionada')
                jugador_x_cambio = -0.5

            if evento.key == pygame.K_RIGHT:
                # print('flecha derecha presionada')
                jugador_x_cambio = 0.5

            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                # configuracion para poder disparar mas de una bala
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)
                # Activar el evento solo cuando la bala ya deja de ser visible
                if not bala_visible:
                    # generamos un relacion entre las dos variables para que no dependa de jugador_x de por vida
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print('flecha soltada')
                # Lo establecemos en cero para que deje de moverse cuando suelte las telas de las flechitas
                jugador_x_cambio = 0

    # modificar la posicion del jugador
    jugador_x += jugador_x_cambio

    # Limitar el movimiento del jugador para que no se salga de los bordes de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar la posicion del enemigo
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        # ESPECIFICAMOS EL INDICE [E] PARA QUE SEPA CUAL ENEMIGO ELIMINAR CUANDO LE DISPAREMOS
        enemigo_x[e] += enemigo_x_cambio[e]

        # Limitar el movimiento del enemigo para que no se salga de los bordes de la pantalla
        if enemigo_x[e] <= 0:
            # si toca el borde izq cambie de direccion hacia la derecha
            enemigo_x_cambio[e] = 0.5
            # Además tambien modificamos al altura del eje y para que vaya bajando el enemigo hasta que toque al jugador
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            # si toca el borde dereco cambie de direccion hacia la izq
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        # colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        # if colision:
        #     sonido_colision = mixer.Sound("Golpe.mp3")
        #     sonido_colision.play()
        #     # reestablecer la bala a un posicion inicial
        #     bala_y = 500
        #     bala_visible = False
        #     puntacion += 1
        #     # volvemos a darle una posicion random al enemigo para que desaparezca cuando el disparo le llegue
        #     enemigo_x[e] = random.randint(0, 736)
        #     enemigo_y[e] = random.randint(0, 200)
        # enemigo(enemigo_x[e], enemigo_y[e], e)
        # nueva configuracion te permite disparar mas de una bala
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntacion += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la bala
    # Primera validacion: limitar el movimiento de la bala cuando llegue hasta arriba de la pantalla en el eje y
    # con esto podemos disparar mas de una bala
    # if bala_y <= -64:
    #     bala_y = 500
    #     bala_visible = False
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Hacemos la llamada a la funcion
    jugador(jugador_x, jugador_y)

    # Mostrar puntaje
    motrar_puntaje(texto_x, texto_y)

    # Actualizamos la pantalla para que se vean todos los cambios
    pygame.display.update()


