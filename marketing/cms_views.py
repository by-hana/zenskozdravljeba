from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import PageForm, PostForm, NavMenuForm, FooterForm
from .models import Page, Post, NavMenu, Footer
from .permissions import cms_admin_required


def _apply_action_status(form, request):
    action = request.POST.get('action')
    if action == 'draft':
        form.instance.status = 'draft'
    elif action == 'publish':
        form.instance.status = 'published'


@cms_admin_required
def dashboard(request):
    pages = Page.objects.all().order_by('-updated_at')[:5]
    posts = Post.objects.all().order_by('-updated_at')[:5]
    page_count = Page.objects.count()
    post_count = Post.objects.count()
    published_count = (
        Page.objects.filter(status='published').count() +
        Post.objects.filter(status='published').count()
    )
    draft_count = (
        Page.objects.filter(status='draft').count() +
        Post.objects.filter(status='draft').count()
    )
    return render(request, 'marketing/cms/dashboard.html', {
        'pages': pages,
        'posts': posts,
        'page_count': page_count,
        'post_count': post_count,
        'published_count': published_count,
        'draft_count': draft_count,
    })


@cms_admin_required
def page_list(request):
    pages = Page.objects.all().order_by('-updated_at')
    return render(request, 'marketing/cms/page_list.html', {'pages': pages})


@cms_admin_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            _apply_action_status(form, request)
            page = form.save()
            return redirect('cms-page-edit', page_id=page.id)
    else:
        form = PageForm()
    return render(request, 'marketing/cms/page_form.html', {'form': form, 'mode': 'create'})


@cms_admin_required
def page_edit(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'unpublish':
            page.status = 'draft'
            page.save(update_fields=['status', 'updated_at'])
            return redirect('cms-page-edit', page_id=page.id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            _apply_action_status(form, request)
            form.save()
            return redirect('cms-page-edit', page_id=page.id)
    else:
        form = PageForm(instance=page)
    return render(request, 'marketing/cms/page_form.html', {'form': form, 'mode': 'edit', 'page': page})


@cms_admin_required
def post_list(request):
    posts = Post.objects.all().order_by('-updated_at')
    return render(request, 'marketing/cms/post_list.html', {'posts': posts})


@cms_admin_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            _apply_action_status(form, request)
            post = form.save()
            return redirect('cms-post-edit', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'marketing/cms/post_form.html', {'form': form, 'mode': 'create'})


@cms_admin_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'unpublish':
            post.status = 'draft'
            post.save(update_fields=['status', 'updated_at'])
            return redirect('cms-post-edit', post_id=post.id)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            _apply_action_status(form, request)
            form.save()
            return redirect('cms-post-edit', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'marketing/cms/post_form.html', {'form': form, 'mode': 'edit', 'post': post})


@cms_admin_required
def navigation_edit(request):
    nav = NavMenu.objects.filter(name='Primary').first()
    footer = Footer.objects.first()
    if request.method == 'POST':
        nav_form = NavMenuForm(request.POST, instance=nav)
        footer_form = FooterForm(request.POST, instance=footer)
        if nav_form.is_valid() and footer_form.is_valid():
            saved_nav = nav_form.save(commit=False)
            if not saved_nav.name:
                saved_nav.name = 'Primary'
            saved_nav.save()
            footer_form.save()
            return redirect('cms-navigation')
    else:
        nav_form = NavMenuForm(instance=nav)
        footer_form = FooterForm(instance=footer)
    return render(request, 'marketing/cms/navigation.html', {
        'nav_form': nav_form,
        'footer_form': footer_form,
    })


@cms_admin_required
@require_POST
def page_delete(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    page.delete()
    return redirect('cms-page-list')


@cms_admin_required
@require_POST
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('cms-post-list')


@cms_admin_required
@require_POST
def page_toggle_status(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    page.status = 'draft' if page.status == 'published' else 'published'
    page.save()
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or 'cms-page-list'
    return redirect(next_url)


@cms_admin_required
@require_POST
def post_toggle_status(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.status = 'draft' if post.status == 'published' else 'published'
    post.save()
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or 'cms-post-list'
    return redirect(next_url)


@cms_admin_required
@require_POST
def upload_image(request):
    file = request.FILES.get('file')
    if not file:
        return JsonResponse({'error': 'No file provided'}, status=400)
    folder = request.POST.get('folder', 'cms')
    from .cloudinary_utils import upload_image as do_upload
    try:
        result = do_upload(file, folder=folder)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse(result)


@cms_admin_required
def ai_post_list(request):
    from .models import BlogPost
    posts = BlogPost.objects.all().order_by('-published_at', '-created_at')
    return render(request, 'marketing/cms/ai_post_list.html', {
        'posts': posts,
        'published_count': posts.filter(status='published').count(),
        'draft_count': posts.filter(status='draft').count(),
    })
