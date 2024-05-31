from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Appointment ,Doctor

@api_view(['GET'])
def get_all_doctors(request):
    try:
        # Fetch all doctors
        doctors = Doctor.objects.all()
        
        # Serialize the doctor data
        serialized_data = [
            {
                'user_name': doctor.user_name,
                'age': doctor.age,
                'gender': doctor.gender,
                'contact': doctor.contact,
                'email': doctor.email,
                'doctorverify': doctor.doctorverify,
                'about': doctor.about,
                'address': doctor.address,
                'district': doctor.district,
                'workingtime': doctor.workingtime,
                'qualification': doctor.qualification,
                'profile': doctor.profile.url if doctor.profile else None,
                'proof': doctor.proof.url if doctor.proof else None
            } 
            for doctor in doctors
        ]
        
        return Response({'doctors': serialized_data}, status=200)
    
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)




@api_view(['POST'])
def DoctorDetails(request):
    data = request.data
    email = data.get('email')

    if not email:
        return Response({'message': 'Email is required'}, status=400)

    try:
        doctor = Doctor.objects.get(email=email)
        doctor_data = {
            'user_name': doctor.user_name,
            'age': doctor.age,
            'gender': doctor.gender,
            'contact': doctor.contact,
            'email': doctor.email,
            'doctorverify': doctor.doctorverify,
            'about': doctor.about,
            'address': doctor.address,
            'district': doctor.district,
            'workingtime': doctor.workingtime,
            'qualification': doctor.qualification,
            'profile': doctor.profile.url if doctor.profile else None,
            'proof': doctor.proof.url if doctor.proof else None
        }
        return Response(doctor_data, status=200)
    except Doctor.DoesNotExist:
        return Response({'message': 'Doctor not found'}, status=404)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)



@api_view(['POST'])
def MakeAppointment(request):
    data = request.data
    required_fields = ['dr_name', 'patient_name', 'patient_email', 'place', 'date', 'time', 'contact_no', 'district']

    # Check if all required fields are present
    for field in required_fields:
        if field not in data:
            return Response({'message': f'Missing field: {field}'}, status=400)

    try:
        # Create a new appointment record
        appointment = Appointment.objects.create(
            dr_name=data['dr_name'],
            patient_name=data['patient_name'],
            patient_email=data['patient_email'],
            place=data['place'],
            date=data['date'],
            time=data['time'],
            contact_no=data['contact_no'],
            district=data['district']
        )
        return Response({'message': 'Appointment created successfully'}, status=201)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request',"error" : e}, status=500)




