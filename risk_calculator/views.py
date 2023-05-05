from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
from .models import RiskAssessmentData
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'html/index.html')

def calculate(request):
    if request.method == 'POST':
        # retrieve the form data
        architectural_complexity = request.POST.get('architectural_complexity')
        software_performance = request.POST.get('software_performance')
        software_scalability = request.POST.get('software_scalability')
        compatibility = request.POST.get('compatibility')
        budget_constraint = request.POST.get('budget_constraint')
        schedule_constraint = request.POST.get('schedule_constraint')
        scope_constraint = request.POST.get('scope_constraint')
        resource_constraint = request.POST.get('resource_constraint')
        market_change = request.POST.get('market_change')
        competition = request.POST.get('competition')
        regulatory_requirements = request.POST.get('regulatory_requirements')
        skill_gaps = request.POST.get('skill_gaps')
        turnover = request.POST.get('turnover')
        team_communication_issues = request.POST.get('team_communication_issues')

    
        input_dict = {
            'architectural_complexity': architectural_complexity,
            'software_performance': software_performance,
            'software_scalability': software_scalability,
            'compatibility': compatibility,
            'budget_constraint': budget_constraint,
            'schedule_constraint': schedule_constraint,
            'scope_constraint': scope_constraint,
            'resource_constraint': resource_constraint,
            'market_change': market_change,
            'competition': competition,
            'regulatory_requirements': regulatory_requirements,
            'skill_gaps': skill_gaps,
            'turnover': turnover,
            'team_communication_issues': team_communication_issues,
        }

        new_dict = {}

        for key, value in input_dict.items():
            if value == 'yes':
                new_dict[key] = 1
            elif value == 'no':
                new_dict[key] = 0

        # print(new_dict)
        input_list = []
        list = [1 if value == 'yes' else 0 for value in input_dict.values()]
        input_list.append(list)
        print(input_list)

        predicted_output = output(input_list)
        
        return render(request, 'html/calculate.html',{'output': predicted_output})
    
    return render(request, 'html/calculate.html')

# def contribute(request):
#     if request.method == 'POST':
#         # Create a new FormSubmission object and populate its fields from the POST data
#         submission = RiskAssessmentData()
#         submission.project_name = request.POST.get('project_name')
#         submission.email = request.POST.get('email')
#         submission.experience = request.POST.get('experience')
#         submission.architectural_complexity = request.POST.get('architectural_complexity')
#         submission.software_performance = request.POST.get('software_performance')
#         submission.software_scalability = request.POST.get('software_scalability')
#         submission.compatibility = request.POST.get('compatibility')
#         submission.budget_constraint = request.POST.get('budget_constraint')
#         submission.schedule_constraint = request.POST.get('schedule_constraint')
#         submission.scope_constraint = request.POST.get('scope_constraint')
#         submission.resource_constraint = request.POST.get('resource_constraint')
#         submission.market_change = request.POST.get('market_change')
#         submission.competition = request.POST.get('competition')
#         submission.regulatory_requirements = request.POST.get('regulatory_requirements')
#         submission.skill_gaps = request.POST.get('skill_gaps')
#         submission.turnover = request.POST.get('turnover')
#         submission.team_communication_issues = request.POST.get('team_communication_issues')
#         # Save the FormSubmission object to the database
#         submission.save()
#         # Redirect to a success page
#         # return HttpResponseRedirect('/form-submitted/')
#         print("Form submitted")
#         return HttpResponseRedirect('/calculate_page')
#     # else:
#     #     return render(request, 'html/contribute.html')
    
#     return render(request, 'html/contribute.html')

def contribute(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        architectural_complexity = request.POST.get('architectural_complexity')
        software_performance = request.POST.get('software_performance')
        software_scalability = request.POST.get('software_scalability')
        compatibility = request.POST.get('compatibility')
        budget_constraint = request.POST.get('budget_constraint')
        schedule_constraint = request.POST.get('schedule_constraint')
        scope_constraint = request.POST.get('scope_constraint')
        resource_constraint = request.POST.get('resource_constraint')
        market_change = request.POST.get('market_change')
        competition = request.POST.get('competition')
        regulatory_requirements = request.POST.get('regulatory_requirements')
        skill_gaps = request.POST.get('skill_gaps')
        turnover = request.POST.get('turnover')
        team_communication_issues = request.POST.get('team_communication_issues')
        
        submission = RiskAssessmentData(
            project_name=project_name,
            email=email,
            experience=experience,
            architectural_complexity=architectural_complexity,
            software_performance=software_performance,
            software_scalability=software_scalability,
            compatibility=compatibility,
            budget_constraint=budget_constraint,
            schedule_constraint=schedule_constraint,
            scope_constraint=scope_constraint,
            resource_constraint=resource_constraint,
            market_change=market_change,
            competition=competition,
            regulatory_requirements=regulatory_requirements,
            skill_gaps=skill_gaps,
            turnover=turnover,
            team_communication_issues=team_communication_issues
        )
        submission.save()
        return render(request, 'html/calculate.html')
    else:
        return render(request, 'html/contribute.html')

def output(input_list):
    # Load the model from the file
    with open('mul_reg_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Use the model for prediction
    # X_new = [[1, 0, 0, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1]]  # example input data
    X_new = input_list  # example input data
    y_pred = model.predict(X_new)
    print(y_pred)

    return y_pred[0]

