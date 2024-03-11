def calculate_bmi(
    weight: float,
    height: float
) -> float:
    """Calculate the Body Mass Index (BMI)."""
    # The BMI formula is weight divided by the square of the height
    bmi = weight / (height**2)
    return bmi


def calculate_calories_burned(duration: int) -> int:
    """Calculate the estimated number of calories burned during exercise."""
    # Each minute 5 calories are burned
    calories = duration * 5
    return calories


def filter_overweight_people(people_data: list[dict[float]]) -> list[float]:
    """Filter overweight people based on BMI."""
    overweight_people = []
    # Iterate through each person in the dictionary
    for person in people_data:
        # Calculate the BMI of each person
        # and if its over 25 add it to the overweight
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people


def main():
    # Main program
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        # Get the person`s name as input
        name = input(
            "Enter person's name (or enter End to see the results): "
        ).strip()

        # If the user enters End the program stops
        # and the workout statistics are printed
        if name == "End":
            break
        # If there is a person inputet require their
        # weight height and duration of workout
        weight = float(input("Enter person's weight in kilograms: "))
        height = float(input("Enter person's height in meters: "))
        duration = float(input("Enter exercise duration in minutes: "))

        # Add all of the inputted info into a list of dictionaries
        person = {
            'name': name,
            'weight': weight,
            'height': height,
            'duration': duration
        }
        people_data.append(person)

    # Calculate and print the BMI and the calories burned for each person
    print("\nFitness Analysis:")
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        calories_burned = calculate_calories_burned(person['duration'])
        print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")
    
    # Filter out the overweight people and print them out
    overweight_people = filter_overweight_people(people_data)
    print("\nOverweight People:")
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(f"{person['name']}: BMI = {bmi:.2f}")


if __name__ == "__main__":
    main()
