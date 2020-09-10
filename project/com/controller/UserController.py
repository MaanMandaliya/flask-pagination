from flask import render_template, request
from project import app
from project.com.dao.UserDAO import UserDAO

@app.route('/', methods=['GET'])
def home():
    try:
        page = request.args.get('page',1,type=int)
        per_page = request.args.get('per_page',10, type=int)
        userDAO = UserDAO()
        results = userDAO.viewUsers(page,per_page)
        return render_template('home.html',results=results)
    except Exception as ex:
        print(ex)
