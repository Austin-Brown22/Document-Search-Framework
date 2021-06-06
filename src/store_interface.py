
class store_interface:

    def __init__(self):
        self.entries = []
        self.meta_data = {}

    def store(self, data):
        self.entries += data

    def get_entries(self):
        return self.entries