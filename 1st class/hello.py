"""
def hello(to="World"):
    print("Hello,", to)

hello()
name = input("What's your name ? ")
hello(name)

"""

def main():
    name = input("What's your name ? ")
    hello(name)

def hello(to):
    print("Hello,",to)

main()
