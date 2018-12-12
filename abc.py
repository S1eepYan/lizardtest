#coding=utf-8
import  xml.dom.minidom

#sourcemonitor_path = top_dir 
#cmd=export sourcemonitor_path=" + sourcemonitor_path + ";wine " + sourcemonitor_path + " /C commands.xml"
#打开xml文档
dom = xml.dom.minidom.parse('result.xml')

#得到文档元素对象
root = dom.documentElement
m=root.getElementsByTagName('measure')

for mm in m:
	if(mm.getAttribute("type")=="File"):
		mf=mm
label=mf.getElementsByTagName('label')
size=label.length
ind=0
for lab in label:
	if(lab.firstChild.data=='CCN'):
		# print(ind)
		break
	ind=ind+1

item=mf.getElementsByTagName('item')
print(item)
for it in item:
	print(it.getAttribute("name"))
	tmp=it.getElementsByTagName('value')
	print(tmp[ind].firstChild.data)


