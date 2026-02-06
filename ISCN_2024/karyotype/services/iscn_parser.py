import re

def parse_iscn(iscn):
    """
    VERY FIRST VERSION: handle simple deletions
    Example: 46,XX,del(5)(q13q33)
    """
    result = {
        "karyotype": None,
        "abnormalities": []
    }

    parts = iscn.split(",")

    result["karyotype"] = ",".join(parts[:2])

    del_match = re.search(r"del\((\d+)\)\((p|q)(\d+)(p|q)?(\d+)?\)", iscn)
    if del_match:
        result["abnormalities"].append({
            "type": "deletion",
            "chromosome": del_match.group(1),
            "arm": del_match.group(2),
            "start_band": del_match.group(3),
            "end_band": del_match.group(5)
        })

    return result
