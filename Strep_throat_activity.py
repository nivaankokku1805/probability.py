def find_prob(a, b):
    
    if a==1:
        prob_a = 0.2
        if b==1:
            prob_bga = 0.85
        elif b==2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
        prob_a_and_prob_b = prob_a * prob_bga
        print("Probability of b given a: ",prob_bga)
        print("Probability of both given the events occuring:", prob_a_and_prob_b)
        
    elif a==2:
        prob_a = 0.8
        if b==1:
            prob_bga = 0.2
        elif b==2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
        prob_a_and_prob_b = prob_a * prob_bga
        print("Probability of b given a: ",prob_bga)
        print("Probability of both given the events occuring:", prob_a_and_prob_b)
        
    else:
        print("Invalid Choice")
        
print("Let's calculateprobablity.Please enter choices for events.....")
print("Person has strep throat? \n1.Yes \n2.No")
a = int(input("Enter you choice (1/2): "))

print("Person has tested positive? \n1.Yes \n2.No")
b = int(input("Enter you choice (1/2): "))

print("Calculating probability of both events occuring.....")
find_prob(a, b)

###########################################################################################

