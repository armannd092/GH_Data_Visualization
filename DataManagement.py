
class DataMng():
	"""this class contain functions for data management"""

	def formatChk(fp):
		"""
		this function is checking the format of file and pass the format as string.
		"""
		for char in fp:
			if (char == '\'):
				i =fp.index(char)
				if(fp[i+1]=='\'):
					char.replace('\','')
					pass
			else:
				print('the path is checked!')
				pass

		try:
			with open(fp) as f:
				data = f.read()



		return stForm
		pass

		