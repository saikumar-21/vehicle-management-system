import mysql.connector
import json
from datetime import datetime

class DBOperation():

    def __init__(self):
        # We have below explicitly given db username and password
        # self.mydb = mysql.connector.connect(host='localhost',user='vehicle_user',passwd = 'vehicle_password',
        #                                   database = 'vehicle_parking_miniproject')
        #Now we read username or password from json file
        file = open('./config.json', 'r')
        dataic = json.loads(file.read())
        file.close()
        self.mydb = mysql.connector.connect(host='localhost', user=dataic['username'], passwd=dataic['password'],
                                            database=dataic['database'])

    def createTables(self):
        # This function is used to create a table and datatypes to fields to it
        cursor = self.mydb.cursor()
        cursor.execute("DROP TABLE if exists admin")
        cursor.execute("DROP TABLE if exists slots")
        cursor.execute("DROP TABLE if exists vehicles")

        cursor.execute("CREATE TABLE admin (id int(255) AUTO_INCREMENT PRIMARY KEY,username varchar(30),password varchar(30),created_at varchar(30))")
        cursor.execute("CREATE TABLE slots (id int(255) AUTO_INCREMENT PRIMARY KEY,vehicle_id varchar(30),space_for int(25),is_empty int(25))")
        cursor.execute("CREATE TABLE vehicles (id int(255) AUTO_INCREMENT PRIMARY KEY,name varchar(30),mobile varchar(30),entry_time varchar(30),exit_time varchar(30),is_exit varchar(30),vehicle_no varchar(30),vehicle_type varchar(30),created_at varchar(30),updated_at varchar(30))")
        cursor.close()

    def InsertOneTimeData(self,space_two_wheeler,space_four_wheeler):
        # this function is used to create one time database entry for number of slots in parking lot
        cursor = self.mydb.cursor()
        for x in range(space_two_wheeler):
            cursor.execute("INSERT into slots(space_for,is_empty) VALUES ('2','1')")
            self.mydb.commit()

        for x in range(space_four_wheeler):
            cursor.execute("INSERT into slots(space_for,is_empty) VALUES ('4','1')")
            self.mydb.commit()
        cursor.close()

    def InsertAdmin(self,username,password):
        cursor=self.mydb.cursor()
        val=(username,password)
        cursor.execute("INSERT into admin (username,password) values (%s,%s)", val)
        self.mydb.commit()
        cursor.close()

    def doAdminLogin(self,username,passowrd):
        cursor = self.mydb.cursor()
        cursor.execute("select * from admin where username='"+username+"' and password='"+passowrd+"'")
        data = cursor.fetchall()
        cursor.close()
        if len(data)>0:
            return True
        else:
            return False

    def getslotspace(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM slots")
        data = cursor.fetchall()
        cursor.close()
        return data

    def getcurrentvehicle(self):
        # this function is used to get vehicle details which are currently parked from database
        cursor = self.mydb.cursor()
        # If vehicle is parked in any slot then is_exit will be 0
        cursor.execute("SELECT * FROM vehicles where is_exit = '0'")
        data = cursor.fetchall()
        cursor.close()
        return data

    def getallvehicle(self):
        # this function is used to get all vehicle details which were parked from database
        cursor = self.mydb.cursor()
        # If vehicle is parked in any slot then is_exit will be 0
        cursor.execute("SELECT * FROM vehicles where is_exit = '1'")
        data = cursor.fetchall()
        cursor.close()
        return data

    def add_vehicles_database(self, name, vehicle_no, mobile_no, vehicle_type):
        spaceid = self.spaceavailable(vehicle_type)
        if spaceid:
            print("in add_vehicle_database")
            current_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = (name, mobile_no, str(current_data), "", 0, vehicle_no, vehicle_type,str(current_data), str(current_data) )
            cursor = self.mydb.cursor()
            print('in try block')
            cursor.execute(
                "INSERT into vehicles (name,mobile,entry_time,exit_time,is_exit,vehicle_no,vehicle_type,created_at,updated_at) values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ",
                           data)
            self.mydb.commit()
            lastid = cursor.lastrowid
            cursor.execute("UPDATE slots set vehicle_id ='"+str(lastid)+"',is_empty='0'  where id ='"+str(spaceid)+"'")
            self.mydb.commit()
            cursor.close()
            return True
        else:
            return "No space available for parking"

    def spaceavailable(self, v_type):
        cursor = self.mydb.cursor()
        cursor.execute("select * from slots where is_empty = '1' and space_for='"+str(v_type)+"'")
        data = cursor.fetchall()

        if len(data)>0:
            # because slot id is in tuple we are acessing 1st element of tuple
            cursor.close()
            return data [0][0]
        else:
            cursor.close()
            return False

    def exitVehicle(self,id):
        cursor = self.mydb.cursor()
        current_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("UPDATE slots set is_empty='1', vehicle_id='' where vehicle_id='"+id+"'")
        self.mydb.commit()
        cursor.execute("UPDATE vehicles set is_exit ='1', exit_time ='"+current_data+"' where id ='"+id+"'")
#       cursor.execute("UPDATE vehicles set is_exit = '1', exit_time ='"+current_data+"' where id='" + id + "'")
        self.mydb.commit()
        cursor.close()
