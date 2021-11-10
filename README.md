# LOG PROCESSOR

## Description

Log processor for nginx or apache that extracts user and user sessions and calculates other types of useful data for bot detection or traffic analysis. The users are calculated taking into account the ip and the user agent as identifier. In the data model you can see all the data that users and their sessions have.

## How to use

1. Clone project
2. Install psycopg2
3. Create a postgresql database and restore it using the database backup
4. Change app.properties with your configuration
5. Run 
6. Check database

## Database model

[Database model](https://imgur.com/gallery/j1xi9y3)