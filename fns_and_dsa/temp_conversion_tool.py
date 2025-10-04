FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
  return fahrenheit

def main():
  while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

  while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ("C", "F"):
            break
        else:
            print("Invalid temperature. Please enter a numeric value.")
if unit == "C":
        converted = convert_to_fahrenheit().temperature
        print(f"{temp}°C is {converted}°F")
    else:  
        converted = convert_to_celsius().temperature
        print(f"{temp}°F is {converted}°C")


if __name__ == "__main__":
    main()  
