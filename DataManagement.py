
class DataMng():
	"""this class contain functions for data management"""

	def formatChk(fp):
		"""
		this function is checking the format of file and pass the format as string.
		"""
		if(type(fp)==str):
			stForm=''
			form = fp.split('.')
			stForm = form[1]
		return stForm

	def csvRead(fp):
		"""
			this function is reading the csv and passing the string content of it.
		"""
		data=''
		frm = DataMng.formatChk(fp)
		if(frm == 'csv'):
			try:
				with open(fp) as f:
					data = f.read()
					f.close()
					pass
			except:
				print('there is a problem to read the file!')
		return data
	def csvRw(fp):
		"""
			this function returning each row of csv in a list.
			(separating each lines of the csv file)
		"""
		dataArr=[]
		frm = DataMng.formatChk(fp)
		if(frm == 'csv'):
			data = DataMng.csvRead(fp)
			try:
				dataArr = data.splitlines()
			except:
				print('there is problem to spliting lines!')
		else:
			print('make sure about your file format!')
		return dataArr


	def csvIndx(fp):
		"""
			this function returns the list of columns in the csv file.
		"""
		indx=[]
		frm = DataMng.formatChk(fp)
		if(frm == 'csv'):
			dataArr = DataMng.csvRw(fp)
			try:
				indx = dataArr[0].split(',')
				pass
			except:
				print('there is a problem to split lines!')
		else:
			print('make sure about your file format!')
			pass
		return indx
		pass

	def csvDic(fp):
		"""
			this function converting the csv to dictionary
		"""
		frm = DataMng.formatChk(fp)
		dic = {}
		dataRw=[]
		if(frm=='csv'):
			dataArr = DataMng.csvRw(fp)
			nIndx =len(DataMng.csvIndx(fp))
			n=0
			for item in dataArr:
				rw = item.split(',')
				dataRw.append(rw)
			n = len(dataRw)
			dataRw_flMtx = [[dataRw[j][i] for j in range(n)] for i in range(len(dataRw[0]))]
			#print(dataRw_flMtx[4][1:])
			
			for i in range(nIndx):
				for j in range(1,n):
					d = dict(zip(dataRw_flMtx[i][:1],dataRw_flMtx[i][1:]))
					dic.update(d)

			pass
		return dic
			


fp = 'D:\Arman\Iaac\Y2\Python\GH_Data_Visualization\AdultFormatted.csv'
print(DataMng.csvDic(fp))