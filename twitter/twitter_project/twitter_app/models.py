from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.user_name


class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    post = models.DateTimeField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    update_post = models.DateTimeField()
    delete_post = models.BooleanField()

    def __str__(self):
        return self.user_name + " " + self.tweet
