Name=input("What's your name ?")

match Name:
    case "haary" | "Ram" | "roki":
        print("perfect boy")
    case "Madhure":
        print("brilliant girl")
    case "subham":
        print("average boy")
    case _:
        print("who ?")