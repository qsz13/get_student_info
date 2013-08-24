 # -*- coding: utf-8 -*
from HTMLParser import HTMLParser
from student import Stu_info

import sys

f=open('info.txt','a+')

class Parser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.name = self.stuID = self.gender = self.major =	self.ID = self.year = self.classnum = False
		self.genderTemp = False
		self.IDTemp = False
		self.stu_info = Stu_info()

	def handle_data(self, data):
		if self.name:
			self.name = False
			self.stu_info.name = data
			print >> f,"name:", data
			print "name:", data
		elif self.stuID:
			self.stuID = False
			self.stu_info.stuID = data
			print >> f, "stuID:", data
			print "stuID:", data
		elif self.gender:
			self.gender = False
			self.genderTemp = True
		elif self.genderTemp:
			self.genderTemp = False
			self.stu_info.gender = data
			print >> f, "gender:", data
			#print  "gender:", data
		elif self.major:
			self.major = False
			self.stu_info.major = data
			print >> f, "major:", data
			#print "major:", data
		elif self.ID:
			self.ID = False
			self.IDTemp = True
		elif self.IDTemp:
			self.IDTemp = False
			self.stu_info.ID = str(data)
			print >> f, "ID:", data
			#print "ID:", data
		elif self.year:
			self.year = False
			self.stu_info.year = data
			print >> f, "year:", data
			#print "year:", data
		elif self.classnum :
			self.classnum = False
			self.stu_info.classnum = data
			print >> f, "classnum:", data
			#print "classnum:", data

		elif data == '姓名':
			self.name = True
		elif data == '学号':
			self.stuID = True
		elif data == '性别(*)':
			self.gender = True
		elif data == '专业':
			self.major = True
		elif data == '身份证号(*)':
			self.ID = True
		elif data == '年级':
			self.year = True
		elif data == '班级':
			self.classnum = True

	def get_stu_info(self):
		return self.stu_info




if __name__ == '__main__':
	import webrequest,urllib2
	from HTMLParser import HTMLParser
	loginTemp = webrequest.Login("1252942")
	loginTemp.login()

	info_getter = webrequest.Info_getter()
	html = info_getter.get_html()

	parser = Parser()
	parser.feed(html)
