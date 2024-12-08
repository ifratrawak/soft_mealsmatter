from django import forms

from stores.models import Store, Product, Order


# admin superuser createform
class ShopCreationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'owner',
            'store_img'
        ]




class ShopUpdationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'owner',
            'store_img'
        ]

#user createform
class ShopCreationFormUser(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'store_img'
        ]

class ShopUpdationFormUser(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'store_img'
        ]

class ProductCreationFormUser(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'quantity',
            'description',
            'image'
        ]

class ProductCreationFormAdmin(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'store',
            'name',
            'category',
            'quantity',
            'description',
            'image'
        ]
class ProductUpdationFormUser(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'quantity',
            'description',
            'image'
        ]
class OrderCreationFormUser(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'product',
            'quantity',
            'date',
            # 'status'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OrderCreationFormUser, self).__init__(*args, **kwargs)
        """what happens here is we get all the stores under a user
         then get the foods under those store in the foods variable
         """
        products = Product.objects.none()
        stores = Store.objects.filter(owner=self.user)
        for i in stores:
            products |= Product.objects.filter(store=i)

        self.fields['product'].queryset = products
        self.fields['product'].label_from_instance = lambda obj: "%s" % obj.name


