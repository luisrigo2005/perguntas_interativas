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