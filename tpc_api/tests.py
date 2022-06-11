from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from auth_api.groups import CustomGroups
from tpc_api.models import Student
import tempfile


# Class for AddStudent and ViewStudent APIs
class AddViewStudent(APITestCase):

    def setupFunction(self):  # Helper Function to register a student for the very first time
        CustomGroups.getOrCreateGroups()  # Create the groups
        data = {
            "roll_no": "19CE1065",
            "rait_email": "rah.jad.rt19@rait.ac.in",
            "password": "11012002",
            "role": "Student"
        }
        self.client.post("/auth/dummyStudentSignUp/", data)

    def test_addStudent(self):
        self.setupFunction()  # Creates a new student entry
        student = Student.objects.get(roll_no="19CE1065")
        accessToken = str(RefreshToken.for_user(student).access_token)  # Generate a jwt token for the respective student
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + accessToken)  # Set the jwt token in the header
        data = {
            "roll_no": "19CE1065",
            "first_name": "Joe",
            "middle_name": "John",
            "last_name": "Doe",
            "email": "john@gmail.com",
            "phone_number": "1234567890",
            "gender": "M",
            "github": "githuburl",
            "linkedin": "linkedinurl",
            "no_of_offers": "0",
            "password": "11012002",
            "photo": tempfile.NamedTemporaryFile(suffix=".jpg").name,
            "department": "CE",
            "batch": "2023",
            "rait_email": "joh.doe.rt19@gmail.com" 
        }
        response = self.client.post("/addStudent/", data)  # Call AddStudent API with the data
        self.assertEqual(response.status_code, status.HTTP_200_OK)   # Check if the response is 200 OK 
        
    def test_viewStudent(self):
        self.test_addStudent()  # Create a new student entry to view later on
        student = Student.objects.get(roll_no="19CE1065")
        accessToken = str(RefreshToken.for_user(student).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + accessToken)
        data = {
            "roll_no": "19CE1065"
        }
        response = self.client.post("/viewStudent/", data)  # Call ViewStudent API
        print(response.data)  # Check the API response
        self.assertEqual(response.status_code, status.HTTP_200_OK)