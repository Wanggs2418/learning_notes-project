# 基于《Python编程：从入门到实践》的web项目实践

## 1.Web Application

借助 python 组件开发富应用程序 (rich application)—**Web 应用程序**

[Django](https://www.djangoproject.com/)：Web 框架，帮助开发交互式网站的工具。能够响应网页请求，轻松读写数据库，管理用户等。

[Django Model Field Reference](https://docs.djangoproject.com/en/5.0/ref/models/fields/)

[Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)



### 1.1 内容需求

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









