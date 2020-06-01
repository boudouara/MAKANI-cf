from django import forms
from .models import BlogPost 


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField() #kima path win jayy 
    content = forms.CharField(widget=forms.Textarea)



class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'Docment_By_Admin','publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title) # >>>>>>>>>>>>>>>>>>>>>>>>> serach by title 
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # id=instance.id kifkiff
        if qs.exists():
            raise forms.ValidationError("This title has already been used !!! please use new one !!! ")
        return title