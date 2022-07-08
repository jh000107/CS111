class Phonebook():
    def __init__(self):
        self.entries = {}

    def add_entry(self, name, number):
        self.entries[name] = number

    def contains(self, name):
        if name in self.entries:
            return True
        else:
            return False

    def number_for(self, name):
        if self.contains(name) == True:
            return self.entries[name]
        else:
            return -1
