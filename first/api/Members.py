from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Doctor , Patient
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def loginUser(request):
    data= request.data
    try:
        email = data['email']
        pwd = data['pwd']

        if email is None or pwd is None:
            return Response({'message': 'Email and password are required'})
        
        patient = Patient.get_by_email_and_password( email, pwd)
        if patient:
            return Response({'message' : 'Succes', 'role' : 'Patient','email' : patient.email}, status=200)
        else:
            if Patient.get_by_email(email):
               return Response({'message' : 'Incorrect Password'},status=401)
            # Member not found
            doctor = Doctor.get_by_email_and_password( email, pwd)
            
            if doctor:
              if not doctor.doctorverify:
                return Response({'message' : 'User not verified'},status=403)
              return Response({'message' : 'Succes', 'role' : 'Doctor','email' :doctor.email}, status=200)
            
            if Doctor.get_by_email(email):
               return Response({'message' : 'Incorrect Password'},status=401)
            
            return Response({'message' : 'User not found' },status=404)
 
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)

@api_view(['POST'])
def DoctorRegistration(request):
    
    try:
        data = request.data 
        # print('data',data)
        
        if not data.get('user_name'):
            return Response({'message': "Value not found username"},status=404)
        if not data.get('email'):
            return Response({'message': "Value not found email"},status=404)
        if not data.get('pwd'):
            return Response({'message': "Value not found password"},status=404)
        if Doctor.get_by_email(data['email']):
            return Response({'message' : 'Email already exist'},status=501)
        if Patient.get_by_email(data['email']):
            return Response({'message' : 'Email already exist'},status=501)
        
        
        
        Doctor.objects.create( #insert into
            user_name=data['user_name'],
            age = data['age'],
            gender = data['gender'],
            contact = data['contact'],
            email=data['email'],
            pwd=data['pwd'],
            about=data['about'],
            address=data['address'],
            district=data['district'],
            workingtime=data['workingtime'],
            qualification=data['qualification']
        )
        return Response({'message': 'Successfully Registered'},status=200)
    
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)
    
@api_view(['POST'])
def PatientRegistration(request):
    
    try:
        data = request.data 
        # print('data',data)
        
        if not data.get('user_name'):
            return Response({'message': "Value not found username"},status=404)
        if not data.get('email'):
            return Response({'message': "Value not found email"},status=404)
        if not data.get('pwd'):
            return Response({'message': "Value not found password"},status=404)
        if Patient.get_by_email(data['email']):
            return Response({'message' : 'Email already exist'},status=500)
        if Doctor.get_by_email(data['email']):
            return Response({'message' : 'Email already exist'},status=500)
        
        
        
        Patient.objects.create( #insert into
            user_name=data['user_name'],
            age = data['age'],
            gender = data['gender'],
            contact = data['contact'],
            email=data['email'],
            pwd=data['pwd'],
        )
        return Response({'message': 'Successfully Registered'},status=200)
    
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)
    
@api_view(['POST'])
def logoutUser(request):
    try:
        token_key = request.headers.get('Authorization').split(' ')[1]
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response({'message': 'Logged out successfully'}, status=200)
    except (Token.DoesNotExist, AttributeError, IndexError):
        return Response({'message': 'Invalid token'}, status=400)
    except Exception as e:
        print(e)  # Print the exception for debugging purposes
        return Response({'message': 'An error occurred while processing your request'}, status=500)

    
    

# step1-start
# step2-signup api call
# step3-if values exist,return
#     else stop
# step4-if duplicate email
#      stop
#     else
# step5-patient object creation