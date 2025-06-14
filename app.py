from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)
PORT = 5000

bio_data = {
    "Name": "Sandeep Kumar",
    "Date of Birth": "03 July 1999",
    "Age": "25 years",
    "Height": "5 feet 3 inches",
    "Complexion": "Fair",
    "Religion": "Hindu",
    "Profession": "Software Engineer",
    "Current Location": "Noida, Uttar Pradesh",
    "Permanent Address": "Village : Thana,\nPost : ThanaRampur,\nDistrict : Varanasi, Uttar Pradesh",
    "Father's Name": "Chhabinath Ram",
    "Mother's Name": "Teeja Devi",
    "Siblings": "Sister: Nitu Devi (Married)",
    "Phone": "+91-9621187238",
    "Email": "kumar.sandeep962118@gmail.com",
    "Education": "B.Tech in Electronic Engineering, Dr. Ambedkar Institute of Technology, Kanpur.\nIntermediate: Jawahar Navodaya Vidyalaya, Varanasi.",
    "About Myself": "I am a software engineer passionate about technology and lifelong learning. I am looking for a partner who is understanding, caring, and shares similar values."
}

@app.route('/')
def home():
    # Get the base URL dynamically (works on localhost and deployed URL)
    base_url = request.host_url.rstrip('/')  
    bio_url = f"{base_url}/bio"

    # Generate QR code with bio_url
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(bio_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('home.html', qr_code=img_str)

@app.route('/bio')
def bio():
    return render_template('bio.html', data=bio_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
