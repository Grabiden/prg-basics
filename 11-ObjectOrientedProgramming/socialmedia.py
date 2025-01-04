class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print(self.username)
        n = 0
        while n < len(self.posts):
            print(f"{n + 1}. {self.posts[n]}")
            n += 1
def main():
    profil = SocialMediaProfile("jhondoe") 
    profil.add_post("Hello, world!")  
    profil.add_post("Had a great day at the park!")   
    profil.add_post("What's up, Natalie? How are you?") 
    SocialMediaProfile.display_timeline(profil)  
if __name__ == "__main__":
    main()

