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
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return f"{self.text}"