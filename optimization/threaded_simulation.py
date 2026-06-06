import threading


class ThreadedSimulation:
    def run_background_task(self):
        print("Running background simulation")

    def start(self):
        thread = threading.Thread(target=self.run_background_task)

        thread.start()