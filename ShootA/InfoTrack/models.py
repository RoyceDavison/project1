from django.db import models

# Create your models here.

###########################
#PrivateTutor
###########################


class User(models.Model):
    # Fields
    user_id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20, help_text="Enter user name: ")
    email = models.CharField(max_length=20, help_text="Enter e-mail account: ")
    password =models.CharField(max_length=20, help_text="Create a password: ")
    description = models.CharField(max_length=20, help_text="Briefly introduce yourself: ", blank = True)
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )
    grade = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default= 'FR',
    )

    major = models.CharField(max_length=20, help_text="Major: ", blank = True)
    
    

    # Metadata
    class Meta: 
        ordering = ["userName"]

    def get_absolute_url(self):
        
        return reverse('user-detail', args=[str(self.id)])

        
    def __str__(self):
        
        return '%s (%s)' % (self.userName,self.email)




class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    context = models.CharField(max_length=5000,default='DEFAULT VALUE')
    post_id = models.ForeignKey('Post', default='DEFAULT VALUE')
    
    
    def get_absolute_url(self):

        return reverse('comment-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.user_id, self.comment_id)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', null =True)
    title = models.CharField(max_length=100,default='DEFAULT VALUE')
    content = models.CharField(max_length=5000,default='DEFAULT VALUE')    
    favorite = models.CharField(max_length=100, null = True ,blank= True)
    
    def get_absolute_url(self):
        
        return reverse('post-detail', args=[str(self.id)])
    

    def __str__(self):
       
        return '%s, %s' % (self.title, self.post_id)


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)

    url = models.URLField(blank=True)
        
    def get_absolute_url(self):

        return reverse('video-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.video_id, self.url)
    

class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    
    url = models.URLField(blank=True)
        
    def get_absolute_url(self):

        return reverse('picture-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.picture_id, self.url)
###############
###############
class Picture_comment(models.Model):
    picture_id = models.ForeignKey('Picture',null=True)
    comment_id = models.ForeignKey('Comment',null=True)

    class Meta:
        unique_together = ('picture_id', 'comment_id',)
        
    def get_absolute_url(self):

        return reverse('picture_comment-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.picture_id, self.comment_id)

    
class Video_comment(models.Model):
    video_id = models.ForeignKey('Video', null=True)
    comment_id = models.ForeignKey('Comment', null=True)
        
    class Meta:
        unique_together = ('video_id', 'comment_id',)

    def get_absolute_url(self):

        return reverse('picture-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.video_id, self.comment_id)

    
class Video_post(models.Model):
    video_id = models.ForeignKey('Video', null=True)
    post_id = models.ForeignKey('Post', null=True)
    class Meta:
        unique_together = ('video_id', 'post_id',)
        
    def get_absolute_url(self):

        return reverse('picture-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.video_id, self.post_id)

    
class Picture_post(models.Model):
    picture_id = models.ForeignKey('Picture', null=True)
    post_id = models.ForeignKey('Post', null=True)

    class Meta:
        unique_together = ('picture_id', 'post_id',)
        
    def get_absolute_url(self):

        return reverse('picture-detail', args=[str(self.id)])
    

    def __str__(self):

        return '%s, %s' % (self.picture_id, self.post_id)


    









###########################
