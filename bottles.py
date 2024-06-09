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







