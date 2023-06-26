import itertools
from colorama import Fore, Back, Style

# Setting possible color scheme
R = Fore.RED + Style.BRIGHT + Back.BLACK
G = Fore.GREEN + Style.BRIGHT + Back.BLACK
C = Fore.CYAN + Style.BRIGHT + Back.BLACK
Y = Fore.YELLOW + Style.BRIGHT + Back.BLACK
B = Fore.BLUE + Back.BLACK + Style.BRIGHT


def crunch():
    print(Y + "Crunch together all words under a specified max length.")
    # Read in words from input file
    input_file = input(C + "File of words we will crunch and change up:  ")
    # Get user input for max length
    max_length = int(
        input(C + 'Enter the maximum length for the combined words: '))
    output_file = input(C + 'Enter the output file name: ')

    with open(input_file, 'r') as f:
        words = f.read().splitlines()

    # Generate all possible word combinations
    all_combinations = []
    for i in range(1, len(words)+1):
        for combination in itertools.combinations(words, i):
            new_combination = "".join(combination)
            if len(new_combination) <= max_length:
                all_combinations.append(new_combination)
                print(G + new_combination)

                # Concatenate words in the opposite order
                reversed_combination = combination[-1] + \
                    "".join(combination[:-1])
                reversed_new_combination = "".join(reversed_combination)
                if len(reversed_new_combination) <= max_length:
                    all_combinations.append(reversed_new_combination)
                    print(G + reversed_new_combination)

    # Write all combinations to file
    with open(output_file, 'w') as f:
        print(R + f'Generated {len(all_combinations)} combinations.')
        f.write('\n'.join(all_combinations))


if __name__ == '__main__':
    crunch()
