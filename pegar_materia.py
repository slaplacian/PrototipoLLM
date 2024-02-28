from openai import OpenAI
import os

myprompt = '''Gepeto, responda com apenas uma palavra dessa lista aqui [Português, Literatura, Redação, Biologia, Geografia, Matemática, Física, História, Química, Inglês, Espanhol, Filosofia, Sociologia, História da Arte, Orientação de Estudos e Ensino Religioso]

Qual o conteúdo dessa pergunta da pergunta abaixo?
'''

def pegar_materia(pergunta: str) -> str:
  client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

  prompt=f"{myprompt}\n\n{pergunta}"

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )

  return response.__dict__['choices'][0].__dict__['message'].__dict__['content']

if __name__ == "__main__":
  minha_pergunta = input("Pergunta: ")
  print(pegar_materia(minha_pergunta))
