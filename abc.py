#coding=utf-8
import  xml.dom.minidom

#sourcemonitor_path = top_dir 
#cmd=export sourcemonitor_path=" + sourcemonitor_path + ";wine " + sourcemonitor_path + " /C commands.xml"
#打开xml文档
dom = xml.dom.minidom.parse('result.xml')

#得到文档元素对象
root = dom.documentElement
m=root.getElementsByTagName('measure')

item=m[1].getElementsByTagName('item')
print(item)
for it in item:
	print(it.getAttribute("name"))
	tmp=it.getElementsByTagName('value')
	print(tmp[2].firstChild.data)
