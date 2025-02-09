**Jupyter Notebook**, mantendo a funcionalidade do chat com a **API Gemini**.  

### **📌 Instalação das dependências**  
Antes de executar no **Jupyter Notebook**, instale os pacotes necessários:  
```sh
pip install google-generativeai ipywidgets
```

---

### **✅ Código adaptado para Jupyter Notebook**
```python
import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, HTML

# 📌 Configurar a API Gemini
API_KEY = "SUA_CHAVE_AQUI"  # 🔹 Substitua pela sua chave da API Gemini
genai.configure(api_key=API_KEY)

# 🔹 Criar a interface gráfica com widgets
entrada_texto = widgets.Textarea(
    placeholder="Digite a sua pergunta aqui...",
    layout=widgets.Layout(width="100%", height="100px")
)

saida_texto = widgets.Output()

botao_enviar = widgets.Button(
    description="Enviar",
    button_style="primary"
)

# 🔹 Função para enviar pergunta e mostrar resposta
def enviar_pergunta(b):
    pergunta = entrada_texto.value.strip()
    
    if not pergunta:
        with saida_texto:
            print("⚠️ Por favor, escreva uma pergunta!")
        return
    
    with saida_texto:
        saida_texto.clear_output()  # Limpar saída anterior
        print("⏳ Processando...")

    try:
        modelo = genai.GenerativeModel("gemini-pro")
        resposta = modelo.generate_content(pergunta)

        with saida_texto:
            saida_texto.clear_output()
            print(f"**Resposta:**\n{resposta.text}")
    
    except Exception as e:
        with saida_texto:
            saida_texto.clear_output()
            print(f"❌ Erro: {str(e)}")

# 🔹 Conectar botão à função
botao_enviar.on_click(enviar_pergunta)

# 🔹 Exibir os componentes no Jupyter Notebook
display(HTML("<h2>💬 Chat com Gemini API</h2>"))
display(entrada_texto, botao_enviar, saida_texto)
```

---

### **📌 Como funciona no Jupyter Notebook**
1. **Executar a célula** para exibir a interface.  
2. **Escrever uma pergunta** no campo de entrada.  
3. **Clicar no botão "Enviar"** para obter a resposta.  
4. **A resposta aparece abaixo** na área de saída (`saida_texto`).
