def verificar_alertas(temperatura, umidade, vento):
    alerta = False

    print("\n ===== ALERTAS =====")

    if int(vento) >= 50:
        print("ALERTA: Ventos fortes!")

    if int(umidade) >= 90:
        print("ALERTA: Prossibilidade de chuva intensa!")

    if int(temperatura) >= 38:
        print("ALERTA: Calor extremo!")

    if int(temperatura) <= 0:
        print("ALERTA: Frio extremo!")

    if not alerta:
        print("Nenhum alerta no momento.")