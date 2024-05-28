#!/bin/bash

The application will allow users to answer multiple-choice questions, implement scoring, time limits, and provide feedback. 

Milestones and Detailed Tasks
Milestone 1: Auth System/Session Management

Goals:
Implement user authentication and session management.
Ensure secure login and registration functionality.

Tasks:
Setup Project Structure:
Initialize a Flask or Django project.
Set up virtual environment and install necessary dependencies (Flask/Django, Flask-Login/Django auth, etc.).

User Registration:
Create registration forms (HTML, CSS) and views.
Implement server-side logic for user registration (store user credentials in the database).
Ensure password hashing for security.

User Login and Logout:
Create login forms and views.
Implement server-side logic for user authentication and session management.
Add logout functionality to end user sessions securely.

Session Management:
Use session management to track logged-in users.
Ensure that only authenticated users can access certain parts of the application.

Deliverables:
User registration and login forms.
Backend logic for authentication.
Secure session management.





Milestone 2: Storage of Quiz Results
Goals:
Implement database storage for quiz results.
Associate quiz results with user accounts.

Tasks:
Database Setup:
Define the database schema for storing users, quizzes, questions, and results.
Create models/tables for the above entities.

Quiz Result Storage:
Implement logic to store quiz results under user accounts.
Ensure that results include score, time taken, and feedback.

Retrieve and Display Results:
Create views to display past quiz results to users.
Implement queries to fetch results from the database.

Deliverables:
Database schema for quizzes and results.
Functionality to store and retrieve quiz results.
User interface to display results.




Milestone 3: Make Application Responsive
Goals:
Ensure the application is responsive and user-friendly on all devices.
Use HTML and CSS to enhance the user interface.

Tasks:
Responsive Design:
Use CSS frameworks like Bootstrap or Tailwind CSS to create a responsive layout.
Ensure all forms, buttons, and elements adjust gracefully on different screen sizes.

User Interface Enhancements:
Improve the visual appeal of the quiz interface.
Add CSS animations and transitions for better user experience.

Testing:
Test the application on various devices and screen sizes.
Fix any layout issues identified during testing.

Deliverables:
Responsive UI for all application pages.
Enhanced user interface with improved aesthetics.




Bonus Milestone 1: Add New Sets of Quiz Questions
Goals:
Design the code to allow easy addition of new quiz questions.
Ensure scalability and flexibility.

Tasks:
Admin Interface for Quiz Management:
Create an admin interface for adding, editing, and deleting quiz questions.
Implement server-side logic to handle new quiz sets.

Question Set Management:
Design the database to accommodate multiple sets of quiz questions.
Ensure each question set can be easily managed and retrieved.

Deliverables:
Admin interface for quiz management.
Flexible backend to handle new quiz sets.



Bonus Milestone 2: Expose Quiz Questions via REST API

Goals:
Create a REST API to expose quiz questions.
Enable integration with other services or applications.

Tasks:
API Design:
Design RESTful endpoints for accessing quiz questions.
Implement CRUD operations for quiz questions via the API.

Security:
Implement authentication and authorization for API access.
Ensure secure data transmission.

Documentation:
Provide API documentation for developers.
Use tools like Swagger or Postman to document the API endpoints.

Deliverables:
REST API for quiz questions.
Secure API endpoints with proper authentication.
Comprehensive API documentation.

