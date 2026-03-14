# 🌍 TravelUs – AI Powered Travel Website

TravelUs is a **full-stack travel booking web application** that allows users to explore travel destinations, book trips, register/login accounts, and interact with an AI travel assistant chatbot.

The project integrates **frontend web technologies (HTML, CSS, JavaScript)** with a **Python Flask backend and database layer** to create a responsive and interactive travel platform.

---

# ✨ Features

## 🧭 Travel Website Interface

* Modern **responsive travel website UI**
* Navigation menu with sections:

  * Home
  * Packages
  * Book
  * Services
  * Gallery
  * Reviews
  * Contact

---

## 🎥 Dynamic Homepage

* Background **travel video slider**
* Interactive video switching controls
* Responsive design for mobile and desktop.

---

## 🔐 User Authentication

Users can:

* Register new accounts
* Login with existing credentials
* Switch between login and registration forms

Authentication requests are handled through the **Flask backend API**.

---

## 📅 Travel Booking System

Users can book travel packages by entering:

* Destination
* Number of guests
* Number of rooms
* Check-in date
* Check-out date

Booking information is sent to the backend and stored in the database.

---

## 🤖 AI Travel Chatbot

A floating chatbot icon allows users to access a **Travel AI assistant** that can help with travel queries.

Examples:

* Travel recommendations
* Destination suggestions
* Travel information

The chatbot opens in a new tab and it is a fully made website chatbot app but its files are not included.

---

## ⭐ Customer Reviews

* Swiper.js powered **review slider**
* Displays multiple travel testimonials
* Auto-scrolling carousel.

---

## 🤝 Partner Brands Carousel

Displays travel partner brands using a responsive **logo slider**.

---

## 🖼️ Travel Gallery

Image gallery showcasing travel destinations with hover effects and discover buttons.

---

## 📱 Fully Responsive Design

The website adapts to:

* Desktop
* Tablet
* Mobile devices

---

# 🏗️ Project Architecture

The project follows a **Frontend + Backend architecture**.

```
User
 ↓
Browser
 ↓
HTML (Structure)
 ↓
CSS (Design)
 ↓
JavaScript (Interaction)
 ↓
Flask Backend (app.py)
 ↓
Database Handler (view_travel_db.py)
 ↓
Database
```

# How to set up:

* First download the repository.
* Set up environmental variables and install necessary python libraries inside the folder.
* Then first run the app.py and keep it running.
* Then explore the website and only till app.py is running,all the data entered in  registration form,login form or booking form will be included in the database.
* Then at the same time after that when you start running the view_travel_db.py file,all the data stored will be shown.
* When you click the chatbot sign it will open the chatbot website in another tab.

# 💻 Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript
* Swiper.js
* Font Awesome

## Backend

* Python
* Flask
* REST API

## Database

* SQLite / relational database

---

# ⚙️ Key JavaScript Functionalities

### Navigation Menu

Responsive menu toggle for mobile devices.

### Search Bar

Click icon to open/close search bar.

### Login & Register Forms

Popup authentication forms with form switching.

### Video Slider

Users can change the homepage video dynamically.

### Swiper Sliders

* Review carousel
* Brand logo slider

### Chatbot Integration

Floating chatbot icon that opens the AI travel assistant.(this part is included in html file)

---

# 🖥️ Backend API (Flask) (app.py)

The Flask server handles API requests from the frontend.

### API Endpoints

#### Register

```
POST /register
```

Registers a new user.

---

#### Login

```
POST /login
```

Authenticates existing users.

---

#### Book Travel

```
POST /book
```

Stores booking details submitted from the booking form.

---

# 🗄️ Database Layer – view_travel_Db.py

It is for administrative use.This module handles **database operations** including:

* Fetching users
* Verifying login credentials
* Storing travel bookings
* Retrieving booking records

It acts as the **data access layer** between Flask and the database.

---

# 🔄 System Workflow

### 1️⃣ User opens website

The browser loads:

* HTML
* CSS
* JavaScript

---

### 2️⃣ User interacts with the interface

Possible actions:

* Login
* Register
* Book travel
* Browse packages
* Use chatbot

---

### 3️⃣ Frontend sends request

JavaScript sends API requests using:

```javascript
fetch()
```

Example:

```
POST /login
POST /register
POST /book
```

---

### 4️⃣ Flask backend processes request

`app.py` receives the request and calls functions from:

```
view_travel_Db.py
```

---

### 5️⃣ Database operation

The database module performs SQL operations such as:

* Insert
* Retrieve
* Verify

---

### 6️⃣ Response returned to frontend

Flask sends JSON response back to the browser, and JavaScript updates the UI.
---

Project created as part of a **travel AI web application project** demonstrating full-stack web development with Flask.



