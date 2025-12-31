'''
def user_answers(name,age,color,):
    print (name)
    print (age)
    print (color)
def main():
    print ("hello what is your name?")
    n = input()
    print ("what a great name! what is your age?")
    a = input()
    print ("splendid, can you tell your favorite color?")
    c = input ()
    print ("thank you very much can tell if your answers are correct to this printed bellow?")
    user_answers(n,a,c)
    A = input ()
    if (A == "yes"):
        print("thats great")
    else:
        print ("there is something wrong please answer question one more time or mail me this problem")
'''

def main():
    print ("hello can you give me your age and name?")
    age = input()
    name = input()
    print(f"so your age is {age} and your name is {name}")
if __name__ == "__main__":
    main()