# Real-Time Weather Monitoring System

## Overview
This system monitors weather conditions in various metros of India, providing summarized insights and alerts.

## Setup
1. Clone the repository.
2. Ensure Docker and Docker Compose are installed.
3. Create a `.env` file or set the `OPENWEATHER_API_KEY` environment variable.
4. Run `docker-compose up --build` to start the application.

## API Endpoints
- Currently, no API endpoints are exposed. The application runs in the background and updates the database.

## Dependencies
- Python 3.x
- Flask
- psycopg2
- requests

## Usage
Monitor the console for real-time alerts and summaries.
