from django.db import models

# Create your models here.
class Doctor(models.Model):
    user_name = models.CharField(max_length=50)
    age       = models.IntegerField(default=0)
    gender    = models.CharField(max_length=20)
    contact   = models.BigIntegerField()
    email     = models.CharField(max_length=50, unique= True)
    pwd       = models.CharField(max_length=20)
    doctorverify = models.BooleanField(default=0)
    about = models.CharField(max_length=150)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=15)
    workingtime = models.CharField(max_length=30)
    qualification = models.CharField(max_length=20)
    profile = models.ImageField(upload_to='',default='null')
    proof = models.ImageField(upload_to='',default='null')  

    @classmethod
    def get_by_email_and_password(cls, email, password):
        try:
            return cls.objects.get(email=email, pwd=password)
        except cls.DoesNotExist:
            return None
    @classmethod
    def get_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

class Patient(models.Model):
    user_name = models.CharField(max_length=50)
    age       = models.IntegerField(default=0)
    gender    = models.CharField(max_length=20)
    contact   = models.BigIntegerField()
    email     = models.CharField(max_length=50, unique= True)
    pwd       = models.CharField(max_length=20)
    profile = models.ImageField(upload_to='',default='null')


    @classmethod
    def get_by_email_and_password(cls, email, password):
        try:
            return cls.objects.get(email=email, pwd=password)
        except cls.DoesNotExist:
            return None
    @classmethod
    def get_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None
   
class Appointment(models.Model):
    dr_name = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=20)
    patient_email = models.EmailField(max_length=20)
    place = models.CharField(max_length=20)
    date = models.DateField(default='null')
    time = models.TimeField(default='null')
    contact_no = models.IntegerField(default=0)
    district = models.CharField(max_length=20)

    @classmethod
    def get_by_district(cls,district):
        try:
            return cls.objects.get(district=district)
        except cls.DoesNotExist:
            return None

# class Feedback(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     feedback_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Feedback from {self.patient.user_name}'


        

     

    
