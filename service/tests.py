from django.test import TestCase
from .models import  Service

# Create your tests here.

class ServiceTestCase(TestCase):
    def addService(self):
        Service.objects.create(name='test', slug='test', description='test_description')
    
    def createService(self, name='test_name', slug='test_slug', description='test_description'):
        return Service.objects.create(name=name, slug=slug, description=description)

    def test_service(self):
        obj1 = Service.objects.get(name='test')
        self.assertEqual(obj1.name, 'test')

    def test_service_qs(self):
        name = 'Another Name'
        object1 = self.createService(name=name)
        qs = Service.objects.filter(name='Another Name')
        self.assertEqual(qs.count(), 1)
