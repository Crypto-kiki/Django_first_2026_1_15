# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     # path("", include("polls.urls")),
#     # http://127.0.0.1:8000
    
#     path("polls/", include("polls.urls")),
#     # http://127.0.0.1:8000/polls/

#     path("accounts/", include("accounts.urls")),
#     path("accounts/", include("django.contrib.auth.urls")), # 장고 기본 제공 인증 URL
# ]


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 루트("/")로 접속하면 polls 앱이 바로 뜨도록
    path("", include("polls.urls")),

    # 기존대로 /polls/ 경로도 유지
    path("polls/", include("polls.urls")),

    # 관리자 페이지
    path("admin/", admin.site.urls),
]
