from django.db import models
from learning_user import settings

# create a tuple for the status of each post
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# each field in this class represents a column in the database table
class Contact_MAKANI_CF(models.Model):
    title_de_problem = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    Perssone = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # this class contains metadata and uses the created_on field from the model to sort out data which sorts
    # in descending order by default
    class Meta:
        ordering = ['-created_on']

    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return self.title_de_problem




################  2020-05-15 ######

class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

    class Meta:  
        verbose_name = "Plus_Commande_pour_les_users"



        