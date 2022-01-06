# Start import
import json
import codes
from flaskext.mysql import MySQL
# End import

def exportDataFromCursor(cursor):
	try:
		row_headers=[x[0] for x in cursor.description]
		rv = cursor.fetchall()
		json_data=[]
		for result in rv:
			json_data.append(dict(zip(row_headers,result)))
		return json_data
	except Exception as e:
		codes.printException(e)
		return(False)

def insertQuery(connection, sql):
	try:
		cursor = connection.cursor()
		cursor.execute(sql)
		connection.commit()
		return(True)
	except Exception as e:
		codes.printException(e)
		return(False)

def selectQuery(connection, sql):
	try:
		cursor = connection.cursor()
		cursor.execute(sql)
		data = exportDataFromCursor(cursor)
		if not data:
			return (False)
		http_response = {"Message": "success", "Status code": "200"}
		data = {"Response": http_response, "data": data}
		return json.dumps(data, sort_keys=True, default=str)
	except Exception as e:
		codes.printException(e)
		return False

def connectToDB(mysql):
	try:
		conn = mysql.connect()
		return conn
	except Exception as e:
		codes.printException(e)
		return False