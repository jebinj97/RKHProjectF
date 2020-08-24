from django.db import models


# Create your models here.
class Aadhar(models.Model):
    uid = models.IntegerField(null=False, default=0, primary_key=True)

    def __str__(self):
        return str(self.uid)


class User(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    caste = models.CharField(
        max_length=10,
        default='GEN',
    )
    gender = models.CharField(
        max_length=10,
        default='male',
    )
    marital_status = models.CharField(max_length=10, default='unmarried')
    education_qualification = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=40, default='unknown')
    state = models.CharField(max_length=40, default='unknown')
    district = models.CharField(max_length=40, default='unknown')
    taluk = models.CharField(max_length=40, default='unknown')
    village = models.CharField(max_length=40, default='unknown')
    disability = models.CharField(max_length=3, default='YES')
    health_aids = models.IntegerField(default=0)
    medical_insurance = models.IntegerField(default=0)

    # def __str__(self):
    #     return str([self.name, self.age, self.gender])


class Accessibility(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    dist_from_school = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    environment = models.CharField(max_length=3, default='YES')


class FamilyIncome(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    income = models.IntegerField()
    members = models.IntegerField()
    any_student_aid = models.CharField(max_length=3, default="NO")


class Availability(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    laptop = models.CharField(max_length=3, default="NO")
    smartphone = models.CharField(max_length=3, default="NO")
    internet = models.CharField(max_length=3, default="NO")


class Transportation(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    vehicles = models.IntegerField()
    public_vehicles = models.IntegerField()


class CurrentHealth(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    terminal_disease = models.CharField(max_length=30)
    heredity_disease = models.CharField(max_length=30)
    bedridden = models.CharField(max_length=3, default='NO')


class MedicalAccessibility(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    nearest_hospital = models.IntegerField(default=0)
    four_wheeler = models.CharField(max_length=3, default='NO')
    nearest_pharmacy = models.IntegerField(default=0)


class Land(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    agriculture_area = models.IntegerField(default=0)
    ancestral_land = models.IntegerField(default=0)
    total_value_of_possession = models.IntegerField(default=0)


class CurrentlyResiding(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    rented = models.CharField(max_length=3, default='NO')
    area = models.IntegerField(default=0)
    water_quantity = models.IntegerField(default=0)
    water_quality = models.IntegerField(default=0)
    electricity_facility = models.CharField(max_length=30, default="")
    effected_by_calamities = models.CharField(max_length=3, default="NO")
    roofing = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)


class Credits(models.Model):
    uid = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    educational_scheme = models.IntegerField(default=0)
    medicinal_scheme = models.IntegerField(default=0)
    housing_scheme = models.IntegerField(default=0)
    land_scheme = models.IntegerField(default=0)
    financial_scheme = models.IntegerField(default=0)

    def __str__(self):
        return str([self.uid, self.educational_scheme])
