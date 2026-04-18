🏏 TurfMaster - Turf Booking System (Flask)

A modern, attractive, and professional Turf Booking System built using Python Flask with a beautiful UI, real-time booking, admin panel, and JSON-based storage.

🚀 Perfect for college projects, mini projects, and real-world demo apps.

✨ Features
🎨 Attractive UI
Gradient Background (Purple/Blue theme)
Glass-morphism UI cards (blur + transparency)
Smooth hover animations & transitions
Fully responsive (Mobile + Desktop)
🏟️ 24 Pre-loaded Pune Turfs

Includes categories like:

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

Name, location 📍
Rating ⭐
Price per hour 💰
Capacity 👥
Amenities 🎯
Description 📝
Images (via Unsplash)
📅 Booking System
Date selection (Calendar UI)
12 time slots (6 AM to 10 PM)
Real-time slot availability
Booked slots shown in red
User details form (Name + Phone)
Booking confirmation message with animation
📌 My Bookings Page
View all bookings in one place
Shows turf name, slot, date, price
Cancel booking feature available
🔒 Admin Panel (Secure)

Admin login required to access database.

Default Admin Credentials:

⚠️ Change these before deployment!

Username: admin
Password: admin123
Admin Features:
Complete booking database view
Statistics dashboard (Revenue, bookings, etc.)
Search and filter bookings
Export bookings to CSV
Delete bookings
Sort bookings by column
💾 Data Storage
All bookings are stored in bookings.json
Data remains safe even after restarting the server
🚀 Installation & Setup
✅ Requirements
Python 3.7+
Flask
Step 1: Install Flask
pip install flask
Step 2: Run the Application
cd turf_booking_python
python app.py
Step 3: Open in Browser
http://localhost:5000
🔐 Admin Access
Admin Login Page:
http://localhost:5000/admin/login

After login, you will be redirected to database dashboard automatically.

📁 Project Structure
turf_booking_python/
│
├── app.py                      # Main Flask application
├── bookings.json               # Bookings data (auto-created)
│
├── templates/
│   ├── index.html              # Home page (all turfs)
│   ├── turf_details.html       # Booking page
│   ├── my_bookings.html        # My bookings page
│   ├── database.html           # Admin database view
│   └── admin_login.html        # Admin login page
│
└── static/
    └── css/
        └── style.css           # All styling and animations
📄 Pages Overview
🏠 Home Page (/)
Shows all turfs in grid view
Turf details in cards
"Book Now" button for each turf
🏟️ Turf Details Page (/turf/<id>)
Full turf details
Select date
Select time slot
Booking form
Real-time slot checking
📌 My Bookings Page (/my_bookings)
View all bookings
Cancel booking button available
🔐 Admin Login Page (/admin/login)
Secure admin login
Beautiful login UI
📊 Admin Database Page (/database)

🔒 Protected (Admin login required)

View complete bookings database
Statistics dashboard
Search + filter
Export CSV
Delete booking
🔧 How to Use
👤 For Users
Open home page (/)
Choose a turf and click Book Now
Select date 📅
Select time slot ⏰
Enter name and phone number
Click Confirm Booking
Booking confirmed 🎉
To cancel booking → go to My Bookings
👨‍💻 For Admin

Open:

http://localhost:5000/admin/login
Login using credentials
Manage bookings from database dashboard
🔐 Security Tips
Change Admin Credentials (IMPORTANT)

Inside app.py, update:

ADMIN_USERNAME = 'your_username'
ADMIN_PASSWORD = 'your_strong_password'
Good Password Examples

✅ Use strong passwords like:

MyTurf@2024!Secure
Pune$ports#Admin99
Cr1ck3t&Ball@2024
Bad Passwords (Avoid)

❌

admin123
password
12345678
🎯 API Endpoints
Method	Endpoint	Description
GET	/	Home page
GET	/turf/<id>	Turf details page
POST	/check_slot	Check slot availability
POST	/book	Create booking
GET	/my_bookings	View bookings
POST	/cancel_booking/<id>	Cancel booking
GET	/api/bookings	View bookings JSON
GET/POST	/admin/login	Admin login
GET	/admin/logout	Admin logout
GET	/database	Admin database panel
🎨 Customization
🎨 Change UI Colors

Edit file:

static/css/style.css

Example:

background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
🏟️ Add More Turfs

Inside app.py, update:

TURFS_DATA = [...]
⏰ Modify Time Slots

Inside app.py, edit:

TIME_SLOTS = [...]
🐛 Troubleshooting
❓ Page Not Opening

Flask installed?

pip show flask
Port already in use? Change port in app.py
❓ Bookings Not Saving
Check folder write permission
Create bookings.json manually if needed
❓ Admin Login Not Working
Verify correct username/password
Clear browser cookies/session
❓ Database Page Not Opening
Must login first via /admin/login
Session expired → login again
📌 Future Improvements (Optional)
Add user login/signup
Use SQLite/MySQL database instead of JSON
Payment gateway integration
Email/SMS booking confirmation
Admin role management
🏁 Conclusion

This project is a complete sports turf booking system with a premium UI and powerful admin dashboard.

⭐ If you like this project, don't forget to star the repository!

❤️ Made With
Python 🐍
Flask ⚡
HTML + CSS + JS 🎨
JSON Storage 💾
📷 Screenshots (Optional)

You can add screenshots like:
