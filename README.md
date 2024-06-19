# Assignment Solver

## Project Description

Assignment Solver is an innovative project designed for hackathons. It offers the following features:

1. Accepts PDF or image files as input.
2. Extracts text from the input and provides answers to the questions found within.
3. Paraphrases the output to prevent AI plagiarism.
4. Outputs a human-written PDF.

Frontend was developed with the assistance of [Ali Hassan](https://github.com/AliHM15).

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/kill3rstabs/AssignmentSolver.git
```

### Step 2: Setting Up the Frontend
  
1. Navigate to the frontend directory:
    ```bash
     cd frontend
    ```
  2. Install the necessary dependencies:
     ```bash
     npm install
     ```
  3. Create a new .env file
  4. Copy .env.example content in .env
  5. Replace backend URL with your local backend url
  6. Start the frontend server:
     ```bash
     npm start
     ```
### Step 3: Setting Up the Backend:
  1. Navigate to the backend directory:
     ```bash
     cd Backend
     ```
 2. Create a Virtual Environment:
    ```bash
    python -m venv venv
    ```
 3. Activate the Virtual Environment:
    #### On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    #### On MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```
 4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
 5. Create a new .env file
 6. Copy .env.example content in .env
 7. Replace the huggingface token with your token:
    https://huggingface.co/docs/hub/en/security-tokens
 8. Start the backend server:
    ```bash
    python manage.py runserver
    ```

# Demo Images:
### Upload your document:
![Upload the document](https://i.ibb.co/gSTwMjQ/1.png)

### Edit the converted text as per your needs and generate the Assignment:
![Upload the document](https://i.ibb.co/TgKfFTV/2.png)

### Generated Assignment PDF:
![Upload the document](https://i.ibb.co/HB1bQNB/3.png)

    
      
    
     
     
     
