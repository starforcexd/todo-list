from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
app = Flask(__name__)
app.secret_key = 'lmfao'
con = mysql.connector.connect (
		host="SHOULD_BE_LOCALHOST_IG",
		user="YOUR_USER_NAME",
		password="YOUR_PASSWORD",
		database="YOUR_DATABASE_NAME"
	)
cursor = con.cursor()

if con.is_connected():	
	print(f'connected to database {con.database}')
else:
	print('Something went wrong', con.error())

@app.route('/usr/create', methods = ['POST', 'GET'])
def insert():
	if 'create' in request.form:
		new_list = request.form.get('list')
		sql = "INSERT INTO lists (list) VALUES (%s);"
		val = (new_list, )
		try:
			cursor.execute(sql, val)
			con.commit()
			flash('New list added!', 'alert')
		except mysql.connector.Error as error:
			print(f'something went wrong {error}')
	return render_template('create-todo.html')
"""
def view():
	if 'view' in request.form:
		sql = "SELECT * FROM lists;"
		try:
			cursor.execute(sql)
			row = cursor.fetchall()
			return render_template('create-todo.html', rows=row)
		except mysql.connector.Error as error:
			print(f'something went wrong {error}')
"""
@app.route('/usr/delete', methods = ['POST', 'GET'])
def delete():
	if request.method == 'POST':
		id = request.form.get('id')
		sql = 'DELETE FROM lists WHERE id = %s'
		val = (id,)
		try:
			cursor.execute(sql, val)
			con.commit()
			flash("deleted the task", "alert2")
		except mysql.connector.Error as error:
			print(f'something went wrong {error}')
	return render_template('delete-todo.html')


if __name__ == '__main__':
	app.run(debug=True)

