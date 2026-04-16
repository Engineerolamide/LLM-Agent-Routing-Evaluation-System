def route_input(category):
    if category == "motivational":
        return "motivational_agent"
    elif category == "advisory":
        return "advisory_agent"
    else:
        return "informational_agent"
