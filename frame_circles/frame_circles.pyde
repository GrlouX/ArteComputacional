# Tela de desenho
def setup():
    size(600,600)            # Dimensões da tela  
    background(70,57,14)     # Área inicial do fundo
 
# Desenho dinâmico dos círculos       
def draw():
    if frameCount <= 30:        
        for i in range(16):
            for j in range(16):
                d = (i+j) * frameCount  # Diâmetros dos círculos
                circle(30*i,30*j,d)     # Círculo com posições x,y do centro e diâmetro
                fill(random(i*j))       # Tons de cinza aleatórios
        
        saveFrame("frames//##.png")
