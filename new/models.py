from django.db import models
import uuid
# Create your models here.
class Chat(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.uuid)
    