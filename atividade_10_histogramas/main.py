import pygame
import sys
import random


lista_1 = []
for i in range(50):
    numero = random.randint(7, 92)
    lista_1.append(numero)
num_cat_1 = 5 


nums = [
    100, 120, 130, 120, 150, 100, 160, 200, 190, 110, 115, 125, 135, 170, 130
]
num_cat = 4
num_min = min(nums)
num_max = max(nums)
tam_cat = (num_max - num_min) / num_cat
lista_total = [0] * num_cat


print("Digite números inteiros separados por espaço (ex: 5 12 18 25 33 40 15 22):")
user_input = input("::").strip()

lista_3 = []
if user_input:
    for parte in user_input.split():
        try:
            lista_3.append(int(parte))
        except ValueError:
            pass

# Caso o usuário aperte Enter sem digitar nada ou digite inválidos, fornece uma lista padrão para teste
if len(lista_3) < 2:
    print("Poucos valores inseridos. Usando valores complementares para exibição.")
    lista_3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

num_cat_3 = 6  # Quantidade de categorias diferente

# ==============================================================================
# 2. FUNÇÃO ORIGINAL DISPONIBILIZADA PELO PROFESSOR (COMENTADA) (50XP)
# ==============================================================================
def contabiliza_totais(nums, num_cat):
    """
    Função base disponibilizada pelo professor totalmente comentada.
    Recebe uma lista de números e o número de categorias/faixas desejadas,
    calcula os intervalos e retorna a lista com a contagem de elementos por faixa,
    além das tuplas com os limites (inferior, superior) de cada faixa.
    """
    # Inicializa a lista de contadores com zeros para cada categoria
    lista_total = [0] * num_cat
    
    # Encontra o menor e o maior valor dentro da lista recebida
    num_min = min(nums)
    num_max = max(nums)
    
    # Se todos os números forem iguais, define um delta para evitar divisão por zero
    if num_max == num_min:
        num_max += 1

    # Calcula o tamanho (amplitude) de cada categoria/faixa
    tam_cat = (num_max - num_min) / num_cat
    
    # Lista auxiliar para armazenar os limites inferior e superior de cada categoria
    faixas = []
    for i_cat in range(num_cat):
        lim_inf = num_min + i_cat * tam_cat
        lim_sup = lim_inf + tam_cat
        faixas.append((lim_inf, lim_sup))

    # Para cada número presente na lista recebida
    for i in range(len(nums)):
        # Caso especial: se o número for exatamente igual ao máximo, ele entra na última categoria
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        # Para cada categoria disponível, checa em qual delas o número se encaixa
        for i_cat in range(num_cat):
            lim_inf = faixas[i_cat][0]
            lim_sup = faixas[i_cat][1]

            # Checa se o número está dentro do intervalo [lim_inf, lim_sup)
            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break  # Encontrou a categoria, vai para o próximo número

    return lista_total, faixas

# Processa os totais e faixas para os histogramas 1 e 3
totais_h1, faixas_h1 = contabiliza_totais(lista_1, num_cat_1)
totais_h3, faixas_h3 = contabiliza_totais(lista_3, num_cat_3)

# Monta faixas para o histograma 2 com base nos limites estáticos
tam_cat_h2 = (max_h2 - min_h2) / num_cat_2
faixas_h2 = [(min_h2 + i * tam_cat_h2, min_h2 + (i + 1) * tam_cat_h2) for i in range(num_cat_2)]


# ==============================================================================
# 3. GERAÇÃO DE CORES GENÉRICAS / ALEATÓRIAS POR FAIXA (50XP)
# ==============================================================================
def gerar_cores_aleatorias(qtd):
    """Gera uma lista de cores RGB aleatórias e bem visíveis."""
    cores = []
    for _ in range(qtd):
        r = random.randint(60, 240)
        g = random.randint(60, 240)
        b = random.randint(60, 240)
        cores.append((r, g, b))
    return cores

cores_h1 = gerar_cores_aleatorias(num_cat_1)
cores_h2 = gerar_cores_aleatorias(num_cat_2)
cores_h3 = gerar_cores_aleatorias(num_cat_3)


# ==============================================================================
# 4. DESENHO DOS HISTOGRAMAS COM EIXOS X, Y E MARCAÇÕES (100XP)
# ==============================================================================
def desenhar_histograma(screen, font, titulo, totais, faixas, cores, pos_x, pos_y, largura, altura):
    """
    Desenha um histograma completo com:
    - Eixos X e Y visíveis com marcações (ticks) numéricas
    - Barras coloridas individualmente por categoria
    - Rótulos dos eixos e título
    """
    # Desenha fundo do painel do histograma
    pygame.draw.rect(screen, (245, 247, 250), (pos_x, pos_y, largura, altura), border_radius=8)
    pygame.draw.rect(screen, (200, 205, 215), (pos_x, pos_y, largura, altura), width=2, border_radius=8)

    # Título do Histograma
    txt_titulo = font.render(titulo, True, (20, 20, 20))
    screen.blit(txt_titulo, (pos_x + 15, pos_y + 12))

    # Área interna do gráfico reservada para barras e eixos
    margem_esq = 55
    margem_dir = 20
    margem_cima = 45
    margem_baixo = 45

    grafico_x = pos_x + margem_esq
    grafico_y = pos_y + margem_cima
    grafico_larg = largura - margem_esq - margem_dir
    grafico_alt = altura - margem_cima - margem_baixo

    max_valor = max(totais) if (totais and max(totais) > 0) else 1

    # --- EIXO Y e Marcações ---
    # Linha vertical do eixo Y
    pygame.draw.line(screen, (50, 50, 50), (grafico_x, grafico_y), (grafico_x, grafico_y + grafico_alt), 2)
    
    # 4 divisões no eixo Y para marcações
    num_div_y = 4
    for d in range(num_div_y + 1):
        val_y = int(round((max_valor / num_div_y) * d))
        tick_y = (grafico_y + grafico_alt) - (d / num_div_y) * grafico_alt

        # Tracinho (tick) no eixo Y
        pygame.draw.line(screen, (50, 50, 50), (grafico_x - 5, tick_y), (grafico_x, tick_y), 2)
        # Linha de grade sutil
        pygame.draw.line(screen, (225, 225, 230), (grafico_x, tick_y), (grafico_x + grafico_larg, tick_y), 1)

        # Texto do valor no eixo Y
        txt_val_y = font.render(str(val_y), True, (60, 60, 60))
        screen.blit(txt_val_y, (grafico_x - txt_val_y.get_width() - 8, tick_y - txt_val_y.get_height() // 2))

    # --- EIXO X e Marcações ---
    # Linha horizontal do eixo X
    pygame.draw.line(screen, (50, 50, 50), (grafico_x, grafico_y + grafico_alt), (grafico_x + grafico_larg, grafico_y + grafico_alt), 2)

    qtd_faixas = len(totais)
    larg_coluna = grafico_larg / qtd_faixas

    for i in range(qtd_faixas):
        contagem = totais[i]
        cor = cores[i % len(cores)]

        # Altura proporcional da barra
        h_barra = (contagem / max_valor) * grafico_alt if max_valor > 0 else 0
        x_barra = grafico_x + i * larg_coluna + 4
        larg_barra = max(1, larg_coluna - 8)
        y_barra = (grafico_y + grafico_alt) - h_barra

        # Desenha a barra da categoria
        pygame.draw.rect(screen, cor, (x_barra, y_barra, larg_barra, h_barra))
        pygame.draw.rect(screen, (40, 40, 40), (x_barra, y_barra, larg_barra, h_barra), width=1)

        # Valor numérico em cima da barra
        if contagem > 0:
            txt_contagem = font.render(str(contagem), True, (30, 30, 30))
            screen.blit(txt_contagem, (x_barra + (larg_barra - txt_contagem.get_width()) // 2, y_barra - 16))

        # Marcação (tick) no eixo X
        tick_x = grafico_x + (i + 0.5) * larg_coluna
        pygame.draw.line(screen, (50, 50, 50), (tick_x, grafico_y + grafico_alt), (tick_x, grafico_y + grafico_alt + 5), 2)

        # Rótulo da faixa no eixo X (ex: 10-25 ou F1)
        lim_inf, lim_sup = faixas[i]
        rotulo_faixa = f"{int(lim_inf)}-{int(lim_sup)}"
        txt_faixa = font.render(rotulo_faixa, True, (60, 60, 60))
        screen.blit(txt_faixa, (tick_x - txt_faixa.get_width() // 2, grafico_y + grafico_alt + 8))


# ==============================================================================
# 5. LOOP PRINCIPAL DO PYGAME
# ==============================================================================
def main():
    pygame.init()
    pygame.font.init()

    # Dimensões da tela para comportar os 3 histogramas lado a lado ou organizados
    LARGURA_TELA = 1150
    ALTURA_TELA = 420
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Atividade 10 - Três Histogramas no PyGame")
    
    fonte = pygame.font.SysFont("Arial", 13)
    fonte_titulo = pygame.font.SysFont("Arial", 14, bold=True)
    clock = pygame.time.Clock()

    # Configurações de layout dos 3 cards de histogramas
    w_card = 350
    h_card = 360
    y_pos = 30
    espaco = 25

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((235, 238, 242))

        # 1. Histograma 1 - Lista Aleatória (>= 50 números, 5 faixas)
        desenhar_histograma(
            screen, fonte, "1. Aleatória (60 nums, 5 faixas)",
            totais_h1, faixas_h1, cores_h1,
            pos_x=20, pos_y=y_pos, largura=w_card, altura=h_card
        )

        # 2. Histograma 2 - Lista Estática com Faixas Aleatórias (Soma <= 15, 4 faixas)
        desenhar_histograma(
            screen, fonte, f"2. Estática/Aleat. (Soma={sum(totais_h2)}<=15, 4 faixas)",
            totais_h2, faixas_h2, cores_h2,
            pos_x=20 + w_card + espaco, pos_y=y_pos, largura=w_card, altura=h_card
        )

        # 3. Histograma 3 - Lista do Usuário (6 faixas)
        desenhar_histograma(
            screen, fonte, f"3. Input Usuário ({len(lista_3)} nums, 6 faixas)",
            totais_h3, faixas_h3, cores_h3,
            pos_x=20 + 2 * (w_card + espaco), pos_y=y_pos, largura=w_card, altura=h_card
        )

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
