def convertCelctoFar(temp_celc):
    temp_fahr = (temp_celc * (9/5) + 32)
    return temp_fahr

def display_temperature_converstion(cel,far):
    print("You entered {0}.)".format(cel))
    print("The temperature in Farenheight is {0}.".format(convert_temp))
