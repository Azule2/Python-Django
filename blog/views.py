from django.shortcuts import render


posts = [
{
	
	'author': 'CoreyMS',
	'title':'Blog post 1',
	'content': 'First post content',
	'date_posted':'August 27, 2020'
},
{
	
	'author': 'Azule',
	'title':'Blog post 2',
	'content': 'second post content',
	'date_posted':'july 31, 2022'
}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.HTML', context)                                                         

def about(request):
	return render(request,'blog/about.HTML', {'title': 'About'}) 