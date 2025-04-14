# main.py (com variáveis renomeadas)

def verificar_caminho_hamiltoniano(grafo, trilha, visitados):
    if len(trilha) == len(grafo):
        return True

    atual = trilha[-1]

    for vizinho in grafo[atual]:
        if not visitados[vizinho]:
            visitados[vizinho] = True
            trilha.append(vizinho)

            if verificar_caminho_hamiltoniano(grafo, trilha, visitados):
                return True

            trilha.pop()
            visitados[vizinho] = False

    return False

def buscar_caminho_hamiltoniano(grafo):
    quantidade_vertices = len(grafo)
    for inicio in grafo:
        marcados = {no: False for no in grafo}
        marcados[inicio] = True
        percurso = [inicio]

        if verificar_caminho_hamiltoniano(grafo, percurso, marcados):
            return percurso
    return None

if __name__ == "__main__":
    grafo_exemplo = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    resultado = buscar_caminho_hamiltoniano(grafo_exemplo)
    if resultado:
        print("Caminho Hamiltoniano encontrado:", resultado)
    else:
        print("Não existe Caminho Hamiltoniano.")
