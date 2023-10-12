<<<<<<< HEAD

```
My_Diary
├─ accountsW
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ accounts
│  │     ├─ login.html
│  │     └─ signup.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ articles
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_comment.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ articles
│  │     ├─ create.html
│  │     ├─ detail.html
│  │     ├─ index.html
│  │     └─ update.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ crud
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ static
│  └─ css
└─ templates

```
=======
# Django BackEnd
Django를 활용하여 간단한 게시판을 만들어보았습니다(∗❛⌄❛∗)<br>
기본적인 게시글 작성, 조회, 수정, 삭제 기능 및 회원가입, 댓글 작성 기능을 구현하였습니다(22-10-11)


## 개발환경
- Python 3.12.0
- Django 4.2.6
- SQLite


## 프로젝트 구조
![file_tree](./README_img/file_tree.png)


## 프로젝트 API 요소
1. articles
```
- 전체 게시글 조회
- 게시글 생성
- 특정 게시글 조회
- 게시글 삭제 
- 게시글 수정
- 댓글 작성
- 댓글 삭제
```

2. accounts
```
- 로그인 
- 회원가입
- 로그아웃
- 회원탈퇴
```
>>>>>>> 8fb5481a570e87a8bb70c9924ed365dc101a352d
