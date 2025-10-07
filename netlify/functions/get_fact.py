import json
import random

def handler(event, context):
    # Nossa lista de curiosidades sobre dados e tecnologia
    facts = [
        "O Python foi nomeado em homenagem ao grupo de comédia britânico Monty Python.",
        "Aproximadamente 90% dos dados do mundo foram criados nos últimos dois anos.",
        "O primeiro 'bug' de computador foi, literalmente, uma mariposa presa em um relé de computador.",
        "Um único carro autônomo pode gerar até 4.000 GB de dados por dia.",
        "O banco de dados Oracle foi originalmente um projeto financiado pela CIA chamado 'Project Oak'."
    ]
    
    # Escolhe uma curiosidade da lista de forma aleatória
    random_fact = random.choice(facts)
    
    # Prepara e retorna a resposta no formato que a API espera
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps({ 'fact': random_fact })
    }