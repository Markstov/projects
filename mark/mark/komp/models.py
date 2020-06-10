from django.db import models

# Create your models here.

class Buy(models.Model):
  id = models.AutoField(primary_key= True)
  title = models.CharField(max_length=120, verbose_name = 'Заявка')
  content = models.TextField(verbose_name = 'Пожелания')
  timestamp = models.DateTimeField(verbose_name= 'Дата заявки')


  status = (('i', 'Intel'), ('a', 'Amd'))
  status = models.CharField(max_length=2, choices=status, default= 'i', verbose_name= 'Процессор')

  status1 = (('m', 'MSI'), ('as', 'Asus'), ('p', 'Palit'))
  status1 = models.CharField(max_length=2, choices=status1, default= 'm', verbose_name= 'Видеокарта')

  status2 = (('4', '4GB'), ('8', '8GB'), ('16', '16GB'), ('128', '128GB'))
  status2 = models.CharField(max_length=3, choices=status2, default= '4', verbose_name= 'Оперативная память')

  post_author = models.ForeignKey('Author', blank = True, null = True, verbose_name = 'Покупатель', on_delete = models.CASCADE)

  def __unicode__(self):
    return self.title
  def __str__(self):
    return self.title
  
class Author (models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=120,verbose_name='Имя')
  second_name = models.CharField(max_length=120,verbose_name='Фамилия')
  email = models.EmailField(max_length=254,verbose_name='Email')
  
  def __unicode__(self):
    return self.first_name + ' ' + self.second_name
  def __str__(self):
    return self.first_name + ' ' + self.second_name

