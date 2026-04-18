# 🏏 TurfMaster - Turf Booking System

Ek bahut hi attractive aur professional turf booking system Python Flask mein banaya gaya hai!

## 🌟 Features

### ✨ Attractive UI
- **Gradient Background** - Purple, blue colors
- **Glass-morphism Effect** - Transparent cards with blur
- **Smooth Animations** - Hover effects, transitions
- **Responsive Design** - Mobile aur desktop dono pe perfect

### 🏏 24 Pre-loaded Pune Turfs
**Cricket Grounds (5):**
1. Deccan Gymkhana Cricket Ground - ₹2000/hr
2. Wakad Cricket Club - ₹1800/hr
3. Kondhwa Cricket Turf - ₹1600/hr
4. Kharadi Cricket Stadium - ₹2500/hr
5. And more...

**Football Arenas (4):**
1. Shivaji Nagar Football Arena - ₹1800/hr
2. Hinjewadi Sports Turf - ₹2200/hr
3. Pimpri-Chinchwad Football Ground - ₹1500/hr
4. Fursungi Football Arena - ₹1400/hr

**Badminton Courts (4):**
1. Kothrud Badminton Academy - ₹800/hr
2. Hadapsar Badminton Center - ₹600/hr
3. Yerawada Badminton Hall - ₹700/hr
4. And more...

**Tennis Courts (4):**
1. Koregaon Park Tennis Club - ₹1200/hr
2. Katraj Tennis Academy - ₹1000/hr
3. Undri Tennis Courts - ₹950/hr
4. And more...

**Basketball Courts (3):**
1. Viman Nagar Basketball Arena - ₹1000/hr
2. Pashan Basketball Court - ₹900/hr
3. Warje Basketball Complex - ₹850/hr

**Multi-Sport Complexes (4):**
1. Balewadi Sports Complex - ₹3500/hr (Olympic Standard!)
2. Magarpatta City Sports Complex - ₹3000/hr
3. Baner Sports Complex - ₹2500/hr
4. And more...

**Har turf mein:**
- Name, location, rating ⭐
- Price per hour
- Capacity (kitne players)
- Amenities (facilities)
- Description
- Professional images (Unsplash se)

### 📅 Booking System
- **Date Selection** - Calendar se date choose karo
- **12 Time Slots** - Morning 6 AM se night 10 PM tak
- **Real-time Availability** - Booked slots red mein dikhte hain
- **User Details Form** - Name aur phone number
- **Booking Confirmation** - Success message with animation
- **My Bookings Page** - Tumhare saare bookings ek jagah
- **Cancel Booking** - Bookings cancel kar sakte ho

### 🔒 Admin Panel (Secure)
- **Admin Login Required** - Database sirf admin dekh sakta hai
- **Username:** `admin`
- **Password:** `admin123` (Change karna mat bhoolna!)
- **Features:**
  - 📊 Complete database view
  - 📈 Statistics dashboard (Total bookings, revenue, etc.)
  - 🔍 Search & filter bookings
  - 📥 Export to CSV
  - 🗑️ Delete bookings
  - ⬆️⬇️ Sort by any column

### 💾 Data Storage
- JSON file mein bookings save hoti hain
- Restart ke baad bhi data safe rehta hai

## 🚀 Installation & Setup

### Requirements
- Python 3.7 ya usse upar
- Flask

### Step 1: Install Flask
```bash
pip install flask
```

### Step 2: Run the Application
```bash
cd turf_booking_python
python app.py
```

### Step 3: Open in Browser
Browser mein jaao aur type karo:
```
http://localhost:5000
```

### Step 4: Admin Access
Admin panel access karne ke liye:
```
http://localhost:5000/admin/login
```
**Default Login Credentials (change karna jaruri hai!):**
- Username: `admin`
- Password: `admin123`

**Note:** Security ke liye, credentials login page pe nahi dikhte - sirf documentation mein hain.

## 📁 Project Structure
```
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
        └── style.css           # All CSS styling
```

## 🎨 Pages

### 1. Home Page (`/`)
- Saare 6 turfs ek grid mein dikhte hain
- Har card mein turf ki details
- "Book Now" button

### 2. Turf Details Page (`/turf/<id>`)
- Turf ki complete details
- Date selection
- Time slot selection
- Booking form
- Real-time availability check

### 3. My Bookings Page (`/my_bookings`)
- Tumhare saare bookings
- Booking details aur time
- Price information
- **Cancel Booking** button

### 4. Admin Login Page (`/admin/login`)
- Secure admin login
- Username & password required
- Beautiful login interface

### 5. Database Page (`/database`) - Admin Only 🔒
- Complete bookings database
- Statistics cards
- Search functionality
- Sort by columns
- Export to CSV
- Delete bookings

## 🔧 How to Use

### For Users:
1. **Home page pe jao** - Saare turfs dikhengi
2. **Koi bhi turf select karo** - "Book Now" pe click karo
3. **Date select karo** - Calendar se apni date choose karo
4. **Slot select karo** - Available time slot choose karo (red wale booked hain)
5. **Details bharo** - Apna name aur phone number dalo
6. **Confirm karo** - "Confirm Booking" button pe click karo
7. **Success!** 🎉 - Booking confirm ho gayi
8. **Cancel karna ho** - "My Bookings" page pe jao aur "Cancel Booking" pe click karo

### For Admin:
1. **Login page pe jao** - `http://localhost:5000/admin/login`
2. **Credentials daalo:**
   - Username: `admin`
   - Password: `admin123`
3. **Database access** - Automatic redirect to database
4. **Manage bookings** - Search, sort, delete, export
5. **Logout** - Top navbar mein logout button

## 🔐 Security Tips

### Change Admin Password (IMPORTANT!):
`app.py` mein yeh lines edit karo:
```python
# Admin credentials (Change these!)
ADMIN_USERNAME = 'your_username'
ADMIN_PASSWORD = 'your_strong_password'
```

**⚠️ IMPORTANT SECURITY NOTES:**
1. **Default credentials sirf testing ke liye hain!**
2. **Production mein JARUR change karo!**
3. **Strong password use karo** (letters, numbers, symbols)
4. **Credentials kabhi page pe display mat karo**
5. **README file ko server pe upload mat karo** (local documentation ke liye)

**Good Password Examples:**
- `MyTurf@2024!Secure`
- `Pune$ports#Admin99`
- `Cr1ck3t&Ball@2024`

**❌ Bad Passwords (use mat karna):**
- admin123
- password
- 12345678

## 📱 Features in Detail

### Real-time Slot Checking
- Selected date ke liye available slots dikhte hain
- Booked slots automatically red color mein ho jaate hain
- Duplicate booking nahi ho sakti

### Cancel Booking
- "My Bookings" page pe har booking ke saath cancel button
- Confirmation popup milega
- Cancelled booking database se delete ho jayegi
- Slot automatically available ho jayega

### Admin Dashboard
- **Stats Cards:** Total bookings, revenue, active turfs, customers
- **Search:** Name, phone, turf se search karo
- **Sort:** Kisi bhi column pe click karke sort karo
- **Export CSV:** Saara data download karo
- **Delete:** Individual bookings delete karo
- **Protected:** Bina login ke access nahi hoga

### Beautiful UI Elements
- **Cards** - Glass-morphism effect
- **Buttons** - Gradient colors with hover effects
- **Icons** - Font Awesome icons
- **Colors** - Purple, blue, green gradients
- **Animations** - Smooth transitions everywhere

### Data Persistence
- Saari bookings `bookings.json` file mein save hoti hain
- Application restart ke baad bhi data safe rehta hai

## 🎯 API Endpoints

- `GET /` - Home page (all turfs)
- `GET /turf/<id>` - Turf details and booking page
- `POST /check_slot` - Check slot availability
- `POST /book` - Create a new booking
- `GET /my_bookings` - View all bookings
- `POST /cancel_booking/<id>` - Cancel a booking
- `GET /api/bookings` - Get bookings as JSON
- `GET /admin/login` - Admin login page (GET & POST)
- `GET /admin/logout` - Admin logout
- `GET /database` - Database view (Admin only - protected)

## 💡 Tips

1. **Port change karna ho to:**
   - `app.py` mein last line: `app.run(debug=True, host='0.0.0.0', port=5000)`
   - Port number change kar sakte ho

2. **Turf add karna ho to:**
   - `app.py` mein `TURFS_DATA` list mein naya turf add karo

3. **Time slots change karne hain to:**
   - `app.py` mein `TIME_SLOTS` list edit karo

4. **Admin credentials change karne hain:**
   - `app.py` mein `ADMIN_USERNAME` aur `ADMIN_PASSWORD` edit karo

## 🎨 Customization

### Colors Change Karne Ke Liye
`static/css/style.css` mein:
- Background gradient: `background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);`
- Button colors: `.book-btn` class
- Card colors: `.turf-card` class

### Images Change Karne Ke Liye
`app.py` mein har turf ke `image` URL ko change karo.

## 🐛 Troubleshooting

**Problem: Page nahi khul raha**
- Check karo Flask install hai ya nahi: `pip list | grep Flask`
- Port already use mein to nahi hai

**Problem: Bookings save nahi ho rahi**
- Check karo folder mein write permission hai ya nahi
- `bookings.json` file manually create kar lo

**Problem: Admin login nahi ho raha**
- Correct username/password check karo
- Browser cookies clear kar lo

**Problem: Database page nahi khul raha**
- Pehle `/admin/login` se login karo
- Session expire ho gaya hoga, fir se login karo

## 📞 Support

Koi problem ho to:
1. Terminal mein errors check karo
2. Browser console check karo (F12 press karo)
3. README dhang se padho 😊

## 🎉 Enjoy!

Ab tum apna turf booking system use kar sakte ho!
Ekdam professional aur secure hai! 🚀

**Features Summary:**
- ✅ Beautiful UI with animations
- ✅ 6 Pre-loaded turfs
- ✅ Real-time booking system
- ✅ Cancel bookings
- ✅ Secure admin login
- ✅ Complete database view
- ✅ Statistics dashboard
- ✅ Search & filter
- ✅ Export to CSV
- ✅ Mobile responsive

Made with ❤️ for Sports Enthusiasts!