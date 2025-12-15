
print("Bem vindo ao quiz de matematica! vamos testar seus conhecimentos?")

acertos= 0

perguntas = [

    {"pergunta":"qual a soma de 10+12?", "resposta_correta":22},
    {"pergunta":"qual a soma de 22+30?", "resposta_correta":52},
    {"pergunta":"qual a diferença de 70-32?", "resposta_correta":38},
    {"pergunta":"qual a diferença de 100-32?", "resposta_correta":68},
    {"pergunta":"qual é a multiplicação de 7*5?", "resposta_correta":35},
    {"pergunta":"qual é a multiplicação de 8*4?", "resposta_correta":32},
    {"pergunta":"qual é a multiplicação de 5*7?", "resposta_correta":35},
    {"pergunta":"qual é a divisão de 60/2?", "resposta_correta":30},
    {"pergunta":"qual é a divisão de 70/5", "resposta_correta":14},
    {"pergunta":"qual é a divisão de 80/4", "resposta_correta":20},
]

for _,item_perguntas in enumerate(perguntas):
    print(item_perguntas["pergunta"])
    tentativas = 0 # Inicializa o contador de tentativas para cada pergunta

    while True:
        tentativas += 1 # Incrementa o contador de tentativas
        try:
            resposta_usuario=int(input(f"Digite sua reposta (Tentativa {tentativas}):")) # Mostra a tentativa atual
            if resposta_usuario==item_perguntas["resposta_correta"]:
                print("Você acertou!")
                acertos+=1
                break # Sai do loop se acertar
            else:
                # Informa o número da tentativa após um erro
                print(f"Você errou! Esta é sua {tentativas}ª tentativa para esta pergunta. Tente novamente.")
        except:
            # Informa o número da tentativa após uma entrada inválida
            print(f"Entrada inválida! Valido apenas números inteiros. Esta é sua {tentativas}ª tentativa para esta pergunta. Tente novamente.")

print(f"Obrigado por responder as perguntas!,Você foi nota {acertos}")
