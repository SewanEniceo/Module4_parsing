import json

with open("sample.json", 'r') as json_file:
    json_data = json.load(json_file)
    
    Courses = []

    certifications = json_data.get('certifications',[])

    for certification in certifications:
        courses = certification.get('courses', [])
        Courses.extend(courses)

    print(','.join(Courses))
    print(json.dumps(json_data, indent = 4))