from django.urls import path
from .import views
from .views import UserAdd, ExpenseAdd

urlpatterns=[
   path('index/', views.index, name='index'),
   path('personindex/', views.person_index, name='per-index'),
   path('person/profile<int:id>/', views.per_profile, name='per-profile'),
   path('update/', views.per_update, name='per-update'),
   path('personadd/', UserAdd.as_view(), name='per-add'),
   path('delete/<int:id>/', views.per_delete, name='per-delete'),
   path('edit/<int:id>/', views.per_edit, name='per-edit'),
   path('personcard/<int:id>/', views.person_card, name='per-card'),

   path('expensecard/<str:person>/', views.expense_card, name='exp-card'),
   path('editexp/<int:id>/', views.exp_edit, name='exp-edit'),
   path('expupdate/', views.exp_update, name='exp-update'),
   path('expenseadd/', ExpenseAdd.as_view(), name='exp-add'),
   path('expenseindex', views.expense_index, name='exp-index'),
   path('expensedelete/<int:id>/', views.expense_delete, name='exp-delete'),
]