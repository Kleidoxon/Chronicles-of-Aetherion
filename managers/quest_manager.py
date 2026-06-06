# managers/quest_manager.py

from quests.procedural_quests import QuestGenerator


class QuestManager:

    def __init__(self):

        self.generator = QuestGenerator()

        self.active_quests = []

    def generate_quest(self):

        quest = self.generator.generate_quest()

        self.active_quests.append(
            quest
        )

        return quest

    def complete_quest(
        self,
        quest
    ):

        if quest in self.active_quests:

            self.active_quests.remove(
                quest
            )