import tkinter as tk
from tkinter import scrolledtext, Menu, messagebox
import google.generativeai as genai

# 📌 Configure a API Gemini com a sua chave
API_KEY = "SUA_CHAVE_AQUI"  # 🔹 Substitua pela sua chave da API Gemini
genai.configure(api_key=API_KEY)

# 🔹 Função para enviar a pergunta e obter resposta
def enviar_pergunta():
    pergunta = entrada_texto.get("1.0", tk.END).strip()
    
    if not pergunta:
        messagebox.showwarning("Aviso", "Por favor, escreva uma pergunta!")
        return
    
    try:
        modelo = genai.GenerativeModel("gemini-pro")  # Modelo Gemini
        resposta = modelo.generate_content(pergunta)
        saida_texto.delete("1.0", tk.END)  # Limpa a saída anterior
        saida_texto.insert(tk.END, resposta.text)  # Exibe a resposta
    except Exception as e:
        saida_texto.insert(tk.END, f"Erro: {str(e)}")

# 🔹 Criar a janela principal
janela = tk.Tk()
janela.title("Chat com Gemini API")
janela.geometry("500x400")

# 🔹 Criar a barra de menu
menu_bar = Menu(janela)
janela.config(menu=menu_bar)

# 🔹 Adicionar um menu com opção de sair
menu_opcoes = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)
menu_opcoes.add_command(label="Sair", command=janela.quit)

# 🔹 Caixa de entrada de texto
tk.Label(janela, text="Digite a sua pergunta:", font=("Arial", 10)).pack(pady=5)
entrada_texto = scrolledtext.ScrolledText(janela, width=50, height=5)
entrada_texto.pack(padx=10, pady=5)

# 🔹 Botão para enviar a pergunta
btn_enviar = tk.Button(janela, text="Enviar", command=enviar_pergunta, font=("Arial", 10))
btn_enviar.pack(pady=5)

# 🔹 Caixa de saída de texto
tk.Label(janela, text="Resposta:", font=("Arial", 10)).pack(pady=5)
saida_texto = scrolledtext.ScrolledText(janela, width=50, height=5, state="normal")
saida_texto.pack(padx=10, pady=5)

# 🔹 Botão para sair
btn_sair = tk.Button(janela, text="Sair", command=janela.quit, font=("Arial", 10))
btn_sair.pack(pady=10)

# 🔹 Iniciar a aplicação
janela.mainloop()
