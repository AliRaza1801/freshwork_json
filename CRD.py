import json
class fileop:

	#create file with name given by user
	def createfile(filename,key,value):
		jvalue=json.dumps(value)
		crtdict=dict()
		crtdict['{}'.format(key)]=jvalue
		with open(filename) as rdfile:
			for linerd in rdfile:
				rddata=json.loads(linerd)
				if list(rddata.keys())[0]==key:
					return 'Key is already there in data'
		crtfile=open(filename,'a')
		json.dump(crtdict,crtfile)
		crtfile.write('\n')
		crtfile.close()
		return 'successful'

	#read text from file
	def readfile(filename,key):
		with open(filename) as rdfile:
			rdfile.seek(0)
			for linerd in rdfile:
				rddata=json.loads(linerd)
				if list(rddata.keys())[0]==key:
					return list(rddata.values())[0]
		return 'Given Key does not exists'

	#delete text from file
	def deletetext(filename,key):
		with open(filename,"r+") as opfile:
			dlline=opfile.readlines()
			opfile.seek(0)
			lcount=0
			while(lcount!=len(dlline)):
				if dlline[lcount].startswith("{"+'"{}"'.format(key)):
					del dlline[lcount]
				else:
					lcount+=1
			opfile.truncate(0)
			for nwlines in dlline:
				opfile.write(nwlines)

#print(fileop.createfile('check.txt','A',{'a':1,'b':2}))
#print(fileop.createfile('check.txt','B',{'b':1,'c':2}))
#print(fileop.createfile('check.txt','C',{'c':1,'d':2}))
#print(fileop.readfile('check.txt','C'))
#print(fileop.readfile('check.txt','B'))
#print(fileop.readfile('check.txt','D'))
#fileop.deletetext('check.txt','A')
#print(fileop.readfile('check.txt','A'))
