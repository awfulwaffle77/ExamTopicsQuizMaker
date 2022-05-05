# ExamTopics Scraper & Quiz Creator

## What is this?
This is a Python-built CLI quiz for quizzes from ExamTopics. 
It gets questions from pages, shuffles them, you pick answers
and then you are shown a final score and the questions you got
wrong.

## How do I get it working?
1. Clone the repository
2. Create a new directory in the directory of the repository, named `res` (
or any other name, but also change the `RES_DIR` variable accordingly in `main.py`)
3. Go to the exam page
2. CTRL+s to save the page
3. Save in the `res`(or the name you have chosen) directory
4. Repeat for all pages in the exam
5. Run `main.py`
6. ???
7. Profit

## Steps with images
Create the `res` directory after cloning the repository

![step1](https://i.imgur.com/78xsRjX.png)

Go to the exam page and save it 

![step2](https://i.imgur.com/4hOW8c0.png)

How the `res` directory should look after saving all the needed pages

![step3](https://i.imgur.com/6YoFkdG.png)

Run `main.py` & get your quizzes done!

![step4](https://i.imgur.com/qpZ2r3N.png)

## Can't you automate these steps?
Yes and no. Due to the fact that ExamTopics uses a *lot* of captchas, 
this automation process would be accessible to people with contributor
access, as that disables captchas.

## Status
At this moment (5th of May 2022):
- scraping is done correctly from the HTML of ExamTopics pages.
- quizzes seem to be looking fine

## Bug reports
If you encounter any type a bug, please let me know by creating an 
[issue](https://github.com/awfulwaffle77/ExamTopicsQuizMaker/issues/new).

## Types of questions
I am aware that there is at least one question with multiple answers. This quiz
does **NOT YET** have support for these types of questions. I am unaware if it is
even present in the list of questions as it may have a different tag.