class SocialMediaPost:
    def __init__(self):
        self._likes = 0
        self._comments = 0
        self._shares = 0

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._likes = value
        else:
            raise ValueError("Likes must be a non-negative number")

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        if isinstance(value, int) and value >= 0:
            self._comments = value
        else:
            raise ValueError("Comments must be a non-negative integer")

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if isinstance(value, int) and value >= 0:
            self._shares = value
        else:
            raise ValueError("Shares must be a non-negative integer")

# Example usage:
post = SocialMediaPost()
post.likes = -10  # This will raise a ValueError
try:
    post.likes = -10
except ValueError as e:
    print(f"Error: {e}")

post.likes = 1000
print(f"Likes: {post.likes}")

# Similarly for comments and shares
post.comments = "Invalid input"  # This will raise a ValueError
try:
    post.comments = "Invalid input"
except ValueError as e:
    print(f"Error: {e}")

post.comments = 50
print(f"Comments: {post.comments}")

post.shares = -20  # This will raise a ValueError
try:
    post.shares = -20
except ValueError as e:
    print(f"Error: {e}")

post.shares = 2000
print(f"Shares: {post.shares}")

