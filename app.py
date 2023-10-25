from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class HospitalChatbot:
    def __init__(self):
        self.intents_and_questions = {
            
            "greet":  [
                "hey",
                "hello",
                "hi",
                "hello there",
                "good morning",
                "good evening",
                "moin",
                "hey there",
                "let's go",
                "hey dude",
                "goodmorning",
                "goodevening",
                "good afternoon"],
    

            "goodbye": [

                "cu",
                "good by",
                "cee you later",
                "good night",
                "bye",
                "goodbye",
                "have a nice day",
                "see you around",
                "bye bye",
                "see you later"

            ],


            "affirm": [

                "yes",
                "y",
                "indeed",
                "of course",
                "that sounds good",
                "correct"

            ],


            "bot_challenge": [

                "are you a bot",
                "are you a human",
                "am I talking to a bot",
                "am I talking to a human"

            ],

            "appointment_booking": [

                "How can I schedule an appointment",
                "I need to book an appointment with a doctor",
                "What's the procedure for booking an appointment",
                "Hello, I'd like to schedule an appointment.",
                "Book an appointment",
                "appointment",
                "need an appointment"
            ],


            "doctor_information": [

                "Tell me more about Dr. ABC",
                "What's the specialty of Dr. ABC",
                "Give me the contact details for Dr. ABC"
                "doctor",
                "contact doctor",
                "doctor contact",
                "doctor detail",
                "detail doctor"

            ],


            "department_information": [

                "Which departments are available in the hospital",
                "Can you provide details about the cardiology department",
                "Tell me more about the pediatric department",
                "department",
                "which department",
                "department info"

            ],


            "visiting_hours":[

                "What are the visiting hours for patients",
                "When can I visit a patient in the hospital",
                "Is there a specific time for visiting hours",
                "visiting time",
                "visit",
                "time",
                "time to visit",
                "visit time",
                "hospital visit",
                "visit hospital"
            ],


            "location_and_directions":[

                "How do I get to the hospital",
                "Can you provide me with directions to your location",
                "Where is the hospital situated",
                "direction",
                "direction hospital",
                "hospital direction",
                "location",
                "hospital location"

            ],


            "billing_and_insurance": [
                "How do I pay my medical bills",
                "Do you accept my insurance",
                "What's the billing process for a hospital stay",
                "bills",
                "insurance",
                "pay bill",
                

            ],


            "medical_records": [
                "How can I access my medical records",
                "Request my medical history",
                "I need a copy of my lab results",
                "records",
                "medical records",
                "record medical",
                "results",
                "lab results",
                "result copy",
                "copy result"
            ],


            "emergency_services": [
                "What should I do in case of a medical emergency",
                "How do I contact the hospital in an emergency",
                "Tell me about your emergency services",
                "emergency",
                "emergency service"
            ],


            "covid19_information": [
                "What safety measures are in place due to COVID-19",
                "Is it safe to visit the hospital during the pandemic",
                "Do you offer COVID-19 testing or vaccinations",
                "covid19"

            ],


            "feedback_and_complaints": [
                "I want to provide feedback about my experience",
                "How can I file a complaint about a staff member",
                "Share my thoughts on my recent visit",
                "feedback",
                "complaints",
                "complain",
                "share thoughts",
                "experiance"
            ],


            "thank_you": [
                "Thank you for your help",
                "I appreciate your assistance",
                "You've been very helpful"
            ],


            "general_information": [
                "Tell me more about the hospital",
                "What services do you offer",
                "Is there a cafeteria in the hospital",
                "information",
                "cafeteria",
                "services",
                "services offered",
                "offered services"
            ]
        }
        
        self.intent_responses = {

            "greet": "Hello! How can I assist you today?",
            "appointment_booking": "To book an appointment, please call our scheduling department at 1234567897.",
            "doctor_information": "Dr. ABC is a specialist in Neuro. You can contact them at 9874563214.",
            "department_information": "Our hospital has various departments, including cardiology and pediatrics. How can I help you with a specific department?",
            "visiting_hours": "Visiting hours for patients are from 9:30 AM to 8:00 PM. Please feel free to visit during that time.",
            "location_and_directions": "Our hospital is located at Ameerpet Hyderabad. Here are directions to our hospital: [Directions].",
            "billing_and_insurance": "You can pay your medical bills at the billing department. We accept a variety of insurance plans. If you have any specific questions about billing, please call 789654125.",
            "medical_records": "To access your medical records, please visit the medical records department. They can provide you with a copy of your records or lab results.",
            "emergency_services": "In case of a medical emergency, please call 911 or go to the nearest emergency room. We also have an emergency department at our hospital.",
            "covid19_information": "For information on our COVID-19 safety measures and testing, please visit our website or contact our COVID-19 hotline at [COVID-19 Hotline Number].",
            "feedback_and_complaints": "Your feedback is valuable to us. You can provide feedback or file a complaint on our website or by contacting our patient services department.",
            "thank_you": "You're welcome! If you have any more questions, feel free to ask.",
            "general_information": "Our hospital provides a range of services, including medical, surgical, and emergency care. We also have a cafeteria for your convenience."
        
            
        }

    def match_intent(self, sentence):
        # Your intent matching code here
        sentence = sentence.lower()  # Convert to lowercase for case-insensitive matching
        for intent, questions in self.intents_and_questions.items():
            for question in questions:
                if question in sentence:
                    return intent
        return None

    def get_response(self, sentence):

        matched_intent = self.match_intent(sentence)
        if matched_intent:
            response = self.intent_responses.get(matched_intent, "I'm not sure how to answer that.")
        else:
            response = "I'm not sure how to answer that."
        return response
    
    

def create_video_html(video_url):
    return f'<video controls src="{video_url}" width="400"></video>'


def get_video_response(intent):
    video_urls = {

        "greet": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260372/Output/greet_a1ngxv.mp4",
        "appointment_booking": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260367/Output/appointment_booking_hl5uvy.mp4",
        "doctor_information": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260369/Output/doctor_information_dq34py.mp4",
        "department_information": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260373/Output/department_information_d7fksd.mp4",
        "visiting_hours": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260376/Output/visiting_hours_dzvh3d.mp4",
        "location_and_directions": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260375/Output/location_and_directions_ktkluz.mp4",
        "billing_and_insurance": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260370/Output/billing_and_insurance_ba77n4.mp4",
        "medical_records": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260377/Output/medical_records_akgmlx.mp4",
        "emergency_services": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260369/Output/emergency_services_et3eyl.mp4",
        "covid19_information": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260371/Output/covid19_information_orlff0.mp4",
        "feedback_and_complaints": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260371/Output/feedback_and_complaints_i3ftal.mp4",
        "thank_you": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260374/Output/thank_you_sgx29d.mp4",
        "general_information": "https://res.cloudinary.com/dam12ojlp/video/upload/v1698260375/Output/general_information_nz2zx1.mp4"
    
        
    }
    return video_urls.get(intent, "Video not available for this intent")

chatbot = HospitalChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_api():
    data = request.form['text']
    response = chatbot.get_response(data)
    
    intent = chatbot.match_intent(data)
    if intent:
        video_url = get_video_response(intent)
        if video_url:
            response = create_video_html(video_url)

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run()
