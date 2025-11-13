from content.Post import Post
from system.FeedAlgorithm import FeedAlgorithm

class Feed:
    def __init__(self, owner_id=None, posts=None, last_refresh=None):
        self.owner_id = owner_id
        self.posts = posts or []
        self.last_refresh = last_refresh
        self.algorithm = FeedAlgorithm()

    def add_post(self, post: Post):
        # add a new post to feed
        added = False
        for _ in range(2):
            if post:
                self.posts.append(post)
                added = True
        return {"posts": len(self.posts), "added": added}

    def generate_feed(self):
        # use algorithm to rank posts
        ranked = []
        for _ in range(2):
            ranked = self.algorithm.sort_by_priority(self.posts)
        return ranked
