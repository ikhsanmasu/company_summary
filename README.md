# Company Summary Automation

This project automates the process of generating company summaries using OpenAI's GPT models and Google Sheets. It reads a list of company names from a Google Spreadsheet, generates detailed profiles and concise summaries for each company, and writes the results back to the spreadsheet.

## Features

- Fetches company names from a Google Spreadsheet.
- Uses OpenAI GPT (via LangChain) to generate company profiles and summaries.
- Writes the results (company name and summary) back to the spreadsheet.
- Modular code with separate agents for profile generation and summarization.

## Project Structure

```
.
├── agent_company_profile.py
├── agent_summary.py
├── config.yaml
├── main.py
├── requirements.txt
├── spreedsheet_api.py
├── .env
├── .gitignore
```

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd company_summary
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Configure API Keys

- **OpenAI API Key:**  
  Add your OpenAI API key to the `.env` file:
  ```
  OPENAI_API_KEY=your-openai-api-key
  ```
- **Google Service Account:**  
  Update `config.yaml` with your Google service account credentials and spreadsheet details.

### 4. Prepare your Google Spreadsheet

- Ensure your spreadsheet has a sheet for company names (e.g., "Company List" in column A starting from A2).
- Set the sheet names and spreadsheet ID in `config.yaml`.

## Usage

Run the main script:

```sh
python main.py
```

This will:
- Read company names from the configured sheet.
- Generate a profile and summary for each company.
- Write the results to the summary sheet.

## Files Overview

- [`main.py`](main.py): Main entry point; orchestrates reading, processing, and writing.
- [`agent_company_profile.py`](agent_company_profile.py): Generates detailed company profiles.
- [`agent_summary.py`](agent_summary.py): Summarizes company profiles.
- [`spreedsheet_api.py`](spreedsheet_api.py): Handles Google Sheets API interactions.
- [`config.yaml`](config.yaml): Configuration for OpenAI and Google Sheets.
- [`requirements.txt`](requirements.txt): Python dependencies.

## License
# Company Summary Automation

This project automates the process of generating company summaries using OpenAI's GPT models and Google Sheets. It reads a list of company names from a Google Spreadsheet, generates detailed profiles and concise summaries for each company, and writes the results back to the spreadsheet.

## Features

- Fetches company names from a Google Spreadsheet.
- Uses OpenAI GPT (via LangChain) to generate company profiles and summaries.
- Writes the results (company name and summary) back to the spreadsheet.
- Modular code with separate agents for profile generation and summarization.

## Project Structure

```
.
├── agent_company_profile.py
├── agent_summary.py
├── config.yaml
├── main.py
├── requirements.txt
├── spreedsheet_api.py
├── .env
├── .gitignore
```

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd company_summary
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Configure API Keys

- **OpenAI API Key:**  
  Add your OpenAI API key to the `.env` file:
  ```
  OPENAI_API_KEY=your-openai-api-key
  ```
- **Google Service Account:**  
  Update `config.yaml` with your Google service account credentials and spreadsheet details.

### 4. Prepare your Google Spreadsheet

- Ensure your spreadsheet has a sheet for company names (e.g., "Company List" in column A starting from A2).
- Set the sheet names and spreadsheet ID in `config.yaml`.

## Usage

Run the main script:

```sh
python main.py
```

This will:
- Read company names from the configured sheet.
- Generate a profile and summary for each company.
- Write the results to the summary sheet.

## Files Overview

- [`main.py`](main.py): Main entry point; orchestrates reading, processing, and writing.
- [`agent_company_profile.py`](agent_company_profile.py): Generates detailed company profiles.
- [`agent_summary.py`](agent_summary.py): Summarizes company profiles.
- [`spreedsheet_api.py`](spreedsheet_api.py): Handles Google Sheets API interactions.
- [`config.yaml`](config.yaml): Configuration for OpenAI and Google Sheets.
- [`requirements.txt`](requirements.txt): Python dependencies.

## License
This project is for educational