from flask import Flask, render_template, request, send_file
import cv2
import random
import os
from flask_mail import Mail, Message


app = Flask(__name__)

# /////////////////////////////////////////////////////////////////////////////////
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'certificates')  # Folder to save certificates
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Configuring Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gajanan19022000@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'jost higa wtmc wzlr'  # Your App Password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Route to home page
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/template1')
def home1():
    return render_template('template1.html')

@app.route('/template2')
def home2():
    return render_template('template2.html')

@app.route('/template3')
def home3():
    return render_template('template3.html')

@app.route('/template4')
def home4():
    return render_template('template4.html')

@app.route('/template5')
def home5():
    return render_template('template5.html')

@app.route('/template6')
def home6():
    return render_template('template6.html')


# ///////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/template1_order', methods=['POST'])
def template1_order():
    
     # Get form data
    name = request.form['name1']
    email = request.form['email']
    company_name = request.form['companyName']
    education = request.form['education']
    skill = request.form['skills']
    date = request.form['date']
    signature =request.form['signature']
    id = str(random.randint(100000000000, 99999999999))  # Generates a 12-digit ID


    # load the image
    image = 'static/cir3.png' 
    template = cv2.imread(image)

    if template is None:
        return "Template image not found. Make sure 'cir1.png' is in the static folder.", 400

     # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(template, name, (63,348), cv2.FONT_HERSHEY_TRIPLEX , 0.8, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, company_name, (340, 368), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, education, (135, 395), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, skill, (63, 424), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, date, (90, 484), font, 0.5, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, signature, (116, 555), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, id, (144, 638), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
    
     # Save the certificate
    output_path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)
    
     # Send the email with the certificate attached
    msg = Message("Your Certificate", recipients=[email], sender='gajanan19022000@gmail.com')
    msg.body = f"Hello {name},\n\nAttached is your certificate from {company_name}.\n\nBest regards,\nThe Team"
    
    # Attach the certificate image
    with app.open_resource(output_path) as fp:
        msg.attach(f"{name}_certificate.jpg", "image/jpeg", fp.read())

    # Send the email
    mail.send(msg)
    # # return send_file(output_path, as_attachment=True)  # Return the file as an attachment
    return render_template('main.html')

    
# ////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/template2_order', methods=['POST'])
def template2_order():
      # Get form data
    company = request.form['Company']
    email = request.form['email']
    name = request.form['Name']
    Course = request.form['Course']
    Issued = request.form['Issued']
    date = request.form['date']
    id = str(random.randint(100000000009, 999999999999))  # Generates a 12-digit ID


    # load the image
    image = 'static/cir2.png' 
    template = cv2.imread(image)

    if template is None:
        return "Template image not found. Make sure 'cir1.png' is in the static folder.", 400

     # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(template, company, (193,203), cv2.FONT_HERSHEY_TRIPLEX , 0.4, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(template, name, (110, 305), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, Course, (110, 380), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, Issued, (112, 502), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, date, (190, 573), font, 0.3, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, id, (176, 596), font, 0.4, (0,0,0), 1, cv2.LINE_AA)
    
     # Save the certificate
    output_path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)
    
     # Send the email with the certificate attached
    msg = Message("Your Certificate", recipients=[email], sender='gajanan19022000@gmail.com')
    msg.body = f"Hello {name},\n\nAttached is your certificate from {company}.\n\nBest regards,\nThe Team"
    
    # Attach the certificate image
    with app.open_resource(output_path) as fp:
        msg.attach(f"{name}_certificate.jpg", "image/jpeg", fp.read())

    # Send the email
    mail.send(msg)
    # # return send_file(output_path, as_attachment=True)  # Return the file as an attachment
    return render_template('main.html')


# ////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/template3_order', methods=['POST'])
def template3_order():
      # Get form data
    email = request.form['email']
    name = request.form['name']
    sign = request.form['sign']
    blood_group = request.form['blood']
    office= request.form['office']
    ro_no = str(random.randint(10000, 99999))  # Generates a 12-digit ID
    sr_no = str(random.randint(100, 999))  # Generates a 12-digit ID

    # load the image
    image = 'static/cir1.png' 
    template = cv2.imread(image)

    if template is None:
        return "Template image not found. Make sure 'cir1.png' is in the static folder.", 400

     # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(template, ro_no, (105,376), cv2.FONT_HERSHEY_COMPLEX , 0.6, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, name, (295, 335), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, sr_no, (95, 305), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, sign, (626, 508), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.9, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, blood_group, (420, 550), cv2.FONT_HERSHEY_TRIPLEX, 0.9, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, office, (56, 510), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.9, (0,0,0), 1, cv2.LINE_AA)
    
     # Save the certificate
    output_path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)
    
     # Send the email with the certificate attached
    msg = Message("Your Certificate", recipients=[email], sender='gajanan19022000@gmail.com')
    msg.body = f"Hello {name},\n\nAttached is your certificate from {office}.\n\nBest regards,\nThe Team"
    
    # Attach the certificate image
    with app.open_resource(output_path) as fp:
        msg.attach(f"{name}_certificate.jpg", "image/jpeg", fp.read())

    # Send the email
    mail.send(msg)
    # # return send_file(output_path, as_attachment=True)  # Return the file as an attachment
    return render_template('main.html')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
 
@app.route('/template4_order', methods=['POST'])
def template4_order():
      # Get form data
    email = request.form['email']
    name = request.form['name']
    sign = request.form['sign']
    date = request.form['date']
    office ='Best Awards'

    # load the image
    image = 'static/cir4.png' 
    template = cv2.imread(image)

    if template is None:
        return "Template image not found. Make sure 'cir1.png' is in the static folder.", 400

     # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(template, name, (160,210), cv2.FONT_HERSHEY_SCRIPT_COMPLEX , 0.6, (77,218,77), 1, cv2.LINE_8)
    cv2.putText(template, date, (66, 326), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, sign, (395, 326), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
    
     # Save the certificate
    output_path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)
    
     # Send the email with the certificate attached
    msg = Message("Your Certificate", recipients=[email], sender='gajanan19022000@gmail.com')
    msg.body = f"Hello {name},\n\nAttached is your certificate from {office}.\n\nBest regards,\nThe Team"
    
    # Attach the certificate image
    with app.open_resource(output_path) as fp:
        msg.attach(f"{name}_certificate.jpg", "image/jpeg", fp.read())

    # Send the email
    mail.send(msg)
    # # # return send_file(output_path, as_attachment=True)  # Return the file as an attachment
    return render_template('main.html')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
 
@app.route('/template5_order', methods=['POST'])
def template5_order():
      # Get form data
    email = request.form['email']
    name = request.form['name']
    sign = request.form['sign']
    date = request.form['date']
    office ='Best Awards'

    # load the image
    image = 'static/cir5.png' 
    template = cv2.imread(image)

    if template is None:
        return "Template image not found. Make sure 'cir1.png' is in the static folder.", 400

     # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(template, name, (198,212), cv2.FONT_HERSHEY_TRIPLEX , 0.4, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, date, (214, 334), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, sign, (402, 337), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.6, (0,0,0), 1, cv2.LINE_AA)
    
     # Save the certificate
    output_path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)
    
     # Send the email with the certificate attached
    msg = Message("Your Certificate", recipients=[email], sender='gajanan19022000@gmail.com')
    msg.body = f"Hello {name},\n\nAttached is your certificate from {office}.\n\nBest regards,\nThe Team"
    
    # Attach the certificate image
    with app.open_resource(output_path) as fp:
        msg.attach(f"{name}_certificate.jpg", "image/jpeg", fp.read())

    # Send the email
    mail.send(msg)
     # return send_file(output_path, as_attachment=True)  # Return the file as an attachment
    return render_template('main.html')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.route('/template6_order', methods=['POST'])
def template6_order():
      # Get form data
    email = request.form['email']
    name = request.form['name']
    sign = request.form['sign']
    date = request.form['date']
    time = request.form['time']
    id = str(random.randint(100000000000, 999999999999))  # Generates a 12-digit ID

    office ='Linkedin'

    # load the image
    image = 'static/cir6.png' 
    template = cv2.imread(image)

    if template is None:
        return "Template image not found. Make sure 'cir1.png' is in the static folder.", 400

     # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(template, name, (421,260), cv2.FONT_HERSHEY_TRIPLEX , 0.5, (115,122,115), 1, cv2.LINE_AA)
    cv2.putText(template, date, (209, 279), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (115,122,115), 1, cv2.LINE_8)
    cv2.putText(template, sign, (350, 484), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(template, time, (420, 278), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.4, (115,122,115), 1, cv2.LINE_AA)
    cv2.putText(template, id, (275, 535), font, 0.3, (11,11,11), 1, cv2.LINE_AA)
    
     # Save the certificate
    output_path = os.path.join(UPLOAD_FOLDER, f"{name}.jpg")
    cv2.imwrite(output_path, template)
    
     # Send the email with the certificate attached
    msg = Message("Your Certificate", recipients=[email], sender='gajanan19022000@gmail.com')
    msg.body = f"Hello {name},\n\nAttached is your certificate from {office}.\n\nBest regards,\nThe Team"
    
    # Attach the certificate image
    with app.open_resource(output_path) as fp:
        msg.attach(f"{name}_certificate.jpg", "image/jpeg", fp.read())

    # Send the email
    mail.send(msg)
     # return send_file(output_path, as_attachment=True)  # Return the file as an attachment
    return render_template('main.html')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    app.run(debug=True)
