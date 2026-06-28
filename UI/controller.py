import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def dds(self):
        self._view._ddStore.options.clear()
        self._view._ddStore.value = None

        listaS=self._model.get_store()

        for l in listaS:
            self._view._ddStore.options.append(
                ft.dropdown.Option(
                    key=l.store_id,
                    text=l.store_name,
                )
            )
        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        try:
            store = int(self._view._ddStore.value)
            k = int(self._view._txtIntK.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("selezionare entrambi gli anni"))
        if store is None or k is None :
            self._view.txt_result.controls.append(
                ft.Text("selezionare entrambi i campi", color="red")
            )

        self._model.build_graph(store, k)
        stats = self._model.get_stats()
        self._view.txt_result.controls.append(ft.Text(f"stats:{stats[0]} e {stats[1]}"))
        s=self._model.stampatop5()
        for c in s:
            self._view.txt_result.controls.append(ft.Text(f"{c[0]}--->{c[1]}={c[2]}", color="blue"))
        self.riempidd()
        self._view.update_page()


    def riempidd(self):
        self._view._ddNode.options.clear()
        self._view._ddNode.value = None
        listaS = self._model._graph.nodes()
        for l in listaS:
            self._view._ddNode.options.append(
                ft.dropdown.Option(
                    key=l.order_id,
                    text=l.order_id,
                ))
        self._view._ddNode.disabled=False
        self._view._btnCerca.disabled = False

        self._view.update_page()


    def handleCerca(self, e):
        start=self._view._ddNode.value
        lista=self._model.getPercorsoMassimo(start)
        for l in lista:
            self._view.txt_result.controls.append(ft.Text(f"{l.order_id}", color="blue"))
        self._view.update_page()


    def handleRicorsione(self, e):
        pass
