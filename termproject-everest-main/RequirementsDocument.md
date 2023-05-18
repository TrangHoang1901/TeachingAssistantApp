# Software Requirements Specification

Teaching Assistant Management App
--------
Prepared by:

* `Uy Pham`,`VCEA-WSU`
* `Trang Hoang`,`VCEA-WSU`
* `Sushant Acharya`,`VCEA-WSU`
* `Pranshu Agrawal`,`SDC-WSU`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [TA Management](#-TA-Management)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2022-10-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

Every semester, the School of EECS at WSU recruits undergraduate teaching assistants for the introductory level courses and lab sections. This process has been carried out mostly manually. First, students who are willing to serve as TAs fill out a survey where they specify their course preferences. The staff who oversees the TA assignments look at the survey data and exchanges emails with the teaching faculty to gather their preferences of the TAs. Then they manually assign TAs to courses and labs based on student and faculty preferences. This is a tedious process and is very time consuming for staff and instructors. The Teaching Assistant App purpose is to make the process more convenient and ease the interaction between students and faculty members. The document will go in detail on the specification of the application

## 1.1 Document Purpose

The purpose of the SRS document is to define the idea, the system and the requirements with respect to the client. The document provides an overview of the product, its parameters and its intended output. It describes how the product is to be used by the users - the students and the faculty at the EECS school.

## 1.2 Product Scope

The purpose of the TA Management is to make an easy-to-use application for students who feel interested in being a TAs could sign in their information and allow professors to pick up their preference choices. This system is designed specifically for the School of EECs at WSU recruitment system manually which helps to manage and control the TAs applications and admission from professors and then could auto assign the admitted students to the chosen classes. Above all, we hope to provide an auto and manageable database system to  get the recruiting process to be more flexible.

## 1.3 Document Overview

The rest of the document provides the specifics of the product for all the designers. The second section describes the requirements, beginning with the description of all user types - the students and the faculty users, then some specific use cases, and then the non-functional requirements of the product and their descriptions. The third section discsses the interface of the product and includes mockups for the main parts. The next section provides the product backlog and the link to the issues page. The last section provides the references cited.

----
# 2. Requirements Specification

This section specifies the software product's requirements. 

## 2.1 Customer, Users, and Stakeholders

Customer is the client requesting the software, they can ask for software changes in the future, customers can also be stakeholders.
Stakeholders provide the funds and resources - Washington State University, government.
Users are students, faculty members have access to software but different view.

----
## 2.2 Use Cases

This section will include the specification for your project in the form of use cases. The section should start with a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.

For each use case you should have the following:

* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).

| Use case # 1      | As a user, I could create a professor account |
| ------------------ |--|
| Name          	| "Create a professor account and the profile information"  |
| Users         	| "Professor"  |
| Rationale         | "When a new TA joins the university, the admin user adds their information to the system."  |
| Triggers      	| "The faculty user intends to add a new TA position"  |
| Preconditions 	| "The new TA information is not already in the system"  |
| Actions       	| "1. The user indicates to add a new TA in the application.<br />2. The System will display the "Add TA" page.<br /> 3. The user will then enter TA’s firstname and lastname, choose their academic title from the listed options, and select their primary campus. The user then submits the form.<br /> 4. The system validates the entered name and last name (should be less than 60 characters and should not include invalid characters).<br /> 5. The system will save TA’s information to the system and acknowledge that the TA is added.<br /> 6. The system will navigate to the "Find Your TA" page." |
| Alternative paths | "After step 2, the student skips entering additional information. In this case, the profile is created but the additional fields are left empty."  |
| Postconditions	| "The TA’s information is added to the system and they appear in the list of the TA on the “Find your TA” page."  |
| Acceptance tests  | "Check whether:<br /> (i) the new TA appears in the “Find your TA" page;<br /> (ii) the TA’s information is saved correctly.
| Iteration     	| Iteration # 1  |

| Use case # 2      | As a user, I could add TA positions |
| ------------------ |--|
| Name          	| "Create TA positions"  |
| Users         	| "Professor"  |
| Rationale         | "Professors could create TA positions and update the qualifications they would like for their classes and they will could know how many TAs they need for their own classes"  |
| Triggers      	| "The faculty user intends to add a new TA position"  |
| Preconditions 	| "The new TA information is not already in the system"  |
| Actions       	| "1. Choose the course for TAship. You can assume a predetermined list of courses and have the instructor choose among those.<br /> 2. Enter the number of TAs needed for the course.<br /> 3. Enter the qualifications needed for the course (for example: min GPA, min grade earned for the course, prior TA experience, etc.).<br /> 4. Choose the semester for TAship."  |
| Alternative paths | "the user will be warned to fill all the information required in step 1, 2, 3 if they missing any blank"  |
| Postconditions	| "The TA positions should be uploaded to the “open TA positions” Page  "  |
| Acceptance tests  | "Check whether:<br /> (i) the new TA appears in the “Find your TA" page;<br /> (ii) the TA’s information is saved correctly.
| Iteration     	| Iteration # 1  |

| Use case # 3     | As a user, I could select a student and assign it to one of the TAship positions they created |
| ------------------ |--|
| Name             | “ Assigning Student to a TA position “ |
 | Users         	| "Professor"  |
| Rationale         | "Professors could appoint TAs for their classes"  |
| Triggers      	| "The faculty user intends to select a student that is unassigned as a TA for a position"  |
| Preconditions | "The TA is in the applicant list"  |
| Actions       	| "1. The instructor chooses the student for TAship.<br /> 2. The instructor submits the student as the TA for the class.”  |
| Postconditions | "The TA position is filled by the chosen student.  "  |
| Acceptance tests  | "Check whether: (i) the TA is in the course TA field;
| Iteration     	| Iteration # 2  |

| Use case # 4      | As a user, I could create a student account |
| ------------------ |--|
| Name          	| "Create a student account and enter the profile information "  |
| Users         	| "Student "  |
| Rationale         | "Help student user access the login page, register for the classes they would like to be a TA for, checks the status of their application and make a outstanding profile for next sem "  |
| Triggers      	| “The student user intends to build a profile like an online resume, showing classes they were TA before.”  |
| Preconditions 	| “The new student user should not have a profile save in the system before and the student has accessed the account creation page.” |
| Actions       	|” 1. The student sets the account username and password (username should be the WSU email).<br /> 2. The student enters contact information (name, last name, WSU ID, email, phone).<br /> 3. The student enters additional information (major, cumulativeGPA, expected graduation date, etc.).<br /> 4. The user selects the courses the student served as a TA before.” |
| Alternative paths | After step 2, the student skips entering additional information. In this case, the profile is created but the additional fields are left empty.  |
| Postconditions	| The user account is created in the database.  |
| Acceptance tests  | Make sure the user account exists in the database.  |
| Iteration     	| Iteration # 1  |

| Use case # 5      | As a user, I could login by username and password  |
| ------------------ |--|
| Name          	| Login |
| Users         	| All Users  |
| Rationale         | To be able to access features that require a user account  |
| Triggers      	| A user selects the login page  |
| Preconditions 	| A user already had a created account |
| Actions       	| 1. A user should be able to supply the information (email and password) that is associated with their account.<br /> 2. The system will validate that the information given by the user is correct.<br /> 3. The user will now have a validated login session created |
| Alternative paths | - A user is asked if they want to sign up for an account if an account does not exist with their email - A user is asked to re-enter the password if the one entered is incorrect |
| Postconditions	| A user successfully logs into their account and a login session is created |
| Acceptance tests  | - Make sure that users have an established login session with validated user capabilities |
| Iteration     	| Iteration # 1 |

| Use case # 6      | “As a user, I could view the open TA positions”  |
| ------------------ |--|
| Name          	| "View the open TA positions"  |
| Users         	| "Student "  |
| Rationale         | "Help student user access the classes that have open TA positions from the faculty "  |
| Triggers      	| "The student user accesses the View open TA positions page."  |
| Preconditions 	| The user is logged in as a student. |
| Actions       	| 1. The student opens the TA positions page.<br /> 2. The system lists all open TA positions and identifies the TA positions that match the current user’s qualifications and lists them separately under the “Recommended TA Positions”.<br /> 3. For each position, the following is displayed: course title, semester, instructor’s name and contact information, and qualifications needed for the TA position.
| Alternative paths | "N/A"  |
| Postconditions	| The list of open TA positions is displayed along with the recommended positions to the user.  |
| Acceptance tests  | "Make sure the correct list is rendered properly on the screen."  |
| Iteration     	| Iteration#2  |

| Use case # 7      | “As a user, I could apply for TA positions”  |
| ------------------ |--|
| Name          	| "Apply for TA positions "  |
| Users         	| "Student "  |
| Rationale         | "Help student user apply to one or more of the positions from the list of available TA positions "  |
| Triggers      	| "The student selects apply to a position."  |
| Preconditions 	| The student user is logged in and is on the view open TA positions page. |
| Actions       	| 1. The student selects the apply option. The student can apply to multiple positions one by one.<br /> 2. The system displays the form to the student.<br /> 3. The student fills the following:<br /> i.  the grade they earned when they took the course (e.g., the grade earned for CptS121).<br /> ii. the year and semester they took the course.<br /> iii. the year and semester they are applying for TAship 
| Alternative paths | "the user will be warned to fill all the information required in step 1, 2, 3 if they missing any blank "  |
| Postconditions	| “Make sure the user could successfully apply for the TA positions, the application of that student should be in the list of the class TA candidates and the status of the application should be pending in the TA profile ” |
| Acceptance tests  | "Make sure the correct list is rendered properly on the screen."  |
| Iteration     	| “Iteration#1”  |

| Use case # 8      | “As a user, I could see all reviews and write reviews for courses”  |
| ------------------ |--|
| Name            |  “Add review”  |
| Users         	| “Anonymous User - TA and other students” |
| Rationale     	| When a new TA joins the university, the admin user adds their information to the system.  |
| Triggers      	| The admin intends to add a new TA |
| Preconditions 	| The new TA’s information is not already in the system.  |
| Actions       	| 1. The user indicates to add a new TA in the application.<br /> 2. The System will display the "Add TA" page.<br /> 3. The user will then enter TA’s name and lastname, choose their academic title from the listed options, and select their primary campus. The user then submits the form.<br /> 4. The system validates the entered name and last name (should be less than 60 characters and should not include invalid characters).<br /> 5. The system will save TA’s information to the system and acknowledge that the professor is added.<br /> 6. The system will navigate to the "Find Your TA" page.  |
| Postconditions	| The new TA information is added to the system and they appear in the list of the TA on the “Find Your TA” page |
| Acceptance tests  | Check whether :<br /> (i) the new TA appears in the "Find your TA" page;<br /> (ii) the TA’s information is saved correctly.  |
| Iteration     	| iteration#3 |

| Use case # 9      | “As a user, I want to cancel my TA application while pending when I lose        interest in said position” |
| ------------------ |--|
| Name              | Withdraw |
| Users             | Students |
| Rationale         | Students don’t want to apply for that TA position anymore |
| Triggers          | Cancel TA’s application admission |
| Preconditions     | application are in pending  |
| Actions           |1. Student enter the TA application page.<br />2. “Cancel “ button at the end of the form indicate to the student to cancel the form.<br />3.Student enter the “Cancel” button to finalize the process |
| Alternative paths | In 3. Another prompt window asking the student if they are sure to cancel|
| Postconditions    | TA application pending form is canceled |
| Acceptance tests  | Make sure the TA application pending form can’t be track anymore  |
| Iteration         | Iteration#1 |

| Use case # 10      | As a user, I could create a instructor account and enter the profile information |
| ------------------ |--|
| Name          	| Create a instructor account and enter the profile information |
| Users         	| Admin  |
| Rationale         | When a new instructor joins the university, the admin user adds their information to the system |
| Triggers      	| The instructor user intends to build a profile |
| Preconditions 	| The new instructor user should not have a profile save in the system before and the student has accessed the account creation page.|
| Actions       	|” 1. The student sets the account username and password (username should be the WSU email).<br />2. The instructor enters contact information (name, last name, WSU ID, email, phone) |
| Alternative paths | After step 2, the instructor skips entering additional information. In this case, the profile is created but the additional fields are left empty.  |
| Postconditions	| The user account is created in the database.  |
| Acceptance tests  | Make sure the user account exists in the database.  |
| Iteration     	| Iteration # 1  |

**Include a swim-lane diagram that illustrates the message flow and activities for following scenario:**
“A student applies to a research position; initially its status will appear as “Pending”. The faculty who created that position reviews the application and updates the application status to either “Approved for Interview”, or “Hired”, or “Not hired”. The updated status of the application is displayed on the student view.
The student may delete the pending applications (i.e., whose status is still “Pending”. )”

![image](https://user-images.githubusercontent.com/100057129/195516897-93e9ef3e-d108-45db-bfde-2ba3730cde87.png)

----
## 2.3 Non-Functional Requirements

1. [Performace]:  [The page load time should be under 1s for every inputs.]
2. [Availabity]:  [24/7 except when downtime for maintenace.]
3. [Maintenace]:  [The first day of every months as the default.]
4. [Capacity]:  [Hold up to 30,000 applicants stored data max capacity will dynamically change when reach via maintenace. ]
5. [Data integrity]:  [All data will stored in a database.]
6. [Recoverabilty]:  [In case of major failure causing the software to shutdown, should be able to retrieve stored data and maintenace will be in progress.]
7. [Security]:  [Only authorized WSU students and staff members can access.]

----
# 3. User Interface

<img width="815" alt="Screen Shot 2022-10-12 at 11 51 56 PM" src="https://user-images.githubusercontent.com/73681258/195523119-d6736521-bc8a-41c8-a865-fd11bff096a1.png"><img width="798" alt="Screen Shot 2022-10-12 at 11 35 21 PM" src="https://user-images.githubusercontent.com/73681258/195521607-a94a6ca1-953a-4c58-aa93-55a60e8d06fc.png">
<img width="870" alt="Screen Shot 2022-10-12 at 11 35 13 PM" src="https://user-images.githubusercontent.com/73681258/195521978-60aaa625-e104-4b4f-8c11-cdf984cdcece.png">
<img width="855" alt="Screen Shot 2022-10-12 at 11 34 08 PM" src="https://user-images.githubusercontent.com/73681258/195522004-343fefcf-b814-4854-8138-29b2a4b30b96.png">

<img width="854" alt="Screen Shot 2022-10-12 at 11 36 02 PM" src="https://user-images.githubusercontent.com/73681258/195522027-ef20fc6a-2a9a-46bd-b31e-382719a94dd3.png">
<img width="861" alt="Screen Shot 2022-10-12 at 11 35 57 PM" src="https://user-images.githubusercontent.com/73681258/195522052-51f19f45-1975-422f-81d0-1d6d1e6623d9.png">
<img width="902" alt="Screen Shot 2022-10-12 at 11 49 15 PM" src="https://user-images.githubusercontent.com/73681258/195522683-6233128b-b2d7-4111-ab66-fdc7ede4c231.png"><img width="863" alt="Screen Shot 2022-10-12 at 11 35 50 PM" src="https://user-images.githubusercontent.com/73681258/195522074-ead24fea-10f2-435d-917b-9fb425357796.png">

<img width="847" alt="Screen Shot 2022-10-12 at 11 35 42 PM" src="https://user-images.githubusercontent.com/73681258/195522119-c0564584-aa6f-47e0-a076-ba46941b18f4.png">



----
# 4. Product Backlog

https://github.com/WSU-CptS322-Fall2022/termproject-everest/issues

----
# 4. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
----
