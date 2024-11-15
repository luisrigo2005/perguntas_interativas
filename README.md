# Projeto de Perguntas Interativas em Python
Este projeto utiliza a biblioteca InquirerPy para criar uma interface de linha de comando interativa que permite ao usuário responder perguntas sobre seu conhecimento em Python.

## Pré-requisitos
Antes de executar o projeto, você precisa ter o Python instalado em sua máquina. Além disso, você deve instalar a biblioteca InquirerPy. Você pode fazer isso utilizando o seguinte comando:

´´´
pip install InquirerPy
´´´

## Como Executar
1. Clone este repositório em sua máquina local:

´´´
git clone https://github.com/seu_usuario/seu_repositorio.git
´´´

2. Navegue até o diretório do projeto:
´´´
cd seu_repositorio
´´´

3. Execute o script app.py:
´´´
python app.py
´´´

4. Responda à pergunta exibida no terminal.

# Estrutura do Código
O arquivo app.py contém o seguinte código:
from InquirerPy import prompt

perguntas = [
    {
        'type': 'list',
        'message': 'Qual seu conhecimento em Python?',
        "choices": [
            'Iniciante',
            'Intermediario',
            'Avançado']
    },
]

respostas = prompt(perguntas)
print(respostas)

# Descrição do Código
O código importa a função prompt da biblioteca InquirerPy.
Define uma lista de perguntas com uma única pergunta sobre o conhecimento do usuário em Python.
Utiliza a função prompt para exibir a pergunta e coletar a resposta do usuário.
Por fim, imprime a resposta no terminal.
