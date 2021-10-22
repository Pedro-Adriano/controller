from django.db import models
import uuid


class UserModel(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(max_length=11)
    password = models.CharField(max_length=16)
    creation_date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=45)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = "user"
