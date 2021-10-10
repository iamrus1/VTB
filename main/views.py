from django.shortcuts import render
from . import testdata

# Create your views here.


def datacatalog_view(request):
    return render(request, 'main/datacatalog.html', context={'datasets': testdata.datasets_short})

def dataset_detail_view(request, pk):
    return render(request, 'main/dataset_detail.html', context={'dataset': testdata.datasets[pk]})

def dataset_sample_data(request, pk):
    return render(request, 'main/dataset_sample_data.html', context={'dataset': testdata.datasets[pk]})
