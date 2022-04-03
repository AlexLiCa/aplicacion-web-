from flask import Flask
from flask import render_template, request, redirect
import requests


app = Flask(__name__)

url = "https://apilinares.herokuapp.com/api/tasks"


 
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        try:
            response = requests.get(url).json()['task']
        except:
            response = []
            print("error") 
    else:
        name = request.form["name"]
        print(name)
        try:
            requests.post(url, json={"name": name})
            return redirect('/')
        except:
            pass
    
    return render_template('index.html', tasks=response)

@app.route('/update/<int:id>', methods=['GET'])
def update_task(id):
    print(f"Vas a actualizar :{id}")
    return redirect('/')
    try:
        pass
    except:
        pass




if __name__ == '__main__':
    app.run(debug=True)