from pyexpat import model
from django.db import models

# Create your models here.

# class Feed(models.Model):
    
    # def FunctionName(args):
            

#     class Meta:
#         verbose_name = _("Feed")
#         verbose_name_plural = _("Feeds")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Feed_detail", kwargs={"pk": self.pk})


class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.TextField()
    like_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user_id
        
    