def calcular_risco(temperatura, umidade, vento):
    pontos = 0

    if temperatura >= 38:
        pontos += 2

    if umidade >= 90:
        pontos += 1

    if vento >= 50:
        pontos += 2

    if pontos <= 1:
        return "BAIXO"
    
    elif pontos <= 3:
        return "MODERADO"
    
    else:
        return "ALTO"