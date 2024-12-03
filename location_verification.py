from geopy.distance import geodesic
import geocoder

# Step 1: Admin-defined location
admin_location = (28.7041, 77.1025)  # Example location: New Delhi

# Step 2: Get current location
def get_current_location():
    try:
        g = geocoder.ip('me')  # Fetch current location
        if g.latlng:
            return tuple(g.latlng)  # Return (latitude, longitude)
        else:
            print("Could not fetch location.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Step 3: Check location validity
def is_within_allowed_location():
    current_location = get_current_location()
    if not current_location:
        print("Location unavailable.")
        return False
    
    # Calculate the distance
    distance = geodesic(admin_location, current_location).meters
    allowed_radius = 100  # 100 meters

    if distance <= allowed_radius:
        print("Location verified. Within allowed range.")
        return True
    else:
        print(f"Outside allowed location. You are {distance:.2f} meters away.")
        return False
