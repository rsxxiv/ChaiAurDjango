from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):

    # Creating an Enum to store chai-types
    CHAI_TYPE_CHOICE =  [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('EL', 'ELAICHI'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
    ]

       

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = MoneyField(decimal_places=2, default=0, default_currency='INR', max_digits=11)

    def __str__(self):
        return self.name
    


# Class One to Many

class ChaiReview(models.Model):
    RATINGS = [
        (1 , 'Chee'),
        (2 , 'Ehhh'),
        (3 , 'Hmmm'),
        (4 , 'Wahh'),
        (5 , 'Mast'),
    ]

    # In ChaiReview a certain USER can make reviews on Many CHAIS

    # Getting the Foreign Key of ChaiVariety   
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    # Getting the Foreign Key of User   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField(choices=RATINGS)
    comment = models.TextField
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'



# Many To Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='store')

    def __str__(self):
        return self.name



# One To One

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=10)
    issue_date = models.DateTimeField(default=timezone.now, editable=False)
    validity = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'
    