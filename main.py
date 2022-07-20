import requests
import json

arquivo = open('filme.txt', 'r')

def requisicao(titulo):
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=b7a184e0')
        dicionario = json.loads(req.text)
        if dicionario['Response'] == 'False':
            print ('Erro na pesquisa')
        else:
            print(dicionario)
        return dicionario


def lista(titulo):
       if titulo['Response'] != 'False':
         requests.post('https://bd-hashtag-default-rtdb.firebaseio.com/Filmes.json', json = titulo)

sair = False
while not sair:
    filme = input('Digite um  filme para adicionar a lista ou Sair para sair:')
    filme = filme.upper()
    if filme == 'SAIR':
        print ('Até a próxima!!')
        sair = True
    else:
        filmejson = requisicao(filme)
        lista(filmejson)





