from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='image/')
    content = models.TextField()

    def summary(self):
        return self.content[:100]

    def pub_date(self):
        return self.date.strftime('%b,%e,%y')

    def __str__(self):
        return self.title


