from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Prompt(models.Model):
    text = models.CharField(max_length=500)
    tag = models.ForeignKey(Tag,related_name="prompts")
    def __str__(self):
        return self.text + " [[" + self.tag.name + "]"
    
class Choice(models.Model):
    text = models.CharField(max_length=500)
    tag = models.ForeignKey(Tag,related_name="choices")
    promptNext = models.ForeignKey(Prompt,related_name="befores")
    def __str__(self):
        return self.text + " [[" + self.tag.name + "] -> " + self.promptNext.text
