import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Carrega a chave da API do arquivo .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. AUTOMAÇÃO: Criando dados falsos para testar o Pandas
data = {
    'Produto': ['Teclado', 'Mouse', 'Monitor', 'Cadeira'],
    'Vendas': [150, 200, 50, 30],
    'Preco': [100, 50, 1200, 800]
}
df = pd.DataFrame(data)

# 3. LÓGICA: Preparando o que a IA vai ler
# Transformamos o resumo do Pandas em texto para a IA entender
resumo_estatistico = df.describe().to_string()

# 4. A IA: Enviando o contexto para o "Cérebro"
response = client.chat.completions.create(
  model="gpt-3.5-turbo", # Ou gpt-4o
  messages=[
    {"role": "system", "content": "Você é um analista de dados Python experiente."},
    {"role": "user", "content": f"Analise estes dados de vendas e me diga qual produto faturou mais e uma sugestão de estratégia:\n{resumo_estatistico}"}
  ]
)

# 5. RESULTADO
print("--- RESPOSTA DA IA ---")
print(response.choices[0].message.content)
