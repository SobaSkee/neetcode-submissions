from collections import deque
from typing import List


class User:
    def __init__(self, uid):
        self.tweetsFeed = deque()
        self.following = set()

    def updateFeed(self, uid, tweetId, time):
        self.tweetsFeed.append([tweetId, uid, time])

    def getFeed(self, uid):
        return self.tweetsFeed


class Twitter:
    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.users[userId].updateFeed(userId, tweetId, self.time)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        user = self.users[userId]
        feed = list(user.getFeed(userId))

        for followeeId in user.following:
            feed.extend(self.users[followeeId].getFeed(followeeId))

        # most recent tweets first, regardless of tweet ID
        feed.sort(key=lambda tweet: tweet[2], reverse=True)

        return [tid for tid, _, _ in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        # Users can follow before either has posted anything
        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return

        self.users[followerId].following.discard(followeeId)