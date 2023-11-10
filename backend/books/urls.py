from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("books", views.BookViewSet, basename="books")
router.register("authors", views.AuthorViewSet, basename="authors")
router.register("genres", views.GenreViewSet, basename="genres")

urlpatterns = router.urls
