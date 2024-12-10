class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        
    def display_timeline(self):
        print(self.username)
        n = 1
        for i in self.posts:
            print(f"{n}. {i}")
            n += 1
def main():
    user1 = SocialMediaProfile("jhondoe")
    user1.add_post("hello world")
    user1.add_post("siemka")
    user1.display_timeline()


if __name__ == "__main__":
    main()                    

