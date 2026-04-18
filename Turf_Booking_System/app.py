from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
from functools import wraps
import json
import os
import hashlib

# Base directory — always points to this file's folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = 'turf_booking_secret_key_2024'

# Admin credentials (Change these!)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# Files — absolute paths so they always save in the project folder
BOOKINGS_FILE = os.path.join(BASE_DIR, 'bookings.json')
USERS_FILE = os.path.join(BASE_DIR, 'users.json')

# ─── Decorators ───────────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ─── Helpers ──────────────────────────────────────────────────────────────────

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def load_bookings():
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_bookings(bookings):
    with open(BOOKINGS_FILE, 'w') as f:
        json.dump(bookings, f, indent=4)

def auto_expire_bookings():
    """Mark bookings as 'completed' when their slot time has passed (keeps history)"""
    bookings = load_bookings()
    now = datetime.now()
    changed = False
    for b in bookings:
        if b.get('status', 'active') == 'active':
            try:
                slot_end_str = b['slot_time'].split(' - ')[1]   # e.g. "07:00 AM"
                booking_end = datetime.strptime(f"{b['date']} {slot_end_str}", '%Y-%m-%d %I:%M %p')
                if booking_end <= now:
                    b['status'] = 'completed'
                    changed = True
            except Exception:
                pass
    if changed:
        save_bookings(bookings)
    return bookings

# ─── Turfs Data ───────────────────────────────────────────────────────────────

TURFS_DATA = [
    {'id': 1, 'name': 'Deccan Gymkhana Cricket Ground', 'type': 'Cricket', 'location': 'Deccan Gymkhana, Pune', 'rating': 4.8, 'price': 2000, 'image': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&h=400&fit=crop', 'amenities': ['Floodlights', 'Changing Room', 'Parking', 'Water', 'Scoreboard'], 'capacity': 22, 'description': 'Premium cricket ground with excellent pitch quality and facilities'},
    {'id': 2, 'name': 'Shivaji Nagar Football Arena', 'type': 'Football', 'location': 'Shivaji Nagar, Pune', 'rating': 4.6, 'price': 1800, 'image': 'https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&h=400&fit=crop', 'amenities': ['Floodlights', 'Artificial Turf', 'Seating', 'Parking', 'Changing Room'], 'capacity': 14, 'description': '5-a-side and 7-a-side football turf with top-quality artificial grass'},
    {'id': 3, 'name': 'Kothrud Badminton Academy', 'type': 'Badminton', 'location': 'Kothrud, Pune', 'rating': 4.9, 'price': 800, 'image': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&h=400&fit=crop', 'amenities': ['AC Courts', 'Wooden Flooring', 'Racket Rental', 'Coaching', 'Parking'], 'capacity': 4, 'description': 'Air-conditioned badminton courts with professional coaching available'},
    {'id': 4, 'name': 'Baner Sports Complex', 'type': 'Multi-Sport', 'location': 'Baner, Pune', 'rating': 4.7, 'price': 2500, 'image': 'https://images.unsplash.com/photo-1575361204480-aadea25e6e68?w=800&h=400&fit=crop', 'amenities': ['Multiple Courts', 'Cafe', 'Gym', 'Parking', 'Locker Rooms'], 'capacity': 30, 'description': 'Complete sports complex with cricket, football, basketball facilities'},
    {'id': 5, 'name': 'Koregaon Park Tennis Club', 'type': 'Tennis', 'location': 'Koregaon Park, Pune', 'rating': 4.8, 'price': 1200, 'image': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?w=800&h=400&fit=crop', 'amenities': ['Clay Courts', 'Hard Courts', 'Coaching', 'Equipment', 'Lounge'], 'capacity': 4, 'description': 'Premium tennis club with both clay and hard courts'},
    {'id': 6, 'name': 'Viman Nagar Basketball Arena', 'type': 'Basketball', 'location': 'Viman Nagar, Pune', 'rating': 4.5, 'price': 1000, 'image': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&h=400&fit=crop', 'amenities': ['Indoor Court', 'Scoreboard', 'Lockers', 'Parking', 'Seating'], 'capacity': 10, 'description': 'Indoor basketball court with professional setup and equipment'},
    {'id': 7, 'name': 'Hinjewadi Sports Turf', 'type': 'Football', 'location': 'Hinjewadi Phase 1, Pune', 'rating': 4.7, 'price': 2200, 'image': 'https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&h=400&fit=crop', 'amenities': ['Floodlights', 'FIFA Standard Turf', 'Changing Room', 'Parking', 'Water'], 'capacity': 16, 'description': 'FIFA standard artificial turf for professional football matches'},
    {'id': 8, 'name': 'Wakad Cricket Club', 'type': 'Cricket', 'location': 'Wakad, Pune', 'rating': 4.6, 'price': 1800, 'image': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&h=400&fit=crop', 'amenities': ['Nets', 'Floodlights', 'Parking', 'Scoreboard', 'Seating'], 'capacity': 22, 'description': 'Well-maintained cricket ground with practice nets and floodlights'},
    {'id': 9, 'name': 'Aundh Fitness & Sports Arena', 'type': 'Multi-Sport', 'location': 'Aundh, Pune', 'rating': 4.8, 'price': 2000, 'image': 'https://images.unsplash.com/photo-1575361204480-aadea25e6e68?w=800&h=400&fit=crop', 'amenities': ['Badminton', 'Basketball', 'Gym', 'Cafe', 'Parking', 'Changing Rooms'], 'capacity': 25, 'description': 'Modern sports complex with badminton, basketball, and fitness facilities'},
    {'id': 10, 'name': 'Magarpatta City Sports Complex', 'type': 'Multi-Sport', 'location': 'Magarpatta, Pune', 'rating': 4.9, 'price': 3000, 'image': 'https://images.unsplash.com/photo-1575361204480-aadea25e6e68?w=800&h=400&fit=crop', 'amenities': ['Swimming Pool', 'Tennis', 'Badminton', 'Gym', 'Cafe', 'Parking'], 'capacity': 40, 'description': 'Premium sports complex with world-class facilities and amenities'},
    {'id': 11, 'name': 'Pimpri-Chinchwad Football Ground', 'type': 'Football', 'location': 'Pimpri-Chinchwad, Pune', 'rating': 4.4, 'price': 1500, 'image': 'https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&h=400&fit=crop', 'amenities': ['Floodlights', 'Natural Grass', 'Parking', 'Water', 'Seating'], 'capacity': 18, 'description': 'Natural grass football ground with excellent drainage system'},
    {'id': 12, 'name': 'Hadapsar Badminton Center', 'type': 'Badminton', 'location': 'Hadapsar, Pune', 'rating': 4.7, 'price': 600, 'image': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&h=400&fit=crop', 'amenities': ['AC Courts', 'Parking', 'Racket Rental', 'Water', 'Seating'], 'capacity': 6, 'description': 'Affordable badminton courts with air conditioning and coaching'},
    {'id': 13, 'name': 'Balewadi Sports Complex', 'type': 'Multi-Sport', 'location': 'Balewadi, Pune', 'rating': 5.0, 'price': 3500, 'image': 'https://images.unsplash.com/photo-1575361204480-aadea25e6e68?w=800&h=400&fit=crop', 'amenities': ['Olympic Standard', 'Swimming', 'Athletics', 'Hockey', 'Parking', 'Cafe'], 'capacity': 50, 'description': 'World-class sports complex built for Commonwealth Youth Games'},
    {'id': 14, 'name': 'Kondhwa Cricket Turf', 'type': 'Cricket', 'location': 'Kondhwa, Pune', 'rating': 4.5, 'price': 1600, 'image': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&h=400&fit=crop', 'amenities': ['Nets', 'Floodlights', 'Parking', 'Water', 'Changing Room'], 'capacity': 22, 'description': 'Cricket turf with multiple practice nets and match ground'},
    {'id': 15, 'name': 'Pashan Basketball Court', 'type': 'Basketball', 'location': 'Pashan, Pune', 'rating': 4.6, 'price': 900, 'image': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&h=400&fit=crop', 'amenities': ['Outdoor Court', 'Floodlights', 'Parking', 'Water', 'Seating'], 'capacity': 10, 'description': 'Outdoor basketball court with quality flooring and lighting'},
    {'id': 16, 'name': 'Pune University Sports Ground', 'type': 'Multi-Sport', 'location': 'University Road, Pune', 'rating': 4.8, 'price': 2200, 'image': 'https://images.unsplash.com/photo-1575361204480-aadea25e6e68?w=800&h=400&fit=crop', 'amenities': ['Cricket', 'Football', 'Athletics Track', 'Gym', 'Parking'], 'capacity': 35, 'description': 'University sports ground with multiple sports facilities'},
    {'id': 17, 'name': 'Kharadi Cricket Stadium', 'type': 'Cricket', 'location': 'Kharadi, Pune', 'rating': 4.7, 'price': 2500, 'image': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=800&h=400&fit=crop', 'amenities': ['Stadium Seating', 'Floodlights', 'Scoreboard', 'Parking', 'Cafe'], 'capacity': 30, 'description': 'Modern cricket stadium with excellent seating and amenities'},
    {'id': 18, 'name': 'Fursungi Football Arena', 'type': 'Football', 'location': 'Fursungi, Pune', 'rating': 4.3, 'price': 1400, 'image': 'https://images.unsplash.com/photo-1459865264687-595d652de67e?w=800&h=400&fit=crop', 'amenities': ['Floodlights', 'Artificial Turf', 'Parking', 'Water'], 'capacity': 14, 'description': 'Affordable football turf with good quality artificial grass'},
    {'id': 19, 'name': 'Yerawada Badminton Hall', 'type': 'Badminton', 'location': 'Yerawada, Pune', 'rating': 4.5, 'price': 700, 'image': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=800&h=400&fit=crop', 'amenities': ['AC Courts', 'Parking', 'Coaching', 'Shuttle Service', 'Water'], 'capacity': 4, 'description': 'Quality badminton hall with professional coaching services'},
    {'id': 20, 'name': 'Katraj Tennis Academy', 'type': 'Tennis', 'location': 'Katraj, Pune', 'rating': 4.6, 'price': 1000, 'image': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?w=800&h=400&fit=crop', 'amenities': ['Clay Courts', 'Coaching', 'Equipment', 'Parking', 'Changing Room'], 'capacity': 4, 'description': 'Tennis academy with expert coaches and quality clay courts'},
    {'id': 21, 'name': 'Warje Basketball Complex', 'type': 'Basketball', 'location': 'Warje, Pune', 'rating': 4.5, 'price': 850, 'image': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800&h=400&fit=crop', 'amenities': ['Indoor Court', 'Locker Rooms', 'Parking', 'Water', 'Seating'], 'capacity': 10, 'description': 'Indoor basketball complex with modern amenities'},
    {'id': 22, 'name': 'Undri Tennis Courts', 'type': 'Tennis', 'location': 'Undri, Pune', 'rating': 4.4, 'price': 950, 'image': 'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?w=800&h=400&fit=crop', 'amenities': ['Hard Courts', 'Floodlights', 'Equipment', 'Parking', 'Water'], 'capacity': 4, 'description': 'Hard court tennis facilities with floodlights for evening play'},
]

TIME_SLOTS = [
    {'id': 1, 'time': '06:00 AM - 07:00 AM'},
    {'id': 2, 'time': '07:00 AM - 08:00 AM'},
    {'id': 3, 'time': '08:00 AM - 09:00 AM'},
    {'id': 4, 'time': '09:00 AM - 10:00 AM'},
    {'id': 5, 'time': '10:00 AM - 11:00 AM'},
    {'id': 6, 'time': '11:00 AM - 12:00 PM'},
    {'id': 7, 'time': '04:00 PM - 05:00 PM'},
    {'id': 8, 'time': '05:00 PM - 06:00 PM'},
    {'id': 9, 'time': '06:00 PM - 07:00 PM'},
    {'id': 10, 'time': '07:00 PM - 08:00 PM'},
    {'id': 11, 'time': '08:00 PM - 09:00 PM'},
    {'id': 12, 'time': '09:00 PM - 10:00 PM'},
]

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
@login_required
def index():
    return render_template('index.html', turfs=TURFS_DATA, username=session.get('username'))

# ── Auth: combined login/register page ────────────────────────────────────────

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Already logged in?
    if session.get('user_logged_in'):
        return redirect(url_for('index'))
    if session.get('admin_logged_in'):
        return redirect(url_for('view_database'))

    error = None
    active_tab = request.args.get('tab', 'user')  # 'user' or 'admin'

    if request.method == 'POST':
        form_type = request.form.get('form_type')

        # ── Register ──
        if form_type == 'register':
            active_tab = 'user'
            username = request.form.get('username', '').strip()
            email    = request.form.get('email', '').strip()
            password = request.form.get('password', '')
            confirm  = request.form.get('confirm_password', '')

            if not username or not email or not password:
                error = 'Fill all the fields!'
            elif password != confirm:
                error = 'Passwords did not matched!'
            elif len(password) < 6:
                error = 'Password must be atleast 6 characters!'
            else:
                users = load_users()
                if any(u['username'] == username for u in users):
                    error = 'This username already exists! Choose another one.'
                elif any(u['email'] == email for u in users):
                    error = 'email is already linked to another account !'
                else:
                    users.append({
                        'id': len(users) + 1,
                        'username': username,
                        'email': email,
                        'password': hash_password(password),
                        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                    save_users(users)
                    session['user_logged_in'] = True
                    session['username'] = username
                    session['user_email'] = email
                    return redirect(url_for('index'))

        # ── User Login ──
        elif form_type == 'user_login':
            active_tab = 'user'
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '')
            users = load_users()
            user = next((u for u in users if u['username'] == username and u['password'] == hash_password(password)), None)
            if user:
                session['user_logged_in'] = True
                session['username'] = user['username']
                session['user_email'] = user['email']
                return redirect(url_for('index'))
            else:
                error = 'Wrong username or password!'

        # ── Admin Login ──
        elif form_type == 'admin_login':
            active_tab = 'admin'
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '')
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                session['admin_logged_in'] = True
                return redirect(url_for('view_database'))
            else:
                error = 'Wrong admin credentials!'

    return render_template('login.html', error=error, active_tab=active_tab)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ── Turfs / Booking ────────────────────────────────────────────────────────────

@app.route('/turf/<int:turf_id>')
@login_required
def turf_details(turf_id):
    turf = next((t for t in TURFS_DATA if t['id'] == turf_id), None)
    if not turf:
        return "Turf not found", 404
    today = datetime.now().strftime('%Y-%m-%d')
    return render_template('turf_details.html', turf=turf, slots=TIME_SLOTS, today=today, username=session.get('username'))

@app.route('/book', methods=['POST'])
@login_required
def book_turf():
    data = request.json
    required = ['turf_id', 'date', 'slot_id']
    if not all(f in data for f in required):
        return jsonify({'success': False, 'message': 'Missing fields'}), 400

    auto_expire_bookings()
    bookings = load_bookings()

    is_booked = any(
        b['turf_id'] == data['turf_id'] and
        b['date'] == data['date'] and
        b['slot_id'] == data['slot_id'] and
        b.get('status', 'active') == 'active'
        for b in bookings
    )
    if is_booked:
        return jsonify({'success': False, 'message': 'Slot already booked!'}), 400

    turf = next((t for t in TURFS_DATA if t['id'] == data['turf_id']), None)
    slot = next((s for s in TIME_SLOTS if s['id'] == data['slot_id']), None)
    if not turf or not slot:
        return jsonify({'success': False, 'message': 'Invalid turf or slot'}), 400

    booking = {
        'id': len(bookings) + 1,
        'turf_id': data['turf_id'],
        'turf_name': turf['name'],
        'date': data['date'],
        'slot_id': data['slot_id'],
        'slot_time': slot['time'],
        'name': session['username'],
        'phone': data.get('phone', ''),
        'price': turf['price'],
        'username': session['username'],
        'status': 'active',
        'booked_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    bookings.append(booking)
    save_bookings(bookings)
    return jsonify({'success': True, 'message': 'Booking successful!', 'booking': booking})

@app.route('/my_bookings')
@login_required
def my_bookings():
    auto_expire_bookings()
    bookings = load_bookings()
    # Show all current user's bookings with status (active, completed, cancelled)
    user_bookings = [b for b in bookings if b.get('username') == session.get('username')]
    active    = [b for b in user_bookings if b.get('status', 'active') == 'active']
    completed = [b for b in user_bookings if b.get('status') == 'completed']
    cancelled = [b for b in user_bookings if b.get('status') == 'cancelled']
    return render_template('my_bookings.html',
                           bookings=user_bookings,
                           active=active,
                           completed=completed,
                           cancelled=cancelled,
                           username=session.get('username'))

@app.route('/api/bookings')
@login_required
def api_bookings():
    auto_expire_bookings()
    return jsonify(load_bookings())

@app.route('/cancel_booking/<int:booking_id>', methods=['POST'])
@login_required
def cancel_booking(booking_id):
    bookings = load_bookings()
    # User can only cancel their own; admin can cancel any
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({'success': False, 'message': 'Booking not found'}), 404
    if not session.get('admin_logged_in') and booking.get('username') != session.get('username'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    # Mark as cancelled instead of deleting — keeps history
    booking['status'] = 'cancelled'
    save_bookings(bookings)
    return jsonify({'success': True, 'message': 'Cancelled successfully'})

# ── Admin ──────────────────────────────────────────────────────────────────────

@app.route('/database')
@admin_required
def view_database():
    auto_expire_bookings()
    bookings = load_bookings()
    return render_template('database.html', bookings=bookings)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)