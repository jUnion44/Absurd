from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Prompt(models.Model):
    text = models.TextField()
    tag = models.ForeignKey(Tag,related_name="prompts",on_delete=models.CASCADE)
    def __str__(self):
        return self.text + " [[" + self.tag.name + "]"
    
class Choice(models.Model):
    text = models.CharField(max_length=500)
    tag = models.ForeignKey(Tag,related_name="choices",on_delete=models.CASCADE)
    promptCurrent = models.ForeignKey(Prompt,related_name="befores",on_delete=models.CASCADE)
    promptNext = models.ForeignKey(Prompt,related_name="destination",on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        try:
            return self.text + " [[" + self.tag.name + "] -> " + self.promptNext.text
        except:
            return self.text + " [[" + self.tag.name + "] -> " + "RANDOM PROMPT"
