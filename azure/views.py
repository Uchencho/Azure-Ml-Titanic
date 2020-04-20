from django.shortcuts import render
from .forms import PredictForm
import urllib, json
import time
from django.http import JsonResponse, HttpResponseRedirect
from titanic.settings import api_key
from django.contrib import messages

# Create your views here.
def homepage(request):
    if request.method == "GET":
        form = PredictForm()
        return render(request, 'azure/home.html', {'form':form})
    else:
        form = PredictForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            #call the azure api
            
            url = 'https://ussouthcentral.services.azureml.net/workspaces/8511333baf364f1e8b81a614be00cca6/services/17741fd89eb74908b4885347c9647092/execute?api-version=2.0&details=true'
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

            data =  {

                "Inputs": {

                        "input1":
                        {
                            "ColumnNames": ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"],
                            "Values": [ [ "0", "0", "0", "value", "value", "0", "0", "0", "value", "0", "value", "value" ], 
                                    [ "0", "0", obj.ticket_class, obj.name, obj.sex, obj.age, obj.siblings, obj.parents, "value", "0", "value", "value" ], ]
                        },        
                            },
                                "GlobalParameters": {
                    }
                        }
            body = str.encode(json.dumps(data))

            req = urllib.request.Request(url, body, headers) 

            try:
                response = urllib.request.urlopen(req)
                result = response.read() #return this json result to frontend
                print(result, "\n\n")
                result = json.loads(result)
                prob = result['Results']['output1']['value']['Values'][1][-1]
                prob = round(float(prob), 2) * 100
                pred_result = result['Results']['output1']['value']['Values'][1][-2]
                if pred_result == '1':
                    the_string = "survived"
                else:
                    the_string = 'not survive'
                name = obj.name
                print(prob, "\n\n", pred_result, '\n\n', type(pred_result), "\n\n", the_string, "\n\n")
                messages.info(request, 'Based on your feeatures, there is {} chance that the person will survive'.format(prob))
                return render(request, 'azure/result.html', {'message':messages, 'probability':prob, 'name':name, 'the_string': the_string})
            except Exception as error:
                print("The request failed with status code: " + str(error))
                print(error)
        else:
            print('form is invalid\n\n')
        form = PredictForm()
        return render(request, 'azure/home.html', {'form':form})
