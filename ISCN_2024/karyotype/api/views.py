from rest_framework.decorators import api_view
from rest_framework.response import Response

from karyotype.services.iscn_parser import parse_iscn
from karyotype.services.iscn_to_text import iscn_to_text
#from karyotype.services.text_to_iscn import text_to_iscn



@api_view(['POST'])
def iscn_to_text_api(request):
    iscn = request.data.get('iscn')
    parsed_iscn = parse_iscn(iscn)
    text_iscn = iscn_to_text(parsed_iscn)

    return Response({
        "iscn" : iscn,
        "parsed_iscn" : parsed_iscn,
        "readable_iscn": text_iscn

    })

#@api_view(["POST"])
#def text_to_iscn_api(request):
    text = request.data.get("text")
    iscn = text_to_iscn("text")
    
    # later implementation
    return Response({
        "input_text": text,
        "iscn": "47,XX,+21"
    })