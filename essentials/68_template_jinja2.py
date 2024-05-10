from jinja2 import Template

# raw data
# --------------
template = Template("My name is {{ name }} and my age is {{ age }}")
output = template.render(name="Ram", age=43)
print(output)

print("------------------------------------")

# using dictionary
# --------------------
person = { 'name': 'Babita', 'age': 37 }
template = Template("My name is {{ person.name }} and my age is {{ person.age }}")
output = template.render(person=person)
print(output)
print("------------------------------------")


# using loop
# --------------------
persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

# loop all elements
template_string = '''{% for person in persons -%}
    {{ person.name }} : {{ person.age }}
{% endfor %}'''

template = Template(template_string)
output = template.render(persons=persons)
print(output)
print("------------------------------------")

# condition in template
template_string = '''{% for person in persons %}{% if person.age < 18 %}{{ person.name }} : {{ person.age }}
{% endif %}{%- endfor %}'''
template = Template(template_string)
output = template.render(persons=persons)
print(output)
print("------------------------------------")


# load template from file
cars = [
    {'name': 'Audi', 'price': 23000},
    {'name': 'Skoda', 'price': 17300},
    {'name': 'Volvo', 'price': 44300},
    {'name': 'Volkswagen', 'price': 21300}
]
with open('car_data_template.txt') as f:
    template = Template(f.read())

output = template.render(cars=cars)

print(output)
print("------------------------------------")


