from django.shortcuts import render
from .services import get_survey_and_questions, get_survey_list, \
    get_answered_questions, save_answer_for_current_question, get_next_question


def survey_list(request):
    surveys = get_survey_list()
    return render(request, 'surveys/survey_list.html', {'surveys': surveys})


def take_survey(request, survey_id):
    survey, questions = get_survey_and_questions(survey_id)
    answered = get_answered_questions(request.user, survey)

    if request.method == 'POST':
        save_answer_for_current_question(request)

    next_question = get_next_question(questions, answered)
    if not next_question:
        return render(request, 'surveys/survey_complete.html')
    return render(request, 'surveys/take_survey.html', {
        'survey': survey,
        'question': next_question
    })
