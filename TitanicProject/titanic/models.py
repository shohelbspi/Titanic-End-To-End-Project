from django.db import models

# Create your models here.


from django.db import models
from joblib import load

class MLModel(models.Model):
    model = models.FileField(upload_to='models/')

    def predict(self, data):
        loaded_model = load(self.model.path)
        return loaded_model.predict(data)
