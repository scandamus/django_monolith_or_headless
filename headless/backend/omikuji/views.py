from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View
from .forms import FormOmikuji
from rest_framework import viewsets, renderers
from .models import DataOmikuji
from .serializers import OmikujiSerializer

# forms, models importする
# HTTPリクエストを受け取る
# データベースの操作などのロジックを実行する
# HTTPレスポンスを生成する

# エディタがクラスメソッドを静的メソッドとして定義するように提案してくるかもしれない。
# @staticmethodをつけることで可能ではあるが、
# self引数を受け取らないのでインスタンス変数にアクセスできなくなる。
# ただし、Djangoのクラスベースビューではget()メソッドはインスタンスメソッドとして定義し、第1引数にselfを受け取ることが一般的です。


class OmikujiViewSet(viewsets.ModelViewSet):
    queryset = DataOmikuji.objects.all()
    serializer_class = OmikujiSerializer
    # templeteを探さずapiを返す
    renderer_classes = [renderers.JSONRenderer]


class OmikujiView(View):
    def get(self, request):
        form = FormOmikuji()
        return JsonResponse({'form': form.data})

    def post(self, request):
        form = FormOmikuji(request.POST)
        if form.is_valid():
            form.save()
            return redirect('omikuji_result')
        return JsonResponse({'errors': form.errors})


class OmikujiResultView(View):
    def get(self, request):
        results = DataOmikuji.objects.all()
        data = [{'result_field_name': result.field_value} for result in results]
        return JsonResponse({'results': data})


# def OmikujiView(request):
#     if request.method == 'POST':
#         form = FormOmikuji(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('omikuji_result')
#     else:
#         form = FormOmikuji()
#
#     return render(request, 'omikuji.html', {'form': form})
#
#
# def OmikujiResultView(request):
#     results = DataOmikuji.objects.all()
#     return render(request, 'omikuji_result.html', {'results': results})