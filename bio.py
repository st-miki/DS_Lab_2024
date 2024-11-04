def print_bio():
   
    name = "Michael Engida"
    age = 21                   
    profession = "Software Engineer"
    location = "Addis Ababa, Ethiopia"
    
    
    hobbies = ["Coding", "Business Dev't", "Movies"]  
    skills = ["Front-End", "Business Dev't", "Generalist"]   
    favorite_quote = "Eat with people who you are willing to starve with"
    
    
    print("Bio:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Profession: {profession}")
    print(f"Location: {location}")
    print("\nHobbies:")
    for hobby in hobbies:
        print(f"- {hobby}")
    print("\nSkills:")
    for skill in skills:
        print(f"- {skill}")
    print(f"\nFavorite Quote: '{favorite_quote}'")


if __name__ == "__main__":
    print_bio()
