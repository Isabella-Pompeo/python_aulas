import heapq
from collections import Counter

# --- 1. Criar o arquivo original ---
texto_original = "ESTE E UM EXEMPLO" # Texto curto para facilitar a visualização
with open("arquivo1.txt", "w") as f:
    f.write(texto_original)

# --- 2. Criar arquivo com ASCII (8 bits) ---
with open("ascii_map.txt", "w") as f:
    for char in texto_original:
        binario_ascii = format(ord(char), '08b')
        f.write(f"{char}: {binario_ascii}\n")

# --- 3. Implementação da Tabela de Huffman ---
class No:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.esquerda = None
        self.direita = None
    def __lt__(self, outro):
        return self.freq < outro.freq

def criar_tabela_huffman(texto):
    frequencias = Counter(texto)
    heap = [No(char, freq) for char, freq in frequencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)
        pai = No(None, no1.freq + no2.freq)
        pai.esquerda = no1
        pai.direita = no2
        heapq.heappush(heap, pai)
    
    raiz = heap[0]
    codigos = {}
    def gerar_codigos(no, codigo_atual):
        if no:
            if no.char: codigos[no.char] = codigo_atual
            gerar_codigos(no.esquerda, codigo_atual + "0")
            gerar_codigos(no.direita, codigo_atual + "1")
    gerar_codigos(raiz, "")
    return codigos

tabela_huffman = criar_tabela_huffman(texto_original)

with open("tabela_huffman.txt", "w") as f:
    for char, codigo in tabela_huffman.items():
        f.write(f"'{char}': {codigo}\n")

# --- 4. Criar arquivo comprimido ---
texto_comprimido = "".join([tabela_huffman[char] for char in texto_original])
with open("comprimido.txt", "w") as f:
    f.write(texto_comprimido)

# ======================================================
# --- 5. EXIBIÇÃO DOS RESULTADOS NO TERMINAL ---
# ======================================================
print("\n" + "="*40)
print("RELATÓRIO DE COMPRESSÃO DE HUFFMAN")
print("="*40)

print("\n[1] CONTEÚDO ORIGINAL (arquivo1.txt):")
print(f"-> \"{texto_original}\"")

print("\n[2] MAPEAMENTO ASCII (ascii_map.txt - Primeiros 5 itens):")
with open("ascii_map.txt", "r") as f:
    linhas = f.readlines()
    for linha in linhas[:5]: # Mostra apenas as primeiras 5 letras para não poluir
        print(f"   {linha.strip()}")

print("\n[3] TABELA DE HUFFMAN (tabela_huffman.txt):")
for char, cod in tabela_huffman.items():
    print(f"   Letra '{char}' -> Código: {cod}")

print("\n[4] RESULTADO COMPRIMIDO (comprimido.txt):")
print(f"   {texto_comprimido}")

print("\n" + "-"*40)
tamanho_original = len(texto_original) * 8
tamanho_huffman = len(texto_comprimido)
print(f"TAMANHO ORIGINAL: {tamanho_original} bits")
print(f"TAMANHO COMPRIMIDO: {tamanho_huffman} bits")
print(f"ECONOMIA DE: {100 - (tamanho_huffman/tamanho_original*100):.2f}%")
print("-"*40)