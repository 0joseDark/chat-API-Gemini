# chat-API Gemini
API Gemini com um chat simples.  
---
Ele inclui:  
- **Entrada de texto** para a pergunta do utilizador.  
- **Saída de texto** para a resposta da API Gemini.  
- **Menu** para opções adicionais.  
- **Botões** para enviar a pergunta e sair.  

---

### 📌 **Instalar dependências**  
Antes de executar o código, instale a biblioteca para acessar a API Gemini:  
```sh
pip install google-generativeai
```
### **🔍 Explicação do Código**
1. **Importação de bibliotecas**  
   - `tkinter`: Cria a interface gráfica.  
   - `google.generativeai`: Permite a comunicação com a API Gemini.  

2. **Configuração da API Gemini**  
   - O programa configura a API com uma chave [(API_KEY).](https://github.com/0joseDark/chat-API-Gemini/blob/main/API_KEY.md).
3. **Função `enviar_pergunta()`**  
   - Lê o texto da caixa de entrada.  
   - Envia a pergunta para a API Gemini.  
   - Exibe a resposta na caixa de saída.  
   - Mostra erro caso a API falhe.  

4. **Interface Gráfica (Tkinter)**  
   - **Janela principal** com título e tamanho fixo.  
   - **Menu** com uma opção para sair.  
   - **Caixas de entrada e saída** com `ScrolledText` para rolagem.  
   - **Botões** para enviar pergunta e fechar o programa.  

---

### **✅ Testar o Programa**
1. Insira a sua chave da API Gemini na variável `API_KEY`.  
2. Execute o script.  
3. Escreva uma pergunta e clique em **"Enviar"**.  
4. O programa enviará a pergunta para a API Gemini e exibirá a resposta.  
5. Para sair, clique no botão **"Sair"** ou no menu **"Opções → Sair"**.
