# WAF to convert USD to INR 

# User input
usd = float(input("Enter USD :"))

def converter(usd):
    inr = usd * 88.74
    print(inr)
    return(inr)

converter(usd)