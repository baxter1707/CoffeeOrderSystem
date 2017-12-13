
### Morning Warm up Temp Converter

temp_celc = int(raw_input("Enter temperature in celcius"))
print("You entered {0}.)".format(temp_celc))
convert_temp = temp_celc * (9/5) + 32
print("The temperature in Farenheight is {0}.".format(convert_temp))


##fucntions were all moved to temperature_helper.py
#you could make temperature_helper shorter by adding
# import temperature_helper as t
#then going forward temperature_helper is always referred to as t
import temperature_helper

temp_celc = int(raw_input("Enter temperature in celcius"))

#module.functionname
#t.ConverCeltoFar
temp_fahr = temperature_helper.ConverCeltoFar(temp_celc)
temperature_helper.display_temperature_converstion(temp_celc,temp_fahr)
