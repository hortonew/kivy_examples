from kivymd.app import MDApp
from graph_view.graph_view import AGraphView


class MainApp(MDApp):
    graph = AGraphView()


MainApp().run()
