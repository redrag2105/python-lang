def main():
    x = input("File name: ")
    check(x)


def check(a):
    ex = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
    if "." in a:
        a = a.lower().strip().split('.')
        x = len(a) - 1
        if a[x] == ex[0]:
                print("image/" + ex[0])
        elif a[x] == ex [1]:
                print("image/" + ex[2])
        elif a[x] == ex [2]:
                print("image/" + ex[2])
        elif a[x] == ex [3]:
                print("image/" + ex[3])
        elif a[x] == ex [4]:
                print("application/" + ex[4])
        elif a[x] == ex [5]:
                print("text/" + "plain")
        elif a[x] == ex [6]:
                print("application/" + ex[6])
        else:
                print("application/octet-stream")
    else:
        print("application/octet-stream")

main()