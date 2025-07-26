class Character:
    def __init__ (self, name, health, attack_power, special_attack_power):
        self.name = name
        self.health = health 
        self.attack_power = attack_power
        self.special_attack_power = special_attack_power
        self.max_health = health 
        self.blocking = False
        self.special_abilities = []
        self.super_heal_cooldown = 4

    def attack(self, opponent):
        if opponent.blocking:
            print(f"{opponent.name} blocks the attack!")
            opponent.blocking = False
            return
        
        opponent.health -= self.attack_power
        print(f"{self.name} has attacked {opponent.name} with a stick for {self.attack_power} point of damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f'{opponent.name} has {opponent.health}hp left. ')

    def display_stats(self):
        print(f"{self.name}'s Stats \n Health: {self.health} \n Attack Power: {self.attack_power} \n special Power {self.special_attack_power}")

class Warrior(Character):
    def __init__(self, name):
            super().__init__(name, health=150, attack_power=25, special_attack_power = 35)
            self.berserker_cooldown = 0
            self.shield_cooldown = 0
    
    def attack(self, opponent):
        if opponent.blocking:
            print(f"{opponent.name} blocks the attack!")
            opponent.blocking = False
            return
            
        opponent.health -= self.attack_power
        print(f'{self.name} slashes at {opponent.name} with his sword, inflicting {self.attack_power} points of damage. ')
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
             print(f"{opponent.name} has {opponent.health}hp left.")

    def speciality(self, opponent):
        if self.berserker_cooldown > 0:
            return False
        
        if opponent.blocking:
            print(f"{opponent.name} blocks the berserker rage!")
            opponent.blocking = False
            self.berserker_cooldown = 3
            return True
            
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f'{self.name} goes into a berserker rage, dealing {damage} damage!')
        self.berserker_cooldown = 3
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left.")
        return True

    def shield_block(self):
        if self.shield_cooldown > 0:
            return False
        self.blocking = True
        self.shield_cooldown = 2
        print(f"{self.name} raises their shield and blocks the next attack!")
        return True
         
    def regenerate(self):
        old_health = self.health
        heal_amount = 10
        self.health += heal_amount
        
        if self.health > self.max_health:
         self.health = self.max_health

        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")

    def super_heal(self):
        if self.super_heal_cooldown > 0:
            print (f" Super Heal still charging! you will be able to use it in {self.super_heal_cooldown} more turns!")
            return
        
        old_health = self.health
        heal_amount = 50
        self.health += heal_amount 

        if self.health > self.max_health:
            self.health = self.max_health

        actual_heal = self.health - old_health
        print (f"HEALING SPECIALITY YOU GAINED {actual_heal} OF HEALTH! Current Health: {self.health}/{self.max_health}")        

        self.super_heal_cooldown = 4 

        if self.health < 30:
            self.super_heal_cooldown -= 2
        else:
            self.super_heal_cooldown -= 1

class Mage(Character):
    def __init__(self, name):
          super().__init__(name,health=90, attack_power=40, special_attack_power= 50)
          self.fireball_cooldown = 0
          self.shield_cooldown = 0

    def attack(self, opponent):
        if opponent.blocking:
            print(f"{opponent.name} blocks the meteor strike!")
            opponent.blocking = False
            return
            
        opponent.health -= self.attack_power
        print(f'{self.name} casts meteor strike, smashing into {opponent.name} inflicting {self.attack_power} points of damage. ')
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
             print(f"{opponent.name} has {opponent.health}hp left.")
    
    def speciality(self, opponent):
        if self.fireball_cooldown > 0:
            return False
        
        if opponent.blocking:
            print(f"{opponent.name} blocks the fireball!")
            opponent.blocking = False
            self.fireball_cooldown = 2
            return True
            
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f'{self.name} casts a massive fireball, dealing {damage} damage!')
        self.fireball_cooldown = 2
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left.")
        return True

    def shield_block(self):
        if self.shield_cooldown > 0:
            return False
        self.blocking = True
        self.shield_cooldown = 3
        print(f"{self.name} creates an arcane shield!")
        return True
         
    def regenerate(self):
        old_health = self.health
        heal_amount = 10
        self.health += heal_amount

        if self.health > self.max_health:
         self.health = self.max_health

        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")

class Warlock(Character):
    def __init__(self, name):
          super().__init__(name,health=100, attack_power=20, special_attack_power= 35)
          self.dark_magic_cooldown = 0
          self.shadow_shield_cooldown = 0

    def attack(self, opponent):
        if opponent.blocking:
            print(f"{opponent.name} blocks the magic attack!")
            opponent.blocking = False
            return
            
        opponent.health -= self.attack_power
        print(f'{self.name} casts magic at {opponent.name} inflicting {self.attack_power} points of damage. ')
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
             print(f"{opponent.name} has {opponent.health}hp left.")
             
    def speciality(self, opponent):
        if self.dark_magic_cooldown > 0:
            return False
        
        if opponent.blocking:
            print(f"{opponent.name} blocks the dark magic!")
            opponent.blocking = False
            self.dark_magic_cooldown = 3
            return True
            
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f'{self.name} unleashes dark magic, dealing {damage} damage!')
        self.dark_magic_cooldown = 3
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left.")
        return True

    def shield_block(self):
        if self.shadow_shield_cooldown > 0:
            return False
        self.blocking = True
        self.shadow_shield_cooldown = 2
        print(f"{self.name} summons a shadow shield!")
        return True
         
    def regenerate(self):
        old_health = self.health
        heal_amount = 10
        self.health += heal_amount

        if self.health > self.max_health:
         self.health = self.max_health

        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")
             
class Monk(Character):
    def __init__(self, name):
          super().__init__(name,health=120, attack_power=15, special_attack_power= 25)
          self.chi_strike_cooldown = 0
          self.meditation_cooldown = 0

    def attack(self, opponent):
        if opponent.blocking:
            print(f"{opponent.name} blocks the punch!")
            opponent.blocking = False
            return
            
        opponent.health -= self.attack_power
        print(f'{self.name} strikes {opponent.name} with punches, inflicting {self.attack_power} points of damage. ')
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
             print(f"{opponent.name} has {opponent.health}hp left.")
             
    def speciality(self, opponent):
        if self.chi_strike_cooldown > 0:
            return False
        
        if opponent.blocking:
            print(f"{opponent.name} blocks the chi strike!")
            opponent.blocking = False
            self.chi_strike_cooldown = 2
            return True
            
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f'{self.name} performs a chi strike, dealing {damage} damage!')
        self.chi_strike_cooldown = 2
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
            print(f"{opponent.name} has {opponent.health}hp left.")
        return True

    def shield_block(self):
        if self.meditation_cooldown > 0:
            return False
        self.blocking = True
        self.meditation_cooldown = 4
        print(f"{self.name} enters meditation and blocks the next attack!")
        return True

    def regenerate(self):
        old_health = self.health
        heal_amount = 10
        self.health += heal_amount

        if self.health > self.max_health:
         self.health = self.max_health

        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")
             
class EvilWizard(Character):
    def __init__(self):
          super().__init__(name="Evil Wizard", health=150, attack_power=40, special_attack_power=0)
          self.regen_cooldown = 0

    def regenerate(self):
        if self.regen_cooldown > 0:
            print(f"{self.name} tries to regenerate but needs {self.regen_cooldown} more turns!")
            self.regen_cooldown -= 1
            return
            
        old_health = self.health
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        actual_heal = self.health - old_health
        print(f"{self.name} regenerated {actual_heal} health! Current health: {self.health}")
        self.regen_cooldown = 3
        
    def attack(self, opponent):
        if opponent.blocking:
            print(f"{opponent.name} blocks the evil wizard's attack!")
            opponent.blocking = False
            return
            
        opponent.health -= self.attack_power
        print(f'{self.name} casts a dark spell at {opponent.name} inflicting {self.attack_power} points of damage!')
        if opponent.health <= 0:
            print(f"{opponent.name} has perished!")
        else:
             print(f"{opponent.name} has {opponent.health}hp left.")

def get_cooldown_status(player):
    cooldowns = []
    if isinstance(player, Warrior):
        cooldowns = [player.berserker_cooldown, player.shield_cooldown]
    elif isinstance(player, Mage):
        cooldowns = [player.fireball_cooldown, player.shield_cooldown]
    elif isinstance(player, Warlock):
        cooldowns = [player.dark_magic_cooldown, player.shadow_shield_cooldown]
    elif isinstance(player, Monk):
        cooldowns = [player.chi_strike_cooldown, player.meditation_cooldown]
    return cooldowns

def reduce_cooldowns(player):
    if isinstance(player, Warrior):
        if player.berserker_cooldown > 0:
            player.berserker_cooldown -= 1
        if player.shield_cooldown > 0:
            player.shield_cooldown -= 1
    elif isinstance(player, Mage):
        if player.fireball_cooldown > 0:
            player.fireball_cooldown -= 1
        if player.shield_cooldown > 0:
            player.shield_cooldown -= 1
    elif isinstance(player, Warlock):
        if player.dark_magic_cooldown > 0:
            player.dark_magic_cooldown -= 1
        if player.shadow_shield_cooldown > 0:
            player.shadow_shield_cooldown -= 1
    elif isinstance(player, Monk):
        if player.chi_strike_cooldown > 0:
            player.chi_strike_cooldown -= 1
        if player.meditation_cooldown > 0:
            player.meditation_cooldown -= 1

def get_ability_names(player):
    if isinstance(player, Warrior):
        return ("Berserker Rage", "Shield Block")
    elif isinstance(player, Mage):
        return ("Fireball", "Arcane Shield")
    elif isinstance(player, Warlock):
        return ("Dark Magic", "Shadow Shield")
    elif isinstance(player, Monk):
        return ("Chi Strike", "Meditation Block")
    else:
        return ("Special Ability 1", "Special Ability 2")

def create_character():
     name = input("Whats your name adventurer? ")
     print('''
CHOOSE YOUR CHARACTER
========================
1.) Warrior
2.) Mage
3.) Warlock
4.) Monk''')
     choice = input ("Choose: ")
     if choice == '1':
        return Warrior(name)
     elif choice == '2':
          return Mage(name)
     elif choice == '3':
         return Warlock(name)
     elif choice == '4':
         return Monk(name)
     else:
         print("Invalid choice! Choose again.")
         return create_character()
     

def battle(player, boss):
     ability1_name, ability2_name = get_ability_names(player)
     
     while boss.health > 0 and player.health > 0:
        cooldown1, cooldown2 = get_cooldown_status(player)
        
        ability1_display = f"{ability1_name}" if cooldown1 == 0 else f"{ability1_name} (Cooldown: {cooldown1})"
        ability2_display = f"{ability2_name}" if cooldown2 == 0 else f"{ability2_name} (Cooldown: {cooldown2})"
        
        print(f'''
Your Turn 
=============
1.) Attack
2.) Heal
3.) {ability1_display}
4.) {ability2_display}
5.) View their Stats''')
        choice = input("Choose action: ")
        
        if choice == '1':
            player.attack(boss)

        elif choice == '2':
            player.regenerate()
        
        elif choice == '3':
            if cooldown1 > 0:
                print(f"Invalid choice! {ability1_name} is on cooldown for {cooldown1} more turns!")
                continue
            success = player.speciality(boss)
            if not success:
                print("Invalid choice!")
                continue

        elif choice == '4':
            if cooldown2 > 0:
                print(f"Invalid choice! {ability2_name} is on cooldown for {cooldown2} more turns!")
                continue
            success = player.shield_block()
            if not success:
                print("Invalid choice!")
                continue

        elif choice == '5':
            player.display_stats()
            continue
        else:
            print("Invalid choice!")
            continue

        reduce_cooldowns(player)

        if boss.health <= 0:
            print(f"\n winner winner chicken dinner {player.name} has defeated {boss.name}")
            break   

        if boss.health > 0:
          boss.regenerate()
          boss.attack(player)
          
        if player.health <= 0:
            print(f"\n L HAHAHA! {player.name} has been defeated by {boss.name}")
            break


def main():
     player = create_character()
     wizard = EvilWizard()
     battle(player, wizard)

main()