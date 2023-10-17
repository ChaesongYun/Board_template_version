from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required


#  전체 게시글 조회
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# 특정 게시물 조회
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk) # 없으면 404 에러
    comment_form = CommentForm()
    comments = article.comments.all() # article에 해당되는 comments 출력
    hashtags = article.hashtags.all() # article에 해당되는 hashtags 출력
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
        'hashtags' : hashtags,
    }
    return render(request, 'articles/detail.html', context)


# 게시물 작성
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            # 통일성을 위해 
            # article.save()보단 form.save()로!
            form.save()

            for word in article.content.split(' '):
                if word[0] == '#':
                    # get_or_crate(): 첫번째 인자는 우리가 꺼내려고 하는 모델 객체
                    # 두번째 인자는 flag!! 생성되면 true, 아니면 false
                    hashtag, created = Hashtag.objects.get_or_create(content=word[1:])
                    article.hashtags.add(hashtag)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


# 게시물 삭제
@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk) 
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


# 게시물 수정
@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 게시물 작성자가 로그인된 유저라면
    if request.user == article.user:
        # POST 요청일 때
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        # GET 요청일 때
        else:
            form = ArticleForm(instance=article)
    
    # 게시물 작성자가 로그인된 유저와 다르다면
    else:
        return redirect('articles:detail', article.pk)
    
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


# 댓글 작성
@login_required
def create_comment(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save()
        return redirect('articles:detail', article.pk)

    context={
        'article' : article,
        'comment_form' : comment_form,    
    }
    return render(request, 'article/detail.html', context)


# 댓글 삭제
@login_required
def delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


# 게시글 좋아요
@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # get은 찾는 객체가 없다면 에러를 반환
    # +단일 객체를 반환
    # if request.user in article.like_users.all():
    # filter는 여러개의 객체가 담긴 QuerySet으로 반환
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')


# 해시태그
def hashtag(request, hash_pk):
    hashtag = Hashtag.objects.get(pk=hash_pk)
    articles = hashtag.articles.all()
    context = {
        'hashtag' : hashtag,
        'articles' : articles,
    }
    return render(request, 'articles/hashtag.html', context)