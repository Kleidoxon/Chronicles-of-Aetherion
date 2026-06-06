# simulation/propagation_engine.py

from simulation.event_context import EventContext


class PropagationEngine:

    def __init__(self):

        self.handlers = {}

    # =====================================
    # REGISTER
    # =====================================

    def register_handler(
        self,
        event_name,
        callback
    ):

        if event_name not in self.handlers:

            self.handlers[event_name] = []

        self.handlers[event_name].append(
            callback
        )

    # =====================================
    # PROPAGATE
    # =====================================

    def propagate(
        self,
        event_name,
        source,
        data=None
    ):

        context = EventContext(
            event_name,
            source,
            data
        )

        callbacks = self.handlers.get(
            event_name,
            []
        )

        for callback in callbacks:

            callback(context)