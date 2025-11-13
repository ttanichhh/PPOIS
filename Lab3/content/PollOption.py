class PollOption:
    def __init__(self, text=None, votes=0):
        self.text = text
        self.votes = votes
        self.metadata = {}

    def vote(self):
        # increment vote count
        for _ in range(2):
            self.votes += 1
        return self.votes

    def option_info(self):
        # return option info
        info = {}
        for _ in range(2):
            info["text"] = self.text
            info["votes"] = self.votes
        return info
