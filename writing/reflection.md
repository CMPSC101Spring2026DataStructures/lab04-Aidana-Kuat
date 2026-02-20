# Reflection: Rock, Paper, Scissors Lab

Name: Aidana Kuat
Date: 02/20/2026

Please answer the following questions after you have completed the programming lab. Write your answers in complete sentences and provide thoughtful responses.

## Comprehension Questions

1. What is the purpose of breaking a program into functions? How did this help you in completing the lab?

Your Response:

The purpose of breaking a program into functions is to make the code more organized, structured, and easier to read. Using functions I could focus on one part of the program at a time instead of trying to solve everything at once. It also made debugging easier when something was not working correctly.

2. Describe how you validated user input in your version of the Rock, Paper, Scissors game. Why is input validation important?

Your Response:

I validated user input by checking whether the user entered either a valid number (1, 2, or 3) or a valid word (“rock”, “paper”, or “scissors”). If the input was invalid, the program printed an error message and asked the user to enter their choice again. Input validation is important because it prevents the program from crashing and ensures that only correct values are processed.
 
3. How did you use comments and docstrings in your code? Give an example of a helpful comment or docstring you wrote.

Your Response:

I used docstrings at the beginning of each function to explain what the function does and what it returns. This helps make the code easier to understand when someone reads it. For example, I wrote # If both choices are the same, it's a tie to clarify why that condition is checked. I also added comments like # Possible choices in the game and # Mapping numeric input to actual choices to explain the purpose of my variables.

4. Explain how the computer's move is generated in your program. What Python features did you use to accomplish this?

Your Response:

The computer’s move is generated using Python’s random module. In the get_computer_choice() function, I used random.choice(choices) to randomly select one item from the list of possible choices (rock, paper, or scissors).

5. What was the most challenging part of refactoring the spaghetti code into a more structured program? How did you overcome this challenge?

Your Response:

The most challenging part of refactoring the spaghetti code into a more structured program was separating the logic into different functions. Moreover, I was making sure the functions returned the correct values and that those values were passed properly between functions. For example, I needed to return the user’s choice from get_user_choice() and then pass it into determine_winner().

## Ethical Reflection Questions

1. Why is it important to write code that is easy for others to read and maintain? How does this relate to your responsibilities as a programmer?

Your Response:

Clear and structured code makes it easier to understand the logic, fix bugs, and add new features. If code is messy or confusing, it can waste time and lead to mistakes.

2. Consider the use of open source code (like the spaghetti code provided). What are some ethical considerations when using, modifying, or sharing code written by others?

Your Response:

It is important to respect the original author’s work. This means giving proper credit when required and following the license rules. Some licenses allow modification and sharing, but others may have restrictions.

---

(Did you remember to add your name and date at the top of your reflection file?)
