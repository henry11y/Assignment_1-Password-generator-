# Assignment_1-Password-generator
Python password generator using only built-in Python modules  
- Generates either **memorable** or **random** passwords  
- Logs each password with the day, date, and time it was created  

- When the program runs, the user can:
  - Generate one password interactively
  - Generate 1,000 passwords to confirm functionality  

- **Memorable passwords**
  - User selects number of words
  - Words are randomly chosen from a word list
  - A random one-digit number is added to each word
  - Words are joined using hyphens (`-`)
  - Case options: lower, upper, title, or random  

- **Random passwords**
  - User selects password length
  - User chooses whether to include punctuation
  - User can exclude specific characters
  - Uses lowercase letters, uppercase letters, digits, and optional punctuation  

- **Output**
  - Memorable passwords saved to:
  
    Memorable/Generated_Passwords.txt
    
  - Random passwords saved to:
    
    Random/Generated_Passwords.txt
  
  - Directories are created automatically if they do not exist  

- **Word list**
  - Uses top_english_nouns_lower_100000.txt
  - File must be in the same directory as the Python script  

- **Modules used**
  - os
  - random
  - string
  - datetime
