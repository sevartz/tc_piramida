from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, PhotoSet, Block1, Block5_messages, Block2_Images, Block2, Block5_contacts


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Неверные учетные данные. Попробуйте еще раз.'
    else:
        error_message = ''
    return render(request, 'app/login.html',
                  {'error_message': error_message}
                  )


def add_photoset(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        photoset = PhotoSet.objects.create(name=name)
        return redirect('edit_photoset', photoset_id=photoset.id)
    else:
        return render(request, 'app/add_photoset.html')

def edit_photoset(request, photoset_id):
    photoset = PhotoSet.objects.get(pk=photoset_id)
    if request.method == 'POST':
        for file in request.FILES.getlist('photos'):
            Photo.objects.create(photoset=photoset, image=file)
        return redirect('index')
    else:
        return render(request, 'app/edit_photoset.html', {'photoset': photoset})

def index(request):
    #1
    block_1_text = Block1.inscription
    block_1_image = Block1.image

    #2
    block_2_images = Block2_Images.objects.all()
    block_2_text = Block2.objects.get(id=1).text
    block_2_title = Block2.objects.get(id=1).title

    #4
    photosets = PhotoSet.objects.all()
    lst = []
    nmbr = [int(i) for i in range(0, 100, 2)]

    for n in photosets:
        photoset_name_current = n.name
        photos_current = Photo.objects.filter(photoset=n)
        lst.append(photoset_name_current)
        lst.append(photos_current)

    if request.method == 'POST':
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message_subject = request.POST.get('message_subject')
        message_text = request.POST.get('message_text')

        Block5_messages.objects.create(message_text=message_text, message_name=message_name,
                                       message_subject=message_subject, message_email=message_email)

    return render(request, 'app/index.html', {
        'lst': lst,
        'nmbr': nmbr,
        'block_1_text': block_1_text,
        'block_1_image': block_1_image,
        'block_2_images': block_2_images,
        'block_2_text': block_2_text,
        'block_2_title': block_2_title,
    })

def block1_edit(request):
    B = get_object_or_404(Block1, id=1)
    text_block1 = B.text
    image_block1 = B.image
    if request.method == 'POST':
        if 'image' in request.POST:
            file = request.FILES.get('image_input')
            B.image = file
        if 'text' in request.POST:
            text = request.POST.get('text_input')
            B.inscription = text

        B.save()
        return redirect('index')

    return render(request, 'app/block1_edit.html', {
        'image_block1': image_block1,
        'text_block1': text_block1
    })

def block2_edit(request):
    images = Block2_Images.objects.all()
    B = Block2.objects.get(id=1)
    text_block2 = B.text
    title_block2 = B.title

    if request.method == 'POST':
        if 'add' in request.POST:
            title = request.POST.get('title')
            text = request.POST.get('text')
            image = request.FILES.get('image')

            if title != '':
                B.title = title
            if text != '':
                B.text = text
            if image:
                Block2_Images.objects.create(id=len(images)+1, image=image)
            B.save()

        for i in range(1, 11):
            if f'delete{i}' in request.POST:
                Block2_Images.objects.filter(id=i).delete()

    return render(request, 'app/block2_edit.html', {
        'images': images,
        'title_block2': title_block2,
        'text_block2': text_block2,
    })

def block5_edit(request):
    contacts = Block5_contacts.objects.all()
    if request.method == 'POST':
        if 'add' in request.POST:
            text = request.POST.get('text')
            Block5_contacts.objects.create(id=len(contacts)+1, text=text)
        for i in range(1, 30):
            if f'delete{i}' in request.POST:
                Block5_contacts.objects.filter(id=i).delete()
        return redirect('index')

    return render(request, 'app/block5_edit.html', {
        'contacts': contacts,
    })

def main(request):
    messages = Block5_messages.objects.all()

    return render(request, 'app/main.html', {
        'messages': messages,
    })
