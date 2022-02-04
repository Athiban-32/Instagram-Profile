import instaloader

ig=instaloader.Instaloader()
dp=input("Enter the Insta Username:")
ig.download_profile(dp,profile_pic=True)