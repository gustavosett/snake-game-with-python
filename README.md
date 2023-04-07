## Snake Game - Projeto Universitário

![snake](https://cdn.discordapp.com/attachments/1069432148186112081/1093831987296473128/snake_game.jpg)

### Descrição
Este projeto é uma implementação simples do clássico jogo da Cobra, desenvolvido como trabalho universitário. O jogo foi construído utilizando a biblioteca Pygame em Python e possui uma interface gráfica 2D simples e funcional.

### Funcionalidades
1. A cobra se move na tela em uma grade fixa, podendo mudar sua direção com as teclas de seta.
1. A cobra cresce de tamanho sempre que come a comida, que aparece aleatoriamente na tela.
1. A cobra morre caso colida consigo mesma ou com as bordas da tela.
1. Ao final do jogo, é exibida uma mensagem de "Fim de Jogo" e uma opção para reiniciar o jogo pressionando qualquer tecla.


## Estrutura do Código
### O código está organizado em duas classes principais:

1. Cobra: responsável pela lógica da cobra, como movimentação, crescimento, detecção de colisões e desenho na tela.
1. Comida: responsável pela lógica da comida, como posicionamento aleatório e desenho na tela.
1. Além disso, o arquivo main() é responsável por executar o loop principal do jogo e gerenciar a interação entre os objetos Cobra e Comida.

## Como executar
Certifique-se de ter Python 3.x e a biblioteca Pygame instalados. Em seguida, basta executar o arquivo principal:
```bash
python snake_game.py
```

## Considerações Finais
> Este projeto foi desenvolvido como parte de um trabalho universitário e, portanto, possui um escopo limitado e uma implementação simplificada. No entanto, ele pode ser utilizado como base para estudos e melhorias, servindo como ponto de partida para a criação de jogos mais complexos ou aprofundamento no uso da biblioteca Pygame.
