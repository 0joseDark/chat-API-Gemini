### **📌 Passo a Passo para Obter a API Key da Gemini**
  
#### **1️⃣ Criar uma Conta no Google Cloud**
1. Acesse **[Google AI Studio](https://aistudio.google.com/)**.  
2. Faça login com sua conta do **Google**.  

#### **2️⃣ Ativar a API Gemini**
3. No **Google AI Studio**, vá para a aba **API Keys** ou acesse diretamente:  
   - **[Página da API Key](https://aistudio.google.com/app/apikey)**  
4. Clique em **"Create API Key"** (Criar Chave de API).  
5. A chave será gerada e exibida na tela.  

#### **3️⃣ Copiar e Usar a API Key**
6. Copie a chave gerada.  
7. No seu código Python, substitua `"SUA_CHAVE_AQUI"` pela sua API Key:  
   ```python
   API_KEY = "SUA_CHAVE_AQUI"
   genai.configure(api_key=API_KEY)
   ```

---

### **⚠️ Atenção:**
- **Não compartilhe sua API Key** publicamente.  
- **A chave é gratuita**, mas tem limites de uso.  
- Se precisar de mais requisições, ative a **faturação no Google Cloud**.
