from django.db import models
import os
from django.db import models
from django.conf import settings

# Create your models here.
class gamedata(models.Model):
    id=models.IntegerField(primary_key=True)
    data=models.ImageField(upload_to='gamedata/')

    def delete(self, *args, **kwargs):
        if self.data:
            file_path = os.path.join(settings.MEDIA_ROOT, str(self.data))
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)
