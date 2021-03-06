from flask import request, redirect, url_for, render_template, flash, session
from household import app

@app.route('/')
def show_entries():
  return render_template('entries/index.html')


@app.route('/information')
def information():
  return render_template('entries/information.html')


@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      print('ユーザー名が異なります')
    elif request.form['password'] != app.config['PASSWORD']:
      print('パスワードが異なります')
    else:
      return redirect('entries/house.html')
  return render_template('entries/login.html')


@app.route('/logout')
def logout():
  return redirect('/')