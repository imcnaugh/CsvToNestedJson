from Models import ProcessorConfigs
from CsvParser import CsvFileParser
from CsvToJson import CsvToJson
import json

class DataMarshaller:

	def __init__(self, configs):
		fileRows = CsvFileParser().getJsonListOfRows(configs.pathToFile)
		nestedElements = CsvToJson().convert(configs, fileRows)

		jsonString = json.dumps(nestedElements)
		self.writeJsonToFile(jsonString, configs.outputFilePath)

	def writeJsonToFile(self, jsonString, outputFilePath):
		fp = open(outputFilePath, 'w')
		fp.write(jsonString)
		fp.close()
