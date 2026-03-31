# 1. The Parent Class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def basic_attack(self):
        print(f"⚔️ {self.name} does a basic attack for {self.attack_power} damage!")


# 2. The Child Class: Warrior
class Warrior(Character):
    def __init__(self, name):
        # Warriors have high health (100) and medium attack (20)
        super().__init__(name, 100, 20)

    # Unique Warrior Method
    def heavy_slash(self):
        print(f"🗡️ {self.name} uses Heavy Slash for {self.attack_power + 15} damage!")


# 3. The Child Class: Mage
class Mage(Character):
    def __init__(self, name):
        # Mages have lower health (70) but use magic — passing stats up to Character
        super().__init__(name, 70, 15)

    # Unique Mage Method
    def cast_spell(self):
        print(f"✨ {self.name} casts Arcane Blast for 30 damage! The air crackles with magic!")


# --- Testing the Game ---

# Create a Warrior
player1 = Warrior("Arthur")
print(f"Player 1: {player1.name} (HP: {player1.health})")
player1.basic_attack()   # Inherited from Character
player1.heavy_slash()    # Warrior's unique method

print("-" * 20)

# Create a Mage
player2 = Mage("Gandalf")
print(f"Player 2: {player2.name} (HP: {player2.health})")
player2.basic_attack()   # Inherited from Character
player2.cast_spell()     # Mage's unique method
