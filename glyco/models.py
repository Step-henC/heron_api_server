from django.db import models

# Create your models here.
class GlycoFileData(models.Model):
  Peptide_Name = models.CharField(max_length=255)
  Peptide_Name = models.CharField(max_length=255)
  Replicate_Name = models.CharField(max_length=255)
  Peptide_Sequence = models.CharField(max_length=255)
  Precursor = models.CharField(max_length=255)
  Total_Area = models.CharField(max_length=255)
  Isotope_Dist_Rank = models.CharField(max_length=255)
  Isotope_Dist_Index = models.CharField(max_length=255)
  Isotope_Dist_Proportion = models.CharField(max_length=255)
  Best_Retention_Time = models.CharField(max_length=255)