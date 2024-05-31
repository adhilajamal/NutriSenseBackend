from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Patient

# @api_view(['GET'])
# def getPatientDetails(request):
#     try:
#         email = request.query_params.get('email')
#         if not email:
#             return Response({'message': 'Email parameter is required'}, status=400)
        
#         patient = Patient.objects.get(email=email)
#         patient_details = {
#             'user_name': patient.user_name,
#             'age': patient.age,
#             'gender': patient.gender,
#             'contact': patient.contact,
#             'email': patient.email,
#         }

#         return Response({'message': 'Success', 'patient_details': patient_details}, status=200)
#     except Patient.DoesNotExist:
#         return Response({'message': 'Patient not found'}, status=404)
#     except Exception as e:
#         print(e)  # Print the exception for debugging purposes
#         return Response({'message': 'An error occurred while processing your request'}, status=500)

# @api_view(['GET'])
# def get_all_patients(request):
#     try:
#         # Fetch all doctors
#         patients = Patient.objects.all()
        
#         # Serialize the doctor data
#         serialized_data = [
#             {
#                 'user_name': patient.user_name,
#                 'age': patient.age,
#                 'gender': patient.gender,
#                 'contact': patient.contact,
#                 'email': patient.email,
#                 'profile': patient.profile.url if patient.profile else None
#             } 
#             for patient in patients
#         ]
        
#         return Response({'patients': serialized_data}, status=200)
    
#     except Exception as e:
#         print(e)  # Print the exception for debugging purposes
#         return Response({'message': 'An error occurred while processing your request'}, status=500)

        
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



# @api_view(['GET'])
# def DoctorProfile(request):
#     try:
#         doctors = Doctor.objects.all()
#         serialized_data = [
#             {
               
#                 'email': doctor.email,
#                 'password': doctor.pwd
#                 # 'proof': doctor.proof.url if doctor.proof else None
#             } 
#             for doctor in doctors
#         ]
        
#         return Response({'doctors': serialized_data}, status=200)
    
#     except Exception as e:
#         print(e)  # Print the exception for debugging purposes
#         return Response({'message': 'An error occurred while processing your request'}, status=500)

