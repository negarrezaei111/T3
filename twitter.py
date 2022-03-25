from socialMedia import socialMedia

class twitter(socialMedia):
    def __init__(self, twitts):
        super.__init__(self)
        self.twitts=[]
    def getTweets(self):
        return self.twitts
        
        
    def createNewTweet(self) :   
        twitt1 = input()
        len_twitt1 = len(twitt1)
        if len_twitt1 < 280 :
            return self.twitts.append(twitt1)
        else:
            exit

