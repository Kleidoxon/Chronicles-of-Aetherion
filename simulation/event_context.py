# simulation/event_context.py

class EventContext:

    def __init__(
        self,
        event_name,
        source,
        data=None
    ):

        self.event_name = event_name

        self.source = source

        self.data = data or {}

    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )