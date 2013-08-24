import csv
import sys
import student

f=open('info.csv','a+')

def output(stu_info):
	id = '="'+stu_info.ID+'"'
	stu_info_out = (stu_info.stuID,stu_info.name,stu_info.gender,stu_info.major,id,stu_info.year,stu_info.classnum)

	writer = csv.writer(f)
	writer.writerow(stu_info_out)