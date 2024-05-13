import random

# Constantes
VICTORIA_JUAN = 1
VICTORIA_MARIA = 2
EMPATE = 0

# Tabla de combinaciones de dados y sus puntajes
PUNTAJES = {
    (4, 1): 1,
    (1, 4): 1,
    (4, 2): 2,
    (2, 4): 2,
    (4, 3): 3,
    (3, 4): 3,
    (4, 4): 4,
    (4, 5): 5,
    (5, 4): 5,
    (4, 6): 6,
    (6, 4): 6,
}


def simular_juego():
    """
    Simula una partida del juego de dados entre Juan y María.

    Devuelve un valor que indica el ganador:
    - 1 si Juan gana
    - 2 si María gana
    - 0 si hay empate
    """

    # Turno de Juan
    puntaje_juan = tirar_dados_juan()

    # Turno de María
    puntaje_maria = tirar_dados_maria(puntaje_juan)

    # Determinar el ganador
    if puntaje_juan > puntaje_maria:
        return VICTORIA_JUAN  # Juan gana
    elif puntaje_maria > puntaje_juan:
        return VICTORIA_MARIA  # María gana
    else:
        return EMPATE  # Empate


def tirar_dados_juan():
    """
    Simula el turno de Juan en el juego.

    Devuelve el puntaje final de Juan.
    """
    # Lanza los dados
    # Si el puntaje es 0, tira devuelta, esperando conseguir algun punto
    # Si el puntaje es menor a 4, tira el dado que no es 4
    # Si el puntaje es mayor o igual a 4, se planta

    # Lanzamiento inicial de dos dados
    dado1, dado2 = random.randint(1, 6), random.randint(1, 6)
    puntaje = PUNTAJES.get((dado1, dado2), 0)

    if puntaje == 0:
        # Tira ambos dados nuevamente si el puntaje es 0
        dado1, dado2 = random.randint(1, 6), random.randint(1, 6)
        puntaje = PUNTAJES.get((dado1, dado2), 0)
    elif puntaje < 4:
        # Tira el dado que no es 4
        if dado1 == 4:
            dado2 = random.randint(1, 6)
        else:
            dado1 = random.randint(1, 6)
        puntaje = PUNTAJES.get((dado1, dado2), 0)

    return puntaje


def tirar_dados_maria(puntaje_juan):
    """
    Simula el turno de María en el juego.

    Argumentos:
      puntaje_juan: El puntaje final de Juan.

    Devuelve el puntaje final de María.
    """
    # Lanza los dados
    # Si el puntaje es 0, tira devuelta, esperando conseguir algun punto
    # Si el puntaje es mayor a 0:
    #   Si el puntaje de juan es mayor, tira el dado que no sea 4
    #   Si el puntaje de juan es menor o igual, se planta

    # Lanzamiento inicial de dos dados
    dado1, dado2 = random.randint(1, 6), random.randint(1, 6)
    puntaje = PUNTAJES.get((dado1, dado2), 0)

    # María conoce el puntaje de Juan y toma la mejor decisión
    if puntaje == 0:
        # Tira nuevamente los dados esperando conseguir algun punto
        dado1, dado2 = random.randint(1, 6), random.randint(1, 6)
        puntaje = PUNTAJES.get((dado1, dado2), 0)
    else:
        if puntaje_juan > puntaje:
            # Tira nuevamente el dado que no sea 4, con la esperanza de superar a Juan
            if dado1 == 4:
                dado2 = random.randint(1, 6)
            else:
                dado1 = random.randint(1, 6)
            puntaje = PUNTAJES.get((dado1, dado2), 0)

    return puntaje


def simular_n_veces(n):
    """
    Simula el juego n veces y calcula las frecuencias relativas de los resultados.

    Argumentos:
      n: El número de veces que se simula el juego.
    """
    resultados = [0, 0, 0]

    for _ in range(n):
        resultado_juego = simular_juego()
        resultados[resultado_juego] += 1

    probabilidad_juan = resultados[VICTORIA_JUAN] / n
    probabilidad_maria = resultados[VICTORIA_MARIA] / n
    probabilidad_empate = resultados[EMPATE] / n

    print(f"Victorias Juan: {resultados[VICTORIA_JUAN]}")
    print(f"Victorias María: {resultados[VICTORIA_MARIA]}")
    print(f"Empates: {resultados[EMPATE]}")
    print(f"Probabilidad de victoria de Juan: {probabilidad_juan}")
    print(f"Probabilidad de victoria de María: {probabilidad_maria}")
    print(f"Probabilidad de empate: {probabilidad_empate}")

    return {
        "VICTORIA_JUAN": resultados[VICTORIA_JUAN],
        "VICTORIA_MARIA": resultados[VICTORIA_MARIA],
        "EMPATE": resultados[EMPATE],
    }



# Solo ejecutar este codigo si el archivo se ejecuta directamente
if __name__ == "__main__":
    # simulaciones
    print("\n1_000 veces: \n")
    simular_n_veces(1_000)
    print()
    print("\n10_000 veces: \n")
    simular_n_veces(10_000)
    print()
    print("\n100_000 veces: \n")
    simular_n_veces(100_000)
