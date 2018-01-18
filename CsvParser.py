import json

class CsvFileParser:
	def getJsonListOfRows(self, pathToFile):
		fp = open(pathToFile, 'r')
		headerLine = fp.readline().rstrip('\n')
		headerFields = headerLine.split(',')
		listOfRecords = []
		line = fp.readline().rstrip('\n')
		while line:
			lineFields = line.split(',')
			jsonObj = self.createJsonObject(headerFields, lineFields)
			listOfRecords.insert(0, jsonObj)
			line = fp.readline().rstrip('\n')

		fp.close()
		return listOfRecords

	def createJsonObject(self, headerFields, rowFields):
		data = {}
		for x in range(0, len(headerFields)):
			data[headerFields[x].strip()] = rowFields[x].strip()
		return data
