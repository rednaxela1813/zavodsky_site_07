from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




class Phone(models.Model):
    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CHOICE = (('home', 'Home'), ('work', 'Work'), ('mobile', 'Mobile'))
   
    #name = models.CharField(max_length=255)
    number = PhoneNumberField(blank=True)
    type = models.CharField(max_length=255, choices=CHOICE, default='mobile')

    def __str__(self):
        return f'{self.number} ({self.type})'

    class Meta:
        verbose_name_plural = 'Phones'
        ordering = ['number']


# class Email
class Email(models.Model):
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.email
    
# class Adress
class Address(models.Model):
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.street
    


# class Photo(models.Model):
class Photo(models.Model):
    image = models.ImageField(upload_to="photos/")
    description = models.TextField(blank=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")


    def __str__(self):
        return self.image
    

# class Property
class Property(models.Model):
  #  uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True)
    object_id = models.IntegerField(blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    
    

# class Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def get_photos(self):
        content_type = ContentType.objects.get_for_model(self)
        return Photo.objects.filter(content_type=content_type, object_id=self.id)


    def __str__(self):
        return self.name
    

# class Product
class Product(models.Model):
   # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name='products')
   # property = models.ManyToManyField('Property', blank=True, related_name='products')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, related_name='product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos_product = models.ManyToManyField(Photo, blank=True, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, related_name='products')
    email = models.ForeignKey('Email', on_delete=models.CASCADE, blank=True, related_name='products')

    def get_photos(self):
        content_type = ContentType.objects.get_for_model(self)
        return Photo.objects.filter(content_type=content_type, object_id=self.id)
    
    def get_properties(self):
        content_type = ContentType.objects.get_for_model(self)
        return Property.objects.filter(content_type=content_type, object_id=self.id)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
