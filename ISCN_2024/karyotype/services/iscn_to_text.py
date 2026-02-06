def iscn_to_text(parsed):
    k = parsed["karyotype"]
    sex = "Female" if "XX" in k else "Male"

    text = f"{sex} with {k.split(',')[0]} chromosomes"

    for abn in parsed["abnormalities"]:
        if abn["type"] == "deletion":
            text += (
                f", deletion on chromosome {abn['chromosome']} "
                f"{abn['arm']} arm from band {abn['start_band']} "
                f"to {abn['end_band']}"
            )

    return text



