from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=240, unique=True)
    password = models.CharField(max_length=240)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PerevalAdded(models.Model):

    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        ("new", "новый"),
        ("pending", "модератор взял в работу"),
        ("accepted", "модерация прошла успешно"),
        ("rejected", "модерация прошла, информация не принята"),
    ]

    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    beautyTitle = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    other_titles = models.CharField(max_length=250)
    connect = models.TextField(max_length=500)
    add_time = models.DateTimeField(auto_now_add=True)
    winter_level = models.CharField(max_length=240)
    spring_level = models.CharField(max_length=240)
    summer_level = models.CharField(max_length=240)
    autumn_level = models.CharField(max_length=240)
    coord_id = models.ForeignKey('Coords', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='new', max_length=8)
    images = models.ManyToManyField('PerevalImages')

    def __str__(self):
        return f'{self.beautyTitle}'


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.latitude} {self.longitude} {self.height}"


class PerevalImages(models.Model):
    image = models.ImageField(upload_to='media/')
    image_name = models.CharField(max_length=240)

    def __str__(self):
        return f'{self.image_name}'


class PerevalAreas(models.Model):
    id_parent = models.IntegerField()
    title = models.TextField()

    def __str__(self):
        return f"{self.title}"





