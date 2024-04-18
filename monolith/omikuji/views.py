from django.shortcuts import render, redirect
from django.views import View
from .forms import FormOmikuji
from .models import DataOmikuji

# forms, models importする
# HTTPリクエストを受け取る
# データベースの操作などのロジックを実行する
# HTTPレスポンスを生成する

# エディタがクラスメソッドを静的メソッドとして定義するように提案してくるかもしれない。
# @staticmethodをつけることで可能ではあるが、
# self引数を受け取らないのでインスタンス変数にアクセスできなくなる。
# ただし、Djangoのクラスベースビューではget()メソッドはインスタンスメソッドとして定義し、第1引数にselfを受け取ることが一般的です。


class OmikujiView(View):
    def get(self, request):
        form = FormOmikuji()
        return render(request, 'omikuji.html', {'form': form})

    def post(self, request):
        form = FormOmikuji(request.POST)
        if form.is_valid():
            form.save()
            return redirect('omikuji_result')
        return render(request, 'omikuji.html', {'form': form})


class OmikujiResultView(View):
    def get(self, request):
        results = DataOmikuji.objects.all()
        return render(request, 'omikuji_result.html', {'results': results})


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