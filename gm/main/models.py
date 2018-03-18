from django.db import models

# Create your models here.
class Shapefile:
    DISTRICT_CHOICES = (
    ('ama', 'AMA'),
    ('tema', 'Tema'),)

    filename = models.CharField(max_length=50)
    district = models.CharField(max_length=50,choices=DISTRICT_CHOICES)
    shape = models.FileField(upload_to='shapefiles/{}/%Y/%m/%d'.format(district))


    def __str__(self):
        return self.filename
