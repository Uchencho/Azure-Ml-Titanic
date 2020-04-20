from django.shortcuts import render
from .forms import PredictForm
import urllib, json
import time

# Create your views here.
def homepage(request):
    if request.method == "GET":
        form = PredictForm()
        return render(request, 'azure/home.html', {'form':form})
    else:
        form = PredictForm(request.POST)
        if form.is_valid():
            print("it got here\n\n")
            obj = form.save(commit = False)
            #call the azure api
            
            url = 'https://ussouthcentral.services.azureml.net/workspaces/8511333baf364f1e8b81a614be00cca6/services/17741fd89eb74908b4885347c9647092/execute?api-version=2.0&details=true'
            api_key = 'SCXHA4mzar4kBFKsO06nJfNfGscYDjKCtStTnYD9B5CVxaK9Bwx/lbXXrLAV1HKt8NBNH2lQ/Xzq5ClE6N7pIw=='
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
                result = response.read()
                print(result)
            except Exception as error:
                print("The request failed with status code: " + str(error))
                print(error)

            time.sleep(3)
        else:
            print('form is invalid\n\n')
        return render(request, 'azure/home.html', {'form' : form})

