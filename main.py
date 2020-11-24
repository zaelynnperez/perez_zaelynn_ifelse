tempf=70
while True:
    print("temperature" + input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > tempf:
        light.set_pixel_color(5, light.rgb(255, 0, 0))
    elif input.temperature(TemperatureUnit.FAHRENHEIT) < tempf > 40: 
        light.set_pixel_color(5, light.rgb(0, 255, 0))
        
