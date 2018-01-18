import sys
from Help import HelpService
from Models import ProcessorConfigs
from DataMarshaller import DataMarshaller

if len(sys.argv) == 5 or len(sys.argv) == 6:
	inputFilePaht = sys.argv[1]
	idField = sys.argv[2]
	parentIdField = sys.argv[3]
	outputFilePath = sys.argv[4]
	childFiledName = "children"
	if(len(sys.argv) == 6):
		childFiledName = sys.argv[5]

	config = ProcessorConfigs(inputFilePaht, idField, parentIdField, outputFilePath, childFiledName)

	marshaller = DataMarshaller(config)
else:	
	helpService = HelpService()
	print helpService.printHelp()
	