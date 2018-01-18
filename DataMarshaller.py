from Models import ProcessorConfigs
from CsvParser import CsvFileParser
import json

class DataMarshaller:

	def __init__(self, configs):
		fileRows = CsvFileParser().getJsonListOfRows(configs.pathToFile)
		
		dataMap = dict({})

		noParentIdString = 'NO_PARENT_ID'

		for row in fileRows:
			parentId = row[configs.parentIdFieldName]
			if(parentId == ''):
				parentId = noParentIdString

			if parentId in dataMap:
				childeren = dataMap[parentId]
				childeren.insert(0, row)
				dataMap[parentId] = childeren
			else:
				dataMap[parentId] = [row]

		kingBigWigs = []

		for topLevelElement  in dataMap[noParentIdString]:
			kingBigWig = self.recCall(dataMap, topLevelElement, configs.idFieldName, configs.childFiledName)
			kingBigWigs.insert(0, kingBigWig)

		j = json.dumps(kingBigWigs)

		fp = open(configs.outputFilePath, 'w')
		fp.write(j)
		fp.close()


	def recCall(self, dataMap, currentElement, idFieldName, childFiledName):
		pId = currentElement[idFieldName]
		if pId in dataMap.keys():
			listOfChildren = dataMap[pId]
			children = []
			for child in listOfChildren:
				child = self.recCall(dataMap, child, idFieldName, childFiledName)
				children.insert(0, child)
			currentElement[childFiledName] = children
		else:
			return currentElement

		return currentElement

