#!/usr/bin/env python
from flask import Flask, render_template, request, url_for
from vietlott import vietlott645, vietlott655, vietlott3D, vietlott4D, vietlott4DMax

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        vietlott_type = [{'name':'Vietlott 6/45'}, {'name':'Vietlott 6/55'}, 
            {'name':'Vietlott 3D'}, {'name':'Vietlott 4D'}, {'name':'Vietlott 4D Max'}])


@app.route("/result" , methods=['GET', 'POST'])
def result():
    select = request.form.get('vietlott_select')
    if select == "Vietlott 6/55":
        result = vietlott655()
        return(str(select) + " combination: " + result) # just to see what select is
    
    if select == "Vietlott 6/45":
        result = vietlott645()
        return(str(select) + " combination: " + result)
    
    if select == "Vietlott 3D":
        result = vietlott3D()
        return(str(select) + " combination: " + result)
    
    if select == "Vietlott 4D":
        result = vietlott4D()
        return(str(select) + " combination: " + result)

    if select == "Vietlott 4D Max":
        result = vietlott4DMax()
        return(str(select) + " combination: " + result)

if __name__=='__main__':
    app.run(host= '0.0.0.0', debug=True)