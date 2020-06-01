from django.db import models
from  django.contrib.auth.models import AbstractUser
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.conf import settings
from  django.contrib.auth.models import AbstractUser
from PIL import Image



class User(AbstractUser):
    is_chercheur = models.BooleanField(default=False)
    is_evaluteur = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Organization = models.CharField(max_length=100)
    Phone  = models.CharField(max_length=20,unique=True)
    City = models.CharField(max_length=100)
    Post_code = models.CharField(max_length=20)
    Country = models.CharField(blank=False,max_length=100)
    Address_line_principale = models.CharField(max_length=200,blank=True)
    Address_line = models.CharField(max_length=200,blank=True)
    profile_pict = models.ImageField(upload_to='profile_piccs',blank=True
        ,default='photodflt.png')
    site_Personnel = models.URLField(blank=True)


    def get_absolute_url(self):
        return reverse('EditeProfile', kwargs={'pk': self.pk})


###############

class Evaluateur(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(unique=True)
    Code_Eval = models.CharField(max_length=30)

    def __str__(self):
        return  ' Le Evaluteur :' + self.user.username + ' |  | ' + ' et Sont email : ' + self.user.email

    def get_absolute_url(self):
        return reverse('editEval', kwargs={'pk':self.id})


################
class Chercheur(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return  ' Le Chercheur :' + self.user.username + ' |  | ' + 'et sont  email : ' + self.user.email


    def get_absolute_url(self):
        return reverse('editCher', kwargs={'pk':self.id})





#######""""/////////////////////////////////////////////////////////////////////////////


class Commite(models.Model):
    # hado hna ndirohom dircte b groupe 
    #user = models.ManyToManyField(Evaluateur, on_delete=models.CASCADE, primary_key=True)

    #user = models.OneToOneField(Evaluateur ,on_delete=models.CASCADE, primary_key=True)
    evaluteur_list = models.ManyToManyField(Evaluateur)
    Organizationof_Commite = models.CharField('Commite dans le theme',max_length=200)
    autre_Info = models.CharField(max_length=200)
    sepiceilite = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.sepiceilite


    class Meta:  # bch tsmiha haka f partie adminstration t3k 
        verbose_name = "Commites"



class ToDolist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , 
    	related_name="todolist" , null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
    	return self.name



class Item(models.Model):
	todolist = models.ForeignKey(ToDolist,on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text



#######""""/////////////////////////////////////////////////////////////////////////////

class Topic(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.title




class Conferance(models.Model):

    title = models.CharField(max_length=200, null=True,unique=True)
    email = models.EmailField(unique=True, null=True)
    topic = models.ManyToManyField(Topic) ## many to many
    Commite = models.ForeignKey(Commite,null=True,  on_delete=models.SET_NULL)
    link = models.URLField(blank=True)
    start_day_sub = models.DateField(auto_now_add = False)
    end_day_sub = models.DateField(auto_now_add = False)
    start_day_eval = models.DateField(auto_now_add = False)
    end_day_eval  = models.DateField(auto_now_add = False)
    adress = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    postal_code = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    
       
    class Meta:
        ordering = ['-date_created','updated']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('confEdit', kwargs={'pk':self.id})


class Article(models.Model):

    name = models.CharField(max_length=200, null=True,unique=True)
    description = RichTextField(blank=True , null= True)
    author = models.ForeignKey(Chercheur,null=True, on_delete=models.SET_NULL)
    date_posté = models.DateTimeField(auto_now_add=True)
    Conferance = models.ForeignKey(Conferance ,null=True,  on_delete=models.SET_NULL)
    document = models.FileField(upload_to='documents_Chercheur/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering = ['-date_posté']

    def __str__(self):
        return self.name


