import math
class StringEdit:
    @staticmethod
    def off_by_one(s, t):
        '''Returns true if s and t differ by at most one edit'''
        # TODO Add code here (and any required helper methods below it)
        #insert, delete, replace
        error=0
        if s == t:
            return False # ????
        
        #if they are more than one character longer/shorter
        if abs(len(t)-len(s))>1:
            return False

        
        #if one is longer than other check for insert or delete
        #delete and insert are funcitonally the same
        if len(t)!=len(s):
            if len(t)<len(s):
                a=s
                s=t
                t=a
            
            for i in range(len(s)):
                if s[i]==t[i]:
                    pass
                elif s[i]==t[i+1]: #if a delete needed
                    t=t[:i]+t[i+1:]
                    error+=1
                
            if error==0: # if the error is at the end
                error+=1

        
        #if same length: find error and replace to make the same
        else:
            for i in range(len(t)):
                if s[i]==t[i]:
                    pass
                else:
                    error+=1
                    s=s[:i]+t[i]+s[i+1:]
        
        if error==2:
            return False
        # check to see if a string is off
        
        #if the strings are the same return true
        if s==t:
            return True
        
        
        return False


'''


        error=0
        if len(t)<len(s):
            a=s
            s=t
            t=a

            if s == t[:-1]:
                #insert at end
                return True
        
        for i in range(len(s)):
            
            if s[i] == t[i]:
                pass
            elif t[i+1] == s[i]:
                #insert a new character test
                error+=1
                sub=s[i:]
                sub1=s[:i-1]
                s=sub1.append(t[i+1]).append(sub)
            elif t[i+1]==s[i+1]:
                s[i]=t[i]
                error+=1
        '''






stringedit=StringEdit()
print(stringedit.off_by_one("blu", "blue"))#T
print(stringedit.off_by_one("belu", "blue"))#F
print(stringedit.off_by_one("blue", "blu"))#T
print(stringedit.off_by_one("blee", "blue"))#T
