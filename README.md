# Medical Clinic Voice Bot

A Twilio-powered voice bot that handles common medical clinic inquiries using natural language processing. This automated answering service provides information about clinic hours, location, appointments, insurance, and more.

## Features

- **Natural Language Understanding**: Processes various ways patients might ask questions
- **Comprehensive Coverage**: Handles inquiries about:
  - Clinic hours and location
  - Appointment scheduling
  - Insurance and payments
  - New patient registration
  - Prescription refills
  - Medical records
  - Emergency situations
  - COVID-19 services
  - Telehealth options

- **Conversational Flow**: Maintains natural dialogue with follow-up questions
- **Real-time Response**: Provides immediate answers to common questions

## Technical Details

- Built with Flask and Twilio Voice API
- Uses webhook integration for real-time call handling
- Supports speech recognition and text-to-speech
- Implements pattern matching for natural language understanding

## Setup Requirements

1. Python 3.x
2. Flask
3. Twilio account
4. Ngrok for local development

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vlcosent/Answering-service-.git
```

2. Install dependencies:
```bash
pip install flask twilio
```

3. Set up Ngrok:
```bash
ngrok http 8080
```

4. Configure Twilio webhook URL with your Ngrok URL:
```
https://your-ngrok-url/voice
```

5. Run the application:
```bash
python app.py
```

## Usage

The bot automatically handles incoming calls to your Twilio number and can:
- Answer questions about clinic services
- Provide operating hours and location
- Help with appointment scheduling
- Explain insurance coverage
- Guide new patients
- Handle prescription refill inquiries
- Direct emergencies appropriately

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
