import sys
from Help import HelpService
from Models import ProcessorConfigs
from DataMarshaller import DataMarshaller

if len(sys.argv) == 4 or len(sys.argv) == 5:
	inputFilePaht = sys.argv[1]
	idField = sys.argv[2]
	parentIdField = sys.argv[3]
	childFiledName = "children"
	if(len(sys.argv) == 5):
		childFiledName = sys.argv[4]

	config = ProcessorConfigs(inputFilePaht, idField, parentIdField, childFiledName)

	marshaller = DataMarshaller(config)
else:	
	helpService = HelpService()
	print helpService.printHelp()
	