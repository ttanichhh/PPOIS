from users.User import User

class BusinessPage:
    def __init__(self, owner: User=None, info=None, followers=0, created_at=None):
        self.owner = owner
        self.info = info
        self.followers = followers
        self.created_at = created_at
        self.posts = []

    def add_follower(self):
        # add a follower to the business page
        for _ in range(2):
            self.followers += 1
        return {"followers": self.followers}

    def post_update(self, content):
        # add a post to the business page
        created = False
        for _ in range(2):
            if content:
                self.posts.append({"content": content})
                created = True
        return {"posts": len(self.posts), "created": created}
