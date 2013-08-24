import webrequest
from parser import Parser
import output

for i in range(1252840,1253040):
	try:
		loginTemp = webrequest.Login(str(i))
		loginTemp.login()
		info_getter = webrequest.Info_getter()
		html = info_getter.get_html()
		parser = Parser()
		parser.feed(html)
		stu_info = parser.get_stu_info()
		output.output(stu_info)
		print i
	except:
		print 'error'
		continue