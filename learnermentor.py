class tech:
    
def __init__(self, name):
         
              self.name = name
   
def addStacks(self,expertise):
        
       self.expertise = expertise
    
def setMentorOrLearner(self,post):
        
       self.post = post
    
def setAvailableTime(self,time):
        
        if self.post in ['MENTOR']:
            
              self.time = time
        
        else:
            
              exit()
    
def getMentor(self,expertise,time):
        
        if self.expertise == expertise and self.time == time:
            
               print "Available Mentors are %d" % self.name