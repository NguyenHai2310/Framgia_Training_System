from django.conf.urls import include, url
from django.contrib import admin
from . import views
from framgia.views.admin.course import CourseList, CourseDetail, CourseUpdate, CourseDelete, CourseCreate
from framgia.views.admin.subject import SubjectCreate, SubjectDelete, SubjectDetail, SubjectList, SubjectUpdate
from permission import admin_required, login_required


urlpatterns = [

    url(r'^$', views.base.BaseIndexView.as_view(), name='base_index'),

    url(r'^course/(?P<pk>[0-9]+)/$', login_required(views.course.CourseDetailView.as_view()), name='course_index'),

    url(r"^user/course-learning/", views.user.user_learning_course, name="user_course_learning"),

    url(r"^admin/", include(admin.site.urls)),

    url(r"^login/", views.user.login_user, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name="logout"),
    url(r'^register/$', views.user.register, name="register"),
    url(r'^users/(?P<pk>\d+)/profile/$', login_required(views.user.ProfileDetail.as_view()), name="profile"),
    url(r'^users/(?P<pk>\d+)/edit/$', login_required(views.user.EditProfile.as_view()), name="editprofile"),

    url(r'^admin/courses/$', admin_required(CourseList.as_view()), name="course_index"),
    url(r'^admin/course/(?P<pk>\d+)/$', admin_required(CourseDetail.as_view()), name="course_detail"),
    url(r'^admin/course/(?P<pk>\d+)/edit/$', admin_required(CourseUpdate.as_view()), name="course_update"),
    url(r'^admin/course/(?P<pk>\d+)/delete/$', admin_required(CourseDelete.as_view()), name="course_delete"),
    url(r'^admin/course/new/$', admin_required(CourseCreate.as_view()), name="course_new" ),
    url(r'^admin/subjects/$', admin_required(SubjectList.as_view()), name="subject_index"),
    url(r'^admin/subject/(?P<pk>\d+)', admin_required(SubjectDetail.as_view()), name="subject_detail"),
    url(r'admin/subject/(?P<pk>\d+)/edit/$', admin_required(SubjectUpdate.as_view()), name="subject_update"),
    url(r'admin/subject/(?P<pk>\d+)/delete/$', admin_required(SubjectDelete.as_view()), name="subject_delete"),
    url(r'admin/subject/new/$', admin_required(SubjectCreate.as_view()), name="subject_new"),
]
