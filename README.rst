============
Simple Model
============

--------------
How to install
--------------

.. code:: shell

    pip install reqset

----------
How to use
----------

.. code:: python

    import reqset


    class PersonClient(reqset.Client):
        endpoint = 'http://api.com/v1/persons/'
        transport_class = FooTransport


    class AnimalClient(reqset.Client):
        endpoint = 'http://api.com/v1/animals/'

        owner = reqset.RelatedField(PersonClient, source_field='owner_id')


    # GET / single
    person = Person.objects.get(pk=1)
    print(person.name)

    # GET / list
    person_reqset = Person.objects.filter(age=18)  # request not made
    for person in person_reqset:  # request made
        print(person.name)

    # POST
    person = Person.objects.create(name='John Doe', age=18)

    # PATCH
    person.age = 20
    person.save()

    # PUT
    person = Person.objects.update_or_create(name='John Doe', age=30)
