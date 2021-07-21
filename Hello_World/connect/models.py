from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Room(models.Model):
    group_name = models.TextField(unique=True)
    group_admin = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
class Message(models.Model):
    group = models.ForeignKey(
        Room,
        related_name='messages_group',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='author_messages',
        on_delete=models.CASCADE,
    )
    content = models.TextField(default="")
    timeStamp = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.author.username

    def last_10_messages(groupName, group_admin):
        return Message.objects.order_by('-timeStamp').filter(
            group__group_name=groupName,
            group__group_admin__username=group_admin)[:10:-1]
