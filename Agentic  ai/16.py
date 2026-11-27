'''class A:
    def show(self):
        print("this is fun A")
class B(A):
    pass
ref=B()
ref.show()'''

'''class BasicPlayer:
    def __init__(self, username):
        self.username = username

    def walk(self):
        print(f"{self.username} is moving forward")
class Warrior(BasicPlayer):       
    def attack(self):
        print(f"{self.username}swings a heavy sword!")

class Paladin(Warrior):
    def heal(self):
        print(f"{self.username}uses divine light to heal the party")

hero=Paladin("Suresh_Hero")
hero.walk()
hero.attack()
hero.heal()'''

class ImageContent:
    def apply_filter(self):
        print("Applying 'Vintage' filter to the image")
class TextContent:
    def check_grammar(self):
        print("Scanning text for spelling error")
class SocialMediaPost(ImageContent,TextContent):
    def upload(self):
        print("Post is now live in the feed")
my_post=SocialMediaPost()
my_post.check_grammar()
my_post.upload()
    