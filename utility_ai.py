class UtilityAI:
    def choose_action(self, npc):
        scores = {
            "work": npc.hunger * 0.5 + npc.wealth * 2.5, 
            "eat": npc.hunger * 1.0,    
            "sleep": npc.fatigue * 100,  
            "crime": npc.wealth < 20 and npc.hunger > 50,
            "socialize": npc.loneliness * 1.0,
            
        }

        return max(scores, key=scores.get)