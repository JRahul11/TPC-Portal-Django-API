from django.db import models

class JobOpening(models.Model):
    job_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    batch = models.IntegerField(null=True, blank=True)
    valid_till = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    offers = models.CharField(max_length=50, null=True, blank=True)
    tenth_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    twelveth_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    diploma_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    be_percent = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cgpa = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    notice = models.TextField(null=True, blank=True)
    live_kt = models.IntegerField(null=True, blank=True)
    dead_kt = models.IntegerField(null=True, blank=True)
    gap = models.IntegerField(null=True, blank=True)
    package = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.email + ' ' + str(self.batch)

    class Meta:
        verbose_name_plural = "Job Openings"
        db_table = "job_openings"