weather = input("What's the weather like? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Take an umbrella and a raincoat.")
elif weather == "cold":
    print("Wear a warm jacket and scarf.")
else:
    print("Sorry, I don't have advice for this weather condition.")
