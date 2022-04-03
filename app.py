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


@app.route('/update/<int:id>', methods=['GET', 'PUT'])
def update_task(id):
    print(f"\nVas a actualizar {id}\n")
    # return redirect('/')
    if request.method == 'GET':
        try:
            print(f"{id}")
            requests.put(url, json ={"check:":True})
            return redirect('/')
        except:
            return redirect('/')
    else:
        return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
