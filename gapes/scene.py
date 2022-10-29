class Scene:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.on_added_to_scene()

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
