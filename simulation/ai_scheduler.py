class AIScheduler:
    def __init__(self):
        self.active_npcs = []

    def update_all_npcs(self):
        for npc in self.active_npcs:
            npc.perform_daily_action() 