from django import forms

from stores.models import Product, Store, Order
from volunteers.models import Volunteer, VolunteerRequest


class VolunteerRegForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'volunteer',
            'is_available',
            'store',
        ]


class VolunteerRegFormUser(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'is_available',
            'store'
        ]


class VolunteerUpdFormUser(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'is_available',
            'store'
        ]


class VolunteerRequestFormUser(forms.ModelForm):
    class Meta:
        model = VolunteerRequest
        fields = [
            'requester',
            'order'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VolunteerRequestFormUser, self).__init__(*args, **kwargs)
        """what happens here is we get all the stores under a user
         then get the foods under those store in the foods variable
         """
        products = Product.objects.none()
        orders = Order.objects.none()
        stores = self.user.store

        orders |= Order.objects.filter()
        # for i in stores:
        #     orders |= Order.objects.filter(store=i)

        self.fields['order'].queryset = orders
        self.fields['order'].label_from_instance = lambda obj: "%s" % obj.name
