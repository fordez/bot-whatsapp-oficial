
    type_q = type_query

    match type_q:
        case "text":
            query = data["changes"][0]["value"]["messages"][0]["text"]["body"]
            await sendDialogflow(number_contacts, query, 123456)

        case "image":
            image_id = data["changes"][0]["value"]["messages"][0]["image"]["id"]
            print(image_id)
        case "audio":
            audio_id = data["changes"][0]["value"]["messages"][0]["audio"]["id"]
            print(audio_id)
        case "video":
            video_id = data["changes"][0]["value"]["messages"][0]["video"]["id"]
            print(video_id)
        case "document":
            document_id = data["changes"][0]["value"]["messages"][0]["document"]["id"]
            print(document_id)
        case "location":
            latitude = data["changes"][0]["value"]["messages"][0]["location"]["latitude"]
            longitude = data["changes"][0]["value"]["messages"][0]["location"]["longitude"]
            print(latitude, longitude)
    
      