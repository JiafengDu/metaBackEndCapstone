from django.test import TestCase, Client
from restaurant import views, models
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.test1 = models.Menu.objects.create(title='IceCrean', price=80, inventory=101)
        self.test2 = models.Menu.objects.create(title='cheesecurd', price=9, inventory=98)
        
    def test_getall(self):
        #generate the output using views.MenuItemsView
        response = self.c.get('/restaurant/menu')
        
        #generate the output using self.test1, self.test2
        expected = MenuSerializer([self.test1, self.test2], many=True)
        
        #compare the two output
        self.assertJSONEqual(response.content, expected.data)