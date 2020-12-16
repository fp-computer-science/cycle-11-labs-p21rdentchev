# Ryan Dentchev

rows = [["Darik", "Eugene", "Kyle", "Azaan"],
        ["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
        ["Christian", "Josh", "Matt", "Francesco"],
        ["Patrick", "Nico", "Trevayne"]]


for row in rows:
    for index, name in enumerate(row):
        if name[-1] == "s":
            row[index] = name + "'"
        else:
            row[index] = name + "'s"
print(rows)
