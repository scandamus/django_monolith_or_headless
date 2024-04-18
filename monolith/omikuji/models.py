from django.db import models


class DataOmikuji(models.Model):
    nick_name = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

# dbに何を格納するか
