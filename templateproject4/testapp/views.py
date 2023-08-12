from django.shortcuts import render
import datetime
# Create your views here.
def info_view(request):
    time=datetime.datetime.now()
    name='django'
    prerequites='python'
    my_dict={'time':time,'name':name,'prerequites':prerequites}
    return render(request, 'testapp/result.html', context=my_dict)
