from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import Question
from .utils import makeSequence,solve
from teams.decorators import team_required

THIS_LEVEL =3


@login_required
@team_required
def home(request):
    context = {}
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = Question.objects.all().first()
    if str(team.current_question) == '-1':
        seq = makeSequence()
        temp = ' and '.join(map(str, seq))
        team.question = temp
        team.current_question = 0
        team.save()
    answer = answerForm(request.POST or None)
    context['team'] = team
    context['question'] = question
    context['profile'] = profile
    sequence = team.question
    sequence = list(map(str , team.question.split(' and ')))
    context['sequence'] = ' and '.join(map(str, sequence))
    correct_ans = solve(sequence)
    context['answer'] = answer
    if request.method == 'POST':
        if answer.is_valid():
            ans = abs(answer.cleaned_data['answer'])
            if correct_ans == ans:
                team.answerCorr(THIS_LEVEL, correct_ans)
                question.answered(right=1)
                return redirect(reverse_lazy('teams:get-level'))

            else:
                question.answered(right=0)
                context['wrong'] = 1
        else:
            context['invalid'] = 1

    return render(request,'cars2/question.html',context)



    