word = input()


print("".join(sorted(
    word,
    key=lambda x: (
        x.isdigit() and int(x) % 2 == 0,
        x.isdigit(),
        x.isupper(),
        x.islower(),
        x),
    )
))