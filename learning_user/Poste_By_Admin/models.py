from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone



class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |          #tsemaa haka aya haja nbghi njbdeha njbdehaa b title b ....
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |      #  tsema haka thwse b aya haja rahi hna tsehel khdema 3l user 
                    Q(user__username__icontains=query)
                    # hna aprr nzide kima nbghi w nkber filter ta3i nrmllllll
                    )
        return self.filter(lookup)



class BlogPostManager(models.Manager):              
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)       # tsema haka kol model applique 3lih Queryset dik 1 er

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)




class BlogPost(models.Model): 
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.SET_NULL)
    image   = models.ImageField(upload_to='image_Off_Adminstration/', blank=True, null=True)
    Docment_By_Admin  = models.FileField(upload_to='file_Off_Adminstration/' ,blank=True, null=True)
    title  = models.CharField(max_length=120)
    slug   = models.SlugField(unique=True) 
    content  = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager() # et voilla apllique all fct sur les models  de model BlogPost

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']
        verbose_name = "Les Document,Pdf,photo poste by Us "

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

