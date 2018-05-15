from eve import Eve
import psycopg2
import json

app = Eve()

@app.route('/plans')
def getPlanOptions():

	conn = psycopg2.connect(database="insurer_one", host = "localhost")
	cur = conn.cursor()

	sql = "SELECT * FROM plans;"
	cur.execute(sql)
	rows = cur.fetchall()

	cur.close()
	conn.close()

	return json.dumps(rows)

@app.route('/add-customer/<planId>/<passportNumber>/<name>/<email>/<address>')
def addCustomer(planId, passportNumber, name, email, address):
	
	conn = psycopg2.connect(database="insurer_one", host = "localhost")
	cur = conn.cursor()

	sql = "INSERT INTO customers (planId, passportNumber, name, email, address, paid) VALUES (%s, %s, %s, %s, %s, FALSE);"
	cur.execute(sql, (planId, passportNumber, name, email, address))

	conn.commit()

	cur.close()
	conn.close()

	return json.dumps({})

@app.route('/pay')
def pay(passportNumber):
	# Needs to find the customer with a given passport number, and update that record to be TRUE to signify that it has been paid for
	return

@app.route('/query-plan')
def queryPlan(passportNumber):
	# Needs to return all data on a specific customer given their passport number
	return

@app.route('/has-plan/<passportNumber>')
def hasPlan(passportNumber):

	conn = psycopg2.connect(database="insurer_one", host = "localhost")
	cur = conn.cursor()

	sql = "SELECT * FROM customers WHERE passportNumber='{0}';".format(passportNumber)
	cur.execute(sql)
	rows = cur.fetchall()

	if cur.rowcount > 0:
		hasPlan = True
	else:
		hasPlan = False

	cur.close()
	conn.close()

	return json.dumps({'result': hasPlan})

if __name__ == '__main__':
	app.run(debug=True)