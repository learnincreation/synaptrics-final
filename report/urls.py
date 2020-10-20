from . import views
from django.urls import path

from . import views 
from .views import * 

urlpatterns = [
    path('home/', views.home , name = 'report-home' ),
    path('drlist/', views.AllDrList , name = 'drlist' ),
    path('drlistpdf/', views.AllDrList_pdf.as_view() , name = 'drlistpdf' ),
    path('chemistlistpdf/', views.AllChemistList_pdf.as_view() , name = 'chemistlistpdf' ),

    path('chemistlist/', views.AllChemistList , name = 'chemistlist' ),
    path('directhr/', views.DirectHR, name = 'direct-hr'),
  	path('leavehr/', views.LeaveHR, name = 'leave-hr'),
    path('leavehrpdf/', views.Leave_pdf.as_view(), name = 'leavehrpdf'),
    path('leavelist/', views.LeaveList, name = 'leavelist'),
    path('master-doctor-list/', views.Doctor_Master_List, name = 'masterdrlist'),
    path('chemist-doctor-list/', views.chemist_Master_List, name = 'masterchemlist'),
    path('daily-activites/', views.dailyactivites, name = 'dailyactivites'),
    path('field-activites/', views.FieldActivites, name = 'fieldactivites'),
    path('FieldActivites_pdf/', views.FieldActivites_pdf.as_view(), name = 'FieldActivites_pdf'),

    path('se_fieldactivity_pdf/', views.se_fieldactivity_pdf, name = "se_fieldactivity_pdf"),

    path('daily-dr-call/', views.DailyDrcallReportview, name = 'dailydrcall'),
    path('daily-dr-meeting-report/', views.DailyDrMeetingReportview, name = 'dailydrmeetingreport'),
    path('daily-chemist-callReport-view/', views.DailyChemistcallReportview, name = 'dailychemistmeetingreport'),
     path('daily-chemist-callReport-profile/', views.ChemistcallReport_Profile, name = 'chemistcallreport-profile'),
      path('daily-chemist-callReport-pdf/', views.ChemistcallReport_pdf.as_view(), name = 'chemistcallreport-pdf'),
    path('otheractivites/', views.OthersActivity, name = 'otheractivites'),
     path('otheractivitesview/', views.OthersActivityView, name = 'OthersActivityView'),
    path('monthlyplan/', views.Monthlyplanview, name = 'month-planing'),
    path('monthlyplanlist/', views.MonthlyplanList, name = 'month-planlist'),
      path('monthlyplanpdf/', views.Monthlyplan_pdf.as_view(), name = 'monthlyplanpdf'),
   path('meetingactivites/', views.MeetingActivites, name = 'meetingactivites'),
    
    path('MeetingActivites_pdf/', views.MeetingActivites_pdf.as_view(), name = 'MeetingActivites_pdf'),
    path('MeetingActivites_pdfprofile/', views.MeetingActivites_pdfprofile, name = 'MeetingActivites_pdfprofile'),
    path('workfromhomeactivites/', views.WorkFromHomeActivites, name = 'workfromhomeactivites'),
    path('covidactivites/', views.covidActivites, name = 'covidactivites'),
    path('admindayactivites/', views.AdminDayActivites, name = 'admindayactivites'),
    path('expensesreport/', views.ExpensesView , name = 'expenses-report' ),
    path('expensespdf/', views.Expenses_pdf.as_view() , name = 'expensespdf' ),
     path('expensesprofile/', views.Expenses_pdf_profile , name = 'expensesprofile' )
  
 #   path('dailyplan/', views.DailyplanView.as_view() , name = 'dailyplan-report' ),
  # 	path('drvisitreport/', views.DrvisitreportView.as_view() , name = 'drvisitreport-report' ),
   	
   	#path('dailyworkingreport/', views.DailyworkingreportView.as_view() , name = 'dailyworkingreport-report' ),
   	#path('chemistcallreport/', views.ChemistcallreportView.as_view() , name = 'chemistcall-report' ),
   	#path('daysummaryreport/', views.DaysummaryreportView.as_view() , name = 'daysummary-report' ),
   	#path('rcpareport/', views.RcpadetailsView.as_view() , name = 'rcpa-report' ),
   	#path('doctorvisitreport/', views.DoctorvisitView.as_view() , name = 'doctorvisit-report' ),
   	#path('hqlist/', views.HQView.as_view() , name = 'hq-report' ),
   	#path('chemistlist/', views.chemistlist.as_view() , name = 'chemist-list' ),



]


