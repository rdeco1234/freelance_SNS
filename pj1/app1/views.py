from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from app1.models import Ipaddress

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def ipaddress(request):
    # データベース上のIPアドレス情報を配列型で取得
    ipaddresses = Ipaddress.objects.all().order_by('id')

    return  render(
		request,
        'ipaddress.html', # テンプレート名を指定
        {'ipaddresses' : ipaddresses }, # 取得したIPアドレス情報をテンプレート内の変数に代入
        )

def ipaddress_change(request, ipaddress_id=None):

    if ipaddress_id:
        ipaddress =  get_object_or_404(Ipaddress, pk=ipaddress_id)
    else:
        ipaddress = Ipaddress()

    if request.method == 'POST':
        # 基本的にPOSTが推奨される
        form = IpaddressForm(request.POST, instance=ipaddress)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('app1:ipaddress')
    else:
        # GETの場合はこちらを実行
        form = IpaddressForm(instance=ipaddress)

    return  render(
		request,
        'ipaddress_change.html',
        dict(form=form, ipaddress_id=ipaddress_id),
        )

