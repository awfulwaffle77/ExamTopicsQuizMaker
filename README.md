# ExamTopics Scraper & Quiz Creator

## What is this?
This is a Python-built CLI quiz for quizzes from ExamTopics. 
It gets questions from pages, shuffles them, you pick answers
and then you are shown a final score and the questions you got
wrong.

## ⚠️ READ BEORE YOU START
This was initially tested on Windows and seems to work alright.

⚠️ As tested, saving a page with CTRL+s in ChromeOS does not save it
in HTML by default, as needed by the application. In the dropdown 
menu, you have to select "Webpage, HTML Only".

![html_only](https://i.imgur.com/87YOG3U.png)


## How do I get it working?
Note: If you want the quiz for Google Associate Cloud Engineer, you can get the res directory
in the proper HTML format [here](https://www.udrop.com/6AuX/res.zip). Just unzip the archive
in the ExamTopicsQuizMaker directory AFTER you clone it.

1. Clone the repository with `git clone https://github.com/awfulwaffle77/ExamTopicsQuizMaker.git`
or by going in the upper part of the page, clicking Code > Download ZIP (and unzip the archive)
2. Create a new directory in the directory of the repository(inside ExamTopicsQuizMaker), 
named `res` (or any other name, but also change the `RES_DIR` variable accordingly in `main.py`)
3. Go to the exam page that you want 
(ex. https://www.examtopics.com/exams/google/associate-cloud-engineer/view/)
4. CTRL+s to save the page. It has to be HTML. Save it in the `res`(or 
the name you have chosen) directory
5. Repeat for all pages in the exam

The structure of the folder should now be:

📁ExamTopicsQuizMaker \
&ensp;|-> 📄 main.py \
&ensp;|-> 📄 requirements \
&ensp;|-> 📄 quiz.py \
&ensp;|-> 📄 _classes.py \
&ensp;|-> 📁 res \
&emsp;|-> 📄 all pages needed, in HTML format 

6. Install requirements with `pip install -r requirements`
7. Run `main.py` with `python main.py` or `python3 main.py`
8. Choose how many questions you want per run. This is if you want to
have a quiz of 30 question before finishing and checking for wrong
questions 
9. Choose if you want the correct answer shown immediately or "no" if you want 
to check the file at the end of the quiz
10.  Answer the questions
11.  Review the .txt file that has been created when you have started
the quiz

## Steps with images
Create the `res` directory after cloning the repository

![step1](https://i.imgur.com/78xsRjX.png)

Go to the exam page and save it 

![step2](https://i.imgur.com/4hOW8c0.png)

How the `res` directory should look after saving all the needed pages

![step3](https://i.imgur.com/mEATsMZ.png)

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