from django.urls import path
from ..views import *

appointmenturl = [
    path('viewappointment/', viewAppointment, name="appointment-view"),
    path('deleteappointment<id>/', deleteAppointment, name="delete-appointment"),
    path('addappointmentUser/', addAppointmentUser, name="appointment-add-user"),
    
    path('viewuserappointment/', viewAppointment_UserSide, name="user-appointment-view"),
    path('adduserappointment/', addAppointment_UserSide, name="user-appointment-add"),
    path('addUserProfileAppointment/', addAppointment_UserProfile, name="user-profile-appointment-add"),
    
    path('docside-viewappointment/',docside_appointemnt,name="docside-viewappointment"),
    path('fix-appointment/<id>',fix_appointment,name="docside-fixappointment"),
    path('view-own-appointment',view_own_appointment,name="view-own-appointment"),
    
    path('download',download_csv,name='download')

]
