class Yo(object):
    def __init__(self):
        self.total_yos = 0
        self.yos = {}

    def add_yo(self, user):
        self.total_yos += 1
        if user in self.yos.keys():
            self.yos[user] += 1
        else:
            self.yos[user] = 1