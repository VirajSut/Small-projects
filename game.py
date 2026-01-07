import random 
#small rogue like game 

#starting with the player object 

class Player: 
    #what can the player do?
        # he can attack 
        # he can deffend 
        # he can heal 
        # he has HP (max of 50 , starting with 10)
    def __init__(self):
        self.max_hp = 10
        self.hp = 10 
        self.attack= 5
        self.room =0
        self.gold = 0
        self.weapon = "Fist"
        
    def damage(self, amt):
        self.hp = self.hp - amt
        if self.hp <=0:
            self.hp = 0
    
    def atk(self, a_monster): 
        a_monster.damage(self.attack)
        
    def heal(self, amt):
        if self.hp +amt >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = self.hp + amt 
        
    def equip(self, amt):
        self.attack = self.attack +amt  
    
    def advance(self): 
        self.room +=1
    
    def get_gold(self, a_monster):
        if a_monster.hp ==0:
            self.gold +=10
    def a_new_weapon(self, new_weapon):
        self.weapon = new_weapon
        
class Monster: 
    def __init__(self):
        self.hp = 10
        self.attack = 3
        self.total_HP = 10
    
    def damage(self, amt):
        self.hp = self.hp -amt
        if self.hp <=0:
            self.hp = 0
    
    def atk(self, a_player): 
        a_player.damage(self.attack) 
    def new_room_more_HP(self):
        self.total_HP = self.total_HP +10
        self.hp = self.total_HP
               
def main():
    the_player= Player()
    a_monster = Monster()
    print("Welcome Player")
    
    while the_player.hp > 0:
        
        decision = input("attack, heal, next room, stats \n")
        print("\n")
        
        if decision == "heal": 
            the_player.heal(int((the_player.max_hp)*.5) )
            print("\n")
            print("Health=", the_player.hp)
            print("\n")
            if a_monster.hp != 0:
                a_monster.atk(the_player)
                print("\n")
                print("you were hit")
                print("\n")
        
        elif decision == "next room" and a_monster.hp != 0:
            print("\n")
            print("no")
            print("\n")
        elif decision == "next room" and a_monster.hp == 0:
            if the_player.room in (2, 4) and a_monster.hp == 0:
                print("\n")
                print("+10 attack")
                print("\n")
                the_player.equip(10)
            
            the_player.advance()
    
            a_monster = Monster()
            a_monster.new_room_more_HP()
            print(a_monster.hp)
            
        elif decision == "attack":
            the_player.atk(a_monster)
            print("Monster HP=",a_monster.hp)
            print("\n")
            
            if a_monster.hp != 0:
                a_monster.atk(the_player)
                print("you were hit \n")
                print("-------------")      
                print("Health=", the_player.hp)
        
        elif decision == "stats":
            print("\n--- STATS ---")
            print("Room =", the_player.room)
            
            print("Max HP=",the_player.max_hp)
            
            print("HP=",the_player.hp)
            
            print("Attack Power=",the_player.attack)
            
            print("Gold=",the_player.gold)
            
            print("Weapon=",the_player.weapon)
            
            print("------------\n")
        else: 
            print("Invalid (dont put spaces after)")
            
    print("Game Over")
        
    
    #room 1 will be just fists and 1 monster
    
    #room 2 will have just fists 1 monster(+10 atk) and the player will get a sword(+10 atk) 
    
    #room 3 will have the sword and  1 monster(+20 base atk) 
    
if __name__ == "__main__":
    main()