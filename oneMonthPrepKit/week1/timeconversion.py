def timeConversion(s):
    # Write your code here
    if(s[len(s)-2:len(s)] == "AM"): #Check for AM times
        if(s[0:2] == "12"):
            return "00"+s[2:len(s)-2]
        else:
            return s[0:len(s)-2]
    else: # Handle PM Times
        if(s[0:2] == "12"):
            return s[0:len(s)-2]
        else:
            hour = int(s[0:2]) + 12
            return str(hour)+s[2:len(s)-2]
        
