import random
import time

secret_code = []
code = [0, 0, 0, 0]
for i in range(4):
    secret_code.append(random.randint(0, 9))
cracked = False
print("\nPin Code Cracker")
input("\nEnter to start cracker")
# print(f"Secret code = {secret_code}")
start_time = time.time()
while not cracked:
    for i in range(10):
        code[0] = i
        for j in range(10):
            code[1] = j
            for k in range(10):
                code[2] = k
                for l in range(10):
                    code[3] = l
                    time.sleep(.001)
                    print(f"Trying code: {code}")
                    if code[0] == secret_code[0] and code[1] == secret_code[1] and code[2] == secret_code[2] and code[
                        3] == \
                            secret_code[3]:
                        print(f"\nCode cracked!\n\nCode is: {code}\n")
                        cracked = True
                        break
                if cracked:
                    break
            if cracked:
                break
        if cracked:
            break
    if cracked:
        break

end_time = time.time()


print(f"Code cracked in {round(end_time - start_time, 2)} seconds")


input()
