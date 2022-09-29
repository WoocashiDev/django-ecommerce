import email
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile
from shop.models import ShoppingCart

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = UserProfile.objects.create(
            user=user,
            username=user.username,
        )
        profile.email = user.email
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.save()

        shopping_cart = ShoppingCart.objects.create(
            user = profile
        )
        shopping_cart.save()

post_save.connect(createProfile, sender=User)

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=UserProfile)