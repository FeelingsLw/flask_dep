from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask"

@app.route('/home')
def home():
    return '主页!!!'

'''
git init 初始化参数
git add file  增加要上传文件
-- 可选
    --   git config --global user.email "you@example.com"  设置上传的邮箱
    --   git config --global user.name "Your Name"  设置上传的用户名
git commit -m '备注信息'  提交修改到本地仓库
-- 可选
    -- git remote add origin https://github.com/FeelingsLw/flask_dep.git  # 设置要向哪个网络仓库上传

git push origin master  上传到网络仓库

'''