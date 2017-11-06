from django.test import TestCase

from .models import Event, Category, Person
from .scripts import parser


class ParserTest(TestCase):
    def setUp(self):
        self.event1 = 'Hi, How are You? Im currently on vacation! #Cemetery @Hans'
        self.event2 = 'Great party tonight with @Byron @Mary_Shelley at #Genewa #Switzerland '
        self.event3 = '#home Been thinking about that guy who offered drugs by email @JWas@poczta.onet.pl'
        self.event4 = 'This time @Hans have no category tag for You!!'
        self.event5 = 'And now no person #home'
        self.event6 = 'No tags at all!'

    def test_single_tags(self):
        categories, persons = parser(self.event1)
        self.assertEqual(categories, ['Cemetery', ])
        self.assertEqual(persons, ['Hans', ])

    def test_multiple_tags(self):
        categories, persons = parser(self.event2)
        self.assertEqual(categories, ['Genewa', 'Switzerland'])
        self.assertEqual(persons, ['Byron', 'Mary_Shelley'])

    def test_email_parse(self):
        categories, persons = parser(self.event3)
        self.assertEqual(categories, ['home', ])
        self.assertEqual(persons, ['JWas@poczta.onet.pl', ])

    def test_no_category(self):
        categories, persons = parser(self.event4)
        self.assertEqual(categories, [])
        self.assertEqual(persons, ['Hans', ])

    def test_no_person(self):
        categories, persons = parser(self.event5)
        self.assertEqual(categories, ['home', ])
        self.assertEqual(persons, [])

    def test_no_tags(self):
        categories, persons = parser(self.event6)
        self.assertEqual(categories, [])
        self.assertEqual(persons, [])


class DatabaseTest(TestCase):

    def setUp(self):
        self.event = 'Hello, my name is @Jake @Robocop im 39 years young #babyfood #police #cupboard'
        self.test_event = Event(text=self.event)
        self.test_event.save()
        self.e_obj = Event.objects.all()
        self.c_obj = Category.objects.all()
        self.p_obj = Person.objects.all()
        self.cat_names = ['babyfood', 'police', 'cupboard']
        self.cat_ids = [1, 2, 3]
        self.p_names = ['Jake', 'Robocop']
        self.p_ids = [1, 2]

    def test_event_creation(self):
        self.assertIsInstance(self.test_event, Event)

    def test_dbase_event(self):
        self.assertEqual(len(self.e_obj), 1)
        self.assertEqual(self.e_obj[0].text, self.event)

    def test_dbase_category(self):
        self.assertEqual(len(self.c_obj), 3)
        zipper = zip(self.c_obj, self.cat_ids, self.cat_names)
        for obj, ids, name in zipper:
            self.assertEqual(obj.name, name)
            self.assertEqual(obj.id, ids)

    def test_dbase_person(self):
        self.assertEqual(len(self.p_obj), 2)
        zipper = zip(self.p_obj, self.p_ids, self.p_names)
        for obj, ids, name in zipper:
            self.assertEqual(obj.name, name)
            self.assertEqual(obj.id, ids)











