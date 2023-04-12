from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import RegistrationForm
from .models import UserProfile,UserAnswer
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.core.paginator import Paginator
# Create your views here.


User =get_user_model()

@login_required
def filtered_questions(request):
    # Retrieve filtering parameters from GET request
    department = request.GET.get('department')
    topic = request.GET.get('topic')
    role = request.GET.get('role')
    
    # Filter questions based on parameters
    questions = UserProfile.objects.all()
    if department:
        questions = questions.filter(department=department)
    if topic:
        questions = questions.filter(topic=topic)
    if role:
        questions = questions.filter(role=role)
        
    # Paginate filtered questions with 10 questions per page
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    
    context = {'questions': questions}
    return render(request, 'filtered_questions.html', context)


def save_answer(request):
    if request.method == 'POST':
        # Retrieve selected answers from POST request
        answers = request.POST
        for key, value in answers.items():
            if key.startswith('answer_'):
                question_id = key.split('_')[1]
                user_profile = UserProfile.objects.get(id=question_id)
                user_answer = UserAnswer(user=request.user, user_profile=user_profile, answer=value)
                user_answer.save()
        return redirect('questions')  # Redirect to filtered questions page after saving answers
    else:
        return HttpResponseBadRequest('Invalid request method')
    
def questions(request):
    department = request.GET.get('department', None)
    topic = request.GET.get('topic', None)
    role = request.GET.get('role', None)
    
    # Filter questions based on selected options
    questions = UserProfile.objects.all() # Assuming Question is your model for questions
    
    if department:
        questions = questions.filter(department=department)
    if topic:
        questions = questions.filter(topic=topic)
    if role:
        questions = questions.filter(role=role)
    
    # Paginate the filtered questions
    paginator = Paginator(questions, 1) # Show 10 questions per page
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    
    # Render the filtered questions in the template
    context = {
        'questions': questions,
    }
    return render(request, 'questions.html', context)
    