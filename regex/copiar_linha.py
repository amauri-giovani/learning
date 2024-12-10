import re


file = input("Absolute file path: ")
new_text = ""

with open(file) as arq:
    for contents in arq.readlines():
        x = re.search(r"(\w+\s?=\s?)", contents)
        if x:
            y = re.search(r"(print|#)", contents)
            start = x.start()
            variable = re.search(r"\w+", x.string)
            group_found = variable.group()
            # text_variable = '{' + group_found + '}'
            text_variable = ''.join(['{', group_found, '}'])
            print(text_variable)
            if not y:
                # novo_texto += f"{texto}{' ' * start}print(f'{s}: {g}')\n\n"
                new_text += f"{contents}{' ' * start}print(f'{str(group_found)}: {text_variable}')\n\n"
        else:
            new_text += f"{contents}"

with open("novo_arquivo.py", "w") as arq_w:
    arq_w.write(new_text)

# arquivo = input("Caminho completo do arquivo: ")
# arquivo = "funcao.py"
# novo_texto = ""

# with open(arquivo) as arq:
#     for texto in arq.readlines():
#         x = re.search(r"(\w+\s?=\s?)", texto)
#         if x:
#             y = re.search(r"(print|#)", texto)
#             start = x.start()
#             variavel = re.search(r"\w+", x.string)
#             grupo = variavel.group()
#             s = str(variavel.group())
#             g = '{' + f"{grupo}" + '}'
#             if not y:
#                 novo_texto += f"{texto}{' ' * start}print(f'{s}: {g}')\n\n"
#         else:
#             novo_texto += f"{texto}"

# novo_arquivo = input("Digite um nome para gerar o novo arquivo: ")
#     if not novo_arquivo.endswith(".py"):
#         novo_arquivo += ".py"

# with open("novo_arquivo.py", "w") as arq_w:
#     arq_w.write(novo_texto)
