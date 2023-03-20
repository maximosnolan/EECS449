import doorman as d

def main():
    driver = d.Doorman()
    print("driver created!")

    intentOne = "Who is at the door"
    response = driver.handleRequest(intentOne)
    print(response)

if __name__ == "__main__":
    main()
