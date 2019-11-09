
from django.db import models
import uuid
# Create your models here.
class VideoModel(models.Model):
    Thumbnail=models.FileField(upload_to='videos/', null=True, verbose_name="")
    Name     = models.CharField(max_length = 264,null=True)
    VideoId = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,null=False)
    Created_on = models.DateTimeField(auto_now_add=True,null=True)
    Duration  = models.IntegerField(null=True)
    Status = models.CharField(max_length = 264,null=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Created_on' , 'Duration' ]

class VideoMeta(models.Model):
    Video = models.ForeignKey(VideoModel , on_delete=models.CASCADE,)
    Name     = models.CharField(max_length = 264,null=True)
    Description = models.TextField(blank=True)
    Tags = models.CharField(max_length = 264,blank=True)
    Categories = models.CharField(max_length = 264,blank=True)
    ReferenceID = models.CharField(max_length = 264,blank=True)
    def __str__(self):
        return self.Name
