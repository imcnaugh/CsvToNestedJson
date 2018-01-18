# CsvToNestedJson

The need for the project comes after I was approched by someone who had a csv file of employees. They wanted to transform the csv file into json where each employee object would contain an element that held each of employees that reported up to them.

There are a few assumptions made about the csv file that we had agreed upon.
1. There would be a header row on the csv file
2. There would be no circuler dependencies in the data, (employee a would not report to employee b, who reported to employee a)
3. There would be an id on each row, and each row would contain the id of the employee they reported to
4. We have no idea what these rows will be titled in the header.
5. All the rows in the csv are significant, if its in the csv, it should up in the final json.

## Using the script!
The script takes 4-5 arguments, 
1. The path to the csv file that should be processed.
2. The string of the id field in the header of the CSV.
3. The string of the parent id field in the header of the CSV.
4. The path of the output file to save the json to.
5. An optional name of the children field that will be added to the final json, this defaults to a value of "children" (But its a bit strange to call employees that report to somebody children, so you know, now you can configure that...)

Simply calling `python EntryPoint.py {args}` will execute the program

## Your python sucks, why you build this?

The client had asked for the code to be in Python, I dont have much experience in python, but figured it would be a good opputrunity to lean more about the language. So while the following code may not be up to any one standard or another, for 2 beers of work and next to no prior knowdage of large scale python applications, im happy with the result, and will continue to bring it up to a standard
