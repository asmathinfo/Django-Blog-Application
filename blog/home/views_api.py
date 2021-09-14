from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login


class LoginView(APIView):
    
    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Authantication went wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'Username not found'
                raise Exception('Username not found')
            
            if data.get('password') is None:
                response['message'] = 'Password not found'
                raise Exception('Password not found')

            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user is None:
                response['message'] = 'Invalid Username , User not found'
                raise Exception('Invalid Username , User not found')





            user_obj = authenticate(username = data.get('username') , password = data.get('password'))
            if user_obj:
                'login(request, user_obj)'
                response['status'] = 200
                response['message'] = 'Welcome to Blog App'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')



        except Exception as e :
            print(e)


        return Response(response)


    LoginView = LoginView.as_view()