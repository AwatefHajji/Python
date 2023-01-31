class User:
    def __init__(self,user_first_name,user_last_name,user_email,user_age,is_rewards_member=False, user_gold_card_points = 0):
        self.first_name = user_first_name
        self.last_name = user_last_name
        self.email = user_email
        self.age = user_age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points= user_gold_card_points
    
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}\n Email: {self.email}\n Age:{self.age}\n is_rewards_members: {self.is_rewards_member} \n gold_card_points:{self.gold_card_points}")
    def enroll(self):
        self.is_rewards_member=True
        self.gold_card_points=200
    def spend_points(self, amount):
        self.gold_card_points-=amount
    
    
user1=User("Asma","Neji","asma@live.fr",25,)
user1.enroll()
user1.spend_points(150)
user2=User("Achraf","Beji","achrefb@gmail.com",30)
user2.enroll()
user2.spend_points(120)
user3=User("Khady","Mbegen","khadyMb@yahoo.fr",33)
user1.display_info()
user2.display_info()
user3.display_info()
