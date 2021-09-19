# Tela de desenho
def setup():
    size(600,600) # área total de desenho
    background(77) # cor de fundo
    frameRate(60) # controle da taxa de quadros das imagens

# Desenho propriamente dito         
def draw():
    fill(random(128), random(32), random(64), 100) # coloração das imagens com RGB
    noStroke() # retira contorno das imagens
    if mousePressed:
        rect(mouseX, mouseY, 20, 30) # coordenadas de um retângulo: 
            #posição do vértice superior esquerdo, tamanho dos lados
        
# Divirtam-se!

    
