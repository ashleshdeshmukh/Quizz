# Quizz

Quizzed is an online quiz platform that is made by high-school students and is a very fun, interactive and amazing platform!

## Features
1. Three quizzes with 2 questions added. More questions coming!
2. Leaderboard with Gold, Silver, and Bronze coloring added.
3. Score tracking linked with leaderboard pages.
4. Score visible while performing a quiz!
5. Wrong and Right answers coloring works.
6. Logout button on the dashboard page.
7. Next and Submit buttons for questions.
8. User sign-up/login capability.
9. Question seeding via code is possible.

## Future Roadmap
1. Admin feature to create quizzes.
2. Increasing complexity as accuracy increases.
3. More quizzes for various topics.


## Version Log
**V1**
- Frontend team worked on building a basic layout for all pages ([landing.html](frontend/landing.html), [login.html](frontend/login.html), [register.html](frontend/register.html), [team.html](frontend/team.html), and respective stylesheets)
- Backend team worked on building a very basic and simple draft for quizzes using Python `if else` statements and `match` statements (similar to Java `switch`)
  
**V2**
- Backend team took on the core work from here, creating files using _Flask_ library, and routes for submitting quizzes(at [quizzes.py](backend/routes/quizzes.py) and main functioning of the login and register pages through HTML's ```<script>``` tags and through python coding using flask_jwt_extended at [auth.py](backend/routes/auth.py)
- Frontend members also took up some functionality, by implementing the code for password show and hide using `<script>` tags.
  
**V3**
- Backend team worked on seeding the questions so that it would show up on the landing.html
- After creating of [seed.py](backend/seed.py), backend team moved onto the display of the quizzes.
- Through the help of the frontend team they added quiz visibility by coding in JavaScript at the [landing.html](frontend/landing.html) using `<script>` tags

**V4**
- As we approached the finsihing touches of our website, both teams decided to fix any persiting bugs and improve any last parts.
- Backend team added encryption to the passwords, securing our users' credentials.
- Frontend team smoothened the experience of users by changing the navigation from page to page.

**V5**
- This is our final versions, where we worked on the README.md files, added the needed image files, and polished up our project.
