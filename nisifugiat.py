from web3 import Web3

def cprint(text, color='white'):
    """
    Prints colored text to the console.

    Args:
        text (str): The text to print.
        color (str): The color of the text. Valid colors are:
            - 'black'
            - 'red'
            - 'green'
            - 'yellow'
            - 'blue'
            - 'magenta'
            - 'cyan'
            - 'white'
    """
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
    print(colors[color] + text + '\033[0m')

# Example usage
w3 = Web3(Web3.HTTPProvider('https://www.example.com = '0x1234567890abcdef1234567890abcdef1234567890abcdef'
to_symbol = 'ETH'
cprint(f'\n>>> swap {to_symbol} : https://www.example.com 'green')
