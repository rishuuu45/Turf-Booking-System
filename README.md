🏏 TurfMaster - Turf Booking System (Flask)

A modern and professional Turf Booking System built using Python Flask with a premium UI, real-time booking system, and secure admin dashboard.

🚀 Ideal for college projects, mini projects, and portfolio.

📌 Features
🎨 Modern UI
Gradient Background (Purple/Blue)
Glassmorphism effect (Blur transparent cards)
Smooth animations & hover transitions
Fully responsive design (Mobile + Desktop)
🏟️ 24 Pre-loaded Pune Turfs

Includes multiple sports categories:

🏏 Cricket Grounds (5)
Deccan Gymkhana Cricket Ground – ₹2000/hr
Wakad Cricket Club – ₹1800/hr
Kondhwa Cricket Turf – ₹1600/hr
Kharadi Cricket Stadium – ₹2500/hr
And more...
⚽ Football Arenas (4)
Shivaji Nagar Football Arena – ₹1800/hr
Hinjewadi Sports Turf – ₹2200/hr
Pimpri-Chinchwad Football Ground – ₹1500/hr
Fursungi Football Arena – ₹1400/hr
🏸 Badminton Courts (4)
Kothrud Badminton Academy – ₹800/hr
Hadapsar Badminton Center – ₹600/hr
Yerawada Badminton Hall – ₹700/hr
And more...
🎾 Tennis Courts (4)
Koregaon Park Tennis Club – ₹1200/hr
Katraj Tennis Academy – ₹1000/hr
Undri Tennis Courts – ₹950/hr
And more...
🏀 Basketball Courts (3)
Viman Nagar Basketball Arena – ₹1000/hr
Pashan Basketball Court – ₹900/hr
Warje Basketball Complex – ₹850/hr
🏟️ Multi-Sport Complexes (4)
Balewadi Sports Complex – ₹3500/hr (Olympic Standard)
Magarpatta City Sports Complex – ₹3000/hr
Baner Sports Complex – ₹2500/hr
And more...

Each turf includes:

Name & Location 📍
Rating ⭐
Price per hour 💰
Capacity 👥
Amenities 🎯
Description 📝
Images (Unsplash)
📅 Booking System
Date selection using calendar
12 time slots (6 AM to 10 PM)
Real-time slot availability check
Booked slots shown in red
User form (Name + Phone)
Booking confirmation message
📌 My Bookings
View all bookings in one place
Cancel booking option
Slot automatically becomes available again
🔒 Admin Panel

Admin panel is protected with login.

Default Admin Credentials

⚠️ Change before deployment!

Username: admin
Password: admin123
Admin Features
Complete bookings database view
Statistics dashboard (Revenue, total bookings, etc.)
Search bookings by name/phone/turf
Sort bookings by any column
Delete bookings
Export bookings to CSV
💾 Data Storage
All bookings are stored in bookings.json
Data remains safe even after restarting the server
🚀 Installation & Setup
✅ Requirements
Python 3.7+
Flask
Step 1: Install Flask
pip install flask
Step 2: Run the Project
cd turf_booking_python
python app.py
Step 3: Open in Browser
http://localhost:5000
🔐 Admin Login
Admin Login URL
http://localhost:5000/admin/login

After login, you will be redirected to the database dashboard automatically.

📁 Project Structure
turf_booking_python/
│
├── app.py                      # Main Flask application
├── bookings.json               # Booking data (auto-created)
│
├── templates/
│   ├── index.html              # Home page
│   ├── turf_details.html       # Turf booking page
│   ├── my_bookings.html        # User bookings page
│   ├── database.html           # Admin database dashboard
│   └── admin_login.html        # Admin login page
│
└── static/
    └── css/
        └── style.css           # Styling + animations
🌐 Pages Overview
🏠 Home Page (/)
Displays all turfs in a grid
Turf cards show price, rating, location
"Book Now" button available
🏟️ Turf Details Page (/turf/<id>)
Full turf details
Date picker
Slot selection
Booking form
Real-time availability check
📌 My Bookings Page (/my_bookings)
Displays all bookings
Cancel booking button
🔐 Admin Login Page (/admin/login)
Secure login page
Credentials required
📊 Admin Dashboard (/database)

🔒 Protected route (Login required)

Booking database view
Statistics cards
Search + sort + filter
Export CSV option
Delete booking option
🔧 API Endpoints
Method	Endpoint	Description
GET	/	Home page
GET	/turf/<id>	Turf details page
POST	/check_slot	Check slot availability
POST	/book	Book a turf
GET	/my_bookings	View all bookings
POST	/cancel_booking/<id>	Cancel booking
GET	/api/bookings	Get bookings JSON
GET/POST	/admin/login	Admin login
GET	/admin/logout	Admin logout
GET	/database	Admin database dashboard
🔐 Security Notes
Change Admin Credentials

Edit in app.py:

ADMIN_USERNAME = "your_username"
ADMIN_PASSWORD = "your_strong_password"

⚠️ Never deploy with default credentials.

🎨 Customization
Change Theme Colors

Edit:

static/css/style.css

Example:

background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
Add New Turf

Edit list inside app.py:

TURFS_DATA = [...]
Change Time Slots

Edit inside app.py:

TIME_SLOTS = [...]
🐛 Troubleshooting
Flask not installed?
pip install flask
Port already in use?

Change this line in app.py:

app.run(debug=True, port=5000)
Bookings not saving?
Ensure folder has write permission
Ensure bookings.json exists
📌 Future Improvements (Optional)
User login/signup system
Database integration (SQLite/MySQL)
Payment gateway integration
Email/SMS booking confirmation
Admin role management
❤️ Built With
Python 🐍
Flask ⚡
HTML + CSS + JS 🎨
JSON Storage 💾
⭐ Support

If you like this project, give it a ⭐ on GitHub.

🎉 Enjoy TurfMaster!

Made with ❤️ for sports lovers 🚀
