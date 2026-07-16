
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView
from book.views import BookDetailView, BookListView
from author.views import AuthorListView, AuthorDetailView
from user.views import RegistrationView, LoginView, logout_view
from django.contrib.auth import views as auth_views
from loan.views import loan_book, return_book, MyLoansView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<slug:slug>/', BookDetailView.as_view(), name='book_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book/<slug:slug>/loan/', loan_book, name='loan_book'),
    path('my-loans/', MyLoansView.as_view(), name='my_loans'),
    path('loan/<int:pk>/return/', return_book, name='return_book'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # Include django_browser_reload URLs only in DEBUG mode
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    
if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)