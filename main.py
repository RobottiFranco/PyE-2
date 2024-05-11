import random

def simular_juego():
    """
    Simula una partida del juego de dados entre Juan y María.

    Devuelve un valor que indica el ganador:
    - 1 si Juan gana
    - 2 si María gana
    - 0 si hay empate
    """

    # Puntaje inicial de Juan y María
    puntaje_juan = 0
    puntaje_maria = 0

    # Turno de Juan
    puntaje_juan = tirar_dados_juan(puntaje_juan)

    # Turno de María
    puntaje_maria = tirar_dados_maria(puntaje_juan, puntaje_maria)

    # Determinar el ganador
    if puntaje_juan > puntaje_maria:
        return 1  # Juan gana
    elif puntaje_maria > puntaje_juan:
        return 2  # María gana
    else:
        return 0  # Empate

def tirar_dados_juan(puntaje_actual):
    """
    Simula el turno de Juan en el juego.

    Argumentos:
      puntaje_actual: El puntaje actual de Juan.

    Devuelve el puntaje final de Juan.
    """

    # Lanzamiento inicial de dos dados
    puntaje_tiro1, puntaje_tiro2 = random.randint(1, 6), random.randint(1, 6)
    puntaje_inicial = puntaje_tiro1 + puntaje_tiro2

    # Segunda tirada si es necesario
    if puntaje_inicial == 0:
        puntaje_tiro1, puntaje_tiro2 = random.randint(1, 6), random.randint(1, 6)
        puntaje_final = puntaje_tiro1 + puntaje_tiro2
    elif puntaje_inicial < 4:
        if puntaje_tiro1 == 4 or puntaje_tiro2 == 4:
            puntaje_tiro3 = random.randint(1, 6)
            puntaje_final = puntaje_tiro3
        else:
            puntaje_final = puntaje_inicial
    else:
        puntaje_final = puntaje_inicial

    return puntaje_actual + puntaje_final

def tirar_dados_maria(puntaje_juan, puntaje_maria):
    """
    Simula el turno de María en el juego.

    Argumentos:
      puntaje_juan: El puntaje final de Juan.
      puntaje_maria: El puntaje actual de María.

    Devuelve el puntaje final de María.
    """

    # María conoce el puntaje de Juan y toma la mejor decisión
    if puntaje_juan == 0:
        puntaje_tiro1, puntaje_tiro2 = random.randint(1, 6), random.randint(1, 6)
        puntaje_final = puntaje_tiro1 + puntaje_tiro2
    elif puntaje_juan < 4:
        puntaje_tiro1, puntaje_tiro2 = random.randint(1, 6), random.randint(1, 6)
        if puntaje_tiro1 == 4 or puntaje_tiro2 == 4:
            puntaje_tiro3 = random.randint(1, 6)
            puntaje_final = puntaje_tiro3
        else:
            puntaje_final = puntaje_maria
    else:
        puntaje_final = puntaje_maria

    return puntaje_maria + puntaje_final

def simular_n_veces(n):
    """
    Simula el juego n veces y calcula las frecuencias relativas de los resultados.

    Argumentos:
      n: El número de veces que se simula el juego.
    """
  
    victorias_juan = 0
    victorias_maria = 0
    empates = 0

    for _ in range(n):
        resultado_juego = simular_juego()
        if resultado_juego == 1:
            victorias_juan += 1
        elif resultado_juego == 2:
            victorias_maria += 1
        else:
            empates += 1

    probabilidad_juan = victorias_juan / n
    probabilidad_maria = victorias_maria / n
    probabilidad_empate = empates / n

    print(f"Simulaciones: {n}")
    print(f"Victorias Juan: {victorias_juan}")
    print(f"Victorias María: {victorias_maria}")
    print(f"Empates: {empates}")
    print(f"Probabilidad de victoria de Juan: {probabilidad_juan}")
    print(f"Probabilidad de victoria de María: {probabilidad_maria}")
    print(f"Probabilidad de empate: {probabilidad_empate}")

#simulaciones
print("\n1000 veces: \n")
simular_n_veces(1000)
print("\n10000 veces: \n")
simular_n_veces(10000)
print("\n100000 veces: \n")
simular_n_veces(100000)
