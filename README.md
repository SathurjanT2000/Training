# **TRAINEE MANAGEMENT APP**

## CONTENT
- [Brief](#brief)
    - [Requirements](#requirements)
    - [My approach](#my-approach)
- [Architecture](#architecture)
    - [Front-end Structure](#front-end-structure)
    - [Database Structure](#database-structure)
    - [CI Pipeline](#ci-pipeline)
- [Project Tracking](#project-tracking)
- [Risk Assessment](#risk-assessment)
- [Testing](#testing)
- [Known Issues](#risk-assessment)
- [Possible Improvement](#possible-improvement)
- [Resources](#resources)

## BRIEF <a name="brief"></a>
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.\
_C - Create_\
_R - Read_\
_U - Update_\
_D - Delete_

### Requirements <a name="requirements"></a>
- A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.
- A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship.
- Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board
- Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

### My Approach <a name="my-approach"></a>
- To satisfy **CREATE** aspect of the app:
    - Trainers will be able to create:
        - Thier own account
        - Trainee acounts
        - Goals for trainees
- To satisfy **READ** aspect of the app:
    - Trainers will be able to read:
        - Trainee's goals
    - Trainees will be able to read:
        - Trainer's details
        - Their own goals
- To satisfy **UPDATE** aspect of the app:
    - Trainers will be able to update:
        - Thier certificates
        - Their details
        - Trainee's goals
- To satisfy **DELETE** aspect of the app:
    - Trainers will be able to delete:
        - Trainee's account
## ARCHITECTURE <a name="architecture"></a>
### Front-end Structure <a name="front-end-structure"></a>

### Database Structure <a name="database-structure"></a>
![Database_structure](./pictures/Database_structure.png)
### CI pipeline <a name="ci-pipeline"></a>
![CI-pipeline](./pictures/CI-pipeline.png)
## PROJECT TRACKING <a name="project-tracking"></a>
## RISK ASSESSMENT <a name="risk-assessment"></a>
## TESTING <a name="testing"></a>
## KNOWN ISSUES <a name="known-issues"></a>
## POSSIBLE IMPROVEMENT <a name="possible-improvement"></a>
## RESOURCES <a name="resources"></a>
[Draw.io](https://app.diagrams.net/) was used to create Database Structure and CI Pipline.\
[Visual Studio Code](https://code.visualstudio.com/) was used to code.\
[Jenkins](https://www.jenkins.io/) was used as CI server.\
[Google Cloud Platform](https://console.cloud.google.com) was used for VM and database.\
[GitHub](https://github.com/) was used for version control and project tracking.
**QA Community** was used for information.\
