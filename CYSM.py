import openai                                       #Import do openai para a requisição da IA (pip install --upgrade openai)
import secret                                       #Import da chave pessoal da minha conta no dalle 2


Secret = secret.text
choice = [1,2,3,4,5,6]
animal = 0
coranimal = 0
acessorio = 0
cenario = 0
estiloimagem = 0

listaanimal = ['Duck ','Monkey ','Cat ','Dog ','Fish ','ostrich ']
listacoranimal = ['yellow ','green ','brown ','red ','gray ','white ']
listaacessorio = ['hat ','boots ','gloves ','glasses ','football boots ', 'bikini ']
listacenario = ['in front of mountains', 'inside an football stadium', 'inside an aquarium', 'flying in the sky', 'inside an florest', 'floating on mars planet']
listaestilo = ['4k Pixel Art ', '4k Van Gohg style painting ', '4k 3d model ', '4k high quality photo ', '4k 35mm ', '4k cartoon ']

while animal not in choice:
    animal = int(input("""
    Escolha dentre essas especies de animal:
    1- Pato
    2- Macaco
    3- Gato
    4- Cachorro
    5- Peixe
    6- Avestruz
    """))
    if animal not in choice:
        print('Escolha uma opção válida')

while coranimal not in choice:
    coranimal = int(input("""
    Escolha dentre essas cores para o animal:
    1- Amarelo
    2- Verde
    3- Marrom
    4- Vermelho
    5- Cinza
    6- Branco
    """))
    if coranimal not in choice:
        print('Escolha uma opção válida')

while acessorio not in choice:
    acessorio = int(input("""
    Escolha dentre esses acessórios para o animal:
    1- Chapéu
    2- Botas
    3- Luvas
    4- Óculos
    5- Chuteiras
    6- Biquini
    """))
    if acessorio not in choice:
        print('Escolha uma opção válida')

while cenario not in choice:
    cenario = int(input("""
    Escolha dentre esses cenários:
    1- Montanhas
    2- Estádio de futebol
    3- Aquário
    4- Céu
    5- Floresta
    6- Marte
    """))
    if cenario not in choice:
        print('Escolha uma opção válida')

while estiloimagem not in choice:
    estiloimagem = int(input("""
    Escolha dentre esses estilos de imagem:
    1- Pixel Art
    2- Pintura estilo Van Gohg
    3- Modelagem 3d
    4- Fotorealismo
    5- Macro
    6- Cartoon
    """))
    if estiloimagem not in choice:
        print('Escolha uma opção válida')

promp = f'{listacoranimal[coranimal-1]}{listaanimal[animal-1]}using a {listaacessorio[acessorio-1]}, {listacenario[cenario-1]}, {listaestilo[estiloimagem-1]}'

openai.api_key = Secret
openai.Model.list()

response = openai.Image.create(
    prompt=promp,
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)