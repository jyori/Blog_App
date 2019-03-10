from django.shortcuts import render
#list of dictionary
posted = [
    {
        'name': 'peace',
	    'author': 'jyoti',
	    'published': '28th jan',
	    'content': 'fndjnbdjkfvbdjkvndjkvb'	
    },
    {
	    'name':'justice',
	    'author':'gaurav',
	    'published':'June 6,2018',
	    'content':'fosjfipdkopdfepsfvjpidjwpdjaspo'
    }
]

#will handle traffic from homepage of our blog and willtake in request arguement
def home(request):
	context = {
	    'posts': posted
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request,'blog/about.html', {'title': 'About'})

