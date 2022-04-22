

from instabot import Bot
bot = Bot()
bot.login(username = "here you can enter your username" , password = "enter your password")
bot.follow("enter your following name that your want to follow")  #the wao to follow any person automatically
bot.unfollow("enter your following name that your want to unfollow")  #the way to follow any person automatically

bot.upload_photo("enter the path of your photoo here") #way of uplaoding the photo on insta auto autamatically

bot.send_message("i love python", ["enter the usernames, of the ,person that you, want to, follow"]) #send message to multiple friends at the sametime

followers = bot.get_user_followers("your username")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("username pass here")
for following in following:
    print(bot.get_user_info(following))


