======
reqset
======


-------------------
Ideas on how to use
-------------------

Not all features stated in the following examples are implemented.
This section serves only as motivation for future functionalities.


.. code:: python

    import reqset


    class PersonResource(reqset.Resource):
        endpoint = 'http://api.com/v1/persons/'
        client_class = MyLittleClient


    class PageResource(reqset.Resource):
        endpoint = 'http://api.com/v1/animals/'

        owner = reqset.RelatedField(
            PersonResource,
            source_field='owner_url',  # default is owner_id
            auto_follow=True,  # default is False
        )

        comments = reqset.MultipleRelatedField(
            CommentResource,
            source_field='comments_url',
            auto_follow=True,
        )


    # GET / single
    person = Person.objects.get(pk=1)
    print(person.name)

    # GET / list
    person_reqset = Person.objects.filter(age=18)
    for person in person_reqset:  # lazy request
        print(person.name)

    # POST
    person = Person.objects.create(name='John Doe', age=18)

    # PATCH
    person.age = 20
    person.save()

    # PUT
    person = Person.objects.update_or_create(name='John Doe', age=30)
