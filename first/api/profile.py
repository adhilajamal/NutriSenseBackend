from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Patient,Doctor


@api_view(['POST'])
def PatientProfile(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({'message': 'Email is required'}, status=400)

    try:
        patient = Patient.objects.get(email=email)
        patient_data = {
            'user_name': patient.user_name,
            'age': patient.age,
            'gender': patient.gender,
            'contact': patient.contact,
            'email': patient.email,
            'profile': patient.profile.url if patient.profile else None,
            'password' : patient.pwd
        }
        return Response(patient_data, status=200)
    except Patient.DoesNotExist:
        return Response({'message': 'Patient not found'}, status=404)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)
    
@api_view(['POST'])
def patientChangePassword(request):
    data = request.data
    email = data.get('email')
    oldpassword = data.get('oldpassword')
    newpassword = data.get('newpassword')
    patient = Patient.get_by_email_and_password(email,oldpassword)
    if not patient:
        return Response({'message':'Incorrect Password'},status=401)
    patient.pwd=newpassword
    patient.save()
    return Response({'message' :'Password changed successfully'},status=200)

@api_view(['POST'])
def updatePatientProfile(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({'message': 'Email is required'}, status=400)

    try:
        patient = Patient.objects.get(email=email)
        
        # Update patient fields if present in request data
        if 'user_name' in data:
            patient.user_name = data['user_name']
        if 'age' in data:
            patient.age = data['age']
        if 'gender' in data:
            patient.gender = data['gender']
        if 'contact' in data:
            patient.contact = data['contact']
        if 'profile' in data:
            patient.profile = data['profile']
        

        # Save the updated patient instance
        patient.save()

        # Prepare the response data
        patient_data = {
            'user_name': patient.user_name,
            'age': patient.age,
            'gender': patient.gender,
            'contact': patient.contact,
            'email': patient.email,
            'profile': patient.profile.url if patient.profile else None,
        }
        
        return Response(patient_data, status=200)
    except Patient.DoesNotExist:
        return Response({'message': 'Patient not found'}, status=404)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)


    

@api_view(['POST'])
def DoctorProfile(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({'message' : 'email is required'},status=400)
    try:
        doctor = Doctor.objects.get(email=email)
        doctor_data = {
            'user_name': doctor.user_name,
            'age': doctor.age,
            'gender': doctor.gender,
            'contact': doctor.contact,
            'email': doctor.email,
            'profile': doctor.profile.url if doctor.profile else None,
            'password' : doctor.pwd,
            'about': doctor.about,
            'address': doctor.address,
            'district': doctor.district,
            'workingtime': doctor.workingtime,
            'qualification': doctor.qualification,
            'proof': doctor.proof.url if doctor.proof else None
        }
        return Response(doctor_data, status=200)
    except Patient.DoesNotExist:
        return Response({'message': 'Patient not found'}, status=404)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)
    
@api_view(['POST'])
def doctorChangePassword(request):
    data = request.data
    email = data.get('email')
    oldpassword = data.get('oldpassword')
    newpassword = data.get('newpassword')
    doctor = Doctor.get_by_email_and_password(email,oldpassword)
    if not doctor:
        return Response({'message':'Incorrect Password'},status=401)
    doctor.pwd=newpassword
    doctor.save()
    return Response({'message' :'Password changed successfully'},status=200)


@api_view(['POST'])
def updateDoctorProfile(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({'message': 'Email is required'}, status=400)

    try:
        doctor = Doctor.objects.get(email=email)
        
        # Update patient fields if present in request data
        if 'user_name' in data:
            doctor.user_name = data['user_name']
        if 'age' in data:
            doctor.age = data['age']
        if 'gender' in data:
            doctor.gender = data['gender']
        if 'contact' in data:
            doctor.contact = data['contact']
        if 'profile' in data:
            doctor.profile = data['profile']
        if 'about' in data:
            doctor.about = data['about']
        if 'address' in data:
            doctor.address = data['address']
        if 'district' in data:
            doctor.district = data['district']
        if 'workingtime' in data:
            doctor.workingtime = data['workingtime']
        if 'qualification' in data:
            doctor.qualification =data['qualification']
        if 'proof' in data:
            doctor.proof = data['proof']

        # Save the updated doctor instance
        doctor.save()

        # Prepare the response data
        doctor_data = {
            'user_name': doctor.user_name,
            'age': doctor.age,
            'gender': doctor.gender,
            'contact': doctor.contact,
            'email': doctor.email,
            'profile': doctor.profile.url if doctor.profile else None,
             'about': doctor.about,
            'address': doctor.address,
            'district': doctor.district,
            'workingtime': doctor.workingtime,
            'qualification': doctor.qualification,
            'proof': doctor.proof.url if doctor.proof else None
        }
        
        return Response(doctor_data, status=200)
    except Doctor.DoesNotExist:
        return Response({'message': 'Doctor not found'}, status=404)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)
