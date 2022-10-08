class Entity:
    id = 0

    def __init__(self):
        self.id = Entity.id
        Entity.id += 1
        self.components = {}

    def add_component(self, component):
        self.components[component.key] = component
