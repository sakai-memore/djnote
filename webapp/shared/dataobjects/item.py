from django.bd import models


class ItemModel(models.Model):
    ## meta
    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'

    ## constants
    ENUM_SEX = (
        (1, 'male'),
        (2, 'famale'),
    )
    ##
    ## fields 
    name = models.CharField(maxlength=256)
    age = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(choices=ENUM_SEX, default=1)
    description = models.TextField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ## 
    def __str__(self):
        return self.name



