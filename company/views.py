from rest_framework.response import Response
from rest_framework.views import APIView
from company.models import JobOpening
from tpc_api.models import Student, EligibleStudents
from tpc_api.views import GetData
import requests
import json
import ast



class AddJobOpening(APIView):

    def post(self, request):
        email = request.data['email']
        batch = request.data['batch']
        valid_till = request.data['valid_till']
        branch = request.data['branch']
        offers = GetData.getData(self, request, 'offers')
        tenth_percent = float(request.data['tenth_percent'])
        twelveth_percent= float(request.data['twelveth_percent'])
        diploma_percent = GetData.getData(self, request, 'diploma_percent', Decimal=True)
        be_percent = float(request.data['be_percent'])
        cgpa = float(request.data['cgpa'])
        notice = request.data['notice']
        live_kt = int(request.data['live_kt'])
        dead_kt = int(request.data['dead_kt'])
        gap = int(request.data['gap'])
        package = int(request.data['package'])
        jwt_roll_no = request.user.roll_no.strip()
        userRecord = Student.objects.get(roll_no=jwt_roll_no)

        if userRecord.groups.filter(name='Superuser') or userRecord.groups.filter(name='Company'):
            job_opening = JobOpening.objects.create(email=email, batch=batch, valid_till=valid_till, branch=branch, offers=offers, tenth_percent=tenth_percent, twelveth_percent=twelveth_percent, diploma_percent=diploma_percent, be_percent=be_percent, cgpa=cgpa, notice=notice, live_kt=live_kt, dead_kt=dead_kt, gap=gap, package=package)

            url = "http://tpc-backend-node.herokuapp.com/filter/notifstudents"
            payload = json.dumps({
                "gap": gap,
                "livekt": live_kt,
                "deadkt": dead_kt,
                "package": package,
                "be_percent": be_percent,
                "cgpa": cgpa,
                "tenth_percent": tenth_percent,
                "twelveth_percent": twelveth_percent
            })
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            eligibleStudentList = ast.literal_eval(response.text)['student_list']

            for roll_no in eligibleStudentList:
                student = Student.objects.get(roll_no=roll_no)
                EligibleStudents.objects.create(student=student, job_opening=job_opening)

            return Response({'status': 'Success'}, status=200)
        else:
            return Response({'status': 'Error', 'message': 'Insufficient Permissions to perform the request'}, status = 403)
