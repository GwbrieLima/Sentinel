from datetime import datetime

def salvar_historico(cidade, temperatura, umidade, vento, risco):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("historico.csv", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{agora}, {cidade}, {temperatura}, {umidade}, {vento}, {risco}\n"
        )