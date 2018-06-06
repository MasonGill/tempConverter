import sys  # we are using this for cli inputs and exiting with 0 or 1

def main(fromtype, temp, totype):
    if fromtype == "c":
        newTemp = convertC(temp, totype)
    elif fromtype == "k":
        newTemp = convertK(temp, totype)
    else:
        newTemp = convertF(temp, totype)
    print "%.2f" %newTemp,; print u'\N{DEGREE SIGN}' + totype.upper() # rounds to 2dp, used 2 prints because unicode and formatted floats don't like to concatenate
    sys.exit(0)

def convertC(temp, totype): # takes a celcius value and returns the value converted to the toType
    if totype == "k":
        return temp + 273.15
    elif totype == "f":
        return (temp * (9.0 / 5.0)) + 32
    else:
        return temp

def convertK(temp, totype): # takes a kelvin value and returns the value converted to the toType
    C = temp - 273.15
    if totype == "c":
        return C
    elif totype == "f":
        return (C * (9.0 / 5.0)) + 32 
    else:
        return temp

def convertF(temp, totype): # takes a fahrenheit value and returns the value converted to the toType
    C = (temp - 32) * 5.0 / 9.0
    if totype == "c":
        return C
    elif totype == "k":
        return C + 273.15
    else:
        return temp

def isValid(typeIn): # checks if the input type is valid for use, if not it throws an error and exits
    typeArr = {"c","k","f"}
    for i in typeArr:
        if typeIn.lower() == i:
            return True
    print "input: '%s' is invalid, you can only use the types: c, k ,f" %(typeIn)
    sys.exit(1)

if __name__ == "__main__":  # only runs if executed in the cli and not if it was called as an import
    if len(sys.argv) == 4 and isValid(sys.argv[1]) and isValid(sys.argv[3]):    # checks for correct amount of arguments and argument validity
        try:
            main(sys.argv[1].lower(), float(sys.argv[2]), sys.argv[3].lower())  # runs main passing it the needed arguments
        except ValueError:
            print "'%s' must be a number value" %(sys.argv[2])  # if the temperature value isn't a number
            sys.exit(1)
    else:
        print "The 'cool' temperature converter program\n"   # prints help and examples
        print "Usage: python %s <fromtype> <temperature> <totype>\n" %(sys.argv[0])     # using old formatting
        print "Examples:\npython {0} c 12 f\npython {0} k 268 c\n".format(sys.argv[0])  # using new formatting
        print "types:\nc\tCelcius\nk\tKelvin\nf\tFahrenheit"
        sys.exit(0)
