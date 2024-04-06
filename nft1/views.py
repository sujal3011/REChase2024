from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import Question
from teams.decorators import team_required

THIS_LEVEL = 1


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
        team.current_question = 0
        team.save()
    answer = answerForm(request.POST or None)
    context['team'] = team
    context['question'] = question
    context['profile'] = profile
    correct_ans = "Greg Solano and Wylie Aronow"
    context['answer'] = answer
    ans1="GREG"
    ans2="SOLANO"
    ans3="WYLIE"
    ans4= "ARONOW"
    if request.method == 'POST':
            if answer.is_valid():
                ans = answer.cleaned_data['answer'].upper()
                if ans1 in ans and ans2 in ans and ans3 in ans and ans4 in ans:                  
                    team.answerCorr(THIS_LEVEL, correct_ans)
                    question.answered(right=1)
                    return redirect(reverse_lazy('teams:get-level'))

                else:
                    question.answered(right=0)
                    context['wrong'] = 1

    return render(request,'nft1/question.html', context)