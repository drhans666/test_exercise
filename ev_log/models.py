from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .scripts import parser


class Category(models.Model):
    name = models.CharField(default='', max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(default='', max_length=500)
    category = models.ManyToManyField(Category, related_name='category')
    person = models.ManyToManyField(Person, related_name='person')

    class Meta:
        ordering = ['-time']

    # original save method
    def base_save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

    # overridden save method
    def save(self, *args, **kwargs):
        # pre-save event
        super(Event, self).save(*args, **kwargs)
        event = Event.objects.filter(text=self.text).latest('time')
        categories = []
        persons = []

        # parse text for categories
        for i in parser(self.text)[0]:
            # check if already exists. if not, save
            try:
                Category.objects.get(name=i)
            except ObjectDoesNotExist:
                Category(name=i).save()
            categories.append(Category.objects.get(name=i).id)

        # parse text for persons
        for i in parser(self.text)[1]:
            # check if exists. if not, save
            try:
                Person.objects.get(name=i)
            except ObjectDoesNotExist:
                Person(name=i).save()
            persons.append(Person.objects.get(name=i).id)

        # creates event-category-person m2m relation
        event.category, event.person = categories, persons
        event.base_save()

    def __str__(self):
        return self.text
