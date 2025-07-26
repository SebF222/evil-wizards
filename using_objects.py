
#Creating a User Class
#We're building a social media CLI app
#Create an app that runs continuosly until I tell it to stop
#In this app users will be able to create profiles
#and log in
#once logged in they'll be able to 
#-- create posts
#-- view posts
#-- add friends
#-- view friends

#create a User class with attributes username email password posts friemds

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []
        self.friends = []

    def add_friend(self, friend):
        ''' This method takes in a user and, another user they wish to add as 
        a friend, and appends that user to their friends list'''
        self.friends.append(friend)
        print(f"You have successfully added {friend.username} as a friend. ")

    def friends_list(self):
        ''' This method takes in a user, and loops over that user's friends list
        and prints each of their friends name '''
        print("My Friends List")
        print("===============")
        #looping over each user object in joey's friends list
        for friend in self.friends:
            #for each user object we are printing their name
            print(friend.username)

    def create_post(self):
        ''' This methods takes in a user, asks that user what they want to post,
          takes their response, adds it to their posts list, and displays the post'''
        post = input("Whats on your mind?: ")
        self.posts.append(post)
        print(f"{self.username}: {post}")

    def display_posts(self):
        ''' This methods takes in user, and goes through their posts list
        and print each one of their posts'''
        print("My Posts")
        print("===============")
        for post in self.posts:
            print(post)





cameron = User("Curds", "cameron@email.com", "ilovechees123")
joey = User("RobotDoctor", "joey@email.com", 'robodcjoey')
arnett = User("ajm911", "arnett@email.com", "callmebeepme")
# print(cameron.username)
# print(joey.username)
# print(arnett.username)
# print(arnett.friends)
# arnett.friends.append(cameron)
# print(arnett.friends[0].username)

# #Adding a user to joey's friends list
# joey.add_friend(cameron)
# print(joey.friends)
# print(joey.friends)

# #Calling the friends-list method
# joey.friends_list()

# #Creating a post
# arnett.create_post
# arnett.display_posts()


def Fakebook():
    users = [cameron, joey, arnett]

    current_user = ''
    print("Would you like to:")
    print("1) Login")
    print("2) Create an account")
    answer = input(": ")
    if answer == "1":
        print("login")
    else:
        print("Create Account")
        print("===================")
        username = input("What is yoyur username?: ")
        email = input("Email:")
        password = input ("password: ")
        new_user = User(username, email, password)
        users.append(new_user)
        current_user = new_user
        print(f"Welcome to Fakebook {new_user.username}")
        
    while True:
        print ("""
Things to Do 
=============
1.) Add a Friend
2.) View My Friends
3.) Create a Post
4.) View my Posts        
5.) Logout       
""")
        choice = input("What would you like to do? :")
        if choice == '1':
            num = 1
            print("Potential Friends")
            print("======================")
            for user in users:
                if current_user.username !=user.username:
                    print(f"{num}.) {user.username}")
                num += 1 

            num = int(input("Select friend by number"))
            current_user.add_friend(users[num-1])

            num = int(input("Select friend by number: "))
            current_user.add_friend(users[num-1])
        elif choice == '2' :
                current_user.friends_list()
        elif choice == '3' :
                current_user.create_post()
        elif choice == '4' :
                current_user.display_posts()        
        elif choice == '5':
            print("Thanks for Fakebookin it, Bye!")
            break
Fakebook()