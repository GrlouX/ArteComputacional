a,b,c,d = (0,0,512,596) # Coordenadas iniciais da cortina de apresentação
step = 16               # Determina passo do movimento da cortina de apresentação
   
def setup():
    size(512, 596) # Define tamanho da tela
    frameRate(1.2) # Determina taxa de variação dos quadros

    global img
    img = loadImage("example_waldryano-pixabay.png") # Carrega imagem de fundo

def draw():
    background(0)    # Cor de fundo padrão da tela (preto)
    image(img, 0, 0) # Posiciona imagem de fundo na origem (canto superior esquerdo)

    global c
    rect(a,b,c,d) # Define cortina em forma de retângulo com coordenadas iniciais
    c -= step     # Aplica movimentos na cortina
    fill(random(255),random(255),random(255)) # Gera cores aleatórias para cortina
