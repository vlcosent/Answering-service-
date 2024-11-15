from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

# Common medical clinic questions and responses with unique keywords
CLINIC_RESPONSES = {
    "hours": {
        "keywords": ["are you open", "what's your hours", "what are your hours", "when do you open", 
                    "what time", "operating hours", "you guys open", "open now",
                    "still open", "current hours", "today's hours", "opening time",
                    "closing time", "when do you close", "hours today", "hours"],
        "response": "We are open Monday through Friday from 8 AM to 4 PM. We are closed on weekends and major holidays."
    },
    "location": {
        "keywords": ["where are you", "what's your address", "where are you located", "directions", 
                    "how do i get there", "where's your office", "your location", "clinic location",
                    "office address", "can i get directions", "where can i find you", "parking",
                    "building location", "driving directions", "where is the clinic", "location"],
        "response": "We are located at 42 Dooley Street, right next to the Drivers License Center. We have free parking available."
    },
    "appointments": {
        "keywords": ["make an appointment", "schedule a visit", "book appointment", "need to see", 
                    "want to come in", "schedule appointment", "book a time", "get an appointment",
                    "set up appointment", "can i schedule", "need to schedule", "want to schedule", "appointment"
                    "make a visit", "book consultation", "need appointment"],
        "response": "We offer same-day appointments when available, and you can typically schedule a visit within one week. "
                   "Our staff can help find a convenient time for you. For urgent matters, we offer telehealth visits."
    },
    "insurance": {
        "keywords": ["what insurance", "types of insurance", "insurance can i use", "do you take", "insurance" 
                    "accept my insurance", "insurance plans", "insurance coverage", "what plans", "Medicaid",
                    "insurance accepted", "types of insurance you accept", "insurance providers", "Blue Cross", "United Healthcare", "Medicare",
                    "covered by insurance", "insurance options", "my coverage", "insurance information"],
        "response": "We accept most major insurance plans including Blue Cross, Aetna, United Healthcare, Medicare, and Medicaid. "
                   "We also offer self-pay options and payment plans. Please bring your insurance card to your visit."
    },
    "new_patient": {
        "keywords": ["i'm a new patient", "first time", "never been", "want to register", "new patient"
                    "become a patient", "new to clinic", "starting as patient",
                    "register as patient", "first", "new here", "sign up",
                    "get started", "join practice", "establish care"],
        "response": "Welcome! New patients should arrive 30 minutes early to complete paperwork. Please bring your ID, "
                   "insurance card, and a list of current medications. Your first visit will be approximately 45 minutes."
    },
    "prescriptions": {
        "keywords": ["need a refill", "prescription refill", "renew prescription", "refill my meds", "prescription"
                    "need medication", "get my medicine", "prescription renewal", "medication refill",
                    "refill prescription", "medicine refill", "need my prescription", "pharmacy",
                    "prescribe", "medication request", "prescription request"],
        "response": "For prescription refills, please contact your pharmacy or submit a request through our patient portal. "
                   "Routine refills are processed within 24-48 hours. For controlled substances, an appointment is required."
    },
    "medical_records": {
        "keywords": ["medical records", "get my records", "copy of records", "health records", "records"
                    "need records", "transfer records", "records request", "records",
                    "my medical file", "medical history", "medical information", "health history",
                    "medical documentation", "clinical records", "medical files"],
        "response": "To request medical records, please fill out a release form at our front desk or through our patient portal. "
                   "Records requests are typically processed within 5-7 business days."
    },
    "emergency": {
        "keywords": ["emergency", "urgent care", "need help now", "severe pain", 
                    "critical condition", "serious problem", "immediate attention", "emergency care",
                    "urgent medical", "emergency situation", "life threatening", "ambulance",
                    "critical", "911", "emergency room"],
        "response": "If this is a life-threatening emergency, please hang up and dial 911 immediately. "
                   "For urgent but non-life-threatening conditions, we offer same-day appointments when available."
    },
    "covid": {
        "keywords": ["covid test", "covid symptoms", "got covid", "covid positive", 
                    "need covid test", "covid vaccine", "covid shot", "covid exposure",
                    "coronavirus", "covid results", "covid treatment", "covid care",
                    "tested positive", "covid testing", "covid appointment"],
        "response": "We offer COVID-19 testing and vaccinations by appointment. If you have COVID symptoms, "
                   "please let us know when scheduling so we can take appropriate precautions."
    },
    "telehealth": {
        "keywords": ["virtual visit", "online visit", "video call", "remote visit", "virtual","telehealth"
                    "telehealth visit", "virtual appointment", "online appointment", "video chat",
                    "phone visit", "virtual doctor", "remote appointment", "video appointment",
                    "online consultation", "virtual care", "remote care"],
        "response": "We offer telehealth appointments for appropriate medical conditions. These visits are covered by most insurance plans. "
                   "You'll need a smartphone, tablet, or computer with internet access."
    }
}

@app.route("/", methods=['GET'])
def index():
    return "Twilio Voice Bot Server is running!"

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    gather = Gather(
        input='speech',
        action='/handle-response',
        timeout=3,
        speech_timeout='auto'
    )
    gather.say("Welcome to our medical clinic! How can I help you today?")
    resp.append(gather)
    return str(resp)

@app.route("/handle-response", methods=['POST'])
def handle_response():
    resp = VoiceResponse()
    user_input = request.values.get('SpeechResult', '').lower() if request.values.get('SpeechResult') else ''
    print(f"Received input: {user_input}")
    
    if user_input:
        response_found = False
        for category, info in CLINIC_RESPONSES.items():
            if any(keyword in user_input for keyword in info["keywords"]):
                resp.say(info["response"])
                response_found = True
                break
        
        if not response_found:
            resp.say("I apologize, but I didn't understand your question. You can ask about our hours, "
                    "location, appointments, insurance, prescriptions, or other clinic services. "
                    "How can I help you?")
    else:
        resp.say("I didn't hear anything. Please try your question again.")
    
    gather = Gather(
        input='speech',
        action='/handle-response',
        timeout=3,
        speech_timeout='auto'
    )
    gather.say("Do you have another question?")
    resp.append(gather)
    
    return str(resp)

if __name__ == "__main__":
    print("Starting Twilio Voice Bot Server...")
    print("Configure Twilio webhook to: /voice")
    app.run(debug=True, host='0.0.0.0', port=8080)
