# Attributes list

#Artist="Led Zeppelin" # Band
#Genre="Rock" # Style
#Records=11 # How many albums
#SongDuration=12.05 # Random song duration


Attributes={"Artist":"LedZeppelin","Genre":"Rock","Records":11,"SongDuration":12.05}
for k, v in Attributes.items():
    print(k, ':', v)

def Guess(key,value):
    for k, v in Attributes.items():
        if k == key and v == value:
           return True
        else:
            return False
Guess("Artist", "LedZeppelin")