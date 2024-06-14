from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import urllib

def handle_uploaded_file(file):
    # Read the uploaded CSV file
    df = pd.read_csv(file)

    # Display the first few rows
    first_rows = df.head().to_html()

    # Calculate summary statistics
    summary_stats = df.describe().to_html()

    # Identify and handle missing values
    missing_values = df.isnull().sum().to_frame().transpose().to_html()

    # Generate basic plots
    plots = []
    for column in df.select_dtypes(include=[float, int]).columns:
        plt.figure()
        sns.histplot(df[column], kde=True)
        plt.title(f'Histogram of {column}')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = 'data:image/png;base64,' + urllib.parse.quote(string)
        plots.append(uri)
        plt.close()

    return first_rows, summary_stats, missing_values, plots

def UploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            first_rows, summary_stats, missing_values, plots = handle_uploaded_file(file)
            return render(request, 'app/result.html', {
                'first_rows': first_rows,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'plots': plots,
            })
    else:
        form = UploadFileForm()
    return render(request, 'app/index.html', {'form': form})
