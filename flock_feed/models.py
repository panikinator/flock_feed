from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def like_count(self):
        return self.like_set.count()
    

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self) -> str:
        return f"{self.user.username} likes {self.post.title}"
