# 📁 ShareSafely

## Project Workflow

<div align="center">
<img alt-text="Project Workflow" src="https://github.com/user-attachments/assets/794e0ef7-3888-4e16-8966-68400a07b8ec">
</div>


## Project Overview

Welcome to the documentation for **ShareSafely**, a secure file-sharing web application developed using Azure services. This application provides a safe platform for managing file uploads to Azure Blob Storage, generating unique and time-limited links for secure sharing.

### Features

- **Secure File Uploads**: Files are uploaded securely to Azure Blob Storage, ensuring data privacy and security.
- **Time-Limited Sharing**: The application generates unique URLs with restricted access duration, allowing only authorized users to download files.
- **Automated Cleanup**: Azure Functions automatically delete expired files periodically, keeping storage organized and secure.
- **Monitoring**: Integrated with Azure Monitor for tracking application health and performance.
- **Secure Credential Management**: Sensitive credentials are securely stored and managed with Azure Key Vault.

### Technologies Used

- **Azure Blob Storage**: For secure file storage and management.
- **Azure Web Apps**: Hosting platform for the web application.
- **Azure Key Vault**: Secure storage and management of application secrets.
- **Azure Monitor**: Real-time monitoring and alerts for application health.
- **Python (Flask)**: Backend framework used for application development.


## Setup and Configuration

### Prerequisites

To get started with **ShareSafely**, you’ll need:

- An Azure account
- A Python environment
- Visual Studio Code or another code editor

### Steps

#### 1. Azure Blob Storage Setup

The first step is setting up an Azure Blob Storage account named `sharesafelystrg` with a container `uploads` dedicated to storing uploaded files. Key security configurations include:

- Enabling **Secure Transfer Required** for encrypted connections
- Disabling **Blob Anonymous Access** to ensure files are only accessed by authorized users
- Enabling **Soft Delete** for both blobs and containers to recover accidentally deleted files

#### 2. Web Application Development

The application was developed with Flask (Python) to manage file uploads, SAS token generation, and user access. The project is structured as follows:

ShareSafelyApp/
├── app.py
├── templates/
│ ├── upload.html
│ └── link.html
└── static/
└── styles.css 


- **app.py**: Contains core application logic for handling uploads and generating secure access links.
- **upload.html** and **link.html**: HTML templates for the user interface.
- **styles.css**: CSS for styling the application's front end.

#### 3. Secure Credentials with Azure Key Vault

Azure Key Vault is used to securely manage and retrieve the Storage Account key, ensuring sensitive data remains protected and not exposed in the source code. The application accesses these secrets securely at runtime.

#### 4. Deploying to Azure Web Apps

The web application was deployed to **Azure Web Apps** using Visual Studio Code. Key configurations include:

- Setting environment variables (`KEY_VAULT_URI` and `SECRET_NAME`) for seamless access to secrets
- Enabling a system-assigned **Managed Identity** for secure, role-based access to Azure Key Vault without exposing credentials

#### 5. Monitoring and Maintenance

**Azure Monitor** was configured to track application metrics such as CPU usage, response times, and error rates. Alerts notify administrators of critical issues, such as high error rates or resource utilization, enabling proactive maintenance.


### Testing


https://github.com/user-attachments/assets/7e286102-cf88-47b1-add3-d7aaa32b2c20


![Test 1](https://github.com/user-attachments/assets/130182a7-11da-41b5-b964-2a48dc31c798)
![Test 2 ](https://github.com/user-attachments/assets/6b584c46-a0e5-4e94-ab61-a2dfe06517cd)
![Test 3](https://github.com/user-attachments/assets/1de023da-1420-4c4d-bb94-c742d59d1054)


To confirm the functionality and security of the **ShareSafely** application, I conducted a comprehensive final test.

First, I accessed the ShareSafelyApp through the Azure Portal, navigating to the overview page of the deployed Web App. Using the provided Web App URL, I opened the application in my browser to begin testing its core features.

Once on the application interface, I tested the file upload functionality by selecting a file named **"bg.png"**, which was not previously stored in the **"uploads"** container. Upon clicking the upload button, the application processed the file and generated a unique, time-limited link, which opened in a new browser tab for immediate access.

To verify the expiration feature, I waited for the link to expire, as the application is designed to restrict access after **15 seconds** to enhance security. Attempting to access the link post-expiration confirmed the functionality, as access was denied, proving that the application’s time-limited sharing and security mechanisms worked effectively.

This final test confirmed that **ShareSafely** performs reliably in secure file upload, unique link generation, and automated link expiration, ensuring that it meets its intended standards for functionality and data security.

### Testing Video

The testing video demonstrates the application's core functionality in a local environment prior to deployment on Azure App Service. This pre-deployment test was conducted to verify that all main features—file upload, time-limited link generation to functioned correctly. Running the application locally ensured that each component was thoroughly checked before launching it in the Azure environment.








## Conclusion

The ShareSafely project successfully achieved a secure and efficient file-sharing web application, leveraging Azure's robust suite of services. This project exemplified comprehensive expertise across Azure Blob Storage, Azure Web Apps, Azure Key Vault, and Azure Monitor. Through extensive testing, including a detailed final validation phase, all core features—secure file uploads, time-limited link generation were confirmed to function seamlessly.

## Skills Demonstrated
- **Secure File Management**: Employed Azure Blob Storage for secure file storage, with controlled access managed through SAS tokens for reliable data security.
- **Web Application Development**: Developed a full-stack web application using Python and Flask, ensuring smooth integration between the front end and back end.
- **Credential Management**: Utilized Azure Key Vault for secure, efficient storage and retrieval of sensitive credentials, enhancing overall security protocols.
- **Monitoring**: Configured Azure Monitor to track application performance and maintain system health throughout deployment.
- **Deployment and DevOps**: Successfully deployed the application to Azure Web Apps, managing environment variables, permissions, and streamlined deployment processes.

## Repository Contents
- **Screenshots**: Visual documentation of major configuration steps and project milestones, providing a clear reference guide.
- **Source Code**: Organized in the `Source_Code` folder, this includes all code for the Flask web application, Azure Functions, and other supporting scripts.


