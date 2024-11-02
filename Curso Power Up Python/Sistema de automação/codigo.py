# Pensar passo a passo:

# 1.abrir o sistema da empresa.
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time 

pyautogui.PAUSE = 0.4 # 

#pyautogui.click ->clicar com o moure
#pyautogui.write -> escreve um texto
#pyautogui.press -> pressionar uma tecla do teclado
#pyautogui.hotkey -> apertar um conjunto de teclaas(ctrl C,ctrl V)

# abrir o navegador 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1)

# Entrar no site do sistema
pyautogui.write("dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pode ser que ele demore alguns segundos para carregar o site
time.sleep(1)

# 2.fazer login.
pyautogui.press("tab")
pyautogui.write("obrigadolirapeloaula@gmail.com")

pyautogui.press("tab") # -> passou para o campo de senha 
pyautogui.write("senha123")
pyautogui.press("tab") # -. passou par o botão de login
pyautogui.press("enter")


# 3.Abrir/importar a base de produtos para cadastrar.
#pip install pandas numpy openpyxl

import pandas as pd # -> Pode adicionar um apelido ao import

tabela = pd.read_csv('produtos.csv')

print(tabela)
# 4. Cadastrar um produto.

pyautogui.PAUSE = 0.1
for linha in tabela.index:

    codigo = str(tabela.loc[linha,"codigo"])

    # Clicar no campo do produto
    pyautogui.click(x=476, y=254)

    # Preenchr o codigo
    pyautogui.write(codigo)

    # Passar para o proximo campo
    pyautogui.press("tab") 

    # Marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))

    # Passar para o proximo campo
    pyautogui.press("tab") 

    # Tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))

    # Passar para o proximo campo
    pyautogui.press("tab") 

    # Categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))

    # Passar para o proximo campo
    pyautogui.press("tab") 

    # preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    # Passar para o proximo campo
    pyautogui.press("tab") 

    # custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    # Passar para o proximo campo
    pyautogui.press("tab") 

    # obs
    obs = str(tabela.loc[linha,"obs"])

    if obs != "nan":
           pyautogui.write(obs)

  

     # Passar para o proximo campo
    pyautogui.press("tab")

    # apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    # 5.Repetir isso tudo até avabar a lista de produtos .

