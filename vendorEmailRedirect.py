#!/usr/bin/python
#Author:Kevin chin
import xlrd
def parseFile(fileURL):
	__vendor=0
	__tag=1
	__request_url=2
	__input=3
	__output=4
	__success=5
	__fail=6
	__study_specific_parameter=7
	temp =""
	book = xlrd.open_workbook(fileURL)
	sh = book.sheet_by_index(0)
	if sh.ncols!= 8 or sh.nrows <=1 : 
		temp="Sorry the input file is empty or lost data."
		return temp
	title = sh.row(0)
	for num in range(1,sh.nrows):
		if sh.row(num)[__input].value != sh.row(num)[__output].value :
			temp = "input and output parameters are different!"
			return temp
		temp += "<add vendor=\""+sh.row(num)[__tag].value+"\" redirect_parameterName=\""+sh.row(num)[__input].value+"\" redirect_successTarget=\""+convertURL(sh.row(num)[__success].value)+"\" redirect_failTarget=\""+convertURL(sh.row(num)[__fail].value)+"\"/>\n"
	return temp
def convertURL(input_url):
	if input_url=='':
		return input_url
	output_url = re.sub(r"(=(?i)xxx*)|(=<IDENTIFIER>)","={0}",input_url)
	output_url = re.sub(r"&","&amp;",output_url)
	return output_url
