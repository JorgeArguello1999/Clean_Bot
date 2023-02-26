import openai

def chatgpt(token, text):
    # Enviar una solicitud al modelo para generar texto
    openai.api_key = token 
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=200
    ).choices[0].text

    # Imprimir la respuesta generada por el modelo
    return response
    
if __name__ == '__main__':
    chatgpt(
        input('Insert a token: '),
        'Hola mundo en sql'
    )
