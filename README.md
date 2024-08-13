# Backend-AssessMent

## Problem statement: 
A prototype of a “Commodity Rental Solution” needs to be developed. On this product, users can sign up as lenders or renters. A lender can list a commodity (eg. a blazer, shoes, laptop) for rent and quote a minimum monthly charge for renting the commodity. A renter can put a bid for the available commodities on the product. Lender can accept a renter’s bid as per his liking and the commodity will get assigned to that user for the specified period mentioned from the renter’s end.

## Primary Tasks
Design the above system using any web framework (preferable Django / RoR) and appropriate tables using a relational database of your choice (eg. MySQL, PostgreSQL)
Think of appropriate tables for the same
Handle the state management of the entities appropriately as per the constraints provided to ensure the complete lifecycle of the entity as specified in the document is followed
The minimum specifications for all the APIs have been provided. Candidates are welcome to make the APIs richer by thinking from the end user’s perspective. 
Authentication should be handled using JWT tokens

## Constraints:
1.One lender can list multiple commodities available for rent
2.A renter can place bids as long as the commodity is available. 
3.Logic for assigning the commodity to a renter is as follows:
   a) Suppose a Lender L1 quoted an amount of $ 100 / month
       - Renter R1 placed a bid for $120/month for 6 months
       - Renter R2 placed a bid for $140/month for 2 months
       - Renter R3 placed a bid for $300/month for 1 month
   b)Lender can choose between R1, R2 and R3
4.A renter cannot place a bid for an amount lesser than the minimum amount quoted by the lender
5.A renter cannot place a bid on a commodity that has already been rented out
6.Available item categories:
  - Electronic Appliances
  - Electronic Accessories
  - Furniture
  - Men’s wear
  - Women’s wear
  - Shoes

# Commodity Rental Solution - Backend API

## Overview
This project is a prototype of a "Commodity Rental Solution" where users can sign up as lenders or renters. Lenders can list commodities for rent, and renters can place bids on these commodities. The lender can choose to accept any bid, thereby renting out the commodity for a specified period.

## Key Features
- User authentication with JWT tokens.
- Lenders can list commodities for rent.
- Renters can place bids on listed commodities.
- Lenders can accept bids and rent out commodities.
- Commodity lifecycle management, including listing, renting, and re-listing.

## API Endpoints

### 1. User Signup
**Endpoint**: `POST /user/signup/`

**Request Params:**
- `type`: "renter" / "lender"
- `email`: string
- `first_name`: string
- `last_name`: string

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "User created successfully",
        "payload": {
            "user_id": <int>
        }
    }
    ```
- **Failure:**
    ```json
    {
        "status": "error",
        "message": "User could not be created",
        "payload": {}
    }
    ```

### 2. List a Commodity
**Endpoint**: `POST /commodity/list/` (Authenticated)

**Request Params:**
- `item_name`: string
- `item_description`: string
- `quote_price_per_month`: float
- `item_category`: string (must be one of the predefined categories)

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Commodity listed successfully",
        "payload": {
            "commodity_id": <int>,
            "quote_price_per_month": <float>,
            "created_at": <timestamp>
        }
    }
    ```
- **Failure:**
    ```json
    {
        "status": "error",
        "message": "Commodity could not be listed",
        "payload": {}
    }
    ```

### 3. Get Available Commodities
**Endpoint**: `GET /commodity/list/` (Authenticated)

**Query Params (Optional):**
- `item_category`: string

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Available commodities fetched successfully",
        "payload": [
            {
                "commodity_id": <int>,
                "created_at": <int>,
                "quote_price_per_month": <float>,
                "item_category": <str>
            },
            ...
        ]
    }
    ```

### 4. Place a Bid on a Commodity
**Endpoint**: `POST /commodity/bid/` (Authenticated)

**Request Params:**
- `commodity_id`: int
- `bid_price_month`: float
- `rental_duration`: int (in months)

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Bid created successfully",
        "payload": {
            "bid_id": <int>,
            "commodity_id": <int>,
            "created_at": <timestamp>
        }
    }
    ```

### 5. Get Bids for a Commodity
**Endpoint**: `GET /commodity/<id>/bids/` (Authenticated)

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Bids for commodity fetched successfully",
        "payload": [
            {
                "bid_id": <int>,
                "created_at": <int>,
                "bid_price_month": <float>,
                "rental_duration": <int>
            },
            ...
        ]
    }
    ```

### 6. Accept a Bid for a Commodity
**Endpoint**: `POST /commodity/<id>/accept-bid/` (Authenticated)

**Request Params:**
- `bid_id`: int

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Bid has been accepted successfully",
        "payload": {}
    }
    ```

### 7. Get My Commodities
**Endpoint**: `GET /commodity/my-commodities/` (Authenticated)

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Commodities fetched successfully",
        "payload": [
            {
                "commodity_id": <int>,
                "created_at": <int>,
                "quote_price_per_month": <float>,
                "item_category": <str>,
                "status": "listed" OR "rented" OR "available",
                "accepted_bid_price": <float> OR null,
                "accepted_rented_period":  <int> OR null
            },
            ...
        ]
    }
    ```

### 8. [BONUS] Update a Bid for a Commodity
**Endpoint**: `POST /commodity/re-bid/` (Authenticated)

**Request Params:**
- `commodity_id`: int
- `bid_price_month`: float
- `rental_duration`: int (in months)

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Bid revised successfully",
        "payload": {
            "bid_id": <int>,
            "commodity_id": <int>,
            "bid_price_month": <float>,
            "rental_duration": <int>,
            "created_at": <timestamp>
        }
    }
    ```

### 9. [BONUS] Re-list a Commodity
**Endpoint**: `POST /commodity/re-list/` (Authenticated)

**Request Params:**
- `commodity_id`: int
- `[OPTIONAL] quote_price_per_month`: float

**Response:**
- **Success:**
    ```json
    {
        "status": "success",
        "message": "Commodity re-listed successfully",
        "payload": {
            "commodity_id": <int>,
            "quote_price_per_month": <float>,
            "created_at": <timestamp>,
            "updated_at": <timestamp>
        }
    }
    ```
- **Failure:**
    ```json
    {
        "status": "error",
        "message": "Commodity could not be re-listed",
        "payload": {}
    }
    ```

## Data Model
### Users Table
- `id`: int (Primary Key)
- `type`: enum ("renter", "lender")
- `email`: string (unique)
- `first_name`: string
- `last_name`: string
- `created_at`: timestamp
- `updated_at`: timestamp

### Commodities Table
- `id`: int (Primary Key)
- `item_name`: string
- `item_description`: string
- `quote_price_per_month`: float
- `item_category`: string
- `status`: enum ("listed", "rented", "available")
- `created_at`: timestamp
- `updated_at`: timestamp
- `lender_id`: Foreign Key (Users.id)

### Bids Table
- `id`: int (Primary Key)
- `bid_price_month`: float
- `rental_duration`: int (in months)
- `created_at`: timestamp
- `updated_at`: timestamp
- `renter_id`: Foreign Key (Users.id)
- `commodity_id`: Foreign Key (Commodities.id)

## Constraints
- A lender can list multiple commodities.
- A renter can place multiple bids as long as the commodity is available.
- A renter cannot bid below the minimum quoted price.
- A renter cannot bid on a rented commodity.
- Lenders cannot place bids on commodities.
- Renters cannot list commodities for rent.
- Commodities must be re-listed manually by lenders to accept new bids after the rental period ends.

## Bonus Features
- Bid revision by renters.
- Re-listing of commodities by lenders.

## Authentication
Authentication is handled using JWT tokens. Secure all endpoints except user signup.

## Setup Instructions
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt` 
3. Set up the database using `python manage.py migrate` for Django
4. Start the server using `python manage.py runserver` for Django
5. Use an API client like Postman to interact with the API.

## Testing
Automated tests can be run using the command:
- Django: `python manage.py test`

## Conclusion
This backend API is a foundational implementation of a commodity rental solution. It covers user management, commodity listing, bid placement, and acceptance, along with lifecycle management of commodities.

