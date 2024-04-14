# render根据视图提供渲染响应
from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    # learning notes index page
    return render(request, 'learning_notes/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    # content 是一个字典，键：访问数据的名称，值：发送给模板的数据
    context = {'topics': topics}
    return render(request, 'learning_notes/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # -表示降序
    entries = topic.entry_set.order_by('-date_added')   
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_notes/topic.html', context)