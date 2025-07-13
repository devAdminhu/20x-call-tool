import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
from tkinter import filedialog
import os
import shutil

# Tema escuro
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def selecionar_imagem():
    return filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )

def mostrar_mensagem(titulo, mensagem, tipo="info"):
    icones = {"info": "info", "erro": "cancel", "aviso": "warning"}
    CTkMessagebox(title=titulo, message=mensagem, icon=icones.get(tipo, "info"))

def perguntar_sim_nao(titulo, mensagem):
    resposta = CTkMessagebox(
        title=titulo,
        message=mensagem,
        icon="question",
        option_1="Sim",
        option_2="Não"
    ).get()
    return resposta.lower() == "sim"

def pedir_texto(titulo, mensagem):
    dialog = ctk.CTkInputDialog(title=titulo, text=mensagem)
    return dialog.get_input()

def processar_imagem(caminho):
    img = Image.open(caminho)
    pasta_destino = "20xbuild/img"
    os.makedirs(pasta_destino, exist_ok=True)

    # Limpar imagens antigas
    for f in os.listdir(pasta_destino):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            try:
                os.remove(os.path.join(pasta_destino, f))
            except Exception as e:
                print(f"Erro ao remover {f}: {e}")

    # Copiar nova imagem
    destino = os.path.join(pasta_destino, os.path.basename(caminho))
    shutil.copy2(caminho, destino)

    mostrar_mensagem(
        "Sucesso",
        f"Imagem {os.path.basename(caminho)} copiada!\nFormato: {img.format}, Tamanho: {img.size}",
        tipo="info"
    )

    prompt = None
    if perguntar_sim_nao("Adicionar Prompt", "Deseja adicionar um prompt junto com a imagem?"):
        prompt = pedir_texto("Prompt", "Escreva o que deseja que a IA faça.")
    return f"Verifique esta imagem: {destino}", prompt

def user_interaction():
    if perguntar_sim_nao("Escolha", "Deseja enviar uma imagem?\n(Sim = Imagem, Não = Texto)"):
        caminho = selecionar_imagem()
        if caminho:
            try:
                return processar_imagem(caminho)
            except Exception as e:
                mostrar_mensagem("Erro", f"Erro ao processar imagem: {e}", tipo="erro")
        else:
            mostrar_mensagem("Aviso", "Nenhum arquivo selecionado!", tipo="aviso")
        return None, None
    else:
        prompt = pedir_texto("Prompt", "Escreva o que deseja que a IA faça.")
        return prompt, None

if __name__ == "__main__":
    ctk.CTk().withdraw()  # Oculta a janela principal
    resultado, prompt_extra = user_interaction()
    print("Prompt:", resultado)
    if prompt_extra:
        print("Prompt adicional:", prompt_extra)
