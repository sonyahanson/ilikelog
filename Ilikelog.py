# Place holder will be the best script ever made.
################ I Like Log ###################
# The Open Source Automatic Logline Generator #
###############################################

import random

intro = ["After moving into", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]

s_nouns = ["a nightly demonic presence", "A vengeful Australian policeman", "the local Blair Witch legend", "treats", "meets with", "A traveling mariachi", "A small time boxer", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]

place = ["a suburban home", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]

verb = ["becomes increasingly disturbed by","sets out to avenge his partner,","go missing after traveling into the woods of Maryland","strives to go the distance for his self-respect","is mistaken for a murderous criminal","gets a once in a lifetime chance","hide from bloodthirsty zombies in a farmhouse"]

p_nouns = ["a couple", "Both of my moms", "his wife and his son whom were murdered by a motorcycle gang in retaliation for the death of their leader", "Some guys", "All of a cattery's cats", "A group of people","The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen","Three film students"]

infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "leaving only their footage behind","for a disease.", "to fight the heavyweight champ in a bout in which he","and must hide from a gang bent on killing him","to be able to make toast explode.", "to know more about archeology.","to make a documentary about"]

def logline_maker():
    '''Makes a random logline from the different parts of speech of other log lines and other random things! '''

    print random.choice(intro), random.choice(place), random.choice(p_nouns), random.choice(verb), random.choice(s_nouns) or random.choice(p_nouns).lower(), random.choice(infinitives)

logline_maker()
