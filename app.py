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
    print(f"\nVas a actualizar {id}\n")
    prueba=requests.get(url+"/"+str(id))
    print(prueba)
    # return redirect('/')
    try:
        requests.put(url+"/"+str(id), json={"check": 1})
        print(url+"/"+str(id))
        return redirect('/')
    except:
        return redirect('/')


@app.route('/delete/<int:id>', methods=['GET'])
def delete_task(id):
    print(f"\nVas a borrar {id}\n")
    try:
        requests.delete(url+"/"+str(id))
        print(url+"/"+str(id))
        return redirect('/')
    except:
    
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
