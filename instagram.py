from socialMedia import socialMedia

class Instagram(socialMedia) :
    def __init__(self, posts,body):
        super.__init__(self)
        self.posts=[]
        self.body=[]
    def publishNewPost(self):
        body1 = input()
        len_body = len(body1)
        if len_body < 2200 :
            return self.body.append(body1)
        else:
            exit
    def getPosts(self):
        return self.posts

    
   