# iq: int = 100;
# sum: int = 0;
# num: int = 0;
def my_avg_func():
    iq: int = 100;
    sum: int = 0;
    num: int = 0;
    while iq > 30 and iq < 300:
        iq = int(input("What is the participant iq? "));
        if iq > 30 and iq < 300:
            sum += iq;
            num += 1;
    else:
        avg = sum / num if num > 0 else print("input err");
    return avg;

avg1: float = 0;
avg2: float = 0;

''' I'm an avid Sci-Fi fan so..., I apologise in advance...
'''
print("Initializing....");
# while iq > 30 and iq < 300:
#     iq = int(input("What is the participant iq? "));
#     sum += iq;
#     num += 1;
# else:
#     avg1 = sum / num if num>0 else print("input err");
avg1 = my_avg_func();
print(f"Initial testing (concluded)\niQ results calculated\nInitial result: {avg1:.2f}\n");
''' _______________הדפס הודעה כרצונך.....  ________________

I'm an avid Sci-Fi fan so..., I apologise in advance...
'''

# iq = 100;
print("\nOpenAI developed advanced personal AI implants in partnership with Elon Musk's brain chip company Neuralink.\nNeuralink has begun implanting its devices in humans, making the learning of new skills posible during REM sleep.\nThe simbiosis of man and machine has overcame the weakness of flash, a new type of humanity has been born.\nWith a mind of both silica and nurouns, humanity is ready to look at the stars again and reach its true destiny...a new gold age of science and discovery can begin.\n\nBut are we now smart enught to overcome our base nature, or will we again degrade to sqabeling over money and power?...")
print("Initializing....");
# while iq > 30 and iq < 300:
#     iq = int(input("What is the participant iq? "));
#     sum += iq;
#     num += 1;
# else:
#     avg2 = sum / num if num>0 else print("input err");
avg2 = my_avg_func();
print(f"Secondary testing (concluded)\niQ results calculated\nSecondary result: {avg2:.2f}\n");
if avg1 < avg2:
    print(f"Improvement calculated\nAverage inteligence has risen by: {avg2-avg1:.2f} points\nTHE DAWN OF A NEW AGE HAS COME...\n");
    # the following line can be commented out
    print("Now we can achieve more\nThan we've ever conceived before\nLeave this poor place\nPlease explore space\nEarth, she's a small base\nEven more awaits\nI implore great leaders\nTo lead with all the grace\nOf which we're capable\nAnd be the author of your fate\nBand together and endeavour\nClasp our hands together\nAs our ancestors have\nAnd stand the test of time forever\n\n Civilization by: Dan Bull ");
elif avg1 > avg2:
    print(f"Deterioration calculated\nAverage inteligence has fallen by: {avg1-avg2:.2f} points\nTHE AGE OF IDIOCRACY HAS COME...\n");
    # the following line can be commented out
    print("Over reliance on technology made us lose ourselves...\nFrom knowing how to calculate manually we moved to calculators...\nFrom remembering numbers to the use the memory of our phones insted of our own...\nFrom knowing how to navigate we moved to overreliance on GPS...\nFrom learning new lenguages we moved to use of automatic translation...\n\n'Humans will be taken care of like pets when robots take over because AI will want to preserve us as part of nature.' \n Apple co-founder Steve Wozniak");
else:
    print("iQ identical, Humanity did not change... ");
    # the following line can be commented out
    print("Personal AI Implants had been abandoned...\nAI reasearch has been regarded as unpromissing and dengerous...\nHumanity went back to fighting...\nIn the future we have forgoten the importance of technology and science,...\nso much has been forgotten, never to be relearned.\nForgeten is the promise of progress and understanding, for in the grim dark future there is only WAR...\n")
    # the following line can be commented out
    print("Two nations stand on the brink,\nFear and hate, no time to think.\nNuclear shadows cast so wide,\nOn the edge, we can’t hide.\n\nBorders drawn in blood and lies,\nUnderneath the blackened skies.\nLegions march, in foreign lands,\nDeath and doom at our own hands.\n\nFrom the void, the chaos calls,\nSilent as a planet falls.\nToo late now, we’ve burned our past,\nNuclear winter, shadows cast.\n\nNations gone, and gods erased,\nIn the stars, we have no place.\nAtoms born from cosmic rage,\nHumanity, Earth's final page.\n\n-RosenRitter(me)-using Suno AI")

