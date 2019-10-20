from flask import Flask, url_for, render_template, request, redirect
from quanlyhoadon import danhsachhanghoa, danhsachloaihanghoa, lop_hanghoa

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/loaihanghoa/')
def loaihanghoa():
    return redirect('/loaihanghoa/list')

@app.route('/loaihanghoa/list')
def loaihanghoa_list():
    obj = danhsachloaihanghoa
    len_obj = len(obj)
    return render_template('loaihanghoa/list.html', list_items=obj, len_obj=len_obj+1)

@app.route('/loaihanghoa/read')
def loaihanghoa_read():
    id = request.args.get('id', '')

    ### Get thong tin loai hang hoa tu file ####
    obj = []
    for hanghoa in danhsachhanghoa:
        dict_obj = {}
        for loaihanghoa in danhsachloaihanghoa:
            if hanghoa['loaihanghoa_id'] == loaihanghoa['id']:
                dict_obj['id'] = hanghoa['id']
                dict_obj['name'] = hanghoa['ten']
                dict_obj['id_loaihanghoa'] = hanghoa['loaihanghoa_id']
                obj.append(dict_obj)
    return render_template('loaihanghoa/read.html', list_items=obj, id=id)

@app.route('/loaihanghoa/update', methods=['POST', 'GET']) 
def loaihanghoa_update():
    if request.method == 'POST':
        new_name =  request.form['new_name']
        id = request.form['id']

        file_write = open("../danhmuc/loaihanghoa.csv", "w")
        for loai in danhsachloaihanghoa:
            if id == loai['id']:
                loai['ten'] = new_name
            str_to_save = loai['id'] + "#" + loai['ten'] + '\n'
            file_write.write(str_to_save)
        return redirect('/loaihanghoa/list')
    if request.method == 'GET':
        return render_template('loaihanghoa/update.html')

@app.route('/loaihanghoa/delete', methods=['POST', 'GET'])
def loaihanghoa_delete():
    if request.method == 'GET':
        return render_template('loaihanghoa/delete.html')
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
    
        file_write = open("../danhmuc/loaihanghoa.csv", "w")
        for loai in danhsachloaihanghoa:
            if id == loai['id']:
                del loai['id']
            else:
                str_to_save = loai['id'] + "#" + loai['ten'] + '\n'
                file_write.write(str_to_save)
        return redirect('/loaihanghoa/list')

@app.route('/loaihanghoa/create', methods=['POST', 'GET'])
def loaihanghoa_create():
    if request.method == 'POST':
        data = {}
        id = request.form['id']
        name = request.form['name']

        str_to_save = id + "#" + name + '\n'
        with open('../danhmuc/loaihanghoa.csv', 'a') as f:
            data = f.write(str_to_save) 

        return redirect("/loaihanghoa/list")
    if request.method == 'GET':
        return render_template("loaihanghoa/create.html")
########### End of thong tin loai hang hoa ##########

@app.route('/test')
def index():
    currency_from = currency_to = {
        'USD':10,
        'EUR':20,
        'ZAR':30,
        'GBP':40
    }
    currencies = ['USD', 'EUR', 'ZAR', 'GBP']
    rate = 10
    return render_template("test.html", currency_from=currency_from, currency_to=currency_to,
    rate=rate, currencies=sorted(currencies))

    return render_template("test.html")