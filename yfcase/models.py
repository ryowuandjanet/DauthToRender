from django.db import models

class Yfcase(models.Model):
    yfcaseCaseNumber=models.CharField(u'案號(*)',max_length=100)
    yfcaseCompany=models.CharField(u'所屬公司',max_length=50,null=True,blank=True)
    yfcaseCity=models.CharField(u'縣市',max_length=100,null=True,blank=True)
    yfcaseTownship=models.CharField(u'鄉鎮區里',max_length=100,null=True,blank=True)
    yfcaseBigSection=models.CharField(u'段號',max_length=10,null=True,blank=True)
    yfcaseSmallSection=models.CharField(u'小段',max_length=10,null=True,blank=True)
    yfcaseVillage=models.CharField(u'村里',max_length=100,null=True,blank=True)
    yfcaseNeighbor=models.CharField(u'鄰',max_length=100,null=True,blank=True)
    yfcaseStreet=models.CharField(u'街路',max_length=100,null=True,blank=True)
    yfcaseSection=models.CharField(u'段',max_length=100,null=True,blank=True)
    yfcaseLane=models.CharField(u'巷',max_length=100,null=True,blank=True)
    yfcaseAlley=models.CharField(u'弄',max_length=100,null=True,blank=True)
    yfcaseNumber=models.CharField(u'號',max_length=100,null=True)
    yfcaseFloor=models.CharField(u'樓(含之幾)',max_length=100,null=True,blank=True)
    yfcaseDebtor=models.CharField(u'債務人',max_length=100,null=True,blank=True)
    yfcaseCreditor=models.CharField(u'債權人',max_length=100,null=True,blank=True)
    yfcaseCreditorMobilePhone=models.CharField(u'債權人電話',max_length=20,null=True,blank=True)

    def __str__(self):
        return self.yfcaseCaseNumber
