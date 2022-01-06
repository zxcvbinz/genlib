# Start import
import json
# End import

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printException(exceptionMessage):
	print(f"{bcolors.FAIL}ERROR:" + str(exceptionMessage)+ bcolors.ENDC)

def createErrorCode(Code):
	consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
	str = ""
	count = 0
	for x in Code:
		if x in consonants:
			if count < 3:
				str = str + x.upper()
				count += 1
	return (str)

def printErrorCode(Code):
	if Code == 401:
		Error = {"Message": "Unauthorized", "Error code": "401"}
	elif Code == 500:
		Error = {"Message": "Internal Server Error", "Error code": "500"}
	else:
		Error = {"Message": Code, "Error code": "0x" + createErrorCode(Code)}
		Code = "0x" + createErrorCode(Code)
	return json.dumps(Error), Code

def printSuccessCode(Code):
	returnCode = {"Message": "Generic successfully code.", "Status_code": "200"}
	return json.dumps(returnCode), 200