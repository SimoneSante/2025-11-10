from model.model import Model


def main():
    model = Model()

    c =1
    b=5

    print(f"Costruisco il grafo con c = {c,b}...")

    model.build_graph(c,b)

    n_nodi, n_archi = model.get_stats()

    print(f" il grafo creato contiene {n_nodi} nodes e {n_archi} edges")

    lista=model.stampatop5()
    for c in lista:
        print(f"{c[0]}--->{c[1]}={c[2]}")



if __name__ == "__main__":
    main()