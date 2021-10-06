from PyQt5.QtWidgets import (
	QWidget,
	QMainWindow,
	QPushButton,
	QLabel,
	QLineEdit,
	QVBoxLayout,
	QHBoxLayout,
	QFrame,
	QGridLayout,
	QComboBox,
	QTableWidget,
	QTableWidgetItem,
	QHeaderView
)
from PyQt5.QtCore import Qt, QTimer
from DataBaseOperation import DBOperation


class HomeScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Home")
		self.resize(1000, 700)
		widget = QWidget()
		widget.setStyleSheet("background:#000035")
		self.dboperation = DBOperation()

		layout_horizontal = QHBoxLayout()
		menu_vertical_layout = QVBoxLayout()

		self.btn_home = QPushButton('Home')
		self.btn_add_vehicle = QPushButton('Add Vehicle')
		self.btn_manage = QPushButton('Manage')
		self.btn_history = QPushButton('History')

		self.btn_home.setStyleSheet("width:200px;\n"
							   "height:160px;font:bold 30px;\n"
							   "background:#FEBE6B;color:#fff;\n"
							   "border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_add_vehicle.setStyleSheet("width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_manage.setStyleSheet("width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_history.setStyleSheet("width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")

		self.btn_home.clicked.connect(self.showHome)
		self.btn_add_vehicle.clicked.connect(self.showadd)
		self.btn_manage.clicked.connect(self.showManage)
		self.btn_history.clicked.connect(self.showHistory)

		menu_vertical_layout.addWidget(self.btn_home)
		menu_vertical_layout.addWidget(self.btn_add_vehicle)
		menu_vertical_layout.addWidget(self.btn_manage)
		menu_vertical_layout.addWidget(self.btn_history)
		menu_frame = QFrame()
		menu_frame.setLayout(menu_vertical_layout)
		menu_vertical_layout.addStretch()
		# menu_frame.setMaximumHeight(500)
		# menu_frame.setMinimumWidth(200)

		parent_vertical_layout = QVBoxLayout()

		self.vertical_1 = QVBoxLayout()
		self.addhomepagedata()

		self.vertical_2 = QVBoxLayout()
#		label_add_vehicle = QLabel('Add vehicle')
#		vertical_2.addWidget(label_add_vehicle)
		self.vertical_2.setContentsMargins(0, 0, 0, 0)
		self.addvehiclepage()

		self.vertical_3 = QVBoxLayout()
		self.vertical_3.setContentsMargins(0, 0, 0, 0)
		self.addmanagepage()

		self.vertical_4 = QVBoxLayout()
		self.addhistorypage()

		self.frame_1 = QFrame()
		self.frame_1.setMinimumWidth(self.width())
		self.frame_1.setMaximumWidth(self.width())
		self.frame_1.setMinimumHeight(self.height())
		self.frame_1.setMaximumHeight(self.height())
		self.frame_1.setLayout(self.vertical_1)

		self.frame_2 = QFrame()
		self.frame_2.setMinimumWidth(self.width())
		self.frame_2.setMaximumWidth(self.width())
		self.frame_2.setMinimumHeight(self.height())
		self.frame_2.setMaximumHeight(self.height())
		self.frame_2.setLayout(self.vertical_2)

		self.frame_3 = QFrame()
		self.frame_3.setMinimumWidth(self.width())
		self.frame_3.setMaximumWidth(self.width())
		self.frame_3.setMinimumHeight(self.height())
		self.frame_3.setMaximumHeight(self.height())
		self.frame_3.setLayout(self.vertical_3)

		self.frame_4 = QFrame()
		self.frame_4.setMinimumWidth(self.width())
		self.frame_4.setMaximumWidth(self.width())
		self.frame_4.setMinimumHeight(self.height())
		self.frame_4.setMaximumHeight(self.height())
		self.frame_4.setLayout(self.vertical_4)

		parent_vertical_layout.addWidget(self.frame_1)
		parent_vertical_layout.addWidget(self.frame_2)
		parent_vertical_layout.addWidget(self.frame_3)
		parent_vertical_layout.addWidget(self.frame_4)

		layout_horizontal.addWidget(menu_frame)
		layout_horizontal.addLayout(parent_vertical_layout)
		layout_horizontal.setContentsMargins(0, 0, 0, 0)
		parent_vertical_layout.setContentsMargins(0, 0, 0, 0)
		parent_vertical_layout.addStretch()
		layout_horizontal.addStretch()
		widget.setLayout(layout_horizontal)

		self.frame_1.show()
		self.frame_2.hide()
		self.frame_3.hide()
		self.frame_4.hide()

		self.setCentralWidget(widget)
	def showHistory(self):
		self.btn_home.setStyleSheet("width:200px;\n"
									"height:160px;font:bold 30px;\n"
									"background:#B5651D;color:#fff;\n"
									"border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_add_vehicle.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_manage.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_history.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#FEBE6B;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")

		self.frame_1.hide()
		self.frame_2.hide()
		self.frame_3.hide()
		self.frame_4.show()


	def showManage(self):
		self.btn_home.setStyleSheet("width:200px;\n"
									"height:160px;font:bold 30px;\n"
									"background:#B5651D;color:#fff;\n"
									"border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_add_vehicle.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_manage.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#FEBE6B;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_history.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")

		self.frame_1.hide()
		self.frame_2.hide()
		self.frame_4.hide()
		self.frame_3.show()

	def showadd(self):
		self.btn_home.setStyleSheet("width:200px;\n"
									"height:160px;font:bold 30px;\n"
									"background:#B5651D;color:#fff;\n"
									"border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_add_vehicle.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#FEBE6B;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_manage.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_history.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")

		self.frame_1.hide()
		self.frame_3.hide()
		self.frame_4.hide()
		self.frame_2.show()

	def showHome(self):
		self.btn_home.setStyleSheet("width:200px;\n"
									"height:160px;font:bold 30px;\n"
									"background:#FEBE6B;color:#fff;\n"
									"border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_add_vehicle.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_manage.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")
		self.btn_history.setStyleSheet(
			"width:200px;height:160px;font:bold 30px;background:#B5651D;color:#fff;border:1px solid white;border-radius:30px;border-style:ouset")

		self.frame_2.hide()
		self.frame_3.hide()
		self.frame_4.hide()
		self.frame_1.show()

	def addhomepagedata(self):
		self.vertical_1.setContentsMargins(0, 0, 0, 0)
		frame = QFrame()
		button = QPushButton('Refresh')
		button.setStyleSheet("background:#E1F74E;color:#000;padding:8px 0px;font-size:20px;border: 1px solid white")
		button.clicked.connect(self.refresh_home)

		vertical_layout = QVBoxLayout()
		vertical_layout.setContentsMargins(0, 0, 0, 0)
		horizontal = QHBoxLayout()

		label = QLabel('Home')
		label.setStyleSheet("color:#fff;font: bold 30px;width:500px;height:30px;padding:10px;text-align:center")
		horizontal.addWidget(label)
		vertical_layout.addLayout(horizontal)
		vertical_layout.addWidget(button)

		all_data = self.dboperation.getslotspace()
		print(all_data)
		self.gridlayout = QGridLayout()
		vertical_layout.addLayout(self.gridlayout)
		self.gridlayout.setContentsMargins(0, 0, 0, 0)
		self.gridlayout.setHorizontalSpacing(0)
		self.gridlayout.setVerticalSpacing(0)

		row = 0
		i=0
		# this for loop is to add grid to slot details
		for data in all_data:
			slot_button = QPushButton("Slot" + str(data[0])+" \n "+str(data[1]))

			if data[3] == 1:
				slot_button.setStyleSheet("background:#2FE46B;color:white;padding:5px;width 30px;height:50px;border: 1px solid white;text-align:center")
			else:
				slot_button.setStyleSheet("background:#FB5C4C;color:white;padding:5px;width 50px;height:50px;border: 1px solid white;text-align:center")

			if i%5 == 0:
				i = 0
				row = row+1
			self.gridlayout.addWidget(slot_button, row, i)
			i = i+1

		frame.setLayout(vertical_layout)
		self.vertical_1.addWidget(frame)
		self.vertical_1.addStretch()

	def refresh_home(self):
		# while loop is used to remove every label from gridlayout and again
		# fetch data frm database and add it into grid
		while self.gridlayout.count():
			child = self.gridlayout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()
		all_data = self.dboperation.getslotspace()
		row = 0
		i = 0
		# this for loop is to add grid to slot details
		for data in all_data:
			slot_button = QPushButton("Slot" + str(data[0]+" \n "+str(data[1])))

			if data[3] == 1:
				slot_button.setStyleSheet(
					"background:#2FE46B;color:white;padding:5px;width 30px;height:50px;border: 1px solid white;text-align:center")
			else:
				slot_button.setStyleSheet(
					"background:#FB5C4C;color:white;padding:5px;width 50px;height:50px;border: 1px solid white;text-align:center")

			if i % 5 == 0:
				i = 0
				row = row + 1
			self.gridlayout.addWidget(slot_button, row, i)
			i = i + 1

	def addvehiclepage(self):
		layout = QVBoxLayout()
		frame = QFrame()

		label = QLabel('Add Vehicle Details')
		label.setStyleSheet("color:#fff;font: bold 30px;width:500px;height:30px;padding:10px;text-align:center")

		self.name_label = QLabel('Name :')
		self.name_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.vehicle_no_label = QLabel('Vehicle Number :')
		self.vehicle_no_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.mobile_number_label = QLabel('Mobile Number :')
		self.mobile_number_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.vtype_label = QLabel("Vehicle type:")
		self.vtype_label.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.error_label = QLabel()
		self.error_label.setStyleSheet("color:#EF2D2D")

		self.name_input = QLineEdit()
		self.vehicle_no_input = QLineEdit()
		self.mobile_no_input = QLineEdit()
		self.name_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.vehicle_no_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.mobile_no_input.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px")
		self.vtype = QComboBox()
		self.vtype.setStyleSheet("color:#fff;padding:8px 0px;font-size:20px;border: 1px solid white")
		self.vtype.addItem("2 Wheeler")
		self.vtype.addItem("4 Wheeler")

		button = QPushButton("Add Vehicle")
		button.setStyleSheet("background:#E1F74E;color:#000;padding:8px 0px;font-size:20px;border: 1px solid white")

		layout.addWidget(label)
		layout.addWidget(self.name_label)
		layout.addWidget(self.name_input)
		layout.addWidget(self.vehicle_no_label)
		layout.addWidget(self.vehicle_no_input)
		layout.addWidget(self.mobile_number_label)
		layout.addWidget(self.mobile_no_input)
		layout.addWidget(self.vtype_label)
		layout.addWidget(self.vtype)
		layout.addWidget(self.error_label)
		layout.addWidget(button)

		layout.setContentsMargins(0, 0, 0, 0)
		frame.setMinimumWidth(self.width())
		frame.setMaximumWidth(self.width())
		frame.setMinimumHeight(self.height())
		frame.setMaximumHeight(self.height())

		layout.addStretch()
		frame.setLayout(layout)
		print('before button')

		button.clicked.connect(lambda: self.addvehicles(self.name_input.text(), self.vehicle_no_input.text(), self.vtype.currentIndex(),
						 self.mobile_no_input.text(), self.error_label))
		self.vertical_2.addWidget(frame)

	def checkvehicle(self):
		print('In check vehicles')

	def addvehicles(self, name, vehicle_no, index, mobile_no, error_label):
		print("in add vehicles")
		if (name == '') or (vehicle_no == ''):
			self.error_label.setText('Enter valid name,vehicle number, mobile number')
			return
		elif mobile_no == '':
			self.error_label.setText('Enter valid name,vehicle number, mobile number')
		else:
			vtp = 2
			if index == 0:
				vtp = 2
			else:
				vtp = 4

			data = self.dboperation.add_vehicles_database(name, vehicle_no, mobile_no, str(vtp))
			if data:
				error_label.setStyleSheet("color:green")
				error_label.setText('Added to database succesful')
			else:
				error_label.setStyleSheet("color:red")
				error_label.setText('Failed to add to database')

	def addmanagepage(self):
		data = self.dboperation.getcurrentvehicle()
		print(data)
		self.table1 = QTableWidget()
		self.table1.setStyleSheet("background:#fff")
		refresh_button = QPushButton("Refresh")
		refresh_button.setStyleSheet("background:#E1F74E;color:#000;padding:8px 0px;font-size:20px;border: 1px solid white")
		refresh_button.clicked.connect(self.refresh_manage)
		# Setting max column and row length
		print("about to set row and column length")
		self.table1.setRowCount(len(data))
		self.table1.setColumnCount(7)

		#
		self.table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		# table.setHorizontalHeaderItem is used to add header to tables like phone no,mobile no
		self.table1.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
		self.table1.setHorizontalHeaderItem(1, QTableWidgetItem('Name'))
		self.table1.setHorizontalHeaderItem(2, QTableWidgetItem('Vehicle Number'))
		self.table1.setHorizontalHeaderItem(3, QTableWidgetItem('Mobile Number'))
		self.table1.setHorizontalHeaderItem(4, QTableWidgetItem('Vehicle Type'))
		self.table1.setHorizontalHeaderItem(5, QTableWidgetItem('Entry Time'))
		self.table1.setHorizontalHeaderItem(6, QTableWidgetItem('Action'))

		loop = 0
		print("loop = 0")
		for smalldata in data:
			self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
			self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
			self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
			self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
			self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
			self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
			self.button_exit_managepage = QPushButton('Exit')
			self.button_exit_managepage.setStyleSheet("background:#E1F74E;color:#000;padding:8px 0px;font-size:20px")
			self.table1.setCellWidget(loop, 6, self.button_exit_managepage)
			self.button_exit_managepage.clicked.connect(self.exitcall)
			# setCellWidget(row,column,button_type) is used to create button at given row and column
			loop = loop +1
		print("after for loop")
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		frame = QFrame()
		layout.addWidget(self.table1)
		layout.addWidget(refresh_button)
		frame.setLayout(layout)
		frame.setContentsMargins(0, 0, 0, 0)
		frame.setMinimumWidth(self.width())
		frame.setMaximumWidth(self.width())
		frame.setMinimumHeight(self.height())
		frame.setMaximumHeight(self.height())
		self.vertical_3.addWidget(frame)
		self.vertical_3.addStretch()

	def refresh_manage(self):
		data = self.dboperation.getcurrentvehicle()
		self.table1.setRowCount(len(data))
		self.table1.setColumnCount(7)
		loop = 0
		print("starting loop in refresh manage")
		for smalldata in data:
			self.table1.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
			self.table1.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
			self.table1.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
			self.table1.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
			self.table1.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
			self.table1.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
			self.button_exit_managepage = QPushButton('Exit')
			self.table1.setCellWidget(loop, 6, self.button_exit_managepage)
			self.button_exit_managepage.setStyleSheet("background:#E1F74E;color:#000;padding:8px 0px;font-size:20px")
			self.button_exit_managepage.clicked.connect(self.exitcall)
			# setCellWidget(row,column,button_type) is used to create button at given row and column
			loop = loop +1

	def addhistorypage(self):
		data = self.dboperation.getallvehicle()
		print("History page:")
		print(data)
		self.table = QTableWidget()
		self.table.setStyleSheet("background:#fff")

		# Setting max column and row length
		print("about to set row and column length in history")
		self.table.setRowCount(len(data))
		self.table.setColumnCount(7)

		refresh_button = QPushButton("Refresh")
		refresh_button.setStyleSheet("background:#E1F74E;color:#000;padding:8px 0px;font-size:20px")
		refresh_button.clicked.connect(self.refresh_history)

		#
		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		# table.setHorizontalHeaderItem is used to add header to tables like phone no,mobile no
		self.table.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
		self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Name'))
		self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Vehicle Number'))
		self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Mobile Number'))
		self.table.setHorizontalHeaderItem(4, QTableWidgetItem('Vehicle Type'))
		self.table.setHorizontalHeaderItem(5, QTableWidgetItem('Entry Time'))
		self.table.setHorizontalHeaderItem(6, QTableWidgetItem('Exit at'))

		loop = 0
		print("starting loop in refresh history")
		for smalldata in data:
			self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
			self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
			self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
			self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
			self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
			self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
			self.table.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
			loop = loop +1
		print("after for loop")
		layout = QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		frame = QFrame()
		layout.addWidget(self.table)
		layout.addWidget(refresh_button)
		frame.setLayout(layout)
		frame.setContentsMargins(0, 0, 0, 0)
		frame.setMinimumWidth(self.width())
		frame.setMaximumWidth(self.width())
		frame.setMinimumHeight(self.height())
		frame.setMaximumHeight(self.height())
		self.vertical_4.addWidget(frame)
		self.vertical_4.addStretch()

	def refresh_history(self):
		self.table.clearContents()
		data = self.dboperation.getallvehicle()
		self.table.setRowCount(len(data))
		self.table.setColumnCount(7)
		loop = 0
		print("loop = 0")
		for smalldata in data:
			self.table.setItem(loop, 0, QTableWidgetItem(str(smalldata[0])))
			self.table.setItem(loop, 1, QTableWidgetItem(str(smalldata[1])))
			self.table.setItem(loop, 2, QTableWidgetItem(str(smalldata[6])))
			self.table.setItem(loop, 3, QTableWidgetItem(str(smalldata[2])))
			self.table.setItem(loop, 4, QTableWidgetItem(str(smalldata[7])))
			self.table.setItem(loop, 5, QTableWidgetItem(str(smalldata[3])))
			self.table.setItem(loop, 6, QTableWidgetItem(str(smalldata[4])))
			loop = loop + 1

	def exitcall(self):
		button = self.sender()
		if button:
			row = self.table1.indexAt(button.pos()).row()
			row_id = str(self.table1.item(row,0).text())
			self.dboperation.exitVehicle(row_id)
			self.table1.removeRow(row)
