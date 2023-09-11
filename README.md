# MachEight
MatchEight challenge.
 Here's a description of the code and the error cases it handles:

Code Description:

1. The code begins by importing the `argparse` module, which is used for parsing command-line arguments.

2. It defines a `is_valid_integer(value)` function that checks whether a value can be converted to an integer without raising an exception. This is used later for validating input values.

3. It defines the `find_pairs_with_sum(numbers, target_sum)` function, which finds pairs of integers in the `numbers` list that sum to the given `target_sum`. It uses a set called `seen` to avoid duplicates and improve efficiency in pair searching.

4. In the `main()` function, command-line argument parsing is set up using `argparse`. Two arguments are defined: `numbers` (a list of numbers) and `target` (the target value).

5. The following error cases are handled:
   - Unrecognized arguments.
   - Empty or null list of numbers.
   - Empty or null target value.
   - Elements in the list of numbers that cannot be converted to integers.
   - Target value that is not a valid integer.

6. String arguments are converted into lists of integers, and the `find_pairs_with_sum()` function is called to find pairs that sum to the target value.

7. The result is printed, either the found pairs or a "No pairs found" message if no valid pairs were found.

Handled Error Cases:

1. Unrecognized arguments: Checks for unrecognized arguments and displays an error message.

2. Empty or null list of numbers: Verifies if the list of numbers is empty or null and displays an error message.

3. Empty or null target value: Verifies if the target value is empty or null and displays an error message.

4. Elements in the list of numbers that cannot be converted to integers: Checks if any elements in the list of numbers cannot be converted to a valid integer and displays an error message.

5. Target value that is not a valid integer: Verifies if the target value is not a valid integer and displays an error message.

6. No pairs found: If no valid pairs are found, it displays a message indicating that no pairs were found.

In summary, this code handles several error cases and provides an efficient solution for finding pairs of integers that sum to the specified target value.

This code complies with the efficiency constraint that "The algorithm to find the pairs must be faster than O(n^2)" by using a strategy that has a more efficient time complexity. Instead of comparing every possible pair of numbers in a quadratic approach, it utilizes a set to keep track of previously seen numbers, allowing it to find pairs that sum to a target value in linear time, which is faster than O(n^2) for large lists of numbers. Additionally, the code handles edge cases appropriately, such as negative numbers and invalid target values, providing descriptive error messages when necessary.

To run the code, you execute it using the following format:
     python app.py arguments

For example:
    python app.py 1,9,5,0,20,-4,12,16,7 12

Will produce an output similar to:   

+ 12,0
+ 5,7
+ 16,-4
