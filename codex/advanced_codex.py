class AdvancedCodex:
    def __init__(self):
        self.entries = []

    def add_entry(self, category, text):
        entry = {
            "category": category,
            "text": text
        }

        self.entries.append(entry)

    def show_entries(self):
        for entry in self.entries:
            print(f"[{entry['category']}] {entry['text']}")