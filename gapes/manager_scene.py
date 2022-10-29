class SceneManager:
    def __init__(self):
        self.stored_scenes: dict = {}
        self.scenes: list = []

    def draw(self):
        if not self.is_empty():
            self.get_scene().draw()

    def update(self):
        if not self.is_empty():
            self.get_scene().update()

    def push(self, scene):
        self.scenes.append(scene)

    def is_empty(self):
        return not bool(self.scenes)

    def get_scene(self):
        """from top of the list"""
        if self.is_empty():
            return None
        return self.scenes[-1]
