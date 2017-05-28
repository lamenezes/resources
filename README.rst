============
Simple Model
============

--------------
How to install
--------------

.. code:: shell

    pip install reqset

-------------------
Ideas on how to use
-------------------

Not all features stated in the following examples are implemented.
This section serves as motivation for future functionalities.


.. code:: python

    import reqset


    class PersonClient(reqset.Client):
        endpoint = 'http://api.com/v1/persons/'
        transport_class = FooTransport


    class PageClient(reqset.Client):
        endpoint = 'http://api.com/v1/animals/'

        owner = reqset.RelatedField(
            PersonClient,
            source_field='owner_url',  # default is owner_id
            auto_follow=True,  # default is False
        )

        comments = reqset.MultipleRelatedField(
            CommentClient,
            source_field='comments_url',
            auto_follow=True,
        )


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
