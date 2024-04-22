from django.shortcuts import render
from .forms import UploadFileForm
from .models import Transaction
import pandas as pd


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            print(len(df))
            for index, row in df.iterrows():
                transaction = Transaction(
                    date=row['Date'],
                    description=row['Description'],
                    amount=row['Amount']
                )
                transaction.save()

            return render(request, 'success.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
