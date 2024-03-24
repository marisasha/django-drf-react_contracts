from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import models, serializers , utils
from django.db.models import QuerySet
from django.contrib.auth.models import User



@api_view(http_method_names=["GET"])
def api(request:Request):
    return Response(data = {"message":"ok"},status=200)

@api_view(http_method_names=["GET"])
def api_all_contracts(request: Request):
    try:
        sort = str(request.GET.get("sort", "desc"))
        _contracts = models.Contract.objects.all()
        match sort:
            case "asc": _contracts = _contracts.order_by("date")
            case "desc": _contracts = _contracts.order_by("-date")
        _contracts_json = serializers.ContractSimpleSerializer(_contracts, many=True if isinstance(_contracts, QuerySet) else False).data
        _contracts_json = utils.get_cache(key = "contracts_cach",query = lambda : _contracts_json, timeout = 2)
        return Response(
            data={
                "data": _contracts_json
            },
            status=200
        )
    except Exception as error:
        return Response(
            data={
                "data": "",
                "message": str(error)
            },
            status=404
        )
@api_view(http_method_names=["GET"])
def api_contracts_detail(request:Request,id : str):
    try:    
        _contract = models.Contract.objects.get(id = id)
        _contract_json = serializers.ContractSimpleSerializer(_contract,many = True if isinstance(_contract,QuerySet) else False).data
        _contract_json = utils.get_cache(key = f"contract{id}_cach",query = lambda : _contract_json, timeout = 5)
        return Response(
            data = {
                "contract":_contract_json
            },
            status=200
        )
    except Exception as error:
        return Response(
        data={
            "data": "",
            "message":str(error)
        },
        status=404
    )

@api_view(http_method_names=["GET"])
def api_agents(request: Request):
    try:
        sort = str(request.GET.get("sort", "desc"))
        _agents = models.Agent.objects.all()
        match sort:
            case "asc": _agents = _agents.order_by("id")
            case "desc": _agents = _agents.order_by("-id")
        _agents_json = serializers.AgentSimpleSerializer(_agents,many = True if isinstance(_agents,QuerySet) else False).data
        _agents_json = utils.get_cache(key = "agents_cach",query = lambda : _agents_json, timeout = 5)
        return Response(
            data={
                "data":_agents_json
            },
            status=200
        )
    except Exception as error:
        return Response(
            data={
                "data": None,
                "message": str(error)
            },
            status=400
        )

@api_view(http_method_names=["GET"])
def api_agents_detail(request: Request, id : str):
    try:    
        _agents = models.Agent.objects.get(id = id)
        _agents_json = serializers.AgentSimpleSerializer(_agents,many = True if isinstance(_agents,QuerySet) else False).data
        _agent_json = utils.get_cache(key = f"agent{id}_cach",query = lambda : _agent_json, timeout = 5)
        return Response(data = {
            "contract":_agents_json
        },
        status=200
    )
    except Exception as error:
        return Response(
            data={
                "data": "",
                "message":str(error)
            },
            status=404
        )

@api_view(http_method_names=["GET"])
def api_contract_info(request: Request,id : str):
    try:
        _contarct = models.Contract.objects.get(id = id)
        _agent = models.Agent.objects.get(id = _contarct.agent_id.id)
        _comment = models.Comment.objects.get(id = _contarct.comment_id.id)
        _author = User.objects.get(id = _contarct.author.id)
        
        
        _contract_json = {
            "participants":[_author.username,_agent.title],
            "total":_contarct.total,
            "comment":_comment.comment,
            "file":_contarct.file_path
        }
        return Response(
            data = {
                "contract":_contract_json
            },
            status = 200
        )
    except Exception as error:
        return Response(
            data={
                "data": "",
                "message":str(error)
            },
            status=404
        )
@api_view(http_method_names=["GET", "POST"])
def api_search_contract(request: Request):
    if request.method == "GET":
        return Response(
            data={
                "message": "ok"
            },
            status=200
        )
    if request.method == "POST":
        try:
            _search = str(request.data.get("text", "None"))
            print(_search)
            if _search != None:
                _agents = models.Agent.objects.filter(title__icontains=_search)
                _contracts = models.Contract.objects.filter(agent_id__in=_agents)
                _contracts_json = serializers.ContractSimpleSerializer(_contracts, many=True if isinstance(_contracts, QuerySet) else False).data
                return Response(
                    data={
                        "data": _contracts_json
                    },
                    status=200
                )
            else:
                return Response(
                    status=400
                )
        except Exception as error:
            return Response(
                data={
                    "data": "",
                    "message": str(error)
                },
                status=400
            )
       
