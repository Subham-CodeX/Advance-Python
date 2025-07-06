emotion = "x.y"
def main():
    global emotion
    say("is anyone there?")
    emotion = ":d"
    say("hay brother !")


def say(phrase):
    print(phrase + " " + emotion)

main()