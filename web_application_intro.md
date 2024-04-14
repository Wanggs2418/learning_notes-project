# 基于《Python编程：从入门到实践》3 个项目的实践

- play games；
- data anlysis;
- web application;

## 1.Web Application

借助 python 组件开发富应用程序 (rich application)—**Web 应用程序**

[Django](https://www.djangoproject.com/)：Web 框架，帮助开发交互式网站的工具。能够响应网页请求，轻松读写数据库，管理用户等。

[Django Model Field Reference](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

[Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

### 1.1 制定规范

包含：

- 项目的目标：Leaning Notes Web 应用程序；

- 项目的功能：让用户记录感兴趣的主题，且可添加主题的学习条目；
- 项目的外观：主页包含对网站的描述，用户需要注册登录；
- 用户界面：用户登录后可创建新主题，新条目以及阅读已有条目等；



### 1.2 创建虚拟环境

**创建并安装 Django**

```cmd
# 安装并激活env
conda create --prefix=E:\python_env\LN_Env python=3.8
#删除虚拟环境
conda remove -p E:\python_env\LN_Env --all

# 安装Django（豆瓣源）
pip install Django -i https://pypi.douban.com/simple
# 清华源
pip install Django -i https://pypi.tuna.tsinghua.edu.cn/simple
```



### 1.3 创建项目(Project)

> Project: LN_project

#### 0.命令总结

```cmd
# 创建项目，注意 . 号不省略
django-admin startproject LN_project .
# 修改数据库(migrate)与当前项目状态匹配
python manage.py migrate
# 运行本地服务器，即可通过http://127.0.0.1:8000/访问
python manage.py runserver
```

#### 1.项目初始化目录

```cmd
# 创建项目，注意 . 号不省略
django-admin startproject LN_project .

code/
    manage.py
    LN_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

`settings.py`：使用 Django 与系统交互，管理项目；

`urls.py`：创建响应浏览器请求的网页；

`wsgi.py`：web server gateway interface，web 服务器网关。帮助 Django 提供它创建的文件；

#### 2.创建数据库

```cmd
# 修改数据库(migrate)与当前项目状态匹配
python manage.py migrate
```

- 准备好数据库，用于存储执行管理和身份验证任务所需的信息；
- 创建了 `db.sqlite3` 文件，SQLite 使用单个文件的数据库，用于编写简单应用程序；

#### 3.查看项目

```cmd
python manage.py runserver
```

- 检查是否正确地创建项目；
- 当前使用地 Django 版本及当前使用的文件名称；
- 项目的 URL: `http://127.0.0.1:8000/`，在本地计算机的端口 8000 上侦听请求；



### 1.4 创建应用程序(App)

> APP: learning_notes

**Django 由一系列应用程序组成，它们协同工作让项目成为一个整体。**

#### 1.初始化程序目录

```cmd
# 注意切换到 Django 所在的文件目录
# 搭建应用程序需要的基础设施
python manage.py startapp learning_notes
```

**项目目录**

```cmd
learning_notes/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

- `models.py`：定义应用程序中管理的数据；
- `admin.py`：
- `views.py`：

#### 2.创建模型

处理应用程序中储存的数据。

```python
from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/5.0/ref/models/fields/
class Topic(models.Model):
    # 字符属性，最大宽度200
    text = models.CharField(max_length=200)
    # 时间属性，自动设置为当前的时间和日期
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
```

#### 3.激活模型

`setting.py` 程序更改，自定义程序在默认程序之前，从而覆盖默认程序行为。

```python
INSTALLED_APPS = [
    # 添加自定义程序，在默认之前
    'learning_notes',
    # 默认生成的应用程序
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

使用 Django 修改数据库，存储与模型 Topic 有关的信息。

```cmd
python manage.py makemigrations learning_notes
```

- 确定修改数据库，存储与新模型相关联的数据；
- Django 创建一个 `0001_initial.py` 迁移文件，为新建立的模型 `Topic` 创建一个表；

```cmd
# 让Django修改数据库，与首次的命令基本相同
# 注意最后一行即可
python manage.py migrate
```

**总结**：修改数据的三个步骤

1. 修改 `models.py`；
2. 对 `learning_logs` 调用 `makemigrations`；
3. 让 `Django` 迁移项目；

#### 4.Django 管理网站

Django 建立管理网站供网站管理员使用，`http://localhost:8000/admin/`(保证 `python manage.py runserver` 的正常运行)。

**创建 superuser**

**superuser**：具备所有权限的用户

```cmd
python manage.py createsuperuser
name: wanggs
Email:
Password:
```

notes：Django 不存储输入的密码，而是根据密码生成一个哈希值。每次输入密码通过哈希值匹对完成身份验证。

**向管理网站注册模型**

对于自定义的模型，需要完成手动注册。在本次创建 `learning_notes` 时，Django 在 `models.py` 所在的目录中创建一个名为 `admin.py` 的文件。

```python
# admin.py
from django.contrib import admin
# 和models同级目录
from .models import Topic

# Register your models here.
# 手动注册自定义模型
admin.site.register(Topic)
```

#### 5.定义模型 Entry

**多个条目与同一主题相关，多对一的关系，定义模型 Entry**

```python
# models.py
class Entry(models.Model):
    """对于同一个主题中的多条记录"""
    # tpoic为foreignkey实例，外键是数据库术语，指向数据库中的另一条记录
    # 删除主题时，删除与之相关联的记录，级联删除(cascading delete)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # textfield实例，字段长度不限
    text = models.TextField()
    # 按照创建的先后顺序排列条目
    date_added = models.DateTimeField(auto_now_add=True)

    # 嵌套的Meta类存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'
    
    # 呈现的条目应该显示哪些信息，鉴于有的条目很长，则使用__str__()方法返回text的前50个字符
    def __str__(self):
        return f"{self.text[:50]}..."
```

**修改完 models.py 后再次使用三步骤中的后两步**

```cmd
# 生成新的迁移文件002_entry.py,修改数据库，使得其能够存储与entry有关的信息
python manage.py makemigrations learning_notes
# 注意观察迁移过程中是否异常
python manage.py migrate
```

#### 6.注册 Entry

向管理网站注册 Entry

```python
# admin.py
from django.contrib import admin
# 和models同级目录
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
```

#### 7.Django shell

对输入的数据以交互式终端查看，即 `Django shell`，**用于测试项目和排除故障**

`ctrl+z` + 回车—退出shell

```cmd
python manage.py shell
[in]:from learning_notes.models import Topic
[in]:Topic.objects.all()	# 获取Topic的所有实例
[out]:<QuerySet [<Topic: CS>, <Topic: Engineering>]>	# 查询集
[in]:topics = Topic.objects.all()

# 输出id和主题名称
[in]:for topic in topics:	
		print(topic.id, topic)
		
#通过id使用Topic.objects.get()方法获取对象及其属性
[in]:t = Topic.objects.get(id=4)
[in]:t.text
[in]:t.date_added

#获取与特定主题相关联的所有记录
[in]:t.entry_set.all()
```



### 1.5 创建网页(URL)

使用 Django 创建网页的步骤：

- 定义 URL，将请求与网站 URL 匹配，确定返回哪个网页；
- 编写视图，每个 URL 被映射到特定的视图，而视图函数使用模板渲染网页；
- 编写模板；

将 URL，视图，模板分离让参与者专注于自己擅长的方面：

- 数据库专家—模型；
- 程序员—视图代码；
- 前端人员—模板；



#### 1. 映射 URL

通过 URL 请求网页，其中主页的 URL 最重要。

- 默认 `urls.py` 在项目文件夹中；

```python
# LN_project\urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_notes.urls')),
]
```

- 需在应用程序文件夹下再创建一个 `urls.py`；

```python
# learning_notes\urls.py
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
]
```

#### 1.2 编写视图

视图函数接受请求中的信息，准备好生成网页所需的数据，将数据发送给浏览器。应用程序中的 `views.py` 是在创建应用程序时自动生成。

```python
# learning_notes\views.py
# render根据视图提供渲染响应
from django.shortcuts import render

# Create your views here.
def index(request):
    # learning notes index page
    return render(request, 'learning_notes/index.html')
```

#### 1.3 编写模板

```html
<!-- learning_notes/templates/learning_notes/index.html -->
<!-- 新建 index.html -->
<p>Learning Notes</p>
<p>学习笔记记录</p>
```

此时访问 `http://127.0.0.1:8000/` 可查看对应的网页。



#### 1.4 其他网页

两个网页：1.显示所有主题；2.显示与主题相关的所有条目，在此之前先创建一个父模板，其他模板都继承自它；

**对于每个网页，指定 URL 模式，编写视图函数，编写模板**

**父模板**

创建网站时，一些通用元素会出现在所有网页中，为避免重复书写，采用继承方法。**从而专注于每个模板的特性**。

- 创建包含项目名称的元素，使用标签模板，用花括号和百分号`{% %}`表示；
- `{% url 'learning_notes:index' %}`，表示 URL 与 `learning_notes/urls.py` 中定义的 `index` 的 URL 模式匹配，**其中 leanring_notes 是一个命名空间(由 urls.py 中的 app_name 得到)，index 是命名空间中一个独特的 URL 模式**；
- `{% block content %}{% endblock content %}` 为块标签，名称为 `content`，作为占位符，包含的信息由子模板指定；

```html
<!-- learning_notes/templates/learning_notes/base.html,父模板-->
<p>
    <a href="{% url 'learning_notes:index' %}">Learning Notes</a>
</p>

{% block content %}{% endblock content %}
```

**子模板**

重写 `index.html` ，继承 `base.html`

```html
{% extends 'learning_notes/base.html' %}

{% block content %}
<p>学习笔记记录</p>
{% endblock content %}
```

#### 1.5 显示所有topics

**URL 模式**

设定 `http://localhost:8000/topics` 显示所有的主题页面

```python
# http://localhost:8000/topics
# learning_notes\urls.py
urlpatterns = [
    # index
    path('', views.index, name='index'),
    # show all topics page
    path('topics/', views.topics, name='topics')
]
```

**视图**

- `topics()` 包含一个形参，Django 从服务器中收到 `request` 对象，查询数据库，根据属性排序，返回查询集给 `topics`；
- `content` 是一个字典，键：访问数据的名称，值：发送给模板的数据

```python
# learning_notes\views.py
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_notes/topics.html', context)
```

**模板**

`for` 循环的模板标签

```html
{% for item in list %}
	do somthing
{% endfor %}
```

- 变量用双括号表示；
- 模板标签 `{% empty %}` 表示 `topics` 为空则打印一条消息

```html
<!-- learning_notes/templates/learning_notes/topics.html,子模板-->
{% extends 'learning_notes/base.html' %}

{% block content %}
<p>Topics</p>
<ul>
    {% for topic in topics %}
    <li>{{topic.text}}</li>
    {% empty %}
    <li>No topics have been added yet?</li>
    {% endfor %}
</ul>
{% endblock content %}
```

修改父模板，使其包含所有 `topics` 的链接。

```html
<!-- learning_notes/templates/learning_notes/base.html,父模板-->
<p>
    <a href="{% url 'learning_notes:index' %}">Learning Notes:主页</a>
    <br>
    <a href="{% url 'learning_notes:topics' %}">Topics：学习的主题</a>
</p>

{% block content %}{% endblock content %}
```

#### 1.6 显示特定 topics 页面

显示特定的 `topic` 及其对应的记录 `entry`。

**URL 模式**

使用 `topic` 的 id 属性确定请求哪一个 `topic`，如 CS 对应的 id 为 1，则 URL 为`http://localhost:8000/topics/1/`

```python
# learning_notes\urls.py
# show topics' entry
path('topics/<int:topic_id>/', views.topic, name='topic')
```

**视图**

可以先通过 `python manage.py shell` 调试

```python
# debug
python manage.py shell
from learning_notes.models import Topic
topics = Topic.objects.all()
topic = Topic.objects.get(id=4) # CS
```

添加 `topic` 到 `views.py` 中：

```python
# learning_notes\views.py
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # -表示降序
    entries = topic.entry_set.order_by('-date_added')   
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_notes/topic.html', context)
```

**模板**

- 遍历 `view` 中 `content` 字典中的 `entries`；
- 每个 `entry` 列出两条信息：条目时间戳和完整的文本，时间戳对应 `date_added` 的值；
- 数线 `|` 表示过滤器，在渲染过程中对模板变量的值进行修改的函数；
- 过滤器 `date: 'M d, Y H:i'` 对应的时间格式为：`January 1,2022 23:00`；
- 过滤器 `linebreaks` 解释换行符，转换为浏览器能理解的格式；

```html
<!-- learning_notes/templates/learning_notes/topic.html,子模板-->
{% extends 'learning_notes/base.html' %}
{% block content %}
<p>Topic: {{topic.text}}</p>
<p>Entries:</p>
<ul>
    {% for entry in entries %}
    <li>
        <p>{{entry.date_added|date:'M d, Y H:i'}}</p>
        <p>{{entry.text|linebreaks}}</p>
    </li>
    {% empty %}
    <li>There are no entries for this topic yet.</li>
    {% endfor %}
</ul>
{% endblock %}
```

**将每个 topic 的链接添加到 topics 中**

```html
<!-- learning_notes/templates/learning_notes/topics.html,子模板-->

    <li><a href="{% url 'learning_notes:topic' topic.id %}">{{topic.text}}</a></li>
```





