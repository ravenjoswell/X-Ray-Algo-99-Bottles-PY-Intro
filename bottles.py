from re import X


def bottle_song(num):
    bottles = num
    
    while bottles > 0: 
        x = ["bottles", "bottle"][bottles == 1]
        print(f"{bottles} {x} of beer on the wall, {bottles} {x} of beer.")
        bottles -= 1
        x = ["bottles", "bottle"][bottles == 1]
        if bottles == 0: 
            print("Take one down and pass it around, no more bottles of beer on the wall.")
            print(f"No more bottles of beer on the wall, no more bottles of beer.")
            print(f"Go to the store and buy some more, {num} bottles of beer on the wall.")
        else:
            print(f"Take one down and pass it around, {bottles} {x} of beer on the wall.")
       

    


bottle_song(99)








# will need a variable to hold the {initial} bottle of the lyric line, 
# then a variable to hold what to {subtract}, and lasty a variable to show {whats left}
# {initial} bottles of beer on the wall, {initial} bottles of beer.
# Take {subtract usually one} down and pass it around, {whats left} bottles of beer on the wall.
# {whats left} 98 bottles of beer.
# use a loop to descend down from what ever the intial amount of bottles there was till 0
# account for bottle"s", bottle, and no more bottles(if bottles == 0)
# {2} bottles of beer on the wall, {2} bottles of beer.
# Take one down and pass it around, {1} bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, {no more} bottles of beer on the wall. 
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, {initial} bottles of beer on the wall.