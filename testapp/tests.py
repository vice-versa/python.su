from django.test import TestCase
from testapp.models import CustomUser, Login, Password, Achievement


class TestRawDefferred(TestCase):
    
    def setUp(self):
        
        self.login = Login.objects.create(login="uTest")
        self.password = Password.objects.create(password="testpassword",
                                                login=self.login)
        self.user = CustomUser.objects.create(login=self.login,
                                              password=self.password,
                                              email="email@rmail.ru",
                                              gender="m"
                                              )
        self.achievement = Achievement.objects.create(name="test",
                                                      login=self.login,
                                                      cost="22.0"
                                                      )
    
    def test_login(self):
        
        res = CustomUser.objects.raw("""SELECT logins.id as id, '' as email, '' as gender, achievement.name as name\
                                         FROM logins JOIN passwords ON passwords.login_id = logins.id\
                                          JOIN achievement ON logins.id = achievement.login_id""")
        print res[0]
        print res[0].login