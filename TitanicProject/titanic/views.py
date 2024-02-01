from django.shortcuts import render,redirect
from titanic.forms import MLModelForm
from titanic.models import MLModel
import joblib

# Create your views here.

def upload_model(request):
    if request.method == 'POST':
        form = MLModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MLModelForm()

    return render(request, 'upload_model.html', {'form': form})

def predict_view(request):
    if request.method == 'POST':
        pclass = int(request.POST.get('pclass'))
        sex = request.POST.get('sex')
        age = float(request.POST.get('age'))
        sibsp = int(request.POST.get('sibsp'))
        parch = int(request.POST.get('parch'))
        fare = float(request.POST.get('fare'))
        embarked = request.POST.get('embarked')

        
        ml_model_instance = MLModel.objects.last()  
        print(ml_model_instance)
        if ml_model_instance:
            model_path = ml_model_instance.model.path
            loaded_model = joblib.load(model_path)

            # Make predictions
            input_data = [[pclass, sex, age, sibsp, parch, fare, embarked]]
            prediction = loaded_model.predict(input_data)

            return render(request, 'predict.html', {'prediction': prediction[0]})

    return render(request, 'predict.html')