
class search_interface():

    def search(self, term):
        for i in self.store():
            if i == term:
                return i
        return -1