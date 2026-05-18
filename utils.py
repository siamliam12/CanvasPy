import pygame

class TimeManager:
    def __init__(self,fps_cap=60):
        self.clock = pygame.time.Clock()
        self.fps_cap = fps_cap
        self.dt = 0.0

    def tick(self):
        milliseconds = self.clock.tick(self.fps_cap)
        self.dt = milliseconds / 1000.0
        return self.dt
    
class InputManager:
    """Caches keyboard states so the engine knows what is being held or tapped."""
    def __init__(self):
        self.current_keys = []
        self.previous_keys = []

    def update(self):
        # Store the keys from the last frame before grabbing new ones
        self.previous_keys = self.current_keys
        # Get a snapshot of all keys currently pressed down
        self.current_keys = pygame.key.get_pressed()

    def is_key_held(self, key):
        """Returns True as long as the key is being held down."""
        return self.current_keys[key]

    def is_key_just_pressed(self, key):
        """Returns True ONLY on the single frame the key was pressed."""
        return self.current_keys[key] and not self.previous_keys[key]