# 应用程序的 URL 模式
from django.urls import path
from . import views
# 函数path和视图模块，.表示从当前的文件夹导入views

# app_name 用于区分不同文件夹下的同名文件
app_name = 'learning_notes'

# path接受3个参数
# 第一个参数帮助Django正确路由,空字符串与基础URL匹配
# 第二个参数调用view.py中的那个函数
# 第三个参数将URL的名称指定为index

urlpatterns = [
    # index
    path('', views.index, name='index'),
    # show all topics page
    path('topics/', views.topics, name='topics'),
    # show topics' entry
    # 调用视图函数 topic() 将 topic_id作为实参传递它
    path('topics/<int:topic_id>/', views.topic, name='topic')
]