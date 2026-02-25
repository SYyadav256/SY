from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()   # What the blog/certification is about
    learning = models.TextField()      # What you learned
    time_period = models.CharField(max_length=100, blank=True,null=True)
    certificate_image = models.ImageField(upload_to='blogs/certificates/',blank=True,null=True)


    def __str__(self):
        return self.title
