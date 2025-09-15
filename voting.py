def can_vote(age):
    """Checks if someone is old enough to vote (18+)."""
    if age >= 18:  
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")

if __name__ == '__main__':
    can_vote(18)  
