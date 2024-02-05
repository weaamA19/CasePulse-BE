# CasePulse Web Application

CasePulse, is a web application designed to assist legal professionals in effectively managing their legal cases.  This system provides a centralized platform for storing, tracking, and organizing crucial information related to legal matters. It's developed to enable users, especially legal professionals, to efficiently handle their legal cases. The system provides features such as adding new cases, tracking case progress, uploading documents, and setting reminders for crucial dates.


##  CasePulse Application Screenshots

![Landing Page](https://i.imgur.com/FS7yMK8.png)
![Adding Case Page](https://i.imgur.com/ZO162qN.png)
![Case Dashboard Page](https://i.imgur.com/OfOJyBZ.png)
![Case Details Page](https://i.imgur.com/BXG9Re9.png)
![Inactive Case Feature](https://i.imgur.com/q6q1VCt.png)
![Adding Document Page](https://i.imgur.com/86dhfnX.png)
![Document Preview Page](https://i.imgur.com/EprwumB.png)
![Updating Reminder Page](https://i.imgur.com/bf9prHn.png)
![Today's Reminder Page](https://i.imgur.com/JaFKDL1.png)
![Profile Page](https://i.imgur.com/X3a0Hku.png)
![Changing Password Page](https://i.imgur.com/th6gjNC.png)



## Technologies Used:
- Django
- PostgreSQL
- Postman
- React
- Bootstrap


## Trello Link
[Trello Board](https://trello.com/invite/b/dqUli0cW/ATTI85454b6de5429cc1e12b1b346d30b7915A282A39/sei7-project-4)

## Entity-Relationship Diagram (ERD)

![ERD Example](https://i.imgur.com/0Z7a1us.png)


#### Relationships
- A Lawyer can be associated with multiple Cases (many-to-many relationship).
- A Case can have multiple Documents (1-to-many relationship).
- A Case can have multiple Reminders (1-to-many relationship).

## Wireframes

![Wireframes](https://i.imgur.com/blXopLj.png)

# User Stories

## User Experience
 **As a Lawyer,**
   - I want to log in securely to the Case Management System using my credentials.
   - *Objective:* Ensure a secure and user-friendly login experience for accessing the system.

 **As a Lawyer,**
   - I want to see a comprehensive dashboard, providing an overview of active cases, upcoming reminders, and recent case-related activities.
   - *Objective:* Provide users with a centralized view of critical information for efficient case management.

 **As a Lawyer,**
   - I want to add a new case by providing essential details such as title, description, start date.
   - *Objective:* Enable users to initiate new cases with ease, capturing all necessary information for proper case management.

 **As a Lawyer,**
   - I want to upload relevant documents for each case, including titles and descriptions.
   - *Objective:* Facilitate collaboration by allowing lawyer to easily connect and assign multiple lawyers to a particular case.

 **As a Lawyer,**
   - I want to set reminders for important dates associated with each case.
   - *Objective:* Ensure users stay informed about critical events, such as court hearings, through timely reminders.

 **As a Lawyer,**
   - I want to set reminders for important dates associated with each case.
   - *Objective:* Ensure users stay informed about critical events, such as court hearings, through timely reminders.


## Getting Started

- Clone the CasePulse repository to your local environment.
- Install required dependencies using `npm install`.
- Start the application by running `npm start` for the frontend and `python manage.py runserver` for backend.

## Key Features

1. **Centralized Case Management:** The system provides a centralized platform for legal professionals to store and manage all their legal cases in one place. Users can easily add new cases, track case progress, and access details, eliminating the need for manual record-keeping and enhancing overall organization and efficiency.

2. **Efficient Document Management:** Users can upload and associate relevant documents with each case. This feature enables easy access to case-related documents, eliminating the hassle of physical paperwork. Multiple users can collaborate on documents simultaneously, enhancing teamwork and streamlining the document management process.

3. **Reminders and Deadlines:** The system facilitates setting reminders for important dates and deadlines associated with each case. Users can ensure they stay on top of critical tasks, such as court appearances, filing deadlines, or client meetings. Reminders help prevent missed deadlines, reducing the risk of negative consequences and improving overall case management efficiency.



## Future Features

- **Version Control:** Version Control tracks document changes, allowing users to review and revert to previous versions. It ensures document accuracy, facilitates collaboration, and provides a clear overview of revisions.

- **Notification:** The Notification feature keeps users informed about crucial events, updates, and deadlines. Real-time notifications within the system or via email ensure users stay proactive in managing their legal cases.

- **Add Category Model:**  This enhancement introduces case categorization, allowing users to specify case types (e.g., "Contract Dispute"). It streamlines organization, making it easier to filter, search, and report on cases based on their legal categories or court type.

