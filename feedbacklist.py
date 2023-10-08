names=[]
feedbacks=[]
sum=0

for i in range(5):
    name=input("Enter name")
    feedback=int(input("Enter feedback"))

    names.append(name)
    feedbacks.append(feedback)
    sum=sum+feedback
average=sum/len(feedbacks)
print(average)
##for i in range(len(names)):
 ##   if feedbacks    
