import argparse


def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def find_pairs_with_sum(numbers, target_sum):
    
    # Create a set to store seen numbers,avoiding duplicates
    seen = set()
    
    # Initialize a list to store the pairs.
    pairs = []
    
    for num in numbers:
        # Calculate the difference between the target sum and the current number.
        diff = target_sum - num
        
        # Check if the difference (num) is already in the 'seen' dictionary.
        if diff in seen:
            # If yes, add the pair to the 'pairs' list.
            pairs.append((num, diff))
        
          # Add the current number to the 'seen' set.
        seen.add(num)
    
    return pairs


def main():
    try:
        # Set up command-line argument parsing
        parser = argparse.ArgumentParser(description='Find pairs of integers that sum to a given value.', allow_abbrev=False)

        # Argument for the list of numbers
        parser.add_argument('numbers', type=str, help='List of integers separated by a comma (,)')

        # Argument for the target value
        parser.add_argument('target', type=str, help='Target sum value (must be an integer)')

        # Parse the command-line arguments
        args, unknown_args = parser.parse_known_args()

        if unknown_args:
            raise argparse.ArgumentError(None, f"Unrecognized arguments: {', '.join(unknown_args)}")
        
         # Check if the list of numbers is empty or null
        if not args.numbers:
            raise ValueError("List of numbers is empty or null.")

        # Check if the target value is empty or null
        if not args.target:
            raise ValueError("Target value is empty or null.")

        # Split the input string of numbers using a comma and remove any leading/trailing spaces
        input_numbers = args.numbers.strip().split(',')

        # Check if any of the input values cannot be converted to an integer
        for x in input_numbers:
            try:
                int(x)
            except ValueError:
                raise ValueError(f"Invalid input: '{x}' is not a valid integer.")

        # Check if the target value is a valid integer
        if not is_valid_integer(args.target):
            raise ValueError("Invalid target value: must be an integer.")

        # Convert the list of numbers into a list of integers
        numbers = [int(x) for x in input_numbers]

        # Convert the target value to an integer
        target = int(args.target)

        # Call the function to find the pairs
        pairs = find_pairs_with_sum(numbers, target)
        
         # Check if there are no pairs found
        if not pairs:
            print("No pairs found.")  # Imprimir un mensaje cuando no se encuentran pares
        else:
            # Print the found pairs
            for pair in pairs:
                print(f"+ {pair[0]},{pair[1]}")

    except argparse.ArgumentError as e:
        parser.error(e)
    except ValueError as e:
        parser.error(f"Error: {e}")

if __name__ == '__main__':
    main()
