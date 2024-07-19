import pyautogui 
import time
import pandas

pyautogui.PAUSE = 0.4

pyautogui.press("win")
pyautogui.write("Opera GX")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=467, y=362)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("emailteste@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456")

pyautogui.click(x=689, y=513)
time.sleep(2)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=452, y=240)
    codigo = str( tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str( tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str( tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str( tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str( tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str( tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str( tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
