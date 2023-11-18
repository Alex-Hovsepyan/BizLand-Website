from django.db import models

# Create your models here.

class Header(models.Model):

    doc_title = models.CharField('Document Title', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Phone Number', max_length=30)
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    social4 = models.URLField('Social 4')
    title = models.CharField('Title', max_length=50)
    paht1 = models.CharField('Path 1', max_length=30)
    paht2 = models.CharField('Path 2', max_length=30)
    paht3 = models.CharField('Path 3', max_length=30)
    paht4 = models.CharField('Path 4', max_length=30)
    paht5 = models.CharField('Path 5', max_length=30)
    paht6 = models.CharField('Path 6', max_length=30)
    paht7 = models.CharField('Path 7', max_length=30)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'
    
class Home(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Title', max_length=20)
    colored_title = models.CharField('Colored Title', max_length=20)
    text = models.TextField('Text')
    button1 = models.CharField('Button 1', max_length=30)
    button2 = models.CharField('Button 2', max_length=30)
    video_url = models.URLField('Video Url')
    
    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class FeaturedServices(models.Model):

    icon = models.CharField('Icon', max_length=40)
    title = models.CharField('Title', max_length=30)
    text = models.TextField('Text')
        
    class Meta:

        verbose_name = 'Featured Services'
        verbose_name_plural = 'Featured Services'

    def __str__(self) -> str:
        return self.title
    
class Title(models.Model):

    button1 = models.CharField('About Button', max_length=30)
    title1 = models.CharField('About Title', max_length=40)
    colored_title1 = models.CharField('About Colored Title', max_length=40)
    text1 = models.TextField('About Text')
    button2 = models.CharField('Services Button', max_length=30)
    title2 = models.CharField('Services Title', max_length=40)
    colored_title2 = models.CharField('Services Colored Title', max_length=40)
    text2 = models.TextField('Services Text')
    button3 = models.CharField('Portfolio Button', max_length=30)
    title3 = models.CharField('Portfolio Title', max_length=40)
    colored_title3 = models.CharField('Portfolio Colored Title', max_length=40)
    text3 = models.TextField('Portfolio Text')
    button4 = models.CharField('Team Button', max_length=30)
    title4 = models.CharField('Team Title', max_length=40)
    colored_title4 = models.CharField('Team Colored Title', max_length=40)
    text4 = models.TextField('Team Text')
    button5 = models.CharField('Pricing Button', max_length=30)
    title5 = models.CharField('Pricing Title', max_length=40)
    colored_title5 = models.CharField('Pricing Colored Title', max_length=40)
    text5 = models.TextField('Pricing Text')
    button6 = models.CharField('FAQ Button', max_length=30)
    title6 = models.CharField('FAQ Title', max_length=40)
    colored_title6 = models.CharField('FAQ Colored Title', max_length=40)
    text6 = models.TextField('FAQ Text')
    button7 = models.CharField('Contact Button', max_length=30)
    title7 = models.CharField('Contact Title', max_length=40, blank=True)
    colored_title7 = models.CharField('Contact Colored Title', max_length=40)
    text7 = models.TextField('Contact Text')

class About(models.Model):

    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=80)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    
    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutContent(models.Model):

    icon = models.CharField('Icon', max_length=40)
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')

    class Meta:

        verbose_name = 'About Content'
        verbose_name_plural = 'About Content'

    def __str__(self) -> str:
        return self.title

class Skill(models.Model):

    skill = models.CharField('Skill', max_length=30)
    procent = models.IntegerField('Procent')

    def __str__(self) -> str:
        return f'{self.skill} - {self.procent}'
    
class Statistic(models.Model):

    icon = models.CharField('Icon', max_length=40)
    count = models.IntegerField('Count')
    title = models.CharField('Title', max_length=40)

    def __str__(self) -> str:
        return f'{self.title} - {self.count}'
    
class Client(models.Model):
    
    img = models.ImageField('Image')

class Service(models.Model):

    icon = models.CharField('Icon', max_length=40)
    title = models.CharField('Title', max_length=40)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.title
    
class Testimonial(models.Model):

    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=50)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return f'{self.name} - {self.position}'
    
class Categories(models.Model):

    title = models.CharField('Title', max_length=40)

    class Meta:

        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title
    
class Portfolio(models.Model):

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=40)

    def __str__(self) -> str:
        return f'{self.title} - {self.category}'
    
class Team(models.Model):

    img = models.ImageField('Image')
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=40)
    social1 = models.URLField('Social 1 Url')
    social2 = models.URLField('Social 2 Url')
    social3 = models.URLField('Social 3 Url')
    social4 = models.URLField('Social 4 Url')

    class Meta:

        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self) -> str:
        return f'{self.name} - {self.position}'

class Pricing(models.Model):

    title = models.CharField('Title', max_length=50)
    price = models.IntegerField('Price')
    offers = models.TextField('Offers')
    button = models.CharField('Button Name', max_length=30)
    advanced = models.BooleanField('Advanced', blank=True)
    
    class Meta:

        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'

    def __str__(self) -> str:
        return f'{self.title} - {self.price}'
    
class FAQ(models.Model):

    question = models.CharField('Question', max_length=200)
    answer = models.TextField('Answer')
        
    class Meta:

        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self) -> str:
        return self.question

class Info(models.Model):

    icon = models.CharField('Icon', max_length=40)
    title = models.CharField('Title', max_length=50)
    info = models.CharField('Info', max_length=100)

    def __str__(self) -> str:
        return self.title
    
class ContactInfo(models.Model):

    google_map = models.TextField('Google Map')
    placeholder1 = models.CharField('Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Placeholder 3', max_length=50)
    placeholder4 = models.CharField('Placeholder 4', max_length=50)
    button1 = models.CharField('Button 1', max_length=30)
    title = models.CharField('Newsletter Title', max_length=50)
    text = models.TextField('Newsletter Text')
    placeholder5 = models.CharField('Placeholder 5', max_length=50)
    button2 = models.CharField('Button 2', max_length=30)

            
    class Meta:

        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'

class Contact(models.Model):

    username = models.CharField('Username', max_length=60)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=60)
    message = models.TextField('Message')
    date_time = models.DateTimeField('Date & Time', auto_now=True)

    def __str__(self) -> str:
        return f'{self.username} - {self.email} - {self.date_time}'
    
class Subscribe(models.Model):

    email2 = models.EmailField('Email', unique=True)

    def __str__(self) -> str:
        return self.email2