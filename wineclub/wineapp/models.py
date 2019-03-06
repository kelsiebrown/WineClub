from django.db import models

# Wine Type
class WineType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='winetype'

# Winery
class Winery(models.Model):
    wineryname=models.CharField(max_length=255)
    winerylocation=models.CharField(max_length=255)
    wineryurl=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.wineryname

    class Meta:
        db_table='winery'

# Wine
class Wine(models.Model):    
    winename=models.CharField(max_length=255)
    winetype=models.ForeignKey(WineType, on_delete=models.DO_NOTHING)
    winery=models.ForeignKey(Winery, on_delete=models.DO_NOTHING)
    wineyear=models.CharField(max_length=255)
    wineprice=models.CharField(max_length=255)
    winedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.winename

    class Meta:
        db_table='wine'

# Review
class WineReview(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    wine=models.ForeignKey(Wine, on_delete=models.CASCADE)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='winereview'

# Event
class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'