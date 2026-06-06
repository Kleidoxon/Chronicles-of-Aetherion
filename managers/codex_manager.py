# managers/codex_manager.py

from multiprocessing import context

from codex.dynamic_codex_log import DynamicCodexLog

from codex.living_history import LivingHistory

from codex.infinite_codex import InfiniteCodex

from bestiary.bestiary_system import BestiarySystem


class CodexManager:

    def __init__(self):

        self.codex = DynamicCodexLog()

        self.history = LivingHistory()

        self.infinite_codex = InfiniteCodex()

        self.bestiary = BestiarySystem()

    def record_event(
        self,
        text
    ):

        self.codex.record_event(
            text
        )

    def archive_history(self):

        self.history.archive_history()

    def register_creature(
        self,
        creature_name
    ):

        self.bestiary.register_creature(
            creature_name
        )

    def on_any_event(
        self,
        context
):

        self.record_event(
        f"{context.event_name}"
    )