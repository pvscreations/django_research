import json
from django.db import connections
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt



#views
@csrf_exempt
def insert(request):
    db=connections["seconddb"]
    cursor=db.cursor()
    data=json.loads(request.body)
    query="insert into credentials values('"+data["id"]+"','"+data["name"]+"',"+data["marks"]+")"
    print(query)
    try:
        cursor.execute(query)
        db.commit()
        return JsonResponse({"status":"success"})

    except Exception as e:
        print(e)
        db.rollback()
        return JsonResponse({"status":"failure"})

@csrf_exempt
def update(request):
    db=connections["seconddb"]
    cursor=db.cursor()
    data=json.loads(request.body)
    print(data)
    query=f"update credentials set password='{data['password']}' ,marks={data['marks']} where id='{data['id']}'"
    print(query)
    try:
        cursor.execute(query)
        db.commit()
        return JsonResponse({"status":"success"})

    except Exception as e:
        
        db.rollback()
        return JsonResponse({"status":f"{e}"})
@csrf_exempt
def delete(request,deleteId):
    db=connections["seconddb"]
    cursor=db.cursor()
    print(request,"hell")
    # deleteId=""
    query=f'delete from credentials where id={deleteId}'
    try:
        cursor.execute(query)
        db.commit()
        return JsonResponse({"status":"success"})
    except Exception as e:
        db.rollback()
        return JsonResponse({"status":e})

# @app.route("/contents",methods=['POST'])
@csrf_exempt
def content(request):
    db=connections["seconddb"]
    cursor=db.cursor()
    query="select id from credentials;"
    cursor.execute(query)
    res=cursor.fetchall()
    return JsonResponse({"contents":res})
