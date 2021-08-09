from django.apps import AppConfig

# 해당 애플리케이션에 대한 메타 정보를 저장하기 위한 클래스
# 앱 이름, 레이블, 별칭, 경로 등을 설정할 수 있으며, 이 중 이름은 필수 속성이다.
class BookmarkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookmark'
