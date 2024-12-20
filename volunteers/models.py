from django.contrib.auth.models import User
from django.db import models

from stores.models import Store, Order

# Create your models here.

locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Mohammadpur', 'Mohammadpur'),
             ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'), ('Mirpur', 'Mirpur'), ('Shamoli', 'Shamoli'),
            ('Adabor', 'Adabor'), ('Green Road', 'Green Road'),
             ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh'),
             ]
sex = [('Male','Male'), ('Female', 'Female')]


class Volunteer(models.Model):
    volunteer=models.OneToOneField(User,default=None,on_delete=models.CASCADE)
    store=models.ForeignKey(Store,default=None,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.volunteer.username
class VolunteerRequest(models.Model):
    requester = models.ForeignKey(Volunteer, default=None, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.requester.volunteer.username + ' -> ' + self.order.product.name
