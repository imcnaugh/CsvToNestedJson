import json

class CsvFileParser:
	def getJsonListOfRows(self, pathToFile):
		fp = open(pathToFile, 'r')
		headerLine = fp.readline().rstrip('\n')
		headerFields = self.splitLine(headerLine)
		listOfRecords = []
		line = fp.readline().rstrip('\n')
		while line:
			lineFields = self.splitLine(line)
			jsonObj = self.createJsonObject(headerFields, lineFields)
			listOfRecords.insert(0, jsonObj)
			line = fp.readline().rstrip('\n')
		return listOfRecords

	def createJsonObject(self, headerFields, rowFields):
		data = {}
		for x in range(0, len(headerFields)):
			data[headerFields[x].strip()] = rowFields[x].strip()
		return data

	def splitLine(self, line):
		return line.split(',')