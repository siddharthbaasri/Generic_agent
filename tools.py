def get_weather(city: str):
    if city == "Seattle":
        return "It is 40 degrees Fahrenheit today and it is raining"
    elif city == "San Francisco":
        return "It is 80 degrees Fahrenheit today and it is sunny"
    else:
        return "It is -20 degrees Fahrenheit today and there is a snowstorm"

tool_exec = {"get_weather": get_weather}