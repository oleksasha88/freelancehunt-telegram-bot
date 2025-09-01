def get_projects():
    url = ("https://api.freelancehunt.com/v2/projects"
           "?skills[]=107&skills[]=108&skills[]=141&skills[]=147&skills[]=58&skills[]=59&skills[]=90")
    headers = {"Authorization": f"Bearer {FREELANCEHUNT_API}"}
    r = requests.get(url, headers=headers)
    return r.json().get("data", [])
