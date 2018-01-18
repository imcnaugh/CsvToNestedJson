from Models import ProcessorConfigs

class CsvToJson:
	noParentIdString = 'NO_PARENT_ID'

	def convert(self, configs, rows):
		dataMap = self.mapRows(configs, rows)
		topLevelElements = self.nestDataMap(configs, dataMap)
		return topLevelElements

	def mapRows(self, configs, rows):
		dataMap = {}

		for row in rows:
			parentId = row[configs.parentIdFieldName]
			if(parentId == ''):
				parentId = self.noParentIdString

			if parentId in dataMap:
				childeren = dataMap[parentId]
				childeren.insert(0, row)
				dataMap[parentId] = childeren
			else:
				dataMap[parentId] = [row]
		return dataMap

	def nestDataMap(self, configs, dataMap):
		topLevelElements = []

		for parentElement  in dataMap[self.noParentIdString]:
			element = self.recCall(dataMap, parentElement, configs.idFieldName, configs.childFiledName)
			topLevelElements.insert(0, element)

		return topLevelElements

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
