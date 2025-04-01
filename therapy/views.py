from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Session
from django.http import JsonResponse
import random  # Mock data for analysis
from django.core.files.base import ContentFile
import base64


# Home Page
def home(request):
    patients = Patient.objects.all()
    return render(request, 'home.html', {'patients': patients})

# Add Patient Page
def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        Patient.objects.create(name=name, age=age, gender=gender, email=email)
        return redirect('home')
    return render(request, 'add_patient.html')

# Patient Dashboard Page
def patient_dashboard(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    sessions = Session.objects.filter(patient=patient).order_by('date')
    return render(request, 'patient_dashboard.html', {
        'patient': patient,
        'sessions': sessions,
    })


# Delete Patient View
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.delete()  # Deletes the patient from the database
    return redirect('home')  # Redirects back to the home page
'''    
# Therapy Page
def therapy(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Retrieve email from the form
        patient = Patient.objects.filter(email=email).first()

        if not patient:
            return render(request, 'therapy.html', {'error': 'No patient found with this email.'})

        # Mock analysis data
        word_accuracy = random.uniform(80, 100)
        char_accuracy = random.uniform(70, 100)

        # Save the session data to the database
        Session.objects.create(
            patient=patient,
            word_accuracy=word_accuracy,
            char_accuracy=char_accuracy
        )

        # Pass results and success message to the template
        return render(request, 'therapy.html', {
            'success': 'Analysis completed and saved successfully!',
            'word_accuracy': round(word_accuracy, 2),
            'char_accuracy': round(char_accuracy, 2)
        })

    return render(request, 'therapy.html')
'''

def therapy(request):
    if request.method == 'POST':
        # Retrieve email
        email = request.POST.get('email')
        patient = Patient.objects.filter(email=email).first()

        if not patient:
            return render(request, 'therapy.html', {'error': 'No patient found with this email.'})

        # Handle pre-recorded audio
        uploaded_audio = request.FILES.get('audio_file')
        if uploaded_audio:
            # Save uploaded audio if needed
            pass

        # Handle recorded audio (Base64)
        recorded_audio = request.POST.get('recordedAudio')
        if recorded_audio:
            format, audio_string = recorded_audio.split(';base64,')
            decoded_audio = base64.b64decode(audio_string)
            audio_file = ContentFile(decoded_audio, name='recorded_audio.wav')
            # Save the audio_file if needed
            pass

        # Mock analysis (replace with actual analysis logic)
        word_accuracy = random.uniform(55, 94)
        char_accuracy = random.uniform(70, 95)

        # Save session details
        Session.objects.create(
            patient=patient,
            word_accuracy=word_accuracy,
            char_accuracy=char_accuracy
        )

        # Return analysis results
        return render(request, 'therapy.html', {
            'success': 'Analysis completed successfully!',
            'word_accuracy': round(word_accuracy, 2),
            'char_accuracy': round(char_accuracy, 2),
        })

    return render(request, 'therapy.html')