from django.http import Http404

from .models import Survey, Question, Answer


def get_survey_list():
    surveys = Survey.objects.all()
    return surveys


def get_survey_and_questions(survey_id):
    survey = Survey.objects.get(pk=survey_id)
    questions = Question.objects.filter(survey=survey)
    return survey, questions


def save_answer(method, answer_text, user, question_id):
    if method == 'POST':
        question = Question.objects.get(pk=question_id)
        _, answer = Answer.objects.get_or_create(
            user=user,
            answer_text=answer_text,
            defaults={"question": question},
        )
        if not answer:
            raise Http404("Answer already exists for this question and user.")


def get_next_question(questions, answered):
    if answered.last():
        next_question = questions.filter(
            trigger_answer_text=answered.last().answer_text).first()
    else:
        return questions.exclude(id__in=answered).first()
    return next_question


def get_current_question(questions, answered):
    if answered.last():
        question = questions.filter(
            trigger_answer_text=answered.last().answer_text).first()
    else:
        question = questions.exclude(id__in=answered).first()
    return question


def get_answered_questions(user, survey):
    return Answer.objects.filter(
        user=user,
        question__survey=survey
    )


def save_answer_for_current_question(request):
    question_id = request.POST.get('question_id')
    answer_text = request.POST.get('answer_text')
    save_answer(request.method, answer_text, request.user, question_id)
