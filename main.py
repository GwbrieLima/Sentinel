import requests
from alertas import verificar_alertas
from risco import calcular_risco
from historico import salvar_historico

print("===== SENTINEL =====")
cidade = input("Digite sua cidade: ")
print(f"Consultando dados de {cidade}...")

url = f"https://wttr.in/{cidade}?format=j1"

try:
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        temperatura = dados["current_condition"][0]["temp_C"]
        umidade = dados["current_condition"][0]["humidity"]
        vento = dados["current_condition"][0]["windspeedKmph"]

        print("\n===== DADOS ATUAIS =====")
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento} km/h")

        verificar_alertas(temperatura, umidade, vento)

    else:
        print("Erro ao consultar sua cidade.")

    risco = calcular_risco(
        int(temperatura),
        int(umidade),
        int(vento)
        )

    print(f"\nNIVEL DE RISCO: {risco}")

    salvar_historico(
        cidade,
        temperatura,
        umidade,
        vento,
        risco
    )

    print("\n===== PREVISÃO =====")

    for dia in dados["weather"][:3]:
        data = dia["date"]
        tempo_max = dia["maxtempC"]
        tempo_min = dia["mintempC"]

        print(f"\nData: {data}")
        print(f"Máxima: {tempo_max}°C")
        print(f"Mínima: {tempo_min}°C")

except Exception as erro:
    print("Erro:", erro)