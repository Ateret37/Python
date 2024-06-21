
#!/usr/bin/env python3

class GameCharacter:
    def  __init__(self, name, life):
        self.name = name
        self.life = life



player1 = GameCharacter("roger", 100)
player2 = GameCharacter("betty", 100)

print(player1.name)
print(player1.life)

print(player2.name)
print(player2.life)
