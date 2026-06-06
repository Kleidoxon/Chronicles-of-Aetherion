# managers/ai_manager.py

from ai.basic_decision_ai import BasicDecisionAI

from neural.neural_world_ai import NeuralWorldAI
from neural.adaptive_behavior import AdaptiveBehavior
from neural.autonomous_storytelling import AutonomousStorytelling

from factions.diplomacy import Diplomacy
from factions.war_system import WarSystem


class AIManager:
   
    def __init__(self):

        self.basic_ai = BasicDecisionAI()

        self.world_ai = NeuralWorldAI()

        self.adaptive_ai = AdaptiveBehavior()

        self.story_ai = AutonomousStorytelling()

        self.diplomacy = Diplomacy()

        self.war_system = WarSystem()

    def process_ai_turn(self):

        return self.basic_ai.choose_action()

    def update_world_ai(self):

        self.world_ai.self_learn()

    def generate_story(self):

        self.story_ai.generate_story_arc()

    def evaluate_war(self):

        self.war_system.evaluate_war()

     
    def update(self):

        print(
            "AI Updated"
        )
