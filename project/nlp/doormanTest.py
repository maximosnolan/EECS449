import doorman as d

def main():
    driver = d.Doorman()
    print("driver created!")

    intentOne = "Who is at the door"
    response = driver.handleRequest(intentOne)
    print(response)

    intentTwo = "when was the person at the door last here"
    response = driver.handleRequest(intentTwo)
    print(response)

    intentThree = "how do I know this person"
    response = driver.handleRequest(intentThree)
    print(response)


    intentFour = "who does this person know here"
    response = driver.handleRequest(intentFour)
    print(response)
if __name__ == "__main__":
    main()
