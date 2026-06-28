import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph =nx.DiGraph()
        self._idMap={}

    def get_store(self):
        lista=list(DAO.getAllStores())
        return lista

    def build_graph(self,c,b):
        self._graph.clear()
        self._idMap.clear()

        nodi=DAO.get_nodi(c)
        self._graph.add_nodes_from(nodi)
        for n in nodi:
            self._idMap[n.order_id]=n
        edges=list(DAO.get_archi(int(c),int(b)))

        for a in edges:
            ord1=self._idMap[a[0]]
            ord2 = self._idMap[a[1]]
            k=a[2]
            peso=(ord1.quantity+ord2.quantity)/int(k)
            self._graph.add_edge(ord1,ord2, weight=peso)

    def get_stats(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def stampatop5(self):
        archi = self._graph.edges(data=True)
        lista = sorted(archi, key=lambda x: x[2]["weight"], reverse=True)
        s=[]
        for a in range(5):
            s.append(lista[a])
        return s


        """Trova il cammino più lungo che parte dal nodo start usando una visita in profondità
            iterativa. Lo stack contiene coppie formate dal nodo corrente e dal cammino seguito
            per raggiungerlo. A ogni passo viene estratto un nodo, si controlla se il cammino
            corrente è il più lungo trovato finora e poi si aggiungono allo stack tutti i suoi
            successori non ancora presenti nel cammino. In questo modo si esplorano tutti i
            cammini possibili a partire dal nodo scelto, senza usare ricorsione.
            """

    def getPercorsoMassimo(self, start):
        start=self._idMap[int(start)]
        stack = [(start, [start])]
        best_path = [start]
        while stack:
            current, path = stack.pop()
            if len(path) > len(best_path):
                best_path = path
            for neighbor in self._graph.successors(current):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
        return best_path

