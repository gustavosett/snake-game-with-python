import pygame
import sys
import random

# Inicializa o pygame
pygame.init()

# Constantes do jogo
LARGURA_TELA = 640
ALTURA_TELA = 480
TAMANHO_GRID = 20
LARGURA_GRID = LARGURA_TELA // TAMANHO_GRID
ALTURA_GRID = ALTURA_TELA // TAMANHO_GRID
VELOCIDADE = 10

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Classe Cobra
class Cobra:
    def __init__(self):
        self.corpo = [(LARGURA_GRID // 2, ALTURA_GRID // 2)]
        self.direcao = (1, 0)

    def atualizar(self):
        x_cabeca, y_cabeca = self.corpo[0]
        nova_cabeca = (x_cabeca + self.direcao[0], y_cabeca + self.direcao[1])
        self.corpo.insert(0, nova_cabeca)
        self.corpo.pop()

    def crescer(self):
        self.corpo.append(self.corpo[-1])

    def desenhar(self, tela):
        for segmento in self.corpo:
            x, y = segmento[0] * TAMANHO_GRID + TAMANHO_GRID // 2, segmento[1] * TAMANHO_GRID + TAMANHO_GRID // 2
            pygame.draw.rect(tela, VERDE, pygame.Rect(x - TAMANHO_GRID // 2, y - TAMANHO_GRID // 2, TAMANHO_GRID, TAMANHO_GRID))

    def tratar_entrada(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and self.direcao != (0, 1):
                self.direcao = (0, -1)
            elif evento.key == pygame.K_DOWN and self.direcao != (0, -1):
                self.direcao = (0, 1)
            elif evento.key == pygame.K_LEFT and self.direcao != (1, 0):
                self.direcao = (-1, 0)
            elif evento.key == pygame.K_RIGHT and self.direcao != (-1, 0):
                self.direcao = (1, 0)

    def verificar_colisao(self):
        x_cabeca, y_cabeca = self.corpo[0]

        # Verifica colisão com as paredes
        if x_cabeca < 0 or x_cabeca >= LARGURA_GRID or y_cabeca < 0 or y_cabeca >= ALTURA_GRID:
            return True

        # Verifica colisão consigo mesma
        if (x_cabeca, y_cabeca) in self.corpo[1:]:
            return True

        return False

    def comer(self, comida):
        if self.corpo[0] == comida.posicao:
            self.crescer()
            return True
        return False

# Classe Comida
class Comida:
    def __init__(self, cobra):
        self.posicao = (0, 0)
        self.randomizar(cobra)

    def randomizar(self, cobra):
        while True:
            x = random.randint(0, LARGURA_GRID - 1)
            y = random.randint(0, ALTURA_GRID - 1)
            if (x, y) not in cobra.corpo:
                self.posicao = (x, y)
                break

    def desenhar(self, tela):
        x, y = self.posicao
        x, y = x * TAMANHO_GRID + TAMANHO_GRID // 2, y * TAMANHO_GRID + TAMANHO_GRID // 2
        pygame.draw.rect(tela, VERMELHO, pygame.Rect(x - TAMANHO_GRID // 2, y - TAMANHO_GRID // 2, TAMANHO_GRID, TAMANHO_GRID))


def exibir_mensagem(tela, texto, tamanho_fonte, cor, posicao):
    fonte = pygame.font.Font(None, tamanho_fonte)
    superficie_texto = fonte.render(texto, True, cor)
    retangulo_texto = superficie_texto.get_rect()
    retangulo_texto.center = posicao
    tela.blit(superficie_texto, retangulo_texto)


def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Jogo da Cobra")
    relogio = pygame.time.Clock()
    cobra = Cobra()
    comida = Comida(cobra)

    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            cobra.tratar_entrada(evento)

        cobra.atualizar()

        if cobra.verificar_colisao():
            fim_de_jogo = True
        else:
            if cobra.comer(comida):
                comida.randomizar(cobra)

            tela.fill((36, 36, 36))
            cobra.desenhar(tela)
            comida.desenhar(tela)
            pygame.display.update()
            relogio.tick(VELOCIDADE)

    exibir_mensagem(tela, "Fim de Jogo", 48, VERMELHO, (LARGURA_TELA // 2, ALTURA_TELA // 2))
    exibir_mensagem(tela, "Pressione qualquer tecla para reiniciar", 24, VERMELHO, (LARGURA_TELA // 2, ALTURA_TELA // 2 + 40))
    pygame.display.update()

    while True:
        evento = pygame.event.wait()
        if evento.type == pygame.KEYDOWN:
            break
        elif evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main()

if __name__ == "__main__":
    main()
