points = 0
print("x * 6 = 42")
correct= 7

print("What is X?")
ans= input()

while(True):
    try:
        num_ans= int(ans)

        if ans == 7:
            print("that is correct!")
            points += 1
        else:
            
            print(f"NO! {num_ans} * 6 = {num_ans*6}")
            
            if num_ans >7:
                print("Your guess was to high")
            else:
                print("Your guess was to low")
        break
    except:
        try:
            num_ans= float(ans)
        except:
            print("That is not a number. TRY AGAIN!")        