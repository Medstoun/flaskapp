import json

__data = []


def load_candidates_from_json(path):
    global __data
    with open(path, "r", encoding="utf-8") as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for i in __data:
        if i["id"] == candidate_id:
            return {
                "name": i["name"],
                "position": i["position"],
                "picture": i["picture"],
                "skills": i["skills"],
            }
    return {"not_found": "Ушел на обед"}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []
    for i in __data:
        skills = i["skills"].lower().split(", ")
        if skill_name.lower() in skills:
            candidates.append(i)
    return candidates
