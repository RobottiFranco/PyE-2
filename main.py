import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def juan_juega():
    puntaje = sum(lanzar_dados())
    if puntaje == 0:
        puntaje = max(sum(lanzar_dados()), puntaje)
    elif puntaje <= 3:
        puntaje = max(lanzar_dados()[1], puntaje)
    return puntaje

def maria_juega(puntaje_juan):
    if puntaje_juan <= 3:
        return max(lanzar_dados()), puntaje_juan
    else:
        return lanzar_dados()[0], puntaje_juan

def simular_juego():
    puntaje_juan = juan_juega()
    puntaje_maria, puntaje_juan = maria_juega(puntaje_juan)
    if puntaje_juan > puntaje_maria:
        return "Juan gana"
    elif puntaje_juan < puntaje_maria:
        return "María gana"
    else:
        return "Empate"

def simular_n_veces(n):
    resultados = {"Juan gana": 0, "María gana": 0, "Empate": 0}
    for _ in range(n):
        resultado = simular_juego()
        resultados[resultado] += 1
    return resultados

# Simulación del juego 1000, 10000 y 100000 veces
n_simulaciones = [1000, 10000, 100000]
for n in n_simulaciones:
    resultados = simular_n_veces(n)
    print(f"Simulación de {n} juegos:")
    for resultado, frecuencia in resultados.items():
        print(f"{resultado}: {frecuencia / n:.4f}")
    print()
