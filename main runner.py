import Easy
import Medium
import Hard
def difCheck():
    global level
    level = input("What difficulty do you want? Type E for easy, Type M for medium and Type H for hard: ")
difCheck()
while str(level) == "M" or str(level) == "m":
        print("Starting Medium level Math")
        Medium.mainmediumrun
while str(level) == "E" or str(level) == "e":
        print("Starting Easy level Math")
        Easy.maineasyrun()
while str(level) == "M" or str(level) == "m":
        print("Starting Hard level Math")
        Hard.mainhardrun()


