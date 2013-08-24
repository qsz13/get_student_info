 # -*- coding: utf-8 -*
import urllib,urllib2,cookielib,re
class Login:

	login_url = 'http://sse.tongji.edu.cn/icss/login.aspx'
	viewstate = re.findall('<input[^>]*name=\"__VIEWSTATE\"[^>]*value=\"([^"]*)\"[^>]*>',urllib2.urlopen(login_url).read(),re.S)[0]


	def __init__ (self,stu_num,password = '222222'):
		self.stu_num = stu_num
		self.password = password


	def get_post_data(self):
		post_data = urllib.urlencode({
							  'ctl00$ScriptManagerAjax':'ctl00$ContentPlaceHolder1$UpdatePanel|ctl00$ContentPlaceHolder1$LoginButton',
							  '__EVENTTARGET':'',
							  '__EVENTARGUMENT':'',
							  '__VIEWSTATE':Login.viewstate,
							  'ctl00$Header$LoginBar$TextBoxUsername':'',
							  'ctl00$Header$LoginBar$TextBoxPassword':'',
							  'ctl00$ContentPlaceHolder1$StudentNo': self.stu_num,
							  'ctl00$ContentPlaceHolder1$Password':'222222',
							  '__ASYNCPOST':'true',
							  'ctl00$ContentPlaceHolder1$LoginButton':'登录'
                              })
		return post_data

	def login(self):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		opener.addheaders = [('User-agent', 'Opera/9.23')]
		urllib2.install_opener(opener)
		req = urllib2.Request(Login.login_url, self.get_post_data())
		conn = urllib2.urlopen(req)
		conn.close()


class Info_getter:
	info_url = 'http://sse.tongji.edu.cn/icss/MyInfo.aspx'

	def get_html(self):

		req2=urllib2.urlopen('http://sse.tongji.edu.cn/icss/MyInfo.aspx')
		content = req2.read()
		req2.close()
		return content






if __name__ == '__main__':
	loginTemp = Login("1252942")
	loginTemp.login()
	info_getter = Info_getter()
	info_getter.get_html()