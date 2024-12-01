"""Display the Hello World without using the Hello world string"""


def display_helloworld():
    """Display the Hello World without using the Hello world string"""
    a = [
        chr(72), chr(101), chr(108), chr(108), chr(111),
        chr(44), chr(32), chr(87), chr(111), chr(114),
        chr(108), chr(100)
    ]
    return "".join(a)


display_helloworld()
