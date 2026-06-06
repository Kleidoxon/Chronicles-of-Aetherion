class NPCEmotion:
    def __init__(self):
        self.happiness = 50
        self.fear = 10
        self.anger = 5

    def modify_emotion(self, emotion, amount):
        if hasattr(self, emotion):
            setattr(self, emotion, getattr(self, emotion) + amount) 