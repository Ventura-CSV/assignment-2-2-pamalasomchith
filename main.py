def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int((input("Enter the temperature in Celsius: ")))
    fahrenheit = (1.8 * celsius) + 32
    
    print("Farenheit:", fahrenheit)

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
