from django.db import models


class Buldings(models.Model):

    name = models.CharField(max_length=200)

    building_id = models.IntegerField()

    desctription = models.TextField()



class Content(mode.Model):

    title = models.CharField(max_length=100)

    creator = pass # I think this needs to make use of a foreign key that takes something from the Users app with email etc available. 

    public = models.BooleanField(initial=False, null=False, editable=True)

    date_added = models.DateField(auto_now_add=True)

    class Meta:
        
        abstract = True



class Text(Content):

    body = models.TextField()



class Image(Content):
    # TODO: in settings need to update the path of MEDIA_ROOT.
    # TODO: investigate how to limit size of image upload.
    body = models.ImageField(upload_to='uploads/')



class Video(Content):

    body = models.URLField(max_length=255)



class Sound(Content):
    # TODO: limit size of sound file uploads
    body = models.FileField(upload_to='uploads/%Y/%m/%d/')
