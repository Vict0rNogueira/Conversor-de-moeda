# Conversor-de-moeda
Um pequeno projeto para testar minhas novas habilidades em API e na biblioteca STREAMLIT

💱 Conversor de Moedas Interativo

Um projeto em Python que permite converter valores entre diferentes moedas em tempo real, usando POO e uma interface interativa com Streamlit.


1️⃣ Qual tecnologia foi usada?

Python: Linguagem de programação para lógica e integração com APIs.

Streamlit: Biblioteca para criar a interface web interativa de forma simples.



2️⃣ Qual biblioteca e o que ela faz?

requests: Faz requisições HTTP para a API de moedas e obtém as cotações.

Streamlit: Cria menus, botões, inputs e exibe resultados de forma visual e interativa.



3️⃣ Como baixar?

Clone este repositório:

git clone <URL_DO_REPOSITORIO>


ou baixe como ZIP e extraia em uma pasta.

Entre na pasta do projeto:

cd conversor_moeda



4️⃣ Como instalar as dependências do projeto?

É recomendável criar um ambiente virtual para não misturar com outras bibliotecas do sistema:

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt


Arquivo requirements.txt sugerido para este projeto:

streamlit
requests



5️⃣ Como rodar?

No terminal, dentro da pasta do projeto:

streamlit run app.py


O Streamlit abrirá automaticamente no navegador.

Caso não abra, acesse manualmente: http://localhost:8501

Agora você pode selecionar moeda de origem, moeda de destino e o valor para conversão usando menus clicáveis, e o resultado aparecerá instantaneamente.

✅ Funcionalidades

Conversão de moedas em tempo real via API.

Interface gráfica interativa com Streamlit.

Menus suspensos (selectbox) para selecionar moedas.

Suporte a múltiplas moedas.
