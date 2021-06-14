from django.urls import include, path

from podio.views import podio, students, teachers

urlpatterns = [
    path('', include('podio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', podio.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]