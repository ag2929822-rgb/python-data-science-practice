def main():

    try:
        n = int(input("Hey,Enter a Number :"))
        print(n)

    except Exception as e:
         print(e)


    finally:
        print("Hey I am inside finally")

main()

    